#მომხმარებელს შეაყვანინეთ რიცხვები. სანამ მომხმარებელი არ შეიყვანს 0-ს, დაამატეთ რიცხვები total ცვლადში. 0-ის შეყვანისას გამოიყენეთ break და ბოლოს გამოიტანეთ ჯამი.

total = 0

while True:
    i = int(input('type a number: '))
    if i == 0:
        break
    total += i
print(total)