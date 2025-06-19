#!/bin/python3

import random
 
print("MasterMind")
 
def maak_code():
    return ''.join(str(random.randint(1, 6)) for _ in range(4))
 
def vergelijk(code, gok):
    zwart = sum(a == b for a, b in zip(code, gok))
    rest_code = [c for i, c in enumerate(code) if c != gok[i]]
    rest_gok = [g for i, g in enumerate(gok) if g != code[i]]
    wit = 0
    for g in set(rest_gok):
        wit += min(rest_gok.count(g), rest_code.count(g))
    return zwart, wit
 
def admin_toegang():
    invoer = input("Admin login (of Enter om over te slaan): ").strip().lower()
    return invoer == "admin123"
 
def speel():
    print("Raad een code van 4 cijfers (1 t/m 6). Je hebt 10 pogingen.")
    code = maak_code()
    if admin_toegang():
        print(f"[Admin] Code: {code}")
    for i in range(1, 11):
        gok = input(f"Poging {i}: ").strip().lower()
        if len(gok) != 4 or not all(c in "123456" for c in gok):
            print("Fout: gebruik 4 cijfers van 1 t/m 6.")
            continue
        zwart, wit = vergelijk(code, gok)
        print(f"Zwart: {zwart}, Wit: {wit}")
        if zwart == 4:
            print(f"Goed gedaan! De code was {code}")
            return
    print(f"Op! De code was {code}")
 
if __name__ == "__main__":
    doorgaan = "y"
    while doorgaan.lower() == "y":
        speel()
        doorgaan = input("Opnieuw spelen (Y/N)? ").strip().lower()

import random

print("MasterMind")

def generate_Code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    secret_Counts = {}
    guess_Counts = {}
    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1
    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    return black_Pegs, white_Pegs

def is_Admin():
    wachtwoord = input("Admin toegang? Voer wachtwoord in (of druk Enter om te overslaan): ").strip()
    return wachtwoord.lower() == "admin123"

def play_Mastermind():
    print("Welkom bij Mastermind!")
    print("Raad de 4-cijferige code. Elke cijfer is tussen 1 en 6. Je hebt 10 pogingen.")
    secret_Code = generate_Code()
    if is_Admin():
        print(f"[Admin] De geheime code is: {''.join(secret_Code)}")
    attempts = 10
    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Poging {attempt}: ").strip().lower()
            valid_Guess = len(guess) == 4 and all(c in "123456" for c in guess)
            if not valid_Guess:
                print("Ongeldige invoer. Geef 4 cijfers tussen 1 en 6.")
        black, white = get_Feedback(secret_Code, guess)
        print(f"Zwarte pinnen: {black}, Witte pinnen: {white}")
        if black == 4:
            print(f"Gefeliciteerd! Je hebt de code geraden: {''.join(secret_Code)}")
            return
    print(f"Helaas, de juiste code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'y'
    while again.lower() == 'y':
        play_Mastermind()
        again = input("Opnieuw spelen (Y/N)? ").strip().lower()

