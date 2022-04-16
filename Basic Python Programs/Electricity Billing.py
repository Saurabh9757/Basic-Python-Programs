CR=int(input("Enter Current Reading: "))
PR=int(input("Enter Previous Reading: "))
TU=CR-PR
if TU>=0 and TU<100:
    AMT = TU*5.5
elif TU > 100 and TU <= 200:
    AMT = (100*5.5)+(TU-100)*6
elif TU>200 and TU<=300:
    AMT =(100*5.5)+(100*6)+(TU-200)*6.5
elif TU>300:
    AMT =(100*5.5)+(100*6)+(100*6.5)+(TU-300)*7.5
else:
    print("Invalid")
print("Amount(in INR)= ", AMT)
input()
