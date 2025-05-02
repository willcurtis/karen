#!/usr/bin/env python3

import csv
import time
import os
import sys
import random
import readline  # Enables proper terminal input (e.g., backspace)

# ANSI color codes
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

RESPONSES_FILE = "responses.csv"

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def display_boot_message():
    logo = r"""
 
 _   __                        ___  _____ 
| | / /                       / _ \|_   _|
| |/ /  __ _ _ __ ___ _ __   / /_\ \ | |  
|    \ / _` | '__/ _ \ '_ \  |  _  | | |  
| |\  \ (_| | | |  __/ | | | | | | |_| |_ 
\_| \_/\__,_|_|  \___|_| |_| \_| |_/\___/ 
                                          
                                                 
    """
    print(logo)
    print("Booting up Karen AI...\n")
    time.sleep(1.5)
    print(f"{CYAN}Karen: Ready to judge your questions.{RESET}\n")
    time.sleep(1)

def load_responses():
    responses = {}
    try:
        with open(RESPONSES_FILE, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                responses[row['prompt'].strip().lower()] = row['response']
    except FileNotFoundError:
        print(f"{CYAN}Karen: Ugh, I can't find my brain (responses.csv is missing).{RESET}")
        sys.exit(1)
    return responses

def matrix_effect(duration=5):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    columns = os.get_terminal_size().columns
    end_time = time.time() + duration
    try:
        while time.time() < end_time:
            line = ''.join(random.choice(chars) for _ in range(columns))
            print(line)
            time.sleep(0.05)
    except KeyboardInterrupt:
        pass

def main():
    clear_terminal()
    display_boot_message()
    responses = load_responses()
    while True:
        try:
            user_input = input(f"{MAGENTA}Karen > {RESET}").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{CYAN}Karen: Ugh, fine. Bye.{RESET}")
            break

        response = responses.get(user_input, "I'm not answering that.")

        if user_input == "self destruct":
            print(f"{CYAN}Karen: {response}{RESET}")
            print()  # Add a blank line for spacing
            time.sleep(1)
            matrix_effect()
            print("Good Bye..", end="", flush=True)
            print()  # Add a blank line for spacing
            try:
                while True:
                    sys.stdout.write('\u2588')  # █ flashing block
                    sys.stdout.flush()
                    time.sleep(0.5)
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
                    time.sleep(0.5)
            except KeyboardInterrupt:
                sys.exit(0)
        else:
            print(f"{CYAN}Karen: {response}{RESET}")

if __name__ == "__main__":
    main()
