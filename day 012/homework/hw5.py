#5. მომხმარებელს შემოატანინეთ რიცხვი n და while loop-ის გამოყენებით გამოთვალეთ 1-დან n-მდე ყველა ლუწი რიცხვის ჯამი.
total = 0
i = 1

n = int(input('type a number: '))

while i <= n:
    if i % 2 == 0:
        total += i
    i += 1

print(total)
    