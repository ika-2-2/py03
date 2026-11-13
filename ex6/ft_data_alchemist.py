import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    players: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gragory", "john", "kevin", "Liam"]
    # 要素一つずつcapitalizeしてぶちこむ
    capitalized = [name.capitalize() for name in players]
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized}")

    # [集める値 for 変数 in 元のデータ if 条件]
    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")

    # {キー: 値 for 変数 in 元のデータ}
    scores = {name: random.randint(0, 1000) for name in capitalized}
    print(f"Score dict: {scores}")

    average = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")

    high_scores = {name: scores[name] for name in scores if scores[name] > average}
    print(f"High scores: {high_scores}")
