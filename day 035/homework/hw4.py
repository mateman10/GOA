# 4) შექმენი list, რომელშიც შეინახავ 12 რიცხვს. გამოიყენე while ციკლი და დაბეჭდე 
# მხოლოდ უარყოფითი რიცხვები. ყველა დადებითი რიცხვი კი დაამატე ცალკე tuple-ში 
# (შეგიძლია ჯერ ცალკე List გამოიყენო და შემდეგ Tuple-ად გადააქციო).

nums = [-2,2,4,-4,7,-8,22,-34,44,-64,11,-53]

nums_tuple = []
i = 0
while i < len(nums):
    if nums[i] < 0:
        print(nums[i])
    else:
        nums_tuple.append(nums[i])
    i += 1

numbers_tuple = tuple(nums_tuple)

print(numbers_tuple)