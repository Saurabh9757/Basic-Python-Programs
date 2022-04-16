a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a>b:
    if a>c:
        print("Bigger Number= "+str(a))
    else:
        print("Bigger Number= "+str(c))
else:
    if b>c:
        print("Bigger Number= "+str(b))
    else:
        print("Bigger Number= "+str(c))

    if a>b and a>c:
                  print("Bigger Number= "+str(a))
    if b>a and b>c:
                  print("Bigger Number+ "+str(b))
    if c>a and c>b:
                  print("Bigger Number= "+str(c))

    if a==b and a==c:
                  print("All are equal")


        
