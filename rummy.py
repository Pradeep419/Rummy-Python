import random


class Functions():
    def __init__(self, player_deck):

        self.player_deck = player_deck

    def removeCards(self):
        for k in range(len(self)):
            deck.remove(self[k])
            return deck

    def sort(self):

        ispet_symbol = []
        kalaavar_symbol = []
        heart_symbol = []
        diamond_symbol = []

        for k in range(len(self)):

            split_1 = self[k].split(' ')
            symbol = split_1[1]

            if symbol == 'Ispet':

                ispet_symbol.append(self[k])

            elif symbol == 'Kalaavar':

                kalaavar_symbol.append(self[k])

            elif symbol == 'Diamond':

                diamond_symbol.append(self[k])

            else:

                heart_symbol.append(self[k])

        return ispet_symbol + kalaavar_symbol + diamond_symbol + heart_symbol

    def validateTheGame(self):
        deck1 = []
        for m in range(len(self)):
            deck1 = self[m].split(' ')






numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
bSymbols = ['Ispet', 'Kalaavar']
rSymbols = ['Diamond', 'Heart']
colors = ['R', 'B']

deck = []

for i in range(len(colors)):

    for j in range(len(numbers)):

        if (colors[i] == 'R'):
            deck.append(colors[i] + ' ' + rSymbols[0] + ' ' + numbers[j])
            deck.append(colors[i] + ' ' + rSymbols[1] + ' ' + numbers[j])
        else:
            deck.append(colors[i] + ' ' + bSymbols[0] + ' ' + numbers[j])
            deck.append(colors[i] + ' ' + bSymbols[1] + ' ' + numbers[j])

deck = deck * 2
print(len(deck))

playerA = random.choices(deck, k=13)
deck = Functions.removeCards(playerA)
playerB = random.choices(deck, k=13)
deck = Functions.removeCards(playerB)

openCard = random.choice(deck)

playerA_sort = Functions.sort(playerA)
print(playerA_sort)
playerB_sort = Functions.sort(playerB)
print(playerB_sort)

print(len(deck))
remainingcards_dek = random.choices(deck, k=78)

print('Lets Start the game')

game_end = 0

while (game_end == 0):

    print(playerA_sort)
    print(openCard)
    option_open_card = input('Enter your option Y or N...?')

    if (option_open_card == 'Y'):
        playerA_sort.append(openCard)
        playerA_sort = Functions.sort(playerA_sort)
        print(playerA_sort)
        discard = int(input('Enter the card number you want to discard'))
        openCard = playerA_sort[discard]
        del playerA_sort[discard]
    else:
        playerA_sort.append(remainingcards_dek[0])
        print("appended card is: "+remainingcards_dek[0])
        del remainingcards_dek[0]
        playerA_sort = Functions.sort(playerA_sort)
        print(playerA_sort)
        discard = int(input('Enter the card number you want to discard'))
        openCard = playerA_sort[discard]
        del playerA_sort[discard]

    print(playerB_sort)
    print(openCard)
    option_open_card = input('Enter your option Y or N...?')
    if (option_open_card == 'Y'):
        playerB_sort.append(openCard)
        playerB_sort = Functions.sort(playerB_sort)
        print(playerB_sort)
        discard = int(input('Enter the card number you want to discard'))
        openCard = playerB_sort[discard]
        del playerB_sort[discard]
    else:
        playerB_sort.append(remainingcards_dek[0])
        print("appended card is: " + remainingcards_dek[0])
        playerB_sort = Functions.sort(playerB_sort)
        del remainingcards_dek[0]
        print(playerB_sort)
        discard = int(input('Enter the card number you want to discard'))
        openCard = playerB_sort[discard]
        del playerB_sort[discard]

    game_end = 0
