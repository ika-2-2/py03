import sys

args = sys.argv

def score_analytics() -> None:

    l: int = len(args)
    high: int = args[1]
    low: int = args[1]
    total: int = 0
    average: float = 0.0

    print("Scores processed: [", end="")

    for i in args[1:]:
        print(f"{i}, ", end="")
        total += i
        if (high < i):
            high = i
        if (low > i):
            low = i
        
    print("]")
    print(f"Total players: {l - 1}")
    average = total / (l - 1)
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    

