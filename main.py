import qrcode
import os
from datetime import datetime as dt

def greet():
    print("=" * 40)
    print("🌟 WELCOME TO QR GENERATOR 🌟")
    print("\n", "=" * 40)

def history():
    while True:
        print("\n", "=" * 40)
        print("\n1.View history\n2.Search Qr\n3.Delete History\n4.Exit")
        print("\n", "=" * 40)

        history_in = input("\nEnter your choice(in digit)")

        if history_in == "1":
            try:
                with open("history.txt", "r") as file:
                    readed = file.readlines()

                    if len(readed) == 0:
                        print("\n!!history is empty!!")
                        continue

                    for number, line in enumerate(readed, start=1):
                        print(number, ".", line.strip())

                    print("📊 Total QR Codes Generated: ", len(readed))

            except Exception as e:
                print("📁 file not found", e)

        elif history_in == "2":
            try:
                search = input("\nEnter QR Name : ")

                with open("history.txt", "r") as file:
                    readeed = file.readlines()

                for line in readeed:
                    if search in line:
                        print(line.strip())

            except Exception as e:
                print(e)

        elif history_in == "3":
            conform = input("\nAre You sure(yes/no) : ").lower()

            if conform == "yes":
                open("history.txt", "w").close()

        elif history_in == "4":
            return

        else:
            print("Enter appropriate value")

def menu():
    while True:
        try:
            print("=" * 40)
            print("\n1.Generate QR\n2.History\n3.Exit")
            print("=" * 40)

            menu_choice = input("Enter your choice: ")

            if menu_choice == "1":
                work()

            elif menu_choice == "2":
                history()

            elif menu_choice == "3":
                break

            else:
                print("Enter appropriate input")

        except Exception as e:
            print("something went wrong", e)

def work():
    url = input("\n🔗 Enter Text / URL: ")

    if url == "":
        print("URL cannot be empty")
  return

 qrcoe
import os
from datetime import datetime as dt

def greet():
    print("=" * 40)
    print("🌟 WELCOME TO QR GENERATOR 🌟")
    print("\n", "=" * 40)

def history():
    while True:
        print("\n", "=" * 40)
        print("\n1.View history\n2.Search Qr\n3.Delete History\n4.Exit")
        print("\n", "=" * 40)

        history_in = input("\nEnter your choice(in digit)")

        if history_in == "1":
            try:
                with open("history.txt", "r") as file:
                    readed = file.readlines()

                    if len(readed) == 0:
                        print("\n!!history is empty!!")
                        continue

                    for number, line in enumerate(readed, start=1):
                        print(number, ".", line.strip())

                    print("📊 Total QR Codes Generated: ", len(readed))

            except Exception as e:
                print("📁 file not found", e)

        elif history_in == "2":
            try:
                search = input("\nEnter QR Name : ")

                with open("history.txt", "r") as file:
                    readeed = file.readlines()

                for line in readeed:
                    if search in line:
                        print(line.strip())

            except Exception as e:
                print(e)

        elif history_in == "3":
            conform = input("\nAre You sure(yes/no) : ").lower()

            if conform == "yes":
                open("history.txt", "w").close()

        elif history_in == "4":
            return

        else:
            print("Enter appropriate value")

def menu():
    while True:
        try:
            print("=" * 40)
            print("\n1.Generate QR\n2.History\n3.Exit")
            print("=" * 40)

            menu_choice = input("Enter your choice: ")

            if menu_choice == "1":
                work()

            elif menu_choice == "2":
                history()

            elif menu_choice == "3":
                break

            else:
                print("Enter appropriate input")

        except Exception as e:
            print("something went wrong", e)

def work():
    url = input("\n🔗 Enter Text / URL: ")

    if url == "":
        print("URL cannot be empty")
        return

