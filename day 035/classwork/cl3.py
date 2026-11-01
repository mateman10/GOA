# დავალება 3:
# შექმენი list, რომელშიც მომხმარებლის მიერ შეყვანილი 5 საყვარელი ხილი იქნება შენახული. 
# გამოიყენე for ციკლი და თითოეული ხილი დაამატე set-ში. ბოლოს დაბეჭდე Set, რათა ნახო, რომელი უნიკალური ხილები შეიყვანა მომხმარებელმა.

user_fruits = []

print("type ur fav 5 fruits:")

for i in range(5):
    fruit = input(f"fruits {i + 1}: ")
    user_fruits.append(fruit)

set_fruits = set()

for fruit in user_fruits:
    set_fruits.add(fruit)

print(set_fruits)