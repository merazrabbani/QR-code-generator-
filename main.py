import qrcode as qr

def greet():
    print("=" * 40)
    print("🌟 WELCOME TO QR GENERATOR 🌟")
    print("=" * 40)

def work():
    url = input("🔗 Enter Text / URL: ")
    file = input("enter the name")
    make = qr.make(url)
    make.save(file+".png")
    print("\n✅ QR Code Generated Successfully!")
    print("📁 Saved as: ",file+".png")

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

        except:
            print("❌ Something went wrong!")

greet()
start()
