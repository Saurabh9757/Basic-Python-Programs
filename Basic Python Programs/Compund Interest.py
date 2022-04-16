p=int(input("Enter principle amount(in INR): "))
r=int(input("Enter rate of interest(in %): "))
t=int(input("Enter time(in years): "))
CI=p*(1+r/100)**t
print("The principle amount is INR {} and the rate of interest is {} % and the time is {} years and its compund interest is INR {}.".format(p,r,t,CI))
input()  
