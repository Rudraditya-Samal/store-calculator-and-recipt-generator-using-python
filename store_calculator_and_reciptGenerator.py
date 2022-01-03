from datetime import date

today = date.today()
Date = today.strftime("%d/%m/%Y")

sum = 0

Shop_name = input('Enter Shop name:\t')

SGST = input('Enter SGST(%):\t')
SGST = int(SGST)

CGST = input('Enter CGST(%):\t')
CGST = int(CGST)

Carry_bagCost = input('Enter Carry bag cost:\t')
Carry_bagCost = int(Carry_bagCost)

while (True):
    UserInput = input('\nEnter the Order:\t')
    if (UserInput!='q'):
        sum = sum + int(UserInput)
        print(f"Price so far:\t ₹{sum}")
    else :
        name = input('\nEnter customers name:\t')
        print('\n' + Shop_name + ' ' + 'Recipt')
        print(f'Customers name:\t{name}')
        print(f"Due date:\t{Date}")
        print(f"bill is:\t ₹{sum}")
        print(f"SGST:\t {SGST}%")
        print(f"CGST:\t {CGST}%")
        print(f"Carry bag Cost is:\t ₹{Carry_bagCost}")
        print(f"Total bill is:\t ₹{sum * SGST * CGST + Carry_bagCost}")
        print("Thanks for shopping 😁🙏")
        


        