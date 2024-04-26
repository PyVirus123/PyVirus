import os
import time
import random
import re

# List of known threats (real-life computer malware)
known_threats = ["Mirai", "Sasser", "Code Red", "Zeus", "CryptoLocker", "Conficker", "Wiper", "Shamoon", "BlackEnergy", "Havex", "Dragonfly", "Triton", "Emotet", "Ryuk", "Sodinokibi", "Netwalker", "RansomExx", "Maze", "REvil", "Conti", "Clop", "DarkSide", "RagnarLocker", "Snake", "WastedLocker", "Sunburst", "Kaseya VSA", "QakBot", "Buer Loader", "Ursnif", "TrickBot", "ZLoader", "Emotet", "Dridex", "Faketoken", "Crysis", "DanaBot", "Remcos", "TrickBot", "Ursnif", "Ryuk", "SamSam", "GlobeImposter", "Matrix", "WannaCry", "ILOVEYOU", "Mydoom", "Slammer", "Stuxnet", "Sobig", "Storm Worm", "Melissa","SQL Slammer","BlackEnergy","Emotet","Zeus","Sasser","Code Red","Mirai","CryptoLocker","Conficker","Nimda","Anna Kournikova","Blaster","CIH","Netsky","Bagle","Klez","Sobig","Witty","Nimda","Slammer","Code Red","SQL Slammer","Zeus","Sasser","Storm Worm","WannaCry","ILOVEYOU","Mydoom","Stuxnet","BlackEnergy","Emotet","Netsky","Bagle","Klez","Witty"]


print("Welcome To Fake Antivirus!")

def ask_action():
    action = input("What should we do for you? (scan): ")
    if action.lower() == "scan":
        print("Starting scan...")
        time.sleep(2)
        print("Scanning...")

        # Generate a random number of known threats
        num_threats = random.randint(1, 10)
        detected_threats = random.sample(known_threats, num_threats)

        for i, threat in enumerate(detected_threats, start=1):
            print(f"Detected threat {i}: {threat}")

        print("Scan complete. Results below:")
        print(f"Found {num_threats} threat(s).")

        print("To remove threats, purchase the full plan. If you already have it, enter your existing subscription code.")
        print("Opening payment page in 5 seconds...")
        time.sleep(5)

        # Check if the payment page file exists before opening it
        payment_page = "payment.html"
        if os.path.exists(payment_page):
            os.startfile(payment_page)

            # Validate subscription code
            subscription_code = input("Enter your subscription code to remove the threats: ")
            if re.match(r'^[A-Z0-9]{16}$', subscription_code):
                print("Removing threats...")
                time.sleep(2)

                # Simulate removing threats
                removed_threats = random.randint(0, num_threats)
                failed_threats = num_threats - removed_threats

                print(f"Removed {removed_threats} threat(s).")
                print(f"Failed to remove {failed_threats} threat(s).")
            else:
                print("Invalid subscription code. Please enter a 16-character alphanumeric code.")
        else:
            print("Error: Payment page not found.")
    else:
        print("Sorry, that action isn't recognized.")

    ask_action()

ask_action()
