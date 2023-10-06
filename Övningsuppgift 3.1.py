# Ta emot användarens inmatning för tre tal
num1 = int(input("Ange det första talet: "))
num2 = int(input("Ange det andra talet: "))
num3 = int(input("Ange det tredje talet: "))


# Jämför de inmatade talen för att hitta det största
if num1 >= num2 and num1 >= num3:
        largest = num1
elif num2 >= num1 and num2 >= num3:
        largest = num2
else:
        largest = num3

# Presentera det största talet för användaren
print("Det största talet är:", largest)