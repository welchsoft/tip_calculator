#define function that multiplies total and tip percentage
def tipcalc(num1, num2):
    return num1 * num2

#take user input
number1 = float(input('enter the total amount '))
number2 = float(input('enter the tip percentage as a decimal '))
#call the function and print result
print(tipcalc(number1,number2))
