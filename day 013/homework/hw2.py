#2) მომხმარებელს შემოატანინე რიცხვი და დათვალე, რამდენი რიცხვია 1-დან ამ რიცხვამდე ისეთი, რომელიც 3-ზე იყოფა.

i = int(input('type a number: '))
total = 0
for n in range(1, i):
    if n % 3 == 0:
        total += 1
print(total)