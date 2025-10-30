def unitConvert(unit = 'm', number = 0, newNum = None, newUnit = None):
    """Unit convertion program"""
    print("----------------Welcome---------------\nConvert Mass to Weight and vice versal")
    while True:
        try:
            if unit == 'm':
                result = number * 10
                print(f"\nYour result ==> {result}Kg\n")

            elif unit == 'w':
                result = number / 10
                print(f"\nYour result ==> {result}N\n")

            else:
                print("❌ Enter a valid input\n")
                continue


            convertAgain = input("Want to convert again?(y/n): ")
            if convertAgain != 'y':
                break

        except ValueError:
            print("\n❌ Enter a vaid number\n")
            continue


if __name__ == '__main__':
    unitConvert('w', 49.)
