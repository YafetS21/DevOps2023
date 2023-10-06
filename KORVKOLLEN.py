print("---------------------------")
print("   .: KORVKOLLEN 1.0.1 :.")
print("---------------------------")
print("Hur många elever vill ha... ")

_2_Korv = int(input("2 korvar     > "))
_3_Korv = int(input("3 korvar     > "))
_2_SoyBoy = int(input("2 soyboy korvar > "))
_3_SoyBoy = int(input("3 soyboy korvar > "))

korvPack = round((2 * _2_Korv + 3 * _3_Korv) / 8 + 0.5)
SoyboyPack = round((2 * _2_SoyBoy + 3 * _3_SoyBoy) / 4 + 0.5)
drick = _2_Korv + _3_Korv + _2_SoyBoy + _3_SoyBoy

pris = float(20.95 * korvPack + 34.95 * SoyboyPack + 13.95 * drick)

print("---------------------------")
print("-       Inköpslista       -")
print("---------------------------")
print("| Vanlig korv:  ", korvPack, "förpackningar")
print("| Soyboy korv: ", SoyboyPack, "förpackningar")
print("| Dryck:        ", drick, "drick")
print("---------------------------")
print("| ", pris, "SEK")
print("---------------------------")
