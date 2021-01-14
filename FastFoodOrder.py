# Create menu
menu = {"chicken sandwich": 4.50, "burger": 5.00, "small fries": 2.00, "large fries": 3.00,
        "vanilla shake": 4.00, "small coke": 1.50, "large coke": 2.50}

# Greet user
print("Hi, welcome to McDick's!")


# Take order
def take_order():
    total = 0
    order_list = []
    order = input("What would you like to order?")
    split_order = order.split(", ")
    for item in split_order:
        if item in menu:
            total += menu[item]
            order_list.append(item)
        else:
            print(f"\t>>Sorry, but {item} is not on the menu.")
            continue
    print(f"\t>>Your current total is: ${total:.2f}")

    # Continue to ask if customer wants anything else, until they specify no
    order_more_status = True

    while order_more_status:
        ask_for_more = input("Would you like to order anything else?")
        if ask_for_more == "yes":
            order_more = input("What else would you like?")
            split_order_more = order_more.split(", ")
            for item in split_order_more:
                if item in menu:
                    total += menu[item]
                    order_list.append(item)
                else:
                    print(f"\t>>Sorry, but {item} is not on the menu.")
                    continue
            print(f"\t>>Your current total is: ${total:.2f}")
        elif ask_for_more == "no":
            print(f"\t>>You have ordered: {order_list}")
            print(f"\t>>Your final total is: ${total:.2f}. Have a great day!")
            order_more_status = False
        else:
            print(">>Sorry, I didn't understand that.")
            continue


take_order()