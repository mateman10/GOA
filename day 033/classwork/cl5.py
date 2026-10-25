# 5) შექმენი სამი Set სახელად `python_students`, `javascript_students` და `react_students`. თითოეულში შეინახე იმ მოსწავლეების სახელები, 
# რომლებიც შესაბამის ტექნოლოგიას სწავლობენ. გამოიყენე `union()` მეთოდი, რათა მიიღო ყველა უნიკალური მოსწავლის სახელი. შემდეგ გამოიყენე 
# `intersection()` მეთოდი `python_students` და `javascript_students` Set-ებზე, რათა იპოვო მოსწავლეები, რომლებიც ორივე ტექნოლოგიას
#  სწავლობენ. ორივე შედეგი დაბეჭდე ეკრანზე

python_students = {"mate", "nika", "giorgi", }
javascript_students = {"kaxa", "toma", "tornike", }
react_students = {"zura", "temo", "noe"}
py1 = python_students.union(javascript_students)
py = python_students.intersection(javascript_students)

print(py)
print(py1)