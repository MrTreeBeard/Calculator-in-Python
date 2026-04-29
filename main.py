from models import Calculator

def run_calculator():
    calculator = Calculator()

    while True:
        print("\n=== Калкулатор ===")
        print("1. Събиране")
        print("2. Изваждане")
        print("3. Умножение")
        print("4. Деление")
        print("5. Процент")
        print("6. Степенуване")
        print("7. Корен")
        print("8. История")
        print("9. Изход")

        choice = input("Изберете операция (1-9): ").strip()

        if choice == "9":
            print("Край на програмата.")
            break

        if choice == "8":
            history = calculator.get_history()
            if not history:
                print("Все още няма извършени операции.")
            else:
                print("История на операциите:")
                for index, operation in enumerate(history, start=1):
                    print(f"{index}. {operation}")
            continue

        try:
            if choice in {"1", "2", "3", "4", "6"}:
                first_number = float(input("Въведете първо число: "))
                second_number = float(input("Въведете второ число: "))

                if choice == "1":
                    result = calculator.add(first_number, second_number)
                elif choice == "2":
                    result = calculator.subtract(first_number, second_number)
                elif choice == "3":
                    result = calculator.multiply(first_number, second_number)
                elif choice == "4":
                    result = calculator.divide(first_number, second_number)
                else:
                    result = calculator.power(first_number, second_number)

                print(f"Резултат: {result}")
            elif choice == "5":
                value = float(input("Въведете число: "))
                percent_value = float(input("Въведете процент: "))
                result = calculator.percent(value, percent_value)
                print(f"Резултат: {result}")
            elif choice == "7":
                value = float(input("Въведете число: "))
                degree = int(input("Въведете степен на корена: "))
                result = calculator.root(value, degree)
                print(f"Резултат: {result}")
            else:
                print("Невалиден избор. Опитайте отново.")
        except ValueError as error:
            print(f"Грешка: {error}")

if __name__ == "__main__":
    run_calculator()