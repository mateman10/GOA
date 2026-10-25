


number = 20
user = int(input("type ur number: "))
i = 0
while i != 3:
    
    if user > number:
        print('ეს რიცხვი მეტია')
    elif user < 20:
        print('ეს რიცხვი ნაკლებია')
    elif user == number:
        print("მოიგე")
    elif i == 3:
        print("you lost")
    else:
        print()
    i += 1
    
#ცვლადში უნდა შეინახო ჩაფიქრებული რიცხვი. მომხმარებლს უნდა შემოატანინო რაიმე რიცხვი და ასევე მისცე სამი ცდა რიცხვის გამოცნობის, თუ არასწორად შემოიყვანა რიცხვი უნდა გამოუტანო ტექსტი, 'too low' ან 'too high', იმის მიხედვით შემოყვანილი რიცხვი ჩაფიქრებულზე მეტი იყო თუ ნაკლები. ცდების ამოწურვის შემთხვევაში გათიშე პროგრამა და დაბეჭდე 'you lost', გამოცნობის შემთხვევაში კი 'you win'

# if user > number:
#     print('ეს რიცხვი მეტია')
# elif user < 20:
#     print('ეს რიცხვი ნაკლებია')
# elif user == number:
#     print("მოიგე")
# elif i == 3:
#     print("you lost")

    
