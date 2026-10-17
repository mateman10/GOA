#7. Nested for loop-ის გამოყენებით შექმენით 5x5 კვადრატი, მაგრამ მესამე ვარსკვლავი არ დაბეჭდოთ. გამოიყენეთ continue



for i in range(5):
    for j in range(5):
        if j == 3:
            continue
        print("*", end = " ")

    print()
