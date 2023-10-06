
heltal_lista = []

# Låt användaren mata in fem heltal
for i in range(5):
  heltal = int(input(f"Mata in heltal {i + 1}: "))
 
  heltal_lista.append(heltal)
    

# Använd max-funktionen för att hitta det högsta talet i listan
max_heltal = max(heltal_lista)

# Presentera det högsta talet för användaren
print(f"Det högsta inmatade talet är: {max_heltal}")