
def get_engine_schematic():
    with open("day3input.txt") as f:
        lines = f.readlines()

    schematic = []
    for line in lines:
        schematic.append([l for l in line.strip()])

    return schematic


def is_symbol(schematic, x, y):
    if x < 0 or y < 0 or y >= len(schematic) or x >= len(schematic[0]):
        return False
    elif schematic[y][x] == ".":
        return False
    elif schematic[y][x].isdigit():
        return False
    else:
        return True


def process_schematic_1(schematic):

    symbols = []
    for y, line in enumerate(schematic):
        for x, char in enumerate(line):
            if char.isdigit() or char == ".":
                continue
            else:
                symbol = {
                    "x": x,
                    "y": y,
                }
                symbols.append(symbol)

    part_numbers = []
    for y, line in enumerate(schematic):
        number = ""
        found = False
        for x, char in enumerate(line):
            if char.isdigit():
                number += char
                if not found:
                    entry = {
                        "x": x,
                        "y": y,
                    }
                    found = True
            else:
                if found:
                    entry["number"] = number
                    part_numbers.append(entry)
                number = ""
                found = False

            if found and x == len(line) - 1:
                print("found at end of line")
                entry = {
                    "x": x - len(number) + 1,
                    "y": y,
                    "number": number,
                }
                part_numbers.append(entry)

    qualified_parts = []
    print("symbols", symbols)
    print("part_numbers", part_numbers)
    for symbol in symbols:
        for part in part_numbers:
            px = part["x"]
            py = part["y"]
            plength = len(part["number"])

            is_part = False

            print("checking part", part["number"], "at", px, py, "length", plength)
            if symbol["x"] == px - 1 and symbol["y"] == py:
                is_part = True
            if symbol["x"] == px + plength and symbol["y"] == py:
                is_part = True

            for i in range(-1, plength+1):
                if symbol["x"] == px + i and symbol["y"] == py - 1:
                    is_part = True
                if symbol["x"] == px + i and symbol["y"] == py + 1:
                    is_part = True

            if is_part:
                qualified_parts.append(int(part["number"]))

    return sum(qualified_parts)

def process_schematic_2(schematic):

    symbols = []
    for y, line in enumerate(schematic):
        for x, char in enumerate(line):
            if char.isdigit() or char == ".":
                continue
            else:
                symbol = {
                    "x": x,
                    "y": y,
                    "char": char,
                }
                symbols.append(symbol)

    part_numbers = []
    for y, line in enumerate(schematic):
        number = ""
        found = False
        for x, char in enumerate(line):
            if char.isdigit():
                number += char
                if not found:
                    entry = {
                        "x": x,
                        "y": y,
                    }
                    found = True
            else:
                if found:
                    entry["number"] = number
                    part_numbers.append(entry)
                number = ""
                found = False

            if found and x == len(line) - 1:
                entry = {
                    "x": x - len(number) + 1,
                    "y": y,
                    "number": number,
                }
                part_numbers.append(entry)

    qualified_parts = []
    for symbol in symbols:
        if symbol['char'] != "*":
            continue
        print("found a gear at", symbol["x"], symbol["y"])
        gears = []
        for part in part_numbers:
            px = part["x"]
            py = part["y"]
            plength = len(part["number"])

            is_part = False

            if symbol["x"] == px - 1 and symbol["y"] == py:
                is_part = True
            if symbol["x"] == px + plength and symbol["y"] == py:
                is_part = True

            for i in range(-1, plength+1):
                if symbol["x"] == px + i and symbol["y"] == py - 1:
                    is_part = True
                if symbol["x"] == px + i and symbol["y"] == py + 1:
                    is_part = True

            if is_part:
                gears.append(int(part["number"]))

        if len(gears) == 2:
            print(gears)
            qualified_parts.append(gears[0] * gears[1])

    return sum(qualified_parts)

if __name__ == "__main__":

    parts2 = process_schematic_2(get_engine_schematic())
    print(parts2)
