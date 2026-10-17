#2) მომხმარებელს შემოაყვანინე პაროლი. isalnum() მეთოდით შეამოწმე, შედგება თუ არა იგი მხოლოდ ასოებისგან ან/და ციფრებისგან, ხოლო isupper() მეთოდით შეამოწმე, არის თუ არა ყველა ასო დიდი. დაბეჭდე ორივე შემოწმების შედეგი (True/False).


password = input('type a password: ')
print(password.isalnum())
print(password.isupper())