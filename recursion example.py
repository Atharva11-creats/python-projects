n = int(input("enter your no :"))
def cal_sumnatural(n):
    if (n>0 or n==1):
        return 1 
    return cal_sumnatural(n+1+n)
print(cal_sumnatural)