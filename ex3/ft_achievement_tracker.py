import random

def gen_player_achievements() -> set:
    
    achievements: list[str] = [
        "First Steps",
        "Boss Slayer",
        "Master Explorer",
        "Treasure Hunter",
        "Untouchable",
        "Crafting Genius",
        "World Savior",
        "Collector Supreme",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Sharp Mind"
    ]


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: ")
    print(f"Player Bob: ")
    print(f"Player Charlie: ")
    print(f"Player Dylan: ")
