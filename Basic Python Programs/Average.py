# a = 76
# b = 98
# c = 51
# print("Average of a,b & c is", (a+b+c)/3)

#_________________________________________

# By Taking Input From User
a = input("Enter First Number: ")
b = input("Enter Second Number: ")
c = input("Enter Third Number: ")

# Typecasting variables because it takes input as string
a = int(a)
b = int(b)
c = int(c)
avg = (a+b+c)/3
print("The Average of a,b & c is: ", avg)
