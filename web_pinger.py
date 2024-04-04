# >>=========================================================<<
# ||  ______         _      __            __               __||
# || /_  __/      __(_)____/ /___  __    / /__  ____ _____/ /||
# ||  / / | | /| / / / ___/ __/ / / /_  / / _ \/ __ `/ __  / ||
# || / /  | |/ |/ / (__  ) /_/ /_/ / /_/ /  __/ /_/ / /_/ /  ||
# ||/_/   |__/|__/_/____/\__/\__, /\____/\___/\__,_/\__,_/   ||
# ||                        /____/                           ||
# >>=========================================================<<
#           This project was developed by TwistyJead ツ
#                    github.com/moonlxght

import os
import sys
import subprocess  # For calling external processes
import socket  # For networking operations
import colorama
from colorama import Fore, Style, init

init()
os.system("title TwistyJead's Web Pinging Tool")

def web_pinger_art():
    sys.stderr.writelines(Fore.LIGHTCYAN_EX + """
                                     _       __     __    ____  _                      
                                    | |     / /__  / /_  / __ \(_)___  ____ ____  _____
                                    | | /| / / _ \/ __ \/ /_/ / / __ \/ __ `/ _ \/ ___/
                                    | |/ |/ /  __/ /_/ / ____/ / / / / /_/ /  __/ /    
                                    |__/|__/\___/_.___/_/   /_/_/ /_/\__, /\___/_/     
                                                                    /____/             
""")

def menu():
    # Clearing the screen
    if os.name == "nt":  # Detecting Windows operating system
        os.system("cls")  # Clearing the screen for Windows
    else:  # For other operating systems (Linux/MacOS)
        os.system("clear")

    web_pinger_art()

    sys.stdout.write(Fore.LIGHTCYAN_EX + "Options:" + "\n")
    sys.stdout.write(Fore.LIGHTYELLOW_EX + "[1] " + Fore.LIGHTCYAN_EX + "Send continuous ping to a specific URL" + "\n")
    sys.stdout.write(Fore.LIGHTYELLOW_EX + "[2] " + Fore.LIGHTCYAN_EX + "Resolve the main address of the entered DNS" + "\n")
    sys.stdout.write(Fore.LIGHTYELLOW_EX + "[3] " + Fore.LIGHTCYAN_EX + "Exit the program" + "\n")

# Function to initiate the main loop
def main():
    while True:
        # Show the main menu
        menu()

        # Ask the user to make a selection
        choice = input("\n" + Fore.LIGHTYELLOW_EX + "Please enter an option number: " + Fore.LIGHTCYAN_EX)

        # Perform actions based on user's choice
        if choice == "1":
            ping_continuous()
        elif choice == "2":
            resolve_address()
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid option! Please try again.")

# Function to continuously send ping to a specific URL
def ping_continuous():
    # Screen clearing operations section for Windows or other operating systems
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    web_pinger_art()
    url = input("Please enter the URL you want to ping: ")  # Get the URL to ping from the user

    try:
        while True:
            process = subprocess.Popen(["ping", "-t", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  # Perform the ping

            try:
                for line in process.stdout:
                    print(line.strip())
            except KeyboardInterrupt:  # Listen for Ctrl+C shortcut
                print("\nPinging stopped.")  # Stop pinging when Ctrl+C is pressed
                break
            finally:
                # Terminate the "process" object (which represents the subprocess) when the operation is complete
                process.terminate()
                process.wait()

    except Exception as e:
        print("An error occurred:", e)

def resolve_address():  # Function to resolve the IP address of the entered URL
    # Screen clearing operations section for Windows or other operating systems
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    web_pinger_art()

    address = input(Fore.LIGHTYELLOW_EX + " [>] " + Fore.LIGHTCYAN_EX + "Please enter the URL to resolve: ")  # Get the URL to resolve from the user

    try:
        # Resolving the IP address of the URL
        resolved_addresses = socket.getaddrinfo(address, None)

        # Printing the resolved IP addresses to the screen
        print(Fore.LIGHTCYAN_EX + f"Resolved IP addresses for {address}:")
        for item in resolved_addresses:
            print(Fore.LIGHTMAGENTA_EX + item[4][0])  # Print the resolved IP addresses to the screen
            input("\n" + Fore.LIGHTYELLOW_EX + " [?] " + "Press Enter to go back to the main menu.")
    except Exception as e:
        print("An error occurred:", e)

# Main program section
if __name__ == "__main__":
    main()  # Initiate the main loop
