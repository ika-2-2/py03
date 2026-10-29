import sys

args = sys.argv

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    l: int = len(args)
    if (len(args) == 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {l - 1}")
        for i in range(1, l):
            print(f"Argument {i}: {args[i]}")

    print(f"Total arguments: {l}\n")
