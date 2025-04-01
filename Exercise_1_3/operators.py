# build cli tool get input from user
first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")
print(first_name, last_name)

## do math
a = input("Enter the a side of triangle: ")
b = input("Enter the b side of the triangle: ")
c_squared = int(a) ** 2 + int(b) ** 2
print("a^2 + b^2 = c^2; c^2 is ",c_squared, "c is ", c_squared ** .5)

## comparison
drinking_age = 21
customer_age = input("What is your age, don't lie I will know: ")
if(int(customer_age) < drinking_age):
    print("sorry kid come back in a few years")
else:
    print("family....")


#range based for loop
#range(start, end, step)
for i in range(0, 100, 5):
    print(i)