import streamlit as st
import sqlite3
import bcrypt
import re
import pandas as pd
import anthropic

# -----------------------------------------------------------------------------
# ANTHROPIC CLAUDE API CONFIGURATION
# -----------------------------------------------------------------------------
API_KEY = ""  # აქ ჩასვი შენი Claude API გასაღები
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
# AUTHENTICATION SCREEN
# -----------------------------------------------------------------------------
def validate_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def validate_password(password):
    return len(password) >= 8 and any(c.isupper() for c in password)

if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #ffffff; font-weight: 800; margin-top: 20px;'>🛡️ EduAudit AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #9aa0a6; margin-bottom: 25px; font-size: 14px;'>Enterprise-Grade Secure Document & Compliance Auditor</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.1, 2.8, 0.1])
    with col2:
        st.markdown('<div class="gemini-card">', unsafe_allow_html=True)
        
        t1, t2 = st.columns(2)
        with t1:
            if st.button("🔑 შესვლა", use_container_width=True):
                st.session_state.auth_mode = "შესვლა"
                st.rerun()
        with t2:
            if st.button("📝 რეგისტრაცია", use_container_width=True):
                st.session_state.auth_mode = "რეგისტრაცია"
                st.rerun()
        
        st.markdown("<hr style='border-color: #333537; margin: 15px 0;'>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: #8ab4f8; font-size: 13px; font-weight: 600;'>რეჟიმი: {st.session_state.auth_mode}</p>", unsafe_allow_html=True)

        email = st.text_input("ელფოსტა", placeholder="name@example.com")
        password = st.text_input("პაროლი", type="password", placeholder="მინ. 8 სიმბოლო, 1 დიდი ასო")
        
        if st.session_state.auth_mode == "რეგისტრაცია":
            if st.button("ანგარიშის შექმნა", use_container_width=True):
                if not validate_email(email):
                    st.error("არასწორი ელფოსტის ფორმატი.")
                elif not validate_password(password):
                    st.error("პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო და შეიცავდეს 1 დიდ ასოს.")
                else:
                    try:
                        # ინახება როგორც სრულიად თავსებადი სტრიქონი (str)
                        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                        c = conn.cursor()
                        c.execute("SELECT COUNT(*) FROM users")
                        user_count = c.fetchone()[0]
                        
                        role = "ADMIN" if (user_count == 0 or email == "mmanagadze123@gmail.com") else "USER"
                        
                        c.execute("INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)", (email, hashed, role))
                        conn.commit()
                        st.success("რეგისტრაცია წარმატებულია! შეგიძლიათ შეხვიდეთ.")
                    except sqlite3.IntegrityError:
                        st.error("ეს ელფოსტა უკვე დაკავებულია.")
        else:
            if st.button("შესვლა", use_container_width=True):
                c = conn.cursor()
                c.execute("SELECT password_hash, role FROM users WHERE email = ?", (email,))
                res = c.fetchone()
                
                # უნივერსალური შემოწმება (მუშაობს როგორც str, ისე bytes ტიპის ჰაშებზე)
                login_success = False
                if res:
                    stored_hash = res[0]
                    if isinstance(stored_hash, str):
                        stored_hash = stored_hash.encode('utf-8')
                    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                        login_success = True

                if res and login_success:
                    st.session_state.logged_in = True
                    st.session_state.user = email
                    st.session_state.role = res[1]
                    st.rerun()
                else:
                    st.error("არასწორი ელფოსტა ან პაროლი.")
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MAIN CHAT / WORKSPACE INTERFACE
# -----------------------------------------------------------------------------
else:
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.markdown("### 🛡️ EduAudit Workspace")
        role_badge = "👑 ადმინისტრატორი" if st.session_state.role == "ADMIN" else "👤 მომხმარებელი"
        st.markdown(f"<span style='color: #9aa0a6; font-size: 13px;'>მომხმარებელი: <b>{st.session_state.user}</b> ({role_badge})</span>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div style='text-align: right;'>", unsafe_allow_html=True)
        if st.button("🚪 გასვლა"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.role = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # Navigation tabs if ADMIN
    if st.session_state.role == "ADMIN":
        app_mode = st.radio("Navigation", ["workspace", "admin"], format_func=lambda x: "📁 სამუშაო სივრცე" if x == "workspace" else "📊 ადმინისტრატორის პანელი", horizontal=True, label_visibility="collapsed")
    else:
        app_mode = "workspace"

    st.markdown("<hr style='border-color: #333537; margin: 15px 0;'>", unsafe_allow_html=True)

    if app_mode == "workspace":
        st.markdown('<div class="gemini-card" style="margin-top: 5px;">', unsafe_allow_html=True)
        st.markdown("""
            <div style='display: flex; align-items: center; gap: 10px; margin-bottom: 15px;'>
                <span style='font-size: 24px;'>📁</span>
                <h3 style='margin: 0; color: #f3f4f6; font-size: 20px;'>დოკუმენტის ატვირთვა და ანალიზი</h3>
            </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("📂 Drag and drop or browse... (TXT, MD, CSV)", type=["txt", "md", "csv"])
        
        if uploaded_file:
            st.markdown(f"<p style='color: #1f2937; font-size: 13px; margin-top: 5px; background: #e5e7eb; padding: 6px; border-radius: 6px;'>არჩეულია ფაილი: <b>{uploaded_file.name}</b></p>", unsafe_allow_html=True)

        user_prompt = st.text_area("შეტყობინება AI-სთვის", placeholder="შეიყვანეთ დავალება (მაგ: ამოიღე ყველა კონფიდენციალური მონაცემი...)", height=90)

        if st.button("✨ ანალიზის გაშვება"):
            try:
                file_content = ""
                if uploaded_file is not None:
                    try:
                        file_content = uploaded_file.getvalue().decode("utf-8")
                    except:
                        file_content = "Binary or non-utf8 file uploaded."
                
                full_input = f"{user_prompt}\n\nDocument Content:\n{file_content}"
                
                with st.spinner("Claude ამუშავებს მონაცემებს..."):
                    message = client.messages.create(
                        model="claude-opus-5-5",
                        max_tokens=2048,
                        messages=[
                            {"role": "user", "content": full_input}
                        ]
                    )
                    answer = next(block.text for block in message.content if hasattr(block, 'text'))
                    
                    c = conn.cursor()
                    c.execute("INSERT INTO history (username, prompt, response) VALUES (?, ?, ?)", 
                              (st.session_state.user, full_input, answer))
                    conn.commit()
                    
                    st.markdown("### 📊 პასუხი:")
                    st.markdown(f"<div class='chat-bubble-ai'>{answer}</div>", unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"შეცდომა API-სთან დაკავშირებით: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("### 🕒 ძველი ანალიზების ისტორია")
        c = conn.cursor()
        c.execute("SELECT prompt, response, timestamp FROM history WHERE username = ? ORDER BY timestamp DESC LIMIT 5", (st.session_state.user,))
        history = c.fetchall()
        
        if history:
            for h in history:
                st.markdown(f"<div class='chat-bubble-user'><b>შეკითხვა:</b> {h[0][:120]}...<br><small style='color: #9aa0a6;'>დრო: {h[2]}</small></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='chat-bubble-ai'><b>AI პასუხი:</b> {h[1][:400]}...</div>", unsafe_allow_html=True)
        else:
            st.info("ისტორია ჯერ ცარიელია.")

    elif app_mode == "admin":
        st.markdown("### 📊 ადმინისტრატორის მართვის პანელი")
        st.markdown("<p style='color: #9aa0a6; font-size: 14px;'>სისტემის ზოგადი სტატისტიკა და მომხმარებელთა მონაცემები</p>", unsafe_allow_html=True)

        c = conn.cursor()
        
        c.execute("SELECT COUNT(*) FROM users")
        total_users = c.fetchone()[0]
        
        c.execute("SELECT COUNT(*) FROM history")
        total_queries = c.fetchone()[0]

        m1, m2 = st.columns(2)
        with m1:
            st.markdown(f"""
                <div class='gemini-card' style='text-align: center;'>
                    <h4 style='color: #9aa0a6; margin: 0;'>სულ მომხმარებელი</h4>
                    <h2 style='color: #8ab4f8; margin: 10px 0 0 0;'>{total_users}</h2>
                </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
                <div class='gemini-card' style='text-align: center;'>
                    <h4 style='color: #9aa0a6; margin: 0;'>სულ გაგზავნილი ანალიზი</h4>
                    <h2 style='color: #8ab4f8; margin: 10px 0 0 0;'>{total_queries}</h2>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("#### 👑 მომხმარებლისთვის ადმინის უფლების მინიჭება")
        st.markdown("<p style='color: #9aa0a6; font-size: 13px;'>ჩაწერეთ მომხმარებლის ზუსტი ელფოსტა და მიანიჭეთ ადმინისტრატორის სტატუსი:</p>", unsafe_allow_html=True)
        
        target_promote_email = st.text_input("მომხმარებლის ელფოსტა", placeholder="user@example.com", key="promote_email_input")
        if st.button("მივანიჭო ADMIN სტატუსი"):
            if target_promote_email:
                c.execute("SELECT * FROM users WHERE email = ?", (target_promote_email,))
                user_exists = c.fetchone()
                if user_exists:
                    c.execute("UPDATE users SET role = 'ADMIN' WHERE email = ?", (target_promote_email,))
                    conn.commit()
                    st.success(f"მომხმარებელი ({target_promote_email}) წარმატებით გახდა ადმინისტრატორი!")
                else:
                    st.error("ასეთი ელფოსტით მომხმარებელი ბაზაში არ მოიძებნა.")
            else:
                st.warning("გთხოვთ ჩაწეროთ ელფოსტა.")

        st.markdown("<hr style='border-color: #333537; margin: 20px 0;'>", unsafe_allow_html=True)

        st.markdown("#### 👥 რეგისტრირებული მომხმარებლები")
        c.execute("SELECT id, email, role, created_at FROM users ORDER BY created_at DESC")
        users_data = c.fetchall()
        if users_data:
            users_df = pd.DataFrame(users_data, columns=["ID", "ელფოსტა", "როლი", "რეგისტრაციის დრო"])
            st.dataframe(users_df, use_container_width=True)
        else:
            st.info("მომხმარებლები არ მოიძებნა.")

        st.markdown("#### 📜 სისტემის სრული ისტორია (ყველა მომხმარებელი)")
        c.execute("SELECT username, prompt, response, timestamp FROM history ORDER BY timestamp DESC LIMIT 20")
        all_history = c.fetchall()
        if all_history:
            for ah in all_history:
                st.markdown(f"<div class='chat-bubble-user'><b>მომხმარებელი:</b> {ah[0]}<br><b>შეკითხვა:</b> {ah[1][:150]}...<br><small style='color: #9aa0a6;'>დრო: {ah[3]}</small></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='chat-bubble-ai'><b>AI პასუხი:</b> {ah[2][:300]}...</div>", unsafe_allow_html=True)
        else:
            st.info("ისტორია ჯერ ცარიელია.")