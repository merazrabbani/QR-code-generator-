import qrcode as qr
import os 
from datetime import datetime as dt
def greet():
    print("=" * 40)
    print("🌟 WELCOME TO QR GENERATOR 🌟")
    print("\n","=" * 40)
def history():
    while True:
        print("\n", "=" * 40)
        print("\n1.View history\n2.Delete History\n3.Exit")
        print("\n", "=" * 40)
        history_in= input("\nEnter your choice(in digit)")
        if history_in == "1":
            try:             
                with open("history.txt", "r") as file:
                      readed = file.readlines()
                      if len(readed) == 0:
                          print("\n!!history is empty!!")
                          continue
                      else:
                          for number, line in enumerate(readed, start=1):
                              print(number, ".",line.strip()) 
                          print("📊 Total QR Codes Generated: ", number)                  
                          continue
            except Exception as e:
                print("📁file not found", e)                                     
            
        elif history_in == "2":
            open("history.txt", "w").close()
            continue
        elif history_in == "3":
             return 
        else:
             print("Enter apprioprate value")
             continue
def menu():
    while True:
         try:
            print("=" * 40)
            print("\n1.Generate QR\n2.History\n3.Exit")
            print("=" * 40)
            menu_choice = input("Enter you choice (in numbers) : ")
            if menu_choice == "1":
                work()
            elif menu_choice == "2":
                history()
            elif menu_choice == "3":
                 break
            else:
                 print("Enter appriopriate input")
         except Exception as e:
             print("something went wrong", e)
             continue
def work():
    url = input("\n 🔗 Enter Text / URL: ")
    if url == "":
        print("\nURLcannot be empty")
        return work()
    if not os.path.exists("QR codes"):
        os.mkdir("QR codes")
    file_n = input(" Enter the name : ")
    if file_n == "":
        print("\nName cannot be empty")
        return work()
    elif os.path.exists("QR codes/"+file_n+".png"):
        print("⚠️ ", file_n, "already exists.")
        return work()
    make = qr.make(url)
    make.save("QR codes/"+file_n+".png")
    print("\n✅ QR Code Generated Successfully!")
    print("📁 Saved as: ",file_n+".png")
    t = dt.now()
    current_time = t.strftime("%d/%m/%Y  %H:%M:%S   ")
    with open("history.txt", "a") as file:
        file.write(f"{url} | {file_n}.png | {current_time}\n")
        start()
def start():
    while True:
        try:
            proced = input("\n🚀 Should we proceed? (yes/no): ").lower()

            if proced == "yes":
                work()

            elif proced == "no":
                print("\n🙏 Thank You For Using QR Generator!")
                print("👋 Have a Great Day!")
                break

            else:
                print("⚠️ Please enter only 'yes' or 'no'\n")
                continue
        except Exception as e:
            print("❌ Something went wrong!",e)
greet()
menu()
