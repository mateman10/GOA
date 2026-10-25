# 4) შექმენი ორი Set სახელად `colors1` და `colors2`. პირველში შეინახე ფერები: `red`, `green`, `blue`, `yellow`, ხოლო მეორეში  
# `blue`, `yellow`, `black`, `white`. გამოიყენე `intersection()` მეთოდი, რათა გაიგო, რომელი ფერები მეორდება ორივე Set-ში. მიღებული შედეგი დაბეჭდე ეკრანზე.

colors1 = {"red", "green", "blue", "yellow"}

colors2 = {"blue", "yellow", "black", "white"}

colors = colors1.intersection(colors2)

print(colors)