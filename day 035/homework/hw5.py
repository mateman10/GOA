# 5) შექმენი ორი set, სახელად subjects1 და subjects2. თითოეულში შეინახე 5 სხვადასხვა სასკოლო საგანი.
#  გამოიყენე for ციკლი, რათა პირველი Set-ის ყველა ელემენტი დაბეჭდო. შემდეგ გამოიყენე union() 
# და intersection() მეთოდები და დაბეჭდე ორივე Set-ის გაერთიანება და საერთო ელემენტები.

subjects1 = {"Biology", "geography", "math", "germany", "history"}

subjects2 = {"music", "english", "pysic", "ED", "music"}

for i in subjects1:
    print(i)


all = subjects1.union(subjects2)

intersection = subjects1.intersection(subjects2)

print(all)

print(intersection)