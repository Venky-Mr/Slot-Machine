import random
credit = input("How much would like to deposit? $")
print(f"Credit to Account: ${credit}")
if credit.isdigit():
    credit = int(credit)
def game():
    symbols = ["Apple", "Mango", "Cherry", "Grapes"]
    payouts = {
        ("Apples", "Apples", "Apples"): 3,
        ("Mango", "Mango", "MAngo"): 6,
        ("Cherry", "Cherry", "Cherry"): 9,
        ("Grapes", "Grapes", "Grapes"): 12
    }
    selected_symbols = [random.choice(symbols)for _ in range(3)]
    print(selected_symbols)
    for combo, payout in payouts.items():
        if tuple(selected_symbols) == combo:
            return f"payout: {payout}"
    return 0


while True:
    bet = int(input("Place your bet (1 to 10 credits): "))
    if bet < 1 or bet > 10 or bet > credit:
        print("Invalid bet amount! Please bet between 1 to 10 credits")
        continue
    credit -= bet
    payout = game()

    if payout > 0:
        winnings = payout * bet
        credit += winnings
        print(f"Congratulations you won ${winnings}")
    if credit == 0:
        print("You've run out of credits. Game over!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thank you for playing! Your final balance is: ${}".format(credit))
