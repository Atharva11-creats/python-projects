usd_val = int(input("enter your USD value:"))

def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD=",inr_val, "INR")

converter(usd_val)