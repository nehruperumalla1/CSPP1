# Functions - Assignment-3 - Using Bisection Search to Make the Program Faster

# value as you did in Assignment 2.

def debt_topay(balance_amount, ann_interest_rate, amount):
    balance_amount_temp = balance_amount
    index = 1
    while index <= 12:
        month_intr = ann_interest_rate/12
        month_up_bal = balance_amount_temp - amount
        balance_amount_temp = month_up_bal + (month_intr*month_up_bal)
        index = index+1
    return balance_amount_temp

def payingbebtoffinayear(balance, annual_interestrate):

    balance_amount_temp = balance
    approx_amnt = 0.03
    month_intr = annual_interestrate/12.0
    high = (balance*(1+month_intr)**12)/12.0
    low = balance/12
    middle = (low + high)/2.0
    while abs(debt_topay(balance_amount_temp, annual_interestrate, middle)) >= approx_amnt:
        if approx_amnt < debt_topay(balance_amount_temp, annual_interestrate, middle):
            low = middle
        else:
            high = middle
        middle = (low + high)/2.0
    num = middle
    return "Lowest Payment: "+str(round(num, 2))
def main():
    '''Main Function'''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebtoffinayear(data[0],data[1]))
if __name__== "__main__":
    main()
