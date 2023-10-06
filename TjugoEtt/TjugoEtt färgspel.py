import random


class ugoett:
    def __init__(self):  # Kortleken och lista för att lagra spelaren och dealerns kort
        self.kortLek = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        self.spelareHand = []
        self.dealerHand = []

    def draw_card(self):  # väljer slumpmässiga kort och tar bort korten från högen
        card = random.choice(self.kortLek)
        self.kortLek.remove(card)
        return card

    def deal_initial_cards(self):  # Två korten kommer delas ut till spelare och dealer
        for _ in range(2):
            self.spelareHand.append(self.draw_card())
            self.dealerHand.append(self.draw_card())

    def calculate_hand_value(self, hand):# Här så räknar funktionen kortens värde
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
                  'A': 1}
        value = sum([values[card] for card in hand])
        if 'A' in hand and value + 10 <= 21:
            value += 13  # Om det finns ett ess och värdet är 14, ändra till 1
        return value

    def player_turn(self):# Representerar spelarens tur
        while True:
            print(f"Dina kort: {self.spelareHand}")
            player_value = self.calculate_hand_value(self.spelareHand)
            print(f"Värdet av dina kort: {player_value}")

            if player_value == 21:
                print("Grattis! Du har 21. Du vinner!")
                return True
            elif player_value > 21:
                print("Du har överskridit 21. Du förlorar!")
                return False

            choice = input("Vill du dra ett kort till? (ja/nej): ").lower()
            if choice != "ja":
                return True

            self.spelareHand.append(self.draw_card())

    def dealer_turn(self):# Reptresenterar dealerns tur
        while self.calculate_hand_value(self.dealerHand) < 17:
            self.dealerHand.append(self.draw_card())

    def play_game(self):# En gameloop, denna funktion ser till att spelet styrs rätt
        print("Välkommen till ugoett!")

        while True: # Oändlig loop tills spelaren väljer att avsluta. Nollställer till nya kort
            self.spelareHand.clear()
            self.dealerHand.clear()
            self.deal_initial_cards() # Anropa för att dela ut 2 nya kort från funktionen

            player_bust = not self.player_turn()
            if not player_bust:# Om spelaren har spruckit blir player_bust True annars False om icke.
                self.dealer_turn()
                dealer_value = self.calculate_hand_value(self.dealerHand)# beräknar värdet av dealerns hand med hjälp av calculate_hand_value-funktionen
                print(f"Datorns kort: {self.dealerHand}")
                print(f"Värdet av datorns kort: {dealer_value}")

                if dealer_value > 21 or self.calculate_hand_value(self.spelareHand) > dealer_value:
                    print("Du vinner!")
                elif dealer_value > self.calculate_hand_value(self.spelareHand):
                    print("Datorn vinner!")
                else:
                    print("Det blev lika!")

            play_again = input("Vill du spela igen? (ja/nej): ").lower()
            if play_again != "ja":
                break

# if __name__ == "__main__": används för att kontrollera om Python-skriptet körs som huvudprogram
# #Game = instant av ugoett klassen
# #Game.play_game() anropar play_game metoden och starta själva spelet samt utför logiken för spelet
if __name__ == "__main__":
    game = ugoett()
    game.play_game()
