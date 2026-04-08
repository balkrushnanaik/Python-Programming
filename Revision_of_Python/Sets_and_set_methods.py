try:
    phone_brands = {"Apple", "Samsung", "Nokia", "Jio", "MI", "Apple"}
    print(phone_brands)

    phone_brands.add("Nothing")
    print(phone_brands)

    phone_brands.remove("Banana")
    print(phone_brands)

except Exception as e:
    print(e)

