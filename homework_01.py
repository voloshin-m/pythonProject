def calculator(a, b, oper):
    result = str(a) + " " + oper + " " + str(b) + " = "
    if oper in ("/", "//", "%") and b == 0:
        result = "На ноль делить нельзя"
    elif oper == "+":
        result += str(a + b)
    elif oper == "-":
        result += str(a - b)
    elif oper == "*":
        result += str(a * b)
    elif oper == "/":
        result += str(a / b)
    elif oper == "//":
        result += str(a // b)
    elif oper == "%":
        result += str(a % b)
    elif oper == "^":
        result += str(a ** b)
    else:
        result = "Я не знаю такой операции"
    return result


a = float(input("Введите первое значение: "))
b = float(input("Введите второе значение: "))
oper = input("Введите операцию (+ сложение, - вычитание,"
             "\n* умножение, / деление, ^ возведение в степень,"
             "\n// целочисленное деление, % остаток от деления): ")
print(calculator(a, b, oper))
