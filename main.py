import os


def __clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        line = input(">>> ")

        if line == "clear":
            __clear()
            continue

        if line == "exit":
            break


if __name__ == "__main__":
    main()
