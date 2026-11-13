# 5) შექმენი Dictionary სახელად school, რომელშიც შეინახავ სკოლის სახელს, მოსწავლეების რაოდენობას და ქალაქს. შემდეგ:
# - დაამატე ახალი Key director, რომელშიც შეინახავ დირექტორის სახელს.
# - შეამოწმე in ოპერატორით, არსებობს თუ არა students Key.
# - წაშალე city Key.
# - შეცვალე სკოლის სახელი.
# - დაბეჭდე საბოლოო Dictionary.


school = {
    "name": "მე-7 საჯარო სკოლა",
    "students": 2000,
    "city": "ზესტაფონი",
}

school["directory"] = "მარეხი ქათამაძე"

print("students" in school)

del school["city"]

school["name"] = "მე-5 საჯარო სკოლა"

print(school)