# 4) შექმენი Dictionary სახელად product, რომელშიც შეინახავ პროდუქტის სახელს, კატეგორიას, 
# ფასს და რაოდენობას. შემდეგ შეცვალე პროდუქტის ფასი და რაოდენობა ახალი მნიშვნელობებით.
# დაბეჭდე განახლებული Dictionary.


product = {
    "name": "xbox series S",
    "category": "console",
    "price": "$200",
    "quantity": 15,
}

product["price"] = "$250"

product["quantity"] = "20"

print(product)
