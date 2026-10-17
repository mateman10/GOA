#6. მომხმარებელს შეაყვანინეთ რიცხვები. თუ მომხმარებელი შეიყვანს უარყოფით რიცხვს, გამოიყენეთ break. დადებითი რიცხვები დაამატეთ total ცვლადში და ბოლოს გამოიტანეთ ჯამი.

total = 0


while True:
    i = int(input('type a number: '))
    if i < 0:
        break
    total += i

print(total)