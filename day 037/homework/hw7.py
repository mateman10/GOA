# 7) შექმენი Dictionary სახელად movie, რომელშიც შეინახავ ფილმის სახელს, რეჟისორს, გამოშვების წელს და ჟანრს. 
# მომხმარებელს შემოატანინე Key და შეამოწმე in ოპერატორით, არსებობს თუ არა ის Dictionary-ში. 
# შემდეგ წაშალე year Key და დაბეჭდე საბოლოო Dictionary.


movie = {
    "title": "The Matrix",
    "director": "The Wachowskis",
    "year": 1999,
    "genre": "i dont know",
    "user": input("type something: ")
}

print("user" in movie)


del movie["year"]

print(movie)