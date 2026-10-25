#გააკეთე ისეთი პროგრამე რომ ჯერ უსერ შეიყვანს colums მერე rows და სიმბოლოს
#ბოლოს მაგ სიმბოლოთი უნდა დახაზოს შესაბამისი ფიგურა როგორც Columns , rows 

colums = int(input('type a column range: '))
rows = int(input('type a row range: '))
symbol = input('type a symbol:  ')

for i in range(rows):
    for j in range(colums):
        print(symbol)
    
   