#A cashier program 
    # Input:  The number of product, the price of each product, the money customer give
    # Output: The total price of products, the money costumer give, the number of each money type to return
    # Money return list =[500,200,100,50,20,10,5,1]
import math
def calc_total_price(number, price):
    return (number * price)


def calc_money_return(money_pay, total_price):
    if money_pay < total_price:
        return -1
    
    return (money_pay - total_price)
    
def money_back_infor(total):
    count = 0
    left_over = 0
    List_of_money  = [500,200,100,50,20,10,5,1]
    List_of_number = []
    for i in range (len(List_of_money)):
        count = math.floor(total/List_of_money[i])
        total = total - (List_of_money[i] * count)
        List_of_number.append(count)

    print("Information about return money to customer")
    for i in range (len(List_of_money)):
        print("The number of "+ str(List_of_money[i]) + ": " + str(List_of_number[i]))



price = float(input("Enter the price of each product: "))
number = int(input(("Enter the number of products: ")))
money_pay = int(input("Enter the number costumer give: "))

total_price = calc_total_price(number,price)
money_back = calc_money_return(money_pay, total_price)
print("The total price of products "+ str(total_price) + " k VND")
print("The money customer give:  "+ str(money_pay) + " k VND")
if money_back == -1:
    print("Not enough money")
else:
    print("The money return: " + str(money_back) + " k VND")
    money_back_infor(money_back) 



