# 2) შექმენი ორი Set სახელად `favorite_movies` და `popular_movies`. პირველში შეინახე 5 შენი საყვარელი ფილმის სახელი, 
# ხოლო მეორეში — 6 პოპულარული ფილმის სახელი. დარწმუნდი, რომ რამდენიმე ფილმი ორივე Set-ში გვხვდება. გამოიყენე 
# `intersection()` მეთოდი, რათა იპოვო ფილმები, რომლებიც ორივე Set-შია. დაბეჭდე მიღებული შედეგი.


favorite_movies = {"dont  got fav film", 1, 2, 3, 4, }

popular_movies = {"i dont know", 3, 4, 7, 8, 9}

intersection = favorite_movies.intersection(popular_movies)

print(intersection)