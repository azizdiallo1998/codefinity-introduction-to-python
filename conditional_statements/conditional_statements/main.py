# Input variables
product_type = "Dialllo"
day_of_week   = "Tuesday"

# Step 1: Fruits on Monday
if product_type == "Fruits" and day_of_week == "Monday":
    print("10% discount on Fruits today!")

# Step 2: Vegetables on Tuesday
elif product_type == "Vegetables" and day_of_week == "Tuesday":
    print("15% discount on Vegetables today!")

# Step 3: Dairy on Wednesday
elif product_type == "Dairy" and day_of_week == "Wednesday":
    print("20% discount on Dairy today!")

# Step 4: Other products (regardless of day)
elif product_type == "Other":
    print("No discount available.")

# Step 5: everything else
else:
    print("No special discounts today.")