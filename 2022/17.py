from math import *

# Your handheld device has located an alternative exit from the cave for you and the elephants. The ground is rumbling almost continuously now, but the strange valves bought you some time. It's definitely getting warmer in here, though.

# The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are falling into the chamber from above, presumably due to all the rumbling. If you can't work out where the rocks will fall next, you might be crushed!

# The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

# ####

# .#.
# ###
# .#.

# ..#
# ..#
# ###

# #
# #
# #
# #

# ##
# ##
# The rocks fall in the order shown above: first the - shape, then the + shape, and so on. Once the end of the list is reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.

# The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input).

# For example, suppose this was the jet pattern in your cave:

# >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
# In jet patterns, < means a push to the left, while > means a push to the right. The pattern above means that the jets will push a falling rock right, then right, then right, then left, then left, then right, and so on. If the end of the list is reached, it repeats.

# The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

# After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the direction indicated by the next symbol in the jet pattern) and then falling one unit down. If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur. If a downward movement would have caused a falling rock to move into the floor or an already-fallen rock, the falling rock stops where it is (having landed on something) and a new rock immediately begins falling.

# Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the example above manifests as follows:

# The first rock begins falling:
# |..@@@@.|
# |.......|
# |.......|
# |.......|
# +-------+

# Jet of gas pushes rock right:
# |...@@@@|
# |.......|
# |.......|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# |.......|
# |.......|
# +-------+

# Jet of gas pushes rock right, but nothing happens:
# |...@@@@|
# |.......|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# |.......|
# +-------+

# Jet of gas pushes rock right, but nothing happens:
# |...@@@@|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# +-------+

# Jet of gas pushes rock left:
# |..@@@@.|
# +-------+

# Rock falls 1 unit, causing it to come to rest:
# |..####.|
# +-------+

# A new rock begins falling:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock left:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |.......|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock right:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock left:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |..@....|
# |.@@@...|
# |..@....|
# |..####.|
# +-------+

# Jet of gas pushes rock right:
# |...@...|
# |..@@@..|
# |...@...|
# |..####.|
# +-------+

# Rock falls 1 unit, causing it to come to rest:
# |...#...|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# A new rock begins falling:
# |....@..|
# |....@..|
# |..@@@..|
# |.......|
# |.......|
# |.......|
# |...#...|
# |..###..|
# |...#...|
# |..####.|
# +-------+
# The moment each of the next few rocks begins falling, you would see this:

# |..@....|
# |..@....|
# |..@....|
# |..@....|
# |.......|
# |.......|
# |.......|
# |..#....|
# |..#....|
# |####...|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@...|
# |..@@...|
# |.......|
# |.......|
# |.......|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@@@.|
# |.......|
# |.......|
# |.......|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |.......|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |....@..|
# |....@..|
# |..@@@..|
# |.......|
# |.......|
# |.......|
# |..#....|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@....|
# |..@....|
# |..@....|
# |..@....|
# |.......|
# |.......|
# |.......|
# |.....#.|
# |.....#.|
# |..####.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@...|
# |..@@...|
# |.......|
# |.......|
# |.......|
# |....#..|
# |....#..|
# |....##.|
# |....##.|
# |..####.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@@@.|
# |.......|
# |.......|
# |.......|
# |....#..|
# |....#..|
# |....##.|
# |##..##.|
# |######.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+
# To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, the tower of rocks will be 3068 units tall.

# How many units tall will the tower of rocks be after 2022 rocks have stopped falling?


x = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
""".strip()


class Piece:
    def __init__(self, shape) -> None:
        self.shape = shape

    def width(self):
        return len(self.shape[0])

    def height(self):
        return len(self.shape)

    def __repr__(self):
        return "Piece"

    def __str__(self) -> str:
        return (
            "\n".join(["".join(["#" if x else " " for x in row])
                      for row in self.shape])
            + "\n"
        )


flat_block = Piece([1, 1, 1, 1])
p_block = Piece([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
l_block = Piece([[0, 0, 1], [0, 0, 1], [1, 1, 1]])
i_block = Piece([[1], [1], [1], [1]])
o_block = Piece([[1, 1], [1, 1]])

blocks = [
    i_block,
    p_block,
    l_block,
    flat_block,
    o_block
]


class Board:
    def __init__(self, state) -> None:

        # moving pieces are represented by 2
        # stationary pieces are represented by 1
        # empty space is represented by 0

        self.state = state
        self.counter = 0
        self.piece_counter = 0
        self.down_next = False

    def next(self):
        self.counter += 1

        # check if there are any moving pieces
        if not any([any([x == 2 for x in row]) for row in self.state]):
            # place a new piece 3 rows above the highest piece
            self.place_piece(blocks[self.piece_counter % 5], 3)
            self.piece_counter += 1

            return

        if self.down_next:
            # move piece down if possible, else make it stationary
            self.down_next = False
            lowest_moving_piece = 10000
            for row in self.state:
                for col in row:
                    if col == 2:
                        lowest_moving_piece = min(lowest_moving_piece, row)

            # check if the piece can move down by checking if the row below is empty and not already 1
            if all([((self.state[lowest_moving_piece - 1][col] == 0) if col == 2 else True) for col in range(7)]):
                # move all moving pieces down
                for row in self.state:
                    for col in row:
                        if col == 2:
                            row[col] = 0
                            row[col - 1] = 2

            else:
                # cannot move down, make stationary
                for row in self.state:
                    for col in row:
                        if col == 2:
                            row[col] = 1

        else:
            # move piece left or right based on the next wave from x
            if x[self.counter % len(x)] == ">":
                self.move_right()
            elif x[self.counter % len(x)] == "<":
                self.move_left()

    def place_piece(self, piece, row):
        # place piece 2 from the left
        # and 3 rows above the highest piece

        # find the highest piece
        highest_piece = 0
        for row in self.state:
            for col in row:
                if col == 1:
                    highest_piece = max(highest_piece, row)

        # place the piece 3 rows above the highest piece
        for i in range(piece.height()):
            for j in range(piece.width()):
                self.state[highest_piece + + i][2 + j] = piece.shape[i][j]

    def __str__(self):
        print("JJJ" * 7)
        board = "\n".join(["".join([{1: "#", 2: "@"}[x] if x else "." for x in row])
                          for row in self.state])

        return board


# make a starting state of width 7 and height 10000
# fill it with 0s
starting_state = [[0 for _ in range(7)] for _ in range(20)]

# make a board
board = Board(starting_state)

print(board)
board.next()
print(board)
