try:
  age = int(input("Vad är din ålder? > "))

  if age < 18:
    print("Du får inte komma in bror")
    print("Vänta tills du fyller 18 år")
    print("Du fyller 18 om", 18 - age, "år")
  elif age >= 18:
    print("Du får komma in bror")
  #else:
    
except TypeError:
    print("Felaktig inmatning. Vänligen ange din ålder som en siffra.")
except ValueError:
    print("Felaktig inmatning. Vänligen ange din ålder som ett heltal.")