#7) შექმენი ცვლადი message = "  Hello World  ". lstrip() მეთოდით მოაშორე ჰარები მხოლოდ მარცხნიდან, ხოლო [::-1] Slicing-ის გამოყენებით ამოატრიალე მთლიანი ტექსტი უკუღმა. დაბეჭდე შედეგი.

message = "  Hello World  "

new_message = message.lstrip()

print(new_message[::-1])