import random


def gen_player_achievements(achievements: list[str]) -> set:

    count = random.randint(1, len(achievements))
    earned: set[str] = set()

    while (len(earned) < count):
        achievement = random.choice(achievements)
        earned.add(achievement)

    return (earned)


if __name__ == "__main__":

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

    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    # 和集合
    all_achive = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_achive}")

    # 共通部分
    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}")

    # 差集合
    only_alice = alice.difference(bob, charlie, dylan)
    only_bob = bob.difference(alice, charlie, dylan)
    only_charlie = charlie.difference(alice, bob, dylan)
    only_dylan = dylan.difference(alice, bob, charlie)
    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    # 未取得の実績
    all_possible = set(achievements)
    missing_alice = all_possible.difference(alice)
    missing_bob = all_possible.difference(bob)
    missing_charlie = all_possible.difference(charlie)
    missing_dylan = all_possible.difference(dylan)
    print(f"Alice is missing: {missing_alice}")
    print(f"Bob is missing: {missing_bob}")
    print(f"Charlie is missing: {missing_charlie}")
    print(f"Dylan is missing: {missing_dylan}")
