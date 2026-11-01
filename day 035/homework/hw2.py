# 2) შექმენი tuple, რომელშიც შეინახავ 6 სხვადასხვა ცხოველის სახელს. გამოიყენე while ციკლი, 
# რათა თითოეული ცხოველის სახელი ცალ-ცალკე დაბეჭდო. შემდეგ ყველა ცხოველი დაამატე 
# ახალ list-ში და დაბეჭდე სია.

animals = ("lion", "wolf", "cat", "dog", "monkey", "horse")

animals_list = list()

i = 0

while i < len(animals):
    print(animals[i])
    animals_list.append(animals[i])
    i += 1
    

print(animals_list)