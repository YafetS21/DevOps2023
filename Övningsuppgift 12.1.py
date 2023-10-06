#En dict skapad
notes = {
    'Medelande från skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

#Användaren ska mata in val

välj_note = input("Välj det du vill göra: ")

#Det som finns i dict ska skrivas ut

if välj_note in notes:
    print("*------*")
    print(välj_note)
    print("*------*")
    print(notes[välj_note])

else:
    print(f"FEL: {välj_note}) är ogiltigt")

print(".: ANTECKNINGAR :.")
print("******************")

# Loopa genom dictionaryn och skriv ut titlarna
for titel in notes.keys():
    print(f"- {titel}")

print("------------------")