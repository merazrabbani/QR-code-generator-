import qrcode as qr
from datetime import datetime as dt
def greet():
    print("=" * 40)
    print("🌟 WELCOME TO QR GENERATOR 🌟")
    print("=" * 40)
def history():
    print("\n1.View history\n2.Delete History\n3.Exit")
    history_in= input("\nEnter your choice(in digit)")
    if history_in == "1":        
        with open("history.txt", "r") as file:
              readed = file.read()
              print("\n", readed, "\n")
    elif history_in == "2":
        open("history.txt", "w").close()
    elif history_in == "3":
         menu()
    else:
         print("Enter apprioprate value")
         history()         
def menu():
    while True:
         try:
            print("\n1.Generate QR\n2.History\n3.Exit")
            menu_choice = input("Enter you choice (in numbers) : ")
            if menu_choice == "1":
                work()
            elif menu_choice == "2":
                history()
            elif menu_choice == "3":
                 break
            else:
                 print("Enter appriopriate input")
         except:
             print("something went wrong")
             continue
def work():
    url = input("🔗 Enter Text / URL: ")
    if url == "":
        print("\nURLcannot be empty")
        work()
    file_n = input(" Enter the name : ")
    if file_n == "":
        print("\nName cannot be empty")
        work()
    make = qr.make(url)
    make.save(file_n+".png")
    print("\n✅ QR Code Generated Successfully!")
    print("📁 Saved as: ",file_n+".png")
    t = dt.now()
    current_time = t.strftime("%d/%m/%Y  %H:%M:%S   ")
    with open("history.txt", "a") as file:
        file.write(f"{url} | {file_n}.png | {current_time}\n")
def start():
    while True:
        try:
            proced = input("\n🚀 Should we proceed? (yes/no): ").lower()

            if proced == "yes":
                work()

            elif proced == "no":
                print("\n🙏 Thank You For Using QR Generator!")
                print("👋 Have a Great Day!")
                menu()

            else:
                print("⚠️ Please enter only 'yes' or 'no'\n")
                continue
        except Exception as e:
            print("❌ Something went wrong!",e)
greet()
menu()
