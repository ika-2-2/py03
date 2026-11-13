import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "move", "swim"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
        events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        pop_index = random.randrange(len(events))
        event = events.pop(pop_index)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    events: list[tuple[str, str]] = []

    for i in range(10):
        events.append(next(stream))

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
