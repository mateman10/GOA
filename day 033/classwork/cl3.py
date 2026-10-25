# 3) შექმენი ორი Set სახელად `students1` და `students2`. პირველში შეინახე 4 მოსწავლის სახელი, ხოლო მეორეში  4 მოსწავლის სახელი. გამოიყენე 
# `union()` მეთოდი, რათა მიიღო ყველა უნიკალური მოსწავლის სახელი. შემდეგ გამოიყენე `len()` 

students1 = {"mate", "nika", "giorgi", "zura"}
students2 = {"kaxa", "toma", "tornike", "temo"}

students = students1.union(students2)

print(len(students))