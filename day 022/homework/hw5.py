#5) შექმენი ცვლადი raw_data = "  html,css,javascript  ". ჯერ strip() მეთოდით აშორე ჰარები, ხოლო შემდეგ split(",") მეთოდით დაყავი ეს ტექსტი სიად. დაბეჭდე მიღებული სია.

raw_data = "  html,css,javascript  "

new_raw_data = raw_data.strip()

print(new_raw_data.split(","))