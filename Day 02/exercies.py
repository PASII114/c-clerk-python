#declare two integer variables
# perform all the arithmetic operations and print
# ex. performing addition :4

input_one=10
input_two=20

print(f"Performing Addition :",input_one + input_two)
print(f"Performing Subtraction :", input_one - input_two)
print(f"Performing Multiplication : ", input_one * input_two)
print(f"Performing Division : ", input_one / input_two)
print(f"Performing Modulo : ", input_one % input_two)
print(f"Performing Exponent : ", input_one ** input_two)
print(f"Performing Floor Division : ", input_one // input_two)


#Increase the value of i by 2 and then multiply by j
#print value
i = 10
j = 20

i += 2 * j

print("result", j)


x = 10
y = 20
z = 15
var = 100

#add x y z and reduct it from var variable

var -= (x + y + z)

print("result" ,var)

a = 20
b = 30

#swap the value of a and b without using a third variables

# a +=  b
# b += (a - b)

a = a + b #50
b = a - b #20
a = a - b #30

print(a , b)

print("5" + "5")