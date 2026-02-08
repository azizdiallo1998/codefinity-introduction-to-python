# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

apple_count = shelf.count("apples")
banana_index = shelf.index("bananas")
print(f"Number of Apples: {shelf.count("apples")}")

print(f"First Banana Index:{shelf.index("bananas")}")


if shelf.count("apples") < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
grape_count = shelf.count("grapes")

if grape_count == 1:
    print("grapes need to be restocked.")
else:
    print("grapes are sufficiently stocked.")

if "oranges" in shelf:
    idx = shelf.index("oranges")
    print(f"Oranges are at index: {idx}")
else:
    print("Oranges are out of stock.")
