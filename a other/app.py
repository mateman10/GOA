import streamlit as st
import sqlite3
import hashlib
import re
import pandas as pd
import anthropic

# -----------------------------------------------------------------------------
# ANTHROPIC CLAUDE API CONFIGURATION (უსაფრთხო მიბმა Streamlit Secrets-იდან)
# -----------------------------------------------------------------------------
try:
    API_KEY = st.secrets["ANTHROPIC_API_KEY"]
except Exception:
    API_KEY = ""  # ფოლბექი ლოკალური ტესტირებისთვის

client = anthropic.Anthropic(api_key=API_KEY)

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION & FULL RESPONSIVE GEMINI / CLAUDE DARK THEME
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="EduAudit AI",
    page_icon="🛡️",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background-color: #131314;
        color: #e3e3e3;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main Container & Cards */
    .gemini-card {
        background-color: #1e1f20;
        border: 1px solid #333537;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }
    
    /* Custom File Uploader Styling inside Streamlit */
    [data-testid='stFileUploader'] {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 15px;
        border: 2px dashed #d1d5db;
    }
    [data-testid='stFileUploader'] section {
        background-color: #ffffff !important;
    }
    [data-testid='stFileUploader'] label, [data-testid='stFileUploader'] small, [data-testid='stFileUploader'] span {
        color: #374151 !important;
    }

    .chat-bubble-user {
        background-color: #2b2c2f;
        border: 1px solid #3c3f44;
        padding: 16px;
        border-radius: 14px;
        margin-bottom: 12px;
        color: #f3f4f6;
        word-break: break-word;
    }
    
    .chat-bubble-ai {
        background-color: #131314;
        border: 1px solid #282a2c;
        padding: 16px;
        border-radius: 14px;
        margin-bottom: 12px;
        color: #e3e3e3;
        word-break: break-word;
    }

    .stTextInput input, .stTextArea textarea {
        background-color: #1e1f20 !important;
        color: #e3e3e3 !important;
        border-radius: 12px !important;
        border: 1px solid #444746 !important;
        padding: 12px 16px !important;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #8ab4f8 0%, #669df6 100%);
        color: #131314;
        border: none;
        border-radius: 12px;
        font-weight: 700;
        padding: 0.6rem 1.4rem;
        box-shadow: 0 4px 12px rgba(138, 180, 248, 0.2);
        transition: all 0.2s ease;
        width: 100%;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #aecbfa 0%, #8ab4f8 100%);
        box-shadow: 0 6px 16px rgba(138, 180, 248, 0.4);
        transform: translateY(-1px);
    }

    /* Mobile Responsiveness Enhancements */
    @media (max-width: 768px) {
        .gemini-card {
            padding: 14px;
            margin-bottom: 12px;
            border-radius: 12px;
        }
        h1 {
            font-size: 24px !important;
        }
        h3 {
            font-size: 18px !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DATABASE SETUP
# -----------------------------------------------------------------------------
@st.cache_resource
def init_db():
    conn = sqlite3.connect('eduaudit.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE,
                    password_hash TEXT,
                    role TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    prompt TEXT,
                    response TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    return conn

conn = init_db()

# -----------------------------------------------------------------------------
# SESSION STATE
# -----------------------------------------------------------------------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user' not in st.session_state:
    st.session_state.user = None
if 'role' not in st.session_state:
    st.session_state.role = None
if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = "შესვლა"

# -----------------------------------------------------------------------------
# AUTHENTICATION SCREEN & MAIN APP LOGIC
# -----------------------------------------------------------------------------
st.title("🛡️ EduAudit AI")

if not st.session_state.logged_in:
    st.markdown('<div class="gemini-card">', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["შესვლა", "რეგისტრაცია"])
    
    with tab1:
        st.subheader("ავტორიზაცია")
        login_email = st.text_input("ელ-ფოსტა", key="login_email")
        login_pass = st.text_input("პაროლი", type="password", key="login_pass")
        if st.button("შესვლა"):
            hashed_input = hashlib.sha256(login_pass.encode('utf-8')).hexdigest()
            c = conn.cursor()
            c.execute("SELECT password_hash, role FROM users WHERE email = ?", (login_email,))
            user_data = c.fetchone()
            if user_data and user_data[0] == hashed_input:
                st.session_state.logged_in = True
                st.session_state.user = login_email
                st.session_state.role = user_data[1]
                st.rerun()
            else:
                st.error("არასწორი ელ-ფოსტა ან პაროლი!")
    
    with tab2:
        st.subheader("რეგისტრაცია")
        reg_email = st.text_input("ელ-ფოსტა", key="reg_email")
        reg_pass = st.text_input("პაროლი", type="password", key="reg_pass")
        reg_role = st.selectbox("როლი", ["მომხმარებელი", "ადმინისტრატორი"], key="reg_role")
        if st.button("რეგისტრაცია"):
            if reg_email and reg_pass:
                hashed_pass = hashlib.sha256(reg_pass.encode('utf-8')).hexdigest()
                try:
                    c = conn.cursor()
                    c.execute("INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)", 
                              (reg_email, hashed_pass, reg_role))
                    conn.commit()
                    st.success("რეგისტრაცია წარმატებით დასრულდა! გადადით შესვლის ტაბზე.")
                except sqlite3.IntegrityError:
                    st.error("ეს ელ-ფოსტა უკვე დაკავებულია!")
            else:
                st.error("გთხოვთ შეავსოთ ყველა ველი!")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="gemini-card">მოგესალმებით, <b>{st.session_state.user}</b> ({st.session_state.role})</div>', unsafe_allow_html=True)
    
    if st.button("გასვლა"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.role = None
        st.rerun()
        
    st.markdown('<div class="gemini-card">', unsafe_allow_html=True)
    st.subheader("AI ასისტენტი (Claude)")
    user_prompt = st.text_area("შეკითხვა ან დავალება AI-ს:", key="ai_prompt")
    if st.button("გაგზავნა"):
        if user_prompt and API_KEY:
            try:
                response = client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1000,
                    messages=[{"role": "user", "content": user_prompt}]
                )
                ai_reply = response.content[0].text
                st.markdown(f'<div class="chat-bubble-ai"><b>Claude AI:</b><br>{ai_reply}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"შეცდომა API-სთან დაკავშირებისას: {e}")
        elif not API_KEY:
            st.warning("API გასაღები არ არის მითითებული Streamlit Secrets-ში!")
        else:
            st.warning("გთხოვთ შეიყვანოთ შეკითხვა!")
    st.markdown('</div>', unsafe_allow_html=True)