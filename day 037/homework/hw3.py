# 3) შექმენი Dictionary სახელად country, რომელშიც შეინახავ ქვეყნის სახელს, დედაქალაქს, 
# მოსახლეობას და ფართობს. მომხმარებელს შემოატანინე Key და in ოპერატორის გამოყენებით შეამოწმე, 
# არსებობს თუ არა ეს Key Dictionary-ში. დაბეჭდე შესაბამისი შეტყობინება.

country = {
    "name": "georgia",
    "capital": "tbilisi",
    "population": "3M",
    "area": "69 700 კმ²",
    "user": input("enter something: ")
}

print("user" in country)