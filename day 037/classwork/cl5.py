# 5) შექმენი Dictionary სახელად game, რომელშიც შეინახავ თამაშის სახელს, ჟანრს და რეიტინგს. შემდეგ:
# დაამატე ახალი Key developer, რომელშიც შეინახავ თამაშის შემქმნელის სახელს.
# შეამოწმე in ოპერატორით, არსებობს თუ არა rating Key.
# წაშალე genre Key.
# შეცვალე თამაშის სახელი.
# დაბეჭდე საბოლოო ობიექტი.

game = {
    "name": "counter strike 2",
    "genre": "competetive",
    "rating": 5,
    
}

game["developer"] = "valve"

print("rating" in game)

del game["genre"]

game["name"] = "valorant"

print(game)