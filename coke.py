print("Amount Due: 50")
price_to_pay = 50

while price_to_pay > 0:
    n = int(input("Insert Coin: "))

    if n == 5 or n == 10 or n == 25:
        #in case the amount inputed is more than they money due
        if n > price_to_pay:
            print(f"Change Owed: {n - price_to_pay}")
            break

        #if not do this
        price_to_pay -= n #price_to_pay = price_to_pay - n

        if price_to_pay == 0:
            print(f"Change Owed: 0")
            break

        #if the conditions above are not met, it means you're not done paying
        print(f"Amount Due: {price_to_pay}")

        #if the customer doesn't input the correct denomination, i.e 5, 10 & 15
    else:
        print(f"Amount Due: {price_to_pay}")
