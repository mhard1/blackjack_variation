# import random for choice method
import random

# Creating a deck of cards from scratch

# Creating the spades
spades_rank = [x for x in range(1, 14)]

spades = {}

for i in range(len(spades_rank)):
    if spades_rank[i] == 1:
        spades[spades_rank[i]] = "Ace of spades"

    elif spades_rank[i] == 11:
        spades[spades_rank[i]] = "Jack of spades"

    elif spades_rank[i] == 12:
        spades[spades_rank[i]] = "Queen of spades"

    elif spades_rank[i] == 13:
        spades[spades_rank[i]] = "King of spades"

    else:
        spades[spades_rank[i]] = " %d of spades" % (spades_rank[i])

# Creating the clubs
clubs_rank = [x for x in range(14, 27)]
clubs = {}

for i in range(len(clubs_rank)):

    if clubs_rank[i] == 14:
        clubs[clubs_rank[i]] = "Ace of clubs"

    elif clubs_rank[i] % 13 == 11:
        clubs[clubs_rank[i]] = "Jack of clubs"

    elif clubs_rank[i] % 13 == 12:
        clubs[clubs_rank[i]] = "Queen of clubs"

    elif clubs_rank[i] % 13 == 0:
        clubs[clubs_rank[i]] = "King of clubs"

    else:
        clubs[clubs_rank[i]] = " %d of clubs" % (clubs_rank[i] % 13)

# Creating the diamonds
diamonds_rank = [x for x in range(27, 40)]
diamonds = {}

for i in range(len(diamonds_rank)):

    if diamonds_rank[i] == 27:
        diamonds[diamonds_rank[i]] = "Ace of diamonds"

    elif diamonds_rank[i] % 13 == 11:
        diamonds[diamonds_rank[i]] = "Jack of diamonds"

    elif diamonds_rank[i] % 13 == 12:
        diamonds[diamonds_rank[i]] = "Queen of diamonds"

    elif diamonds_rank[i] % 13 == 0:
        diamonds[diamonds_rank[i]] = "King of diamonds"

    else:
        diamonds[diamonds_rank[i]] = " %d of diamonds" % (diamonds_rank[i] % 13)

# Creating the hearts
hearts_rank = [x for x in range(40, 53)]
hearts = {}

for i in range(len(hearts_rank)):
    if hearts_rank[i] == 40:
        hearts[hearts_rank[i]] = "Ace of hearts"

    elif hearts_rank[i] % 13 == 11:
        hearts[hearts_rank[i]] = "Jack of hearts"

    elif hearts_rank[i] % 13 == 12:
        hearts[hearts_rank[i]] = "Queen of hearts"

    elif hearts_rank[i] % 13 == 0:
        hearts[hearts_rank[i]] = "King of hearts"

    else:
        hearts[hearts_rank[i]] = " %d of hearts" % (hearts_rank[i] % 13)

# Putting the suits together to make a deck
deck = {}

deck.update(spades)
deck.update(clubs)
deck.update(diamonds)
deck.update(hearts)


# Creating a function for the blackjack value of the key
def blackjack_value(key_value):
    if key_value % 13 == 0:
        value = 10

    elif key_value % 13 > 10:
        value = 10

    else:
        value = key_value % 13

    return value


# Printing instructions for the game to the user
instruction = """\nIn this game, you are the only player, and there are two types of scores - the round score and the game score.
The game score will begin at 100, and the game will last for five rounds.
At the beginning of the round, you will be get two random cards and they are added together to make your round score.
From here, you have two options - draw another card to try to get your round score closer to 21, or end the round.
You can draw as many cards as you want until you end the round or your round score exceeds 21.
At the end of the round, 21 minus the round score will be subtracted from the game score. Then the next round begins.
After the five rounds, you will be given your total score. The closer your score is to 100, the better.

---Other Information About The Game---
Aces are only worth 1.
If you bust, 21 is subtracted from your total score.
All face cards are worth 10.

    """

print(instruction)

# Create a deck as a list of keys to be randomly chosen with choice method
cards = [x for x in range(1, 53)]

# Initialize the values for the scores
current_round = 1
game_score = 100

# A list for chosen cards
chosen = []

# Start first round and set while loop to go for 5 rounds.
while current_round < 6:

    print("\nThe current round is ", current_round)
    print("The current game score is: ", game_score)
    round_score = 0
    # Choose a card at random
    your_card = random.choice(cards)

    print("\nYour card is the", deck.get(your_card))
    print("The value of the card is", blackjack_value(your_card))

    chosen.append(your_card)
    round_score += blackjack_value(your_card)

    while round_score < 21:
        print("Current round score: ", round_score)
        hit = input("\nDo you want another card? Type 'y' for yes or 'n' for no: ")

        if hit != "y" and hit != "n":
            while hit != "y" and hit != "n":
                print("Invalid command. Please try again:")
                hit = input("Do you want another card? Type 'y' for yes or 'n' for no: ")
                if hit == "y" or hit == "n":
                    break

        if hit == "y":
            your_card = random.choice(cards)
            while your_card in chosen:
                your_card = random.choice(cards)

            print("Your card is the", deck.get(your_card))
            print("The value of the card is", blackjack_value(your_card))
            # Set the card equal to the dictionary key value
            chosen.append(your_card)
            round_score += blackjack_value(your_card)

        elif hit == "n":
            break

        print("Total round score: ", round_score)

    if round_score > 21:
        print("Unlucky, you busted")
        game_score -= 21

    else:
        game_score -= (21 - round_score)

    current_round += 1

print("\nYour final score is: ", game_score)


grade_f = [x for x in range(1, 60)]
grade_d = [x for x in range(60, 70)]
grade_c = [x for x in range(70, 80)]
grade_b = [x for x in range(80, 90)]
grade_a = [x for x in range(90, 101)]

if game_score in grade_f:
    print("Your final game grade is an F")

elif game_score in grade_d:
    print("Your final game grade is a D")

elif game_score in grade_c:
    print("Your final game grade is a C")

elif game_score in grade_b:
    print("Your final game grade is a B")

elif game_score in grade_a:
    print("Your final game grade is an A!")
