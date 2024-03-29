import random


def välkomst_text():
    print(f"""
{"*" * 50}
*{'Välkommen till Math Zombies v. 0.1 (alpha)!':^48}*
*{'Du vaknar upp inlåst i ett rum med 12 dörrar.':^48}*
*{'För att ta dig ut måste du svara på:':^48}*
*{'rätt dörr pussel och undvika zombies.':^48}*
{"*" * 50}
""")

# Funktionen skapar en uppsättning unika faktorer
def generera_frågor(vald_tabell):
    frågor = set()  
    while len(frågor) < 12:  # Loopar tills frågorna är slut
        faktor = random.randint(1, 12)  
        fråga = f"{faktor} * {vald_tabell}"
        frågor.add(fråga)  # Genererade fråga läggs till frågor
    return frågor

# Funktionen ställer en mattefråga och verifierar svar.
def ställ_fråga(fråga, nummer, öppnade_dörrar):
    svar = eval(fråga)
    print(f"\nFråga {nummer} av 12, {12-nummer} kvar : Vad blir {fråga}?") 
    användar_svar = int(input("Svar: "))
    return användar_svar == svar 

def zombie_dörren(dörr_nummer):
    return f"Bakom dörr {dörr_nummer} fanns zombiesarna!"

# Funktionen slumpar zombie dörr bland användarens tillgängliga dörrar.
def välj_zombie_dörr(tillgängliga_dörrar):
    return random.choice(tillgängliga_dörrar)

# Funktion för att användaren ska välja en dörr, bland tillgängliga dörrar.
def välj_dörr(tillgängliga_dörrar):
    vald_dörr = 0
    while vald_dörr not in tillgängliga_dörrar:
        vald_dörr = int(input(f"Välj en dörr: {tillgängliga_dörrar}: "))
    return vald_dörr

# Funktion för utskrift av resultat för vinst i spelet. 
def visa_resultat(antal_korrekta_svar, öppnade_dörrar):
    if antal_korrekta_svar == 12: 
        print("Grattis, du överlevde Zombiehuset!")
    else:
        print("Zombiesarna tuggar på dig!")
    print("Öppnade dörrar:", sorted(öppnade_dörrar))

def main():
    välkomst_text()

    # Loop som frågar efter val av tabell och validerar korrekta val.
    while True:
        vald_tabell = 0
        while vald_tabell < 2 or vald_tabell > 12:
            vald_tabell = int(input("Välj multiplikationstabell (2 - 12): "))
            if vald_tabell < 2 or vald_tabell > 12:
                print("Felaktigt val. Välj en multiplikationstabell mellan 2 och 12.")
        öppnade_dörrar = set()  # set() lämpligt här för att ha koll på unika öppna dörrar.
        antal_korrekta_svar = 0
        frågor = generera_frågor(vald_tabell)

        # for loop för speletes logik och skriver ut info om resultat till användaren.
        for nummer, fråga in enumerate(frågor, 1):  # enumerate() håller koll på värdet och index på frågan. 
            if ställ_fråga(fråga, nummer, öppnade_dörrar):
                antal_korrekta_svar += 1
                if nummer < 12:  # Vid 12 rätt behöver använder vinna, därav <12.
                    tillgängliga_dörrar = list(set(range(1, 13)) - öppnade_dörrar)
                    zombie_dörr = välj_zombie_dörr(tillgängliga_dörrar)
                    vald_dörr = välj_dörr(tillgängliga_dörrar)
                    öppnade_dörrar.add(vald_dörr)
                    if vald_dörr == zombie_dörr:
                        print(zombie_dörren(vald_dörr))
                        print("Spelet är över. Du klarade", nummer, "frågor och förlorade.")
                        break
                    else:
                        print("Du valde rätt dörr och undvek zombiesarna bakom den!")
                        print(zombie_dörren(zombie_dörr))
            else:
                print("Fel dörrkod. Spelet är över. Du klarade", nummer, "frågor.")
                break

        visa_resultat(antal_korrekta_svar, öppnade_dörrar)

        nytt_spel = input("Nytt spel? (ja/nej): ")
        if nytt_spel.lower() != "ja": 
            print("Spelet avslutas!")
            break


main()