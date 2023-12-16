def get_input(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines


def parse_game(game):
    # get the number and the list of games from the string

    game_number, game_list = game.split(":")
    game_number = game_number.split(" ")[1]
    game_list = game_list.split(";")

    parsed_games = []
    for g in game_list:
        parsed_game = {}
        for entry in g.strip().split(","):
            entry = entry.strip()
            num, color = entry.split(" ")
            parsed_game[color] = int(num)
        parsed_games.append(parsed_game)

    return game_number, parsed_games


def get_max_cube_count(game_list):
    powers = {}
    for game in game_list:
        base = {"red": 1, "green": 1, "blue": 1}
        game_number, parsed_games = parse_game(game)
        for g in parsed_games:
            for color, amount in g.items():
                print(color, amount)
                base[color] = max(int(amount), int(base[color]))
                print(base)
        powers[game_number] = base["red"] * base["blue"] * base["green"]
    return powers


filename = "day_2_input.txt"


if __name__ == "__main__":
    games = get_input(filename)
    cube_counts = get_max_cube_count(games)
    print(sum(cube_counts.values()))
