import math
import argparse

parser = argparse.ArgumentParser(description="...")

parser.add_argument("--type", default=False)
parser.add_argument("--periods", type=float, default=False)
parser.add_argument("--interest", type=float, default=False)
parser.add_argument("--principal", type=float, default=False)
parser.add_argument("--payment", type=float, default=False)

args = parser.parse_args()

def validate_args(*args):
    for arg in args:
        if arg is False or arg < 0:
                return False
    return True

def calculate_diff(args):
    interest = args.interest / 100 / 12
    total_payment = calculate_and_print_payements(args.principal, args.periods, interest)
    print(f"\nOverpayment = {math.ceil(total_payment - args.principal)}")

def calculate_annuity(args):
    interest = args.interest / 100 / 12

    if args.payment and not args.principal:
        calculate_principal_and_overpayment(args.periods,args.payment, interest)
    elif args.principal and not args.periods:
        calculate_payment_periods_and_overpayment(args.principal,args.payment, interest)
    elif args.periods and not args.payment:
        calculate_payment_and_overpayment(args.principal,args.periods, interest)
    else:
        print("Incorrect parameters")

def calculate_and_print_payements(principal, periods, interest):
    total_payment = 0
    for i in range(1, int(periods) + 1):
        diff = (principal / periods) + interest * (principal - (principal * (i - 1)) / periods)
        print(f"Month {i}: payment is {math.ceil(diff)}")
        total_payment += math.ceil(diff)
    return total_payment

def calculate_principal_and_overpayment(periods, payment, interest):
    principal = payment / ((interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1))
    total_payment = payment * periods
    print(f"Your loan principal = {math.floor(principal)}")
    print(f"\nOverpayment = {math.ceil(total_payment - principal)}")

def calculate_payment_periods_and_overpayment(principal, payment, interest):
    periods = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
    months, years = divmod(periods, 12)

    if months:
        print(f"It will take {years} years and {months} months to repay this loan!")
    elif periods < 12:
        print(f"It will take {periods} months to repay this loan!")
    else:
        print(f"It will take {years} years to repay this loan!")

    total_payment = payment * periods
    print(f"\nOverpayment = {math.ceil(total_payment - principal)}")

def calculate_payment_and_overpayment(principal, periods, interest):
    payment = principal * (interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)
    rounded_payment = math.ceil(payment)
    print(f"Your monthly payment = {rounded_payment}!")
    print(f"\nOverpayment = {math.ceil(rounded_payment * periods - principal)}")
    
if not validate_args(args.periods, args.interest, args.principal, args.payment):
    print("Incorrect parameters")
else:
    if args.type == "diff":
        calculate_diff(args)
    elif args.type == "annuity":
        calculate_annuity(args)
    else:
        print("Incorrect parameters")
