name ="bro"
print(type(name))
age = 21
age +=1
print("Your age is "+str(age))
print(name.capitalize())
print(name.replace("o","a"))
rows = int(input("How many rows do you have?"))
column = int(input("How many columns do you have"))
symbol = input("Choose the symbol to draw")
for i in range(rows):
    for j in range(column):
        print(symbol,end=" ")
    print()

