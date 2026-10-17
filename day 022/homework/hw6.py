#6) შექმენი სია words = ["hello", "world", "python"]. uppercase მეთოდების და join-ის გამოყენებით, შეაერთე ეს სიტყვები ტირეთი ("-") ისე, რომ თითოეული სიტყვის პირველი ასო იყოს დიდი (გამოიყენე title() ან capitalize()). დაბეჭდე შედეგი.

words = ["hello", "world", "python"]

new_words = ("-".join(words))

print(new_words.title())