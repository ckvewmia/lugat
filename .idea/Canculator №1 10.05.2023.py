#                                                 Canculyator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Qo'shish")
print("2.Ayirish")
print("3.Ko'paytirish")
print("4.Ayirish")
while True:
    choice = input("Birini tanlang: (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Birinchi raqamni kiriting: "))
            num2 = float(input("Keyingi raqamni kiriting: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        next_calculation = input("Keyini hisobni kiritasizmi? (Ha/Yoq): ")
        if next_calculation == "Yoq":
            break
    else:
        print("Canculator")