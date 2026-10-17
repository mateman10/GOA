#4) მომხმარებელს შემოაყვანინე ტექსტი. replace() მეთოდით ყველა ჰარი (space) ჩაანაცვლე დეფისით ("-"), ხოლო upper() მეთოდით გადაიყვანე ყველა ასო დიდში. დაბეჭდე მიღებული ტექსტი.

text = input('type a text: ')

new_text = text.replace(" ", "-")

print(new_text.upper())