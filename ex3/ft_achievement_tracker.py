import random

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


def gen_player_achievements() -> set[str]:

    cnt = random.randint(1, len(achievements))
    selected = random.sample(achievements, cnt)
    return set(selected)


if __name__ == "__main__":

    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print(
        "All distinct achievements: "
        f"{alice.union(bob, charlie, dylan)}"
    )

    print(
        "Common achievements: "
        f"{alice.intersection(bob, charlie, dylan)}"
    )

    only_alice = alice.difference(bob, charlie, dylan)
    only_bob = bob.difference(alice, charlie, dylan)
    only_charlie = charlie.difference(bob, alice, dylan)
    only_dylan = dylan.difference(bob, charlie, alice)

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    all_achie = set(achievements)
    print(f"Alice is missing: {all_achie.difference(alice)}")
    print(f"Bob is missing: {all_achie.difference(bob)}")
    print(f"Charlie is missing: {all_achie.difference(charlie)}")
    print(f"Dylan is missing: {all_achie.difference(dylan)}")
