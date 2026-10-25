# 4) შექმენი სამი Set სახელად `monday`, `tuesday` და `wednesday`. თითოეულში შეინახე იმ მოსწავლეების სახელები, 
# რომლებიც შესაბამის დღეს გაკვეთილს დაესწრნენ. თითოეულ Set-ში უნდა იყოს მინიმუმ 5 სახელი და რამდენიმე 
# სახელი უნდა მეორდებოდეს. გამოიყენე `intersection()` მეთოდი, რათა იპოვო მოსწავლეები, რომლებიც სამივე დღეს ესწრებოდნენ გაკვეთილს.
# დაბეჭდე მიღებული შედეგი და მათი რაოდენობა.

monday = {"dato", "mate", "nikolozi", "giga", "temo"}

tuesday = {"mate", "nikolozi", "toma", "demetre", "otari"}

wednesday = {"gia", "grigoli", "mate", "nikolozi", "ilia"}

intersection = monday.intersection(tuesday, wednesday)

print(intersection)

print(len(intersection))