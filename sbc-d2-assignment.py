import random

def lottery(patad, resulta):
    if patad == resulta:
        return "Daug ka!", 1, 0, 0
    elif sorted(patad) == sorted(resulta):
        return "Hapit ra madaug!", 0, 1, 0
    else:
        return "luoya pilde man!", 0, 0, 1

def main():
    total_wins = 0
    total_partial_wins = 0
    total_losses = 0

    for round_number in range(1, 4):
        print(f"Round {round_number}")
        
        patad = input("Enter your Bet(give space on each numbers): ")
        patad = list(map(int, patad.split()))
        
        resulta = random.sample(range(1, 10), 3)
        
        print(f"Lottery resulta: {' '.join(map(str, resulta))}")
        
        outcome, win, partial_win, lose = lottery(patad, resulta)
        total_wins += win
        total_partial_wins += partial_win
        total_losses += lose

        print(outcome)
        print()
        
    print("Game Over!")
    print(f"Total Wins: {total_wins}")
    print(f"Total Partial Wins: {total_partial_wins}")
    print(f"Total Losses: {total_losses}")

if __name__ == "__main__":
    main()
