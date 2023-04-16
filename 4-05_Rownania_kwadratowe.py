zadanie = "Equation a*x**2 + b*x + c == 0"
print(zadanie)

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

delta = (b * b) - 4 * (a * c)
print(f'Delta ma wartość: {delta}')

if delta > 0:
    x_1 = (-b - delta ** 0.5) / (2 * a)
    x_2 = (-b + delta ** 0.5) / (2 * a)
    print("Pierwiastki równania kwadratowego:")
    print(f"x_1 = {x_1}")
    print(f"x_2 = {x_2}")
elif delta == 0:
    x_1 = (-b - delta ** 0.5) / (2 * a)
    x_2 = (-b + delta ** 0.5) / (2 * a)
    print("Pierwiastki równania kwadratowego:")
    print(f"x_1 = {x_1}")
    print(f"x_2 = {x_2}")
else:
    print("no solution")
