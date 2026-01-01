meat =["ham",3.99,50,"Sliced"]
cheese = ["cheddar",5.49,100,"sharp"]
condiment =["Mustard",1.99,75,"Spicy"]

#create deli department
deli_dept =[meat,cheese,condiment]

#print the initial deli department

print(f"Initial Deli List: {deli_dept}")
if "ham" in meat and meat[2] < 100:
    meat[2] = 100
# create seasonal meat list
seasonal_meat =["Turkey",4.50,100,"Sliced"]
deli_dept.append(seasonal_meat)

#remove the condiment list
deli_dept.remove(condiment)

# sort the list

deli_dept.sort()

print(f"Updated Deli List: {deli_dept}")  