def main():
    try:
        value = int(input("Enter a number: "))
        print(f"The number you entered was {value}.")
    except ValueError:
            print("Try again.")
            main()
main()
    