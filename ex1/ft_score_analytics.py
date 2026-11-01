import sys

args = sys.argv


def score_analytics() -> None:
    scores: list[int] = []

    for arg in args[1:]:
        try:
            score = int(arg)
        except ValueError:
            print(f"Invalid parameter: {arg}")
            continue

        scores.append(score)

    print("Scores processed: [", end="")
    for i in range(len(scores)):
        print(scores[i], end="")
        if ((i + 1) != len(scores)):
            print(", ", end="")

    print("]")
    print(f"Total players: {len(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()
