# 3) შექმენი ცარიელი set, სახელად names. მომხმარებელს სთხოვე 7 ადამიანის სახელის შეყვანა.
# გამოიყენე for ციკლი სახელების შესაყვანად და თითოეული სახელი დაამატე Set-ში. 
# ბოლოს დაბეჭდე Set და მისი ელემენტების რაოდენობა len() ფუნქციის გამოყენებით.

names = set()



for i in range(7):
    name = input("input 7 human names: ")
    names.add(name)

print(names)

print(len(names))