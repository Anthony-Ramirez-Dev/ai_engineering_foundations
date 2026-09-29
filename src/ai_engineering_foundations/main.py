from ai_engineering_foundations import greet


def main() -> None:
    print("AI Engineering Foundations")
    print("----------------------------")
    print("1. Greeting")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter your name: ")
        print(greet(name))
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
