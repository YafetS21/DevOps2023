ålder = int(input("Hur gammal är du? "))
if ålder < 18:
  myndig_om = 18 - ålder
  print("Du kommer att uppnå myndig ålder om", myndig_om, "!")

elif ålder == 18:
  print("Du är redan myndig!")
else:
  print("Du är redan myndig och har varit det ett tag")