# 1) შექმენი ორი Set სახელად `fruits1` და `fruits2`. პირველში შეინახე 5 ხილი, ხოლო მეორეში 5 ხილი.
# გამოიყენე `union()` მეთოდი, რათა მიიღო ორივე Set-ის ყველა უნიკალური ხილი და დაბეჭდე მიღებული შედეგი.

fruits1 = {"banana", "apple", "mango", "dragonfruit", "watermelon"}
fruits2 = {"banana", "apple", "mango", "peach", "watermelon"}

fruits = fruits1.union(fruits2)

print(fruits)