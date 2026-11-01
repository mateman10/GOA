# დავალება 4:
# შექმენი tuple, რომელშიც შეინახავ 8 რიცხვს. for ციკლის გამოყენებით იპოვე და დაბეჭდე მხოლოდ ლუწი რიცხვები.
# შემდეგ ყველა კენტი რიცხვი დაამატე ცალკე list-ში და დაბეჭდე მიღებული სია.

nums_tuple = (5,3,6,8,3,23,2,8)


odd_nums_list = []

print("ლუწი რიცხვები:")

for num in nums_tuple:
    if num % 2 == 0:
        print(num)
    else:odd_nums_list.append(num)

print(odd_nums_list)