#1) კომენტარების სახით ახსენით რა არის input() ფუნქცია და რისთვის გამოიყენება.


#input ფუნქცია მომხმარებლისგან მოაქვს ინფორმაცია.


#2) მომხმარებელს შემოატანინეთ თავისი სახელი და დაბეჭდეთ, რა სახელი შემოიტანა.


name = input("whats ur name")

print("ur name:",name)


#3) მომხმარებელს შემოატანინეთ თავისი საყვარელი ფერი და დაბეჭდეთ.


fav_colour = input("whats ur fav colour?")

print("ur fav colour:",fav_colour)


#4) კომენტარებით ახსენით, რა არის f-string და რატომ არის მისი გამოყენება მოსახერხებელი.

#f string გამოიყენება  ცვლადების მარტივად დასაწერათ


#5) მომხმარებელს შემოატანინეთ თავისი ასაკი და f-string-ის გამოყენებით დაბეჭდეთ:
#I am {ასაკი} years old


age = input("whats ur age?")

print(f"i am{age}yrs old")


#6) მომხმარებელს შემოატანინეთ თავისი გვარი და f-string-ის გამოყენებით დაბეჭდეთ:

gvari = input("ra_gvari_xar?")

print(f"me var{gvari}")


#7) მომხმარებელს შემოატანინეთ თავისი საყვარელი ცხოველი და დაბეჭდეთ:
#My favorite animal is {ცხოველი}

fav_animal = input("whats ur fav animal?")


print(f"my fav animal is{fav_animal}")

#8) მომხმარებელს შემოატანინეთ თავისი საყვარელი სპორტი და დაბეჭდეთ:
#I like {სპორტი}

fav_sport = input("whats ur fav sport?")

print(f"my fav sport is{fav_sport}")


#9) მომხმარებელს შემოატანინეთ ქალაქის სახელი და ქვეყანა. შემდეგ f-string-ის გამოყენებით დაბეჭდეთ:
#I live in {ქალაქი}, {ქვეყანა}

city = input("which city are u living?")

country =input("which country are u living?")

print(f"i live in {city}, {country}")


#10) მომხმარებელს შემოატანინეთ თავისი სახელი, ასაკი და საყვარელი ფერი. შემდეგ f-string-ის გამოყენებით დაბეჭდეთ:
#My name is {სახელი}, I am {ასაკი} years old and my favorite color is {ფერი}.

age = input("whats ur age?")

name =input("whats ur name?")

fav_colour = input("whats ur fav colour?")

print(f"my name is {name}, i am {age}years old and my fav colour is {fav_colour}")