# დავალება 2:
# შექმენი tuple, რომელშიც შეინახავ 7 სხვადასხვა ქალაქის სახელს. while ციკლის გამოყენებით დაბეჭდე თითოეული ქალაქი ცალ-ცალკე.
#  ციკლი უნდა გაგრძელდეს მანამ, სანამ Tuple-ის ყველა ელემენტს არ დაბეჭდავ.


citys = ("tbilisi", "batumi", "zestafoni", "gori", "kutaisi", "akhaltsikhe", "xoni")

i = 0

while i < len(citys):
    print(citys[i])
    i += 1