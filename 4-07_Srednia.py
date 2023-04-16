numbers = []
n = int(input("Enter n: "))

i = 0
while i < n:
    numbers.append(int(input("Enter a number: ")))
    i += 1
print(f"Entered numbers: {numbers}")

suma = sum(numbers)
print(f"Sum = {suma}")

average = int(suma / n)
print(f"average = {average}")

if suma > average:
    print("The sum is greater!")
