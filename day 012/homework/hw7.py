#7. მომხმარებელს შეაყვანინეთ რიცხვები. თუ შეიყვანს 0-ს, გამოიყენეთ break. ყველა დადებითი რიცხვი დაამატეთ total ცვლადში, ხოლო უარყოფითი რიცხვები გამოტოვეთ.

total = 0

while True:
    i = int(input('type a number: '))
    if i == 0:
        break
    if i > 0:
        total += i
print(total)