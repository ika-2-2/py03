import sys


args = sys.argv

# なにも入力がなければusageを表示する

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    # なにも入力がない場合usage
    if (len(args) == 1):
        print(
            "Usage: python3 ft_inventory_system.py <item_name>:<quantity> ..."
        )

    else:
        inventory: dict[str, int] = {}
        for arg in args[1:]:
            try:
                parts = arg.split(":")
                # {value:key}の形ではない場合
                if (len(parts) != 2):
                    print(f"Error - invalid parameter '{parts[0]}'")
                    continue
                name = parts[0]
                # 重複がないか
                if (name in inventory):
                    print(f"Redundant item '{name}' - discarding")
                    continue
                quantity = int(parts[1])
                inventory[name] = quantity
            except ValueError as e:
                print(f"Quantity error for '{name}': {e}")
                continue

        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        print(
            f"Total quantity of the {len(inventory)} "
            f"items: {sum(inventory.values())}"
        )

        total = sum(inventory.values())

        for name in inventory:
            per = round(inventory[name] / total * 100, 1)
            print(f"Item {name} represents {per}%")

        # 最大値、最小値を探す
        high: str = ""
        low: str = ""
        first: bool = True
        for name in inventory:
            if first:
                high = name
                low = name
                first = False
            else:
                if (inventory[name] > inventory[high]):
                    high = name
                if (inventory[name] < inventory[low]):
                    low = name
        if not first:
            print(
                f"Item most abundant: {high} with quantity {inventory[high]}"
            )
            print(
                f"Item least abundant: {low} with quantity {inventory[low]}"
            )

        # 新しいアイテムを追加
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
