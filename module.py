import os

def list_directory_contents(path):
    try:
        with open(path, 'r') as file:
            print(path)
    except FileNotFoundError:
        print("File not found")

def main():


    while True:
        if choice == "1":
            path = "trees.txt"
            list_directory_contents("trees.txt")
        elif choice == "2":
            list_directory_contents("flowers.txt")
        elif choice == "3":
            break
        else:
            print("Please choose '1', '2', or '3': ")

if __name__ == "__main__":
    main()
        