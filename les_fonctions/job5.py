def calcule(num1, operator, num2):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "%":
        print(num1 % num2)
    else:
        return

(calcule(8, "*", 4))
