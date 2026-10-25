# 5) შექმენი ორი Set სახელად `available_books` და `new_books`. პირველში შეინახე ბიბლიოთეკაში არსებული
# 6 წიგნის სახელი, ხოლო მეორეში — 4 ახალი წიგნის სახელი. ზოგიერთი წიგნი ორივე Set-ში უნდა გვხვდებოდეს. 
# თავდაპირველად გამოიყენე `intersection()` მეთოდი, რათა გაიგო, რომელი ახალი წიგნები უკვე არსებობს ბიბლიოთეკაში. 
# შემდეგ გამოიყენე `union()` მეთოდი, რათა მიიღო ბიბლიოთეკის განახლებული წიგნების სია. 
# დაბეჭდე ორივე შედეგი და საბოლოო წიგნების რაოდენობა.

available_books = {"python for begginers", "c++ for begginers", "html for begginers", "javascript for begginers", "java for begginers", "css for begginers"}

new_books = {"python for begginers", "c++ for begginers", "PHP for begginers", "c# for begginers"}

intersection = available_books.intersection(new_books)

print(intersection)

all = available_books.union(new_books)

print(all)

print(len(all))