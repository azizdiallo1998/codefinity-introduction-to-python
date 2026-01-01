vegetables = ["tomatoes", "potatoes", "onions"]
vegetables. remove("onions")
if "carrots" not in vegetables:
    vegetables.append("carrots")
    print("Carrots are already in the list")
elif "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("carrots are already in the list")
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
    print("cucumbers are already in the list")
elif "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("cucumbers are already in the list")

vegetables.sort()

print(f"Updated Vegetable Inventory: {vegetables}""")