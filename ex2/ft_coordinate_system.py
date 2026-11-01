import sys
import math

args = sys.argv


def parse_player_pos(text: str) -> tuple[float, float, float]:
    parts = text.split(",")
    if (len(parts) != 3):
        raise ValueError("Invalid syntax")

    values: list[float] = []

    for part in parts:
        try:
            value: float = float(part)
        except ValueError as e:
            raise ValueError(f"Error on parameter {part}: {e}")

        values.append(value)

    return (values[0], values[1], values[2])


def distance(
    pos_1: tuple[float, float, float],
    pos_2: tuple[float, float, float]
) -> float:
    x1, y1, z1 = pos_1
    x2, y2, z2 = pos_2

    result = math.sqrt(
        (x2 - x1) ** 2
        + (y2 - y1) ** 2
        + (z2 - z1) ** 2
    )

    return round(result, 4)


def get_player_pos() -> tuple[float, float, float]:

    while (1):
        text: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        try:
            return parse_player_pos(text)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    pos_1 = get_player_pos()
    print(f"Got a first tuple: ({pos_1[0]}, {pos_1[1]}, {pos_1[2]})")
    print(f"It includes: X={pos_1[0]}, Y={pos_1[1]}, Z={pos_1[2]}")
    result_1 = distance(pos_1, (0.0, 0.0, 0.0))
    print(f"Distance to center: {result_1}\n")

    print("Get a second set of coordinates")
    pos_2 = get_player_pos()

    result_2 = distance(pos_1, pos_2)
    print(f"Distance between the 2 sets of coordinates: {result_2}")
