import random

# Fixa skitbuggen med rogue zombies imorgon...

def välkomst_text():
    print(f"""
{"*" * 50}
*{'Välkommen till Math Zombies v. 0.1 (alpha)!':^48}*
*{'Du vaknar upp inlåst i ett rum med 12 dörrar.':^48}*
*{'För att ta dig ut måste du svara på:':^48}*
*{'rätt dörr pussel och undvika zombies.':^48}*
{"*" * 50}
""")

# Fixa input_valid_str/in imorgon för att göra main kortare 

# Ändra till choice kanske gör funktionen mer lättläst, testa sen..
def generera_frågor(vald_tabell): 
    frågor = set()  # Fått bort att faktorer upprepas med datatypen set(), funktionen raderar dubletter.
    while len(frågor) < 12:  # Loopar tills frågorna är slut
        faktor = random.randint(1, 12)  
        fråga = f"{faktor} * {vald_tabell}"
        frågor.add(fråga) # Genererade fråga läggs till frågor
    return frågor


def ställ_fråga(fråga, nummer, öppnade_dörrar):
    svar = eval(fråga)  # Evaluera svaret för att undvika att splitta och omvandla strängen till en matematisk operation.
    #eval() används för att utvärdera strängen fråga, som antas vara en matematiskt uttryck, till ett numeriskt värde. Till exempel, om fråga är "2 * 5", kommer eval() att utföra multiplikationen och tilldela resultatet, 10, till variabeln svar.
    print(f"\nFråga {nummer} av 12, {12-nummer} kvar : Vad blir {fråga}?") 
    användar_svar = int(input("Svar: "))
    return användar_svar == svar # Returnerar användarens svar till variabeln svar


def zombie_dörren(dörr_nummer):
    return f"Bakom dörr {dörr_nummer} fanns zombiesarna!"  # Testa skapa andra händelser också

def välj_zombie_dörr(tillgängliga_dörrar):
    return random.choice(tillgängliga_dörrar)

def välj_dörr(tillgängliga_dörrar):
    vald_dörr = 0
    while vald_dörr not in tillgängliga_dörrar:
        vald_dörr = int(input(f"Välj en dörr: {tillgängliga_dörrar}: "))
    return vald_dörr

def visa_resultat(antal_korrekta_svar, öppnade_dörrar):
    if antal_korrekta_svar == 12: 
        print("Grattis, du överlevde Zombiehuset!")
    else:
        print("Zombiesarna tuggar på dig!")
    print("Öppnade dörrar:", sorted(öppnade_dörrar)) # printar en lista över vilka dörrar man öppnat vid dödsfall.

def main():
    välkomst_text()

    while True:
        vald_tabell = 0
        while vald_tabell < 2 or vald_tabell > 12:
            vald_tabell = int(input("Välj vilken multiplikationstabell du vill öva på (2 - 12): "))
            if vald_tabell < 2 or vald_tabell > 12:
                print("Felaktigt val. Välj en multiplikationstabell mellan 2 och 12.")

        öppnade_dörrar = set() # Att använda en mängd är användbart här eftersom det garanterar att varje dörrnummer som lagras i öppnade_dörrar endast förekommer en gång. Om samma dörrnummer öppnas flera gånger under spelets gång, kommer det bara att lagras en gång i mängden. Detta är viktigt för att hålla koll på vilka dörrar som har öppnats och för att undvika dubletter.
        antal_korrekta_svar = 0

        frågor = generera_frågor(vald_tabell)

        for nummer, fråga in enumerate(frågor, 1): # enumerate får fram värdet på frågan och index
            if ställ_fråga(fråga, nummer, öppnade_dörrar):
                antal_korrekta_svar += 1
                if nummer < 12:
                    tillgängliga_dörrar = list(set(range(1, 13)) - öppnade_dörrar)
                    zombie_dörr = välj_zombie_dörr(tillgängliga_dörrar)  # För in print(zombie_dörr) under denna rad för testning.
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
        if nytt_spel.lower() != "ja": # lower utifall spelar skriver Ja
            print("Spelet avslutas!")
            break

main()


'''

enumerate(frågor, 1) skapar en räknare (nummer) som börjar från 1 och ökar med 1 för varje iteration. Varje iteration av loopen ger både indexet på frågan (nummer) och själva frågan (fråga).
Kolla svar och hantera spelet:
För varje fråga kallas ställ_fråga(fråga, nummer, öppnade_dörrar) för att ställa frågan till spelaren. Om spelaren svarar korrekt, ökar antal_korrekta_svar med 1.
Om antalet korrekta svar är mindre än 12 (dvs. spelaren inte har svarat på alla frågor än), fortsätter spelet. Annars avbryts loopen och spelet avslutas.
Om spelaren väljer samma dörr som zombierna gömmer sig bakom, avbryts spelet och spelaren förlorar. Annars fortsätter spelet och spelaren undviker zombierna bakom dörren.
Visa resultat:
Efter att loopen är klar och spelet är över, visas resultatet av spelet med visa_resultat(antal_korrekta_svar, öppnade_dörrar).
Sammanfattningsvis möjliggör enumerate() för varje iteration av loopen att hålla reda på vilken fråga som ställs och dess motsvarande index, vilket gör det enklare att hantera spelets logik och visa resultatet i slutet av spelet.
'''