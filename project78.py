def read_leaderboard():
    while True:
        try:
            n = int(input("Enter number of players: ").strip())
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    board = {}
    for _ in range(n):
        try:
            name, score = input("Enter name and score: ").strip().rsplit(maxsplit=1)
            score = int(score)
            board[name] = board.get(name, 0) + score
        except ValueError:
            print("❌ Invalid input! Format should be: NAME SCORE")
            continue

    ranked = sorted(board.items(), key=lambda x: x[1], reverse=True)
    return ranked


def print_leaderboard(ranked, top=None):
    if top is not None:
        ranked = ranked[:top]

    for pos, (name, score) in enumerate(ranked, start=1):
        print(f"{pos}. {name} - {score}")


if __name__ == "__main__":
    ranked = read_leaderboard()
    print_leaderboard(ranked)