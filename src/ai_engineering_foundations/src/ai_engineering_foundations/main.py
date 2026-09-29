from ai_engineering_foundations import greet


def main() -> None:
    name = input("Enter your name: ")
    print(greet(name))

    if __name__ == "__main__":
        main()
