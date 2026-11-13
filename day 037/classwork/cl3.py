# 3) შექმენი Dictionary სახელად book, რომელშიც შეინახავ წიგნის სათაურს, 
# ავტორს და გვერდების რაოდენობას. მომხმარებელს შემოატანინე ინფორმაცია 
# და შეამოწმე in ოპერატორის გამოყენებით, არსებობს თუ არა მის მიერ
# შეყვანილი Key ობიექტში. დაბეჭდე შესაბამისი შეტყობინება.

book = {
    "name": "learn py",
    "author": "unknown",
    "user_information": input("type a information: ")
}

print("user_information" in book)

