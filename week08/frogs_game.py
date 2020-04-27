import copy


def generate_frog_start_and_end_position(left, rigth, count):
    left_sight = left * count
    rigth_sight = rigth * count

    return f'{left_sight}_{rigth_sight}'


def jump_frog(position, leaf, frog_position):
    list_position = list(position)
    list_position[leaf], list_position[frog_position] = list_position[frog_position], list_position[leaf]

    return ''.join(list_position)


def generate_possible_moves_from_given_position(position):
    leaf = position.find('_')
    possible_moves = []

    if leaf - 1 >= 0 and position[leaf - 1] == '>':
        new_position = jump_frog(position, leaf, leaf - 1)
        possible_moves.append(new_position)

    if leaf - 2 >= 0 and position[leaf - 2] == '>':
        new_position = jump_frog(position, leaf, leaf - 2)
        possible_moves.append(new_position)

    if leaf + 1 < len(position) and position[leaf + 1] == '<':
        new_position = jump_frog(position, leaf, leaf + 1)
        possible_moves.append(new_position)

    if leaf + 2 < len(position) and position[leaf + 2] == '<':
        new_position = jump_frog(position, leaf, leaf + 2)
        possible_moves.append(new_position)

    return possible_moves


def generate_path(start, end, frogs_move):
    positions = generate_possible_moves_from_given_position(start)

    frogs_path = copy.copy(frogs_move)
    frogs_path.append(start)

    if start == end:
        return frogs_path

    for value in positions:
        if value not in frogs_path:
            new_position = generate_path(value, end, frogs_move=frogs_path)
            if new_position is not None:
                return new_position

    return None


def frog_game(frogs_count):
    half_frogs = frogs_count // 2

    start = generate_frog_start_and_end_position('>', '<', half_frogs)
    end = generate_frog_start_and_end_position('<', '>', half_frogs)

    return(generate_path(start, end, []))


if __name__ == '__main__':
    frogs_count = int(input('How many frogs are in the lake: '))

    assert frogs_count % 2 == 0, 'frogs have to be even number'

    print(frog_game(frogs_count))
