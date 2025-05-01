def main():
    string = input("Enter a sentence: ")
    def secondary():
        try:
            index = int(input("Enter a number: "))
            print(f"Character {index} is: {string[index]}")
        except ValueError:
            print("Please enter an integer instead!")
            secondary()
        except IndexError:
            print("Your number is bigger than your response!")
            secondary()
    secondary()
main()
