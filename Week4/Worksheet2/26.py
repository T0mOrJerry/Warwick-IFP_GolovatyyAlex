while True:  # The program will work as long as user want it to work
    # Input block
    customer_id = input("type customer's id: ")
    customer_name = input("type customer's name: ")
    # The text of the problem was unclear - I've taken units as the amount of money customer has to pay
    unit = int(input('type unit consumed by the user in £: '))
    if unit < 100:  # Check whether the bill is big enough
        print("That's miserable! Bill should be at least £100")
    else:
        if unit > 400:  # Check whether we need to take extra money from the customer
            print(f'customer {customer_id} - {customer_name} should pay £{(unit / 100) * 115}')
        else:
            print(f'customer {customer_id} - {customer_name} should pay £{unit}')
    # Ask user if they want to exit the program
    a = input("type y/n weather you do or don't want to exit the program: ")
    if a == 'y':
        break
