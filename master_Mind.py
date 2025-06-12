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