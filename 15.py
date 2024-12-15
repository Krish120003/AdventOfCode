import math
import collections
from collections import Counter
import re
from tqdm import tqdm

PROD = """
##################################################
#.#...........O.O....#..O.#O.O#.O....OOO.O...O...#
#.#O......O...O..#...........#...#.....#...##....#
#O.OO..O.OO.O..OO.....O...#...O...#O.O.#..O...##.#
#...OOO..#..OO.....O.O.#OO#.OO#....O.......#..OO##
#.O......OO.O.O...OOO.O#......##..O.O..O......O###
##.......#.O.OO..O.....O....#..........O..O.O...O#
#.....OO..##.O.#...#....#......OO.....O.O...O....#
#OO.OOO...#..#O.....O#O...O.#...........O..#..##O#
#OO##......O.O.#OO.O.OO..#O.O.O.O.O.O.....O.OOO.O#
#O.....#OOO...O.O...#.#O....#......OOO...O.OO....#
#O.O...O.........#..##..O..#.O...O...O..O.OO..#.O#
#.......O..O#....OO.O.O#...O..O.#O..O.O#.....OO..#
#OO.O#O...O#..#...#O.#....O#O..#.O..O#...O..##..O#
#O......O.#..O.......O.O.OO..O#.......O..O#..#..O#
#....O...OO...O.O..##....O.#..O.O..O..O....OOOO..#
#.....O.O.O..O.O.O.O.O.OO....O..OO..O.O...O.O#..O#
#O......OO.O......#O.O.OO#......O....OO..O...O..O#
#O......OO..O....O...O.....OOO.O....OO.O..O#...OO#
#..OOOOOO.O..OO..O...O.....#......OO.#.O...#O.O.O#
#...O..#O..O.OO.......O...##OO.#.........#O.#...O#
#...OO.#O..OO....##....#...OO..#...O.O..O...O..OO#
##...O.#..#O.#OO......O..OO.O#..O.....O.#..O.OOOO#
##.....#......O.OO#O.O..O....O..O.OOO.O..O...O.#O#
#........O.O..OO..O.....@....#..O...OOOO#.O......#
#O....O....O...OO.OOO...O.OO.....OO#..O......O.O.#
#...O..O...O.OOOO.....#...O.O....O##O.....O.#...O#
#...O.....O...#.......O.OO..O..#.#OO.OO........#.#
##.O........#.......#O#.............O...O#..#.O#.#
#O.....O.OOOO.....O.O...OO.O...O.O...OO..O...O.O.#
#...........O...OOOOOO....O.O.#.OO...O.O..OO.....#
#..O##.......OO.OO.##..#..O...#.O..O#O...O.O#..O.#
#...OO...OO.O.......#.....OOO.O..O..O.....O...O..#
#..OO.......OO.....#......OO.O..O..#....OO....O..#
#...OO..OO...O.OO.O#.O...#.O..........OOO...OO..##
#..#O..O#....O....#....O.#...OO.O.#...#.........O#
#O.......O..OO...O.O.O...OO#O.#..O.#O..#..O.#O..O#
#..O..O...#OO...O..O.#OO.O.O...O.......##..O#..#.#
#.O..#....O..O.O..O..O.O..#....O..#...O.OO#.O....#
##OOO.O.O.................O.O..##OO.O.O.O.OO.O.O.#
#..O..................OO...O....OOO#...O....O.#..#
#..#.O#..#...OO....#....OO......#......O..OO..O.O#
#.O..OO...OO.#.OO..OOOOO#.O.OO...O.O.#...O..#.OO.#
#...O..#O#...#..............OO.#.#.....OO.......O#
#.O#.....O#..OO.#..O......#..#O.O#.O.OO........O.#
#OO.O#...O#.O......OO......O...........##.O..#...#
#..O#...O.#...O.O...O...OO.O#OOO..OO#..O..OOOO.O.#
#...O.O#..OO........O#.OO.....#O.O.O#......#O.O#.#
#........O....O....O#..#.....O..O..OO#.OOO....O..#
##################################################

^v<v^^^vv><<><><<^><><>vv><<v^^<<>^^v><>v><^^^vvv^^><<^v^>^^<>><v<vv>v>v<^<^^>v^v<v^>>^vv^v><>>v<v>v>^^><>^>v<vv><^^><>^^^^<<<v^>v>^<vv<<>>v><v^vvv>v^v>^<>^v^vv^<^^<<<vv^<^<^v><<<^v<vvv^v^><>>v^vv^^>^^^^><<<^^^v<^^v>^^vv<>><<>v>v<^^v>v^^<<vv>^>^^<<>^<vv<^v^<^^^>>^<<<^vv^<v>>>v<><>^^><^>><v<<<>^^^vv^v<>v^v<^v^vv<<vv><v>^<^<<>v<^<<><^<>><^<>^v^><<^<<^>><>>><^vv<>vv<^>v><>vvvvv<><>>v>>^vvv^v<><<^><>^<v^><<>>vv<<>>>>v<<>v<><vv>vv>^v<v^<<<v<^>>>^v^<^<<<v<v^v>>v<>^<vv>>^^>^vv>v^^>^vvv<^^vv^^<v^>^>vv<^<v<>^><v>vv<<v>^^<<>v^vvv^<^><^<>^>^^^<<><v>^vv<<><>^^<><^vv<v^<>>^^^>^<<^^<><<<^^v><>^<^<v>v>>^>^^v<>^v^<^v^^v>>v<^>>><v^v^^>>>vv^<v^^>v>^>><v>v^><^<vv<<<<v^^^<>v>^v<^^<><^v>><v>^>>>^v^^<<^^^>v>v^^v^>>^<v^vvv>^<^v<v<<^<<v<>v<^>vv^<v><^<v^<>>v<>v<<<<^<v<>v^^<>^^>^>vv<>^v>^<v>v<<>^><^v<<>>^vv<>v>>^>>^>v>^>^v>v^>^><<><^<<^<>^v>v<^>v^v^>v^><>>><^<v^><>><vv^<<<>v<>vv><^<v<>v<<v^^<<>^>v>^^>^>v^><^><<vv^>^<^vvvvv^v^v^^<<^vv>^vv^<^v><<v>v>v><<^v^^^<>^>^<^vvv^>vv^<>>>^^v^>v>vv<>>>>>v>^<>v><^<<^<v<^<vv^<
vvv<>^>>v>^^vv^vv^<v>>>^^>><<>^<>^<<<><^<<^>vv<v^v>v^>v^<>>^<>v<<>>^>>^^>vv^vvvvvv<<vvvv><<v^^v<<vv><<v^vv<v<>^>^<^^vv><v^^^^v>^>>^>v<^>^>^v<^^^<>><v<><<vvv><<v^v><>vv>>v>>>>v^^>^vv<v>vv>^>><>vv^>v<v>^v<<><>>><><><>><^^^<<>>^^^>^^<>>v^<><<^v<v<<vvvv^^<<^^^>v><v><>v<^vv>>>^<<v>v><^^<v^^>vv>^><>>v<^^^^<^>^^v^<^v<^><^^<>^<^^^vv>>>>>vv^^^v^>^^<^^<v^^^^>^>^v>><>vvv>^v>^^v<<>vv>^^>>vv>>^>>v<v^v>v^^>^^vv<>^>vv^^>^v^>>>v<^>^v^v<v^>v>><>>^<^vvv^<vv^<>^>^>^<vvv>^><>v><>^v^><>v>vv<v^><^v>^vv^<v^<<<<^^^>v><>v^^<v<^v^<^^vvv<>^^^>>^v>vvvvv^>>vv^v^v^^^>^v^^^>v>v>v>v<^<<v<^^><<<^<vv<>>^v<v><^>^^^^>>v^><>>>^>>^vv<v>><^>v^^^<>^>>v><<>>^^<<<<v^<^v<>^v<<>^<^>>>><v<v<^v><>v^vv<<<>>>^><<v<>v^^v^>^^>>v^vvv>>>v^^vv>v<^<<v^<>><>^v<<<>v^><<><<>>>^v^v^^>^vvv<vv<vv<vv<<vv>>^<>^v><>vv<vvv>v^v<<<<v^^vv<v<v^v>^^<vv^v<><^v>v<<>vv^vv<v>vvv>vvv>><^^^v^v^><^v<^<>^>^v^<^<v<v<v>>^>^vv>vv<<><<>^<><<v>><<>v>^<v>><^^v<>><>v^>v<^^^^>^vv>^^v>>vvv>v<^v<v>>>><>^<<<<v<v^v^<>v<<^>>>v<<v^<>>v<<<^v^><^<><><>>^^<<^>^<v>>vv>>v^<v<v>^<
>v>><><>v<>v>^>><v^^^v>>>vv<^>^vv<<><>^v>^<>>>^^^^v>><v^v^<><>^^v<<vvvv<<^<^<^^<>v<v^><><<^vv>v^^><<<<>^><^<^^>vv^v><vv<vv<>>^>^><^<<^<^^><^v<^<<v^><v><>^^v><^^<<^<^v<vv>v^<><vv^^><>^<<><>^>v>vv<v>^>v>^<>vv>>v>^<>vv^<v^>>>>^<v^vv^v^vv^^<^^^<<<v^^^>v<vv<<^><^vv^>vvv^v^vv<^<>vv>^>>>>^<><vv><^>v<<v><<>>vv>>^^v<>v^v>v><<v^><v><>vvvv>vv<<>^<vvvv<^^>^^><v^<><^<><<<>^^>^>^vv^^^vv>^>>vv<>^v<^<<><vv>^>>>^<^v^<<v<v<>><<^vvv^<<^v><^vv^v><vvv^>v<><v><v<^v>^v^>>>v<^^<>^^>^>vvv>>^<v^^^v<<>^><>>>v^^v>^v^v><vv^<<>^>^>^>^<<^^^>v>^<^><<<>^v><<>vvv>^>>v<^<vv^><vv><^<>v^<<><v<^><^<><^><^^v<v^><<>^>^v<^^>v^^v^>>v<^^<v>v<vvv>>^^v^><^>^>>v^^^>^<v^>vv>vvvv>v>v>><^^>><v<^^>vv<^v><v<^><v^v<<v^^^>>>v<v<^v>vv^<^vv><>>>>^v<^><>v<vv>>v^>^>>>v>v^<>v^^>^>^<v<^v^v<vv>>><vv<^><><^>v^^v<v>><>^v^^v<><>>^v>v^^^v^<^<>^v^v^>>vvv>vv^^>>^^<<v<^v>><>^>>vv<vv^<>>>><^v^>>^v^<>^>>^>v<<<<^^v<<^^>>v<^v^<<<vv>v<vv^<v^<v>v>v><vv^<><^^<>>^^^v^v^v><>^<><^<>^><<v>v<^v>v>^><>><><>v><>>v<^<<><><^v><v^v^<^<v>>^<^>>^^vv>>><^>^^^<>^<<^>^><^<
><v<>v<<v<vvv<><<v<><vv^v^^v<<v^<<><<v>v<vv^>^<>^v^>v<^>v>><v>>vv^>>vv><^^v<<^v<v^>vv^v>><vv<<<v<vvv><^>^><v<>><^^>v^^^^^v^<^>v>^v<<>^v<><v<v><^<^^<v><^<v^<<v<<v<><>v^>>^<<^v^vv^^^>v<^^><>^^>^<<<vv<<><<^v><^>^^<v^>^<<>v<v<<><>><<^v^<v<>v>^>><>>vv<^<<^^v^^<^vv>^v<^^^v^<^>><<v>^<v^^^^>v<v<>^>>v<>v^^^>^^><<<<v>^<>^v^v><v>v><>^^<<v^<><v<><<vv>v<^<^><<v<<>>^>v>vv<><>^v><>^^^<^>v><<<^v^<<><vv>v^<^><><^<^^>^^<<>^<<v^^v<v><<<^<<<^^vv<><^^^<<^^^><^<<<>>><><<^^>v<vvv>><^v<vv^<><>^<>>^>v>v>^<^<v^>^v<vvv<vv>>v^v^v>v>^^^^<<>^vv^v><^<>^v>v>>>v<v>v>vv<>v<v<<v>^<<^<><<<v^v>^><>>>vvv<^<<^^<v>^vv^>^^^v>>>^v>v>^>^>v>vv><<>>>>v^v^>^^>^><v>v>>v>>^>^^v<<<v<<v^^<>^>v^v^>^v>>v>>v>v><<>>><>v^v>^<>v>>^<><^^<><<<>>^^^^^v<<>>^<>^>v<><v>>>>^<v^v>^^>v^>>>^v<>v<^^^<v>^^v^>vv^>><>^^>v>v^v<v><><v<^^<^>^^<^^<><><^<>>><v^<<<>><^^vv^>vv^vvv>vvvv^^v<v<><v^^>>>><^>^<v^^><v<<v^>><^<^>v><^><^^<<><<<v^>v>^v^<v<>>^<^v<<<^v^^<^<v^<^v<^<vvvv<<vv<^<><><v>>>v<v><^<vv^v<><^<>v<><^><v^^<<v^>><<>><v^^v^>^^>>^>>v^>><vv<^v^^<>><v<>>>>v
<>>>>>><<<<^^vv<v^>>^v^<^>><><<v>v<>^<^<^>v^^<^<v^^^^>v<^v<>>vv^><<v<<v><^><<<<v^<^vv>v>v<<vvvv>v^^^<v>>><>^vv^>vv><<>>vvv^<>v<v>v>>><<>>v>v^v<v^^<^v^<<>>^v^>^<^^<^<^<^vv>v><>vvv^<>vv>>>^<<>><<^<<v>vvv^>>v^^>><vv>>^^v>v>>v^^v><^^v^^^v<^>v><^v<v^vv^<<v<<<<>vvvv^<^v^^>>^<^^<<^>^v<>^><<>>^v>>>v^v>^^<v<><>^vvv<>>^^^v^<>>^><>v^<v<><<^v^<v<^<v^<<>^<^<^<vv^v<^vvv<<>^^<><>v^^>v<vvv<<^>^><<><vvv<vv>v^<^v<><v<<^<^vv>v<v<<v^><>vv^^<>>^>^<^>>^<vvv^<vv^^^v>>>^^><>>vv<><v>vv^v>>vv<<>^<>vv<^^v<><vvv^<>v><^^vv>vv^^<>><^<<^vv<v<^^>><^><^v^v><v<^vv>>^^v<v<<vv>>>^v<<vv>^^^^^<>^<<^v>vvv>^v<^<v^>vvvv<<><^^<v>>>>v^^v>v>^v<><v<>v^>v^v>vv^><>^^^<^<<>v<>^<vvv^vv>v<^<<><^^v<v>^<>v<v^<v<><>v>^v<^v<vv>><>>^v<v<>^v^<vv^>^vvvv^<>^>^v>v^^^^>^v>vv<v^v^^^vv^^<>v>v^>vv^v>^<^<^<vv>^>^v<><><^>^><^v<^^<>>^^<<<v>><>^<<><<^vvv<v>v>^><>^>^v<>^^><^<>v>^><v<<>^v^<^>>vv>>^^^v^<<<^v^><>v>>>^<vvv>>^<^>^<^v<^>^vv>v^^>^>><><>>><<v<^<>>vv^><><v<<v>><>>>>v><vv>v>v>^<vvv>v<^><v<>v>^<v^><<^^>><v<^>v^^>>>>>^v>v>><<<^^vv^<<>v^<>>><v><^<v
<^<<v^<^v^>^v^>^<>v^v>vv<>v^^<vv>vv>v>^v^^<v<>^v^^><<><<^<<>^vvv<<v^v^<><^^<^<<><^<^>^<><>><v^<vv<v^^<v^>v^v^v<>>v<vv>v<>><>^<<^v^><>^v<^<<<vvv<>>v^^<<<<v<^>^v>^^vv<<v<>^<v>><v<^^v>vv^>vv><>^>v>><<<v><<>>>>>v^vvv<^^^<<<><<^^<>^>^v<>>^^>v>v<v^^^><v<<^<^v>^<<>>^v^>>v>>><>^>v^^<<<v<>^^>vv<<v>v<^<>^<>>^v^>vv>^^v>^vvv>v<<v<^^v^><>>v<^>v^v^<>><<><<>><^>>v^^vvv^v>>^<>vv^>><vv^>^v<<^^vv><^<<<<^^><>^><v^<>^v<<^<^v>>>^v<v>>><v<>v<<^v^<<^v><vvv>^^<^^><vv^v^<v>v<><>^<v<<<^v>>vv^^<<>>v^>>^<>v>^v^^<^^<<>v^>^v^>vvv><>^>>v^<<v<>^^><<vv<><^<<>v>v<^^vv<v>^^<^^<^<v>v^v^v<>v^><<^<^^^v<<^<^^>><<^^^v^vvvv>v<>v<<<>^v>^<^^v><v^<><v<^<^v>^<v>><<<<>^vvv^^v^>v^v<<^^<v>v^^vv^<^^^v>^vv<vvv<<<>^<^>>^<v<>^^v^^<><^<vvv>^v^^v>>>^^><^><<vv<^<>^><>v><<>>^<>^><v<>vv><<v^vv^<^<v>^v^^v^>^<<>v<^>v<vv^^v^>>^>v>v>>>vv>v<vv<vvv^^<>v>^v^^^<v<v<>>>vv^v^>^v<v^><vv>vvvv<>v<^><^<<<v^>vv<v<<<>>v>vv^<<v^><^>v^^^vv>v><>vv^^v>^>>vv>v^^^v>vvv^^<<<v^v<^<^^>^<<v<v^>^^<^>^<<>vv^v^v<>^<^^><vv^v>^>>v><^v^<vv>v^<v^^v^<<<<<<v^v><^>>>>v<^><><>^
v<v^^>v<>><<v>>^>vv>>v<<^^v^v><<<v<>vv<>>><v>^^^vvv><>^v><>^<vvv^^<<>>^<>^^<v<v^>^><^>^><>>^^<>><><<^v><v^><v>v^<<^v^>v^^>>^vv^^<v^v>v^^>v^^v><v<v<v>>^<v>v<<<>v>><vv^v<^>>vv>^^>><<^>vv<v>v^<<<<>vv<<>^<v><<^<<>>v>^>>^>^vv^<v>^^><<<vv<<><><<<<^^^>>^^^v><>>v^v><vv<>v<v^^>^^>v^v><<>>>>^<>v><^v<v^>^v^v<>v<^^^<^>^<^><>v<v^<^vvv<><^<>vvvv^v<v<^v<^^^>^vv^^v>><<<v<>v><vv^^v>v<^^v><^<>^>v^>^v^^^>>v<^<<<v<>><^^vv<<v^<vv><>>^v<^<^<<^vv<v<^<v<>>^<v<^<>^>v>>><>^>v^v^v><>^vvvv<v>^>vv>>>^<><^<^<v<^^^<v^v><>^<>v>>>vv<<^<<^<v>v>>vvvv><^^v>^v>^><<>vv>^><<>>>^^^v>^^<><v<^<v^<^>>v<^^v><v><<^<>>>v<^<^<<vvv^><>>^^>^>^>v^<v>^v<^^<v<vv<<vv<<^^v^v^>v>><>^<v>vvvvv<><^^<^>><<><^<>^>^>v^>^vvvv<^><<v>^^><^v>v<^vvv<v^>^<v^<><v^><^^^<>><<<<><^^vv^><><^<^<^>v><<<^>>>^^^>>^^>v<vv><><<^^>v><<v^<>v<>>^><^v^v>^^<<^>v<^^>v<<^^><v<vv^vv><>v>vv<<v<v>v^^^^^v^>><v<^<v<^vv>^v<>^>>v>v<<^^>>^<><^>v^>><^<^>>>^vv>>v>^^vvv>^v^>>>v<><>^>v^>^>v>><v<v^<^>v>^>^>><v<^<^<v<<<^^^^<>v><^<^><><^<><v<^<v^<<>v^v>^^vv><^^v^vv>^<v<>v^<>^<v^<^<^<
>><>^<<><<^^>>v>><<^<v<^><^<v>>v<^vv^>v><v><><^^v^v>^<>>^<<vvv>v>^^<vvv>v^>^^>><<<<v>^v^v^<^^v^<>>vvv>>^>^^^^vv<v>^<^^^^<><v>>vvv<v^vv><>^>>v^^^v>><^<><^^<^vv><>v>vv<v>>vvv<v^>^^<>>v^<>vv><<^<vv<vv^^<v>^><>v^><>>>><^^v<vv><v<>^>>><^vv><>>v>^<v^<>><<^>^>^>>v<^<><>^>^vv>^v<vv^^v><^<<^<><><^><v>^^^v^^<^vv^v<><^>>^^^<v^v<^>>^<<^<>>>^><<^>>^v^>>v<<>>>v>>^^^^^v>>v>^><^<>^vv>v>vvv><>vv<>v<>>vv^<<^v<v<^>^>vvv>><v^><>>^v^^>>>v<^^^^>>vvv^v<><<>>v^>>v>>v>^<<^^><^^<>v^v^<v<v>^vvv<^>^><^<^^<<v><vv>>>v>^^v^<<>^v>^><^^>>^<<^^>>vv^v^v<v>>vv>>><^>^^v^><>^>v^<^v<^>^^^>v>v^<v><^v<v^v>><<^^<>^<>>v>^<vv<><^v>^^v<><^v^^^<^^<v>v<v^^^<>^v<v^<^vv^><<><<<<v^v^v<^><v^^^v<<vv^v>v<v<>^<<<>><^^v>>v<^>vv^^v<<v^>>^>^vv>v>>>vvvvv><<^<^><><^vv<vvv^>><>v<<><>^<>vv<<^v^>^v^<>^^vvv<v^v^v>v^<><<<<v>v^v>>^<^<v<v<>vv<vv^><<^>vvv^<v^v<v><<v^>><v><^vv^<^^><<^v^vv><v^><>v^^<vv<><^^^>v><<<v^>v>v<<><>v^<^v><^>>>>v>>^^^>>^>v><>>^v<>>vv^^><v^>^<^<v^>v<<<^>^><v^v>>^v<<v^>v>^^v>>v<vv^v<^vv>v^<^><^>vv^<<v^^<<^><>>^^^<<>>v>^^>^^v^>>^><
<<<^v<^>^>vv><v^v>^>v^^^<>^vvv^>v<<>v<<<^^>^^>><^<^<<>>^<<<<<<v^v^^v>>^v^>^^^>vv^<><>^<v^<vv<<v<>>^v>v^><<>>^>>v^><^^^^<<^<v>^<v^>vv^^<<>^>^v<<<^^>vv>>^>^^^<^^^><>^<vv>>v<>v<v>vvv<>^^<^<><<<>^vv>>^><v<<>^<v><>^v>><v<<^^>v<<<v<v>vvv>^<vv^^^^<vv<v^<^v^<<^vv>v^<^><^v<^^<^<<<v>^<<v<^>>>^^<<v<^^<>^v>vv><^^v<^<v^>v^<^v>v>^<^^^v<>vvvv<^<<><><v><>^>>><vv^>>vv<^<<><<^^<<^^^<vv<^><<><>>^v<>>^<^^v^^<>><>>>><^^^v^^vv><v^^>^><><<v<^^^>vv<>>^v>v>vv^<>vv^<vvv^<vvv>^>^vv>^v^<^>^^^>>^^v^>^vv^^<v<vv<<vv<vv^<^<v<v>>vv^v<<>>vv<>^>^^^^<<v<v<v<^v^>^>>^<v<<>vvvv>>>>><v<>v^>^v^><v>>^>^v^^vv>><<^<<v<^^^^>^<^^v^>>v<>^><<vv><<<>>><v<<><<^^^>v<^<v<<^^v<><^v>^<<>vv^v^>>^^<v><^v^v^vvvvv^vvv<^v<v><vv<>^<>v>v>v<>^^<<v<v<>^v<<^v^<v^v^><>>^>vvv<^<^^<>^vv<vv^>^>v<v^v^^>>^^v^<>><<v^^v^<^v<v>>vvv<<^v<<^v<^^vvv<<<>v>v><v>>^v^^<>>v^>>^^<>^^vv<>vvv>>^v^^<>>^><^^>>^<v>><<<<>^v<>^>>v<^^>^v>^>vv<v<<<<>vv^^^vv<^^<v^<<<^>^v><<>v^>v^>^<<v><>v>^>^^^>>vv><vv^^^^^>vvv^>^>^<>v>vvv>>>>^^^>v<<^<>vv<^<^>>^<^<>>><<^v<><><<<v<v^v>v<<vv<^>>
<^v>>><v^>^<^v^v^><v^<^v^<vv>>>^^vv<v^>^<vv<v<><>^^>^<>vv^<vv>>>v<^>>>vvvv<<^^^v^v>><vvv<<v<<vv>>vvv<^<v<^<<<<<^<v<<<vv^^<<>^vv<^>><>vv^<><><^^^^<>vv^^<<>^>^<v^vv>vv^>^vv<<^<^>v>>^<vv^>>v^v^v<>>>v><v>^>>^^<<>>>><^^v<vv^<<<^^v<^<vv^<>>>v<v<vv^^><v^<>v<>vv<v>v^^^><^>^<v^vvv<v>vv^v^<v^^^<^<<>vv<<vv<v<<>><vv<><<v^>^v>>>>>>>^^vv<><vvv^^<v<>><v^^vv^^<>>^>><>>>><v>v<>><><vv^><>^^>^^v^>^^vv<><<v^^<<>vvv>v><v><<^v>^^^>v>^>>v<<<<^<>>v<><<><>^^^vv<<^<v><<^><^^^v>^<>><v^>^^v^>^vvv^^<v><>^><>><>>v^>^<^vvvv><>^<<>>><<v<^v>v<^<>^^<^^>v<vv<^<<>^^<>^<<<>v<v^v<<vv^<v<<^<>vv<v>>v><^>v<<^v>>^<><^vv<v<v>vv<<<v>^>^v>v^><<^vv^><>><>v^^^^<>^v^>^>v^^^>v<>>>>v>><v>v>v><v^vv><>v<<v<^v>^^^^>v^<^^<v^<>>><^><^>v^^^<><^<v<v>vv<<>v^<>^vv<<^vvvv^<>v>v^<><^^>v<>v^<^^v<^v^<v<v^>^vv>>>^^^v>v><^^^<>v^v>vvvvvv><>v^^>^^<<>vv<v^v>><^v^^>^^v<^v>><v^^<><v><^><<v^<<>v<>>^<^vv^>>><v>>>^<^vvv<>>v<^v<^>^v<>vv^>>>v<>><v<v^<^v<v^^v^^<v^^^^>vvvv><^^<^vv^v>v><^<v<<^^>vv^><v>v^v^^v^>vv<<v<>v<^<^><>v^^v<^<v>^^<><^>><<^<<<^>vvv^^>><v^>^>
>>v^^vv^^>^^^^v^>>^vv<^^<v^^^v<>^^^>v>>><>^<>>>v<<><<v<v<^^>>^^<^<<^>^<>^v<<<v>>>vvv>^<>^^^v<^^^^^<<<v^<v>v><v<<>><v>><><v^><^<^v>^>><v^^>>>^v>v^v^<>v<v^^<<<<v<^<<vv^vv^>>><<<v<v>><^>^v^^^<^<><<vv<^^v^><><vvv<v^vvv>>^>^^vvv<<v>><<vv<>v><^v^<^<^^v<v<<v<<^<^>>vvvv>v><<^vv^^<<^^^>v^>>>^^^^^>>^<>v<><<^<<<vv^v<^><<^^v<>>v>vv^>><>vv^>vvv^^<<>>>v<^<^^^^<><>><^^>v<v<v<><<^<v^^<^>><^^v<^^<<^vv><>v<<^>v<>v><<^^<v<v>^>v<^<<v^<v<>^vvv>^^<><><>^<>^^>>>v>>>^vv^^^><v^<<<^>>^<>>>^<>^>^>^v<v^<vv>v^vvv^v>vvv<v^<^^><^^^<v<<vvv<<<^<<<^<v^<<^v>^<>^vv<><>>v<vv<>>><><v>><v<>>^vvvv>><>>vvv^vv<^v<v<^^^v<<<>v>><^<^^<><v^><<^^<><>v^<v^v^<vvv^<<^^><^>v^<<v^<<^v>^^>^^^v^^<<v<^^<>>>v>^<^^v<<>v^v>>v<^v^<^^<^>v^vv^^v^>>v>v><v<^>vvvvv<<><>>^v^^^^>>v<^>><^^>^^<^^v>>v^^<^<^>>v^^^^^<v^>^v><<>^<<^<<^v^^^v<<>^v<v<>>v^^^^>v^>^<vv^v^v>vv^^>v<v<<^vv>^<v<>^>^<<v>>^v<^^v>^v><v<vvv<^v<^v>^^^vv^v^^<><^v>><^^>v<^<>v<v^>^>v>><>v<^>v><<v<^><v>^^>^>^^<<v<^^<^<vv^v^^v<v<v^^>>v<><v>vv^v<^<<^v><v<<>vv^^<<<v^^<<^<<v>v^^<<^<>^>vvv><>>^>>>
><<>^v>>>v<v^<v>><<><v><<^><v>v^^<>v>v<v><<v<<<^^><^>^vv><>v<>v^v>>>v><<>>v<v<>v<<<^<^<<<<v<>>>^>^vv^^<<^<><<>^<^><^v^v<v<v^vv>v<<v<v><^>^<vv^v>^^v^v>>><>v<v<^<<^^>^vv^>><>v<v<<^v^^<>>v<v^><^^v^<^>v^v>vv<<><v^v^v^^<^<^v<>v^v><><>vvv<<>><^v<<<<v>^<><>vv<<>^^^<>^^<v^><vvvv^^^v>>^^^^v>v^<>>v>v>>>vv<vv<>v<<>^<v><<v<^<v<>^<<>vvv><^<^^>>v<^^^<>v>^v<^><^<<<v^>>^<^<^^>>^>^vv^v^<>^<v><<v>^v>>vv^<v<^>vvv<<<<<^>v<<>v^>v^v^^>^<^^>^vv>^<>v><v^<><>>v^>v^><><<<^^^v<<v^<^>^v^>^<^^><v^<>><^vv^^<v>><<^^v^>v>>v>^>v<^^v^<v^<>>><>v<^^<>^<>^^>><<v>vvv^><>^v<^<v<>^>><^^v>v>>>>>^>>vvv><^^>^<>v^<<<<<<>v<^vv^<<<<^v^v^<<<^^v>^vvv>v<^v<^<vv^<>><v^>>v^v><^^>^<^<vvv>>^v>><^><<vv<^^<<^><<^vv<vv><^><>^v^><v<><^><v^<>^>^>>^<^<<vv<vvv><<^vvvv><v>>>>>v>^^>>v^<<>^v<v^^>^><<>^><^^<^>vvv<v<v>v>^v^>^^<vv>>^>^><<<<>><^<^>vv^vv^v>v<vvv^^>><>vv^<>v>^v>v^<>>v>v<^v><>^<v^<<v>v^>>^>^<<>vvv><>v>^v>^v<vvv><>>vvv<v<^><^<^<^vv<>>^^<^>><<^v^<>>v<>v^v^>v><>^>^vv<v^><<><vvv>>>vv>^>>^v^<<^><<v><<><v<<vv^<<^v>>><^<>v^>><^>>^<<v<>^<^<^<>^v
^v>vv<^><^^^<^<<<<<<>v^vvv>>>><v<v^v><<vv>vvvv>^<>v>v<><v>vvvv>v>>^>^v>v<><<^v<<><<^<^v<v^v>>^^v>vvv<>v^v<<>v>>>>v>><vv>><><><^v><<v>^<<>>>><^>>>v^>>>>v^><<^<<<^v^vv<^><^>^vvvv^vv>^v>><>v^<>^^^^^vv^<^v<^^>^^<<<vv^vv^<<^>vv><<>vv^^^^v^<<<<^^<<>v>^^vv^v<<>>^<^^v^v>>><^>^>v^<>^>v<<>><^<>^>><^<^><>>^<>v^vv^v^<^<^vv>^v<<v><><<><>>vvv<>>v>>^<>^<vv<<v>>^>^v^>>^>vv^^<>v^>>>^v^v>^>^v^>v^vv<>v^^<>^^<v<<<><>^<>><>^<><v<<v<>^^>^>^^<<v<<<<^^v^<^<<>v<<^>>>^^v<>v<>v>^<v^>^<^><^v^><>^>v<>vv^<>v>^^<^^^>v^^v^<v^<<<^^>v<<>^v^<>><v<<>><>>^^^v>v^vv><<>v^v^^><><>^v^<>v<>><^>^><vv^^v<<v>>^^vvvv>vvv^>v^v<<vv<>^v<<>^<^<v>>vvvv<^v<><v<^<>^^v^v<<>>^<v>vvv>^^v<v>>v<<>^^v<^><^^>v^<^><v<><><>><v<>^<<><><<<<<v^vv>><v><^v><vv>^^^v><^^>^<<^>>^^<^v>^>v<v><vv<vv^v<^>^vv^><<v>vv^>><^<^<^v^>^^vv^^^<>v<v><v><^v^^<v^<v>vv><<<<^^v^^^vvv<<v<^<^><<><^>>v<<^>><^v<<<v<>^><vv<<<vvv>>^vv<^<^v<>>^>v>>v<v^v^>^<>^^>^<>^>v>>v^<v<v>>>>^<<>v^v<v^v<^^><<>v<<<v<vvv>>^>>v>>^^<>^><^^v<>^><v^<>^v<>v^^><<<^>v^v<^>^>^><<<^<v<>v^^^v>>vv<^v^^^^v
v^>v^vv><v^<^<v>vv>vv^>v^<>v^vv><>>^v<>v>^><^<^>>^^>><<<v^^<>vv>v>><<^<v<<v<<>v>^^v<>v>^>vvv^v<vv>v>v>^vv>^<^^>>v^<v<v>v<<>^<>^v><><^^^<<v>v><<<>>^v><v<>^vv^^^^><>^vv>^v^<v><v<>^<^v>v^>^^v^>>v>v^>vv<v<>>v^>vv<^v<v<^<>v>>v<^>^<v<>^>v><>^vv<<>v^v<<<<<^v>^<<v^^>^<v>^v^v<<^>>>>><^<vv^<v>v^>^<v^<><><><>vv<v^^vv^><>^><>><<v^<>v^><>>>^vv<>^>>v>>^^<^^^>>^vvv<<>>><>^>>v^v<>v>vvv^><^^^^<>vv><^>^^v<^v<<><^<>vv>^^v>^>>^^>^>>><<^<vv^v^v>^vv^vvv^><><v^<<v<<^^v^v<^v<^><^v>^<^v>^^v>vv>^<v^>>vvvvv>>><>^v>v>>>vv>^v<vv><><><v<vvv>v^v^>^^<^^^^^^>>v>>^>v^^><<<^<^<>v>v<vvv^>>^vv^vvv^v^>^vv^vv>^>>^>v^<v^^^v<<^^v^<vv>^v<<<v^v^<^^<v^v<v^<<>><><>>v>>vv<>vv^>vv>^>v>><<<<^>v>v^>v><>v<<<^>^^>>><>v>^<^><<<v>v<<v^^><<v>>>^<>><^^>^^<v>vv<>>><<^^>><>><^><<>^^^vv^<<^>>>vvv>^v<v^>>^^>v^>vvvv>^<vv<^<^v^^v^<<><vv^^>^>v<^<<vv<>>v^>^v<><vv<v<v<v>>><v<>>><>^<^v^>v>^>vvv^^>v^<<<v>v><><>>^>>^^<<<v^>>^vvv^vv>>^^>v^v>v<><^<^<><v><<>v<<>>>v<^<v^^>>v<^^^><<^v><^<^<>^^^^<vvvv^>^>vv^v^<vv<v<^><<^<^^<<<v><>^>^v^^>>>vvv^<^v<v^<>>^v^<>
>^^>^>v^<v<^^^>^^vvv><vvv>>v^^v>^v>^<^<^^v<v<>><vvvv><>^<<<^v^v^<^><<^<^v>v><<vv^<>^^<>^<><><^v>^^<^<>>><>>^<v>>^v>>>vv><^><>vvvv<<^<<<>><^vvv^vv>v>^^^<<><>^vv>^><v<<v>^v><vv^v>^^v<v<v<<^^^vv>^>vvvv>><^^<^>vv>^<><>^^^^><v^v^vv<><>><^>vv><^<<v<^>>><>v<><vvv^^v^^^^>>^<v>v>^v^^<^v^<^^<^>^^<>^^^^v<><>v><vv<vv^<>>^>v>^>>>v^v<v^^>^v^^v>><<<>^v>^><v>>>v^v><^>v>vv<^^><^>^^>v^^vv>vv>vv<v<v^<>^^^^v^<^vv^<^v^v>^<v<v><^><^>>v>^>><v<v^<><vv>>vv^^v<><v^<^<^^>>^^<>><^>vv>v>>v<<v><<vv^<vvvvv^v><>v><<>^^^v<v<vv^>v>^^vv><v<>^v^<>^><v<<^<v<>>>>><>^><^>^<>v<<^^v^<v<<<^>^vvv>^>v>>>v^^vv^v<v><v><<v^vv<v<^^<<>v<<v^^><^>^<^>v<^v<>v^<<>>><^<v^>><^v>><v^<>v<<v<^<v<v<>>>v<v^v^>>>^<>v<^^<>>v<<<>><^^>>v^^<^>v>^^<^^<<vvv>v^<<^v>^^<<v>>v<>^<^v>v>v>>v><^>^<v>>^>>v<<vvv^vv<<^><^<<v>v><<^v<v>>v^^^>v^v^>><^^v>v<^vvv^<><^<v<^<^v<vv>^v^^<>>v^<>^<v<v^>>^v^<^<v<>^<<^v<<<v<^v<^v^><^<^<v^<v<^v^<^vv<^><>^^><v>v^><v^<^<^<<>^^v>^<v^^<<<<^>v^<v^vv<^>v^<>>^<^^<<><^^>^^<v<>vv<v>^<^<vv>vv><>^<v>>v<>v>>v^<^>^^>v^v><<v^<vvv>><<>v^>^v<
^<><<^^>vv<^^<<<^>v>v>>vv>>^<^<v^vv><<v^^^^>v^vv>v^<v^v^<>^>^v<>v<v<^>><<v^<>^^^<>^^><v>^>^v^>>^^v>^>>^^^>^v^^^<<v<<<><^^<^v^vv<vv<><^v><<>v>v^<^<<v>>><vvv>^v><^^>^^<v^>^>v<v>><<^>^v<^>>>^^>>v<>>v^^>^v>^<vv<v^^v<<^v^v<<^<>>^v<<<<v<<vv><^><v>><^<>>v><>^v^>>v<v><<v^v>v<^<>v^>^>v><v<>^^<^>>^^<v<v>>v^>^^^><v^<^<^vv<^^vv><v><v>v><v><>^^<v^>^>^^v<^<v^>>>^>vv<v<v<^^v<^^^>>v<>>>vvv><>^^^v<^<<^>^^<>v>^>vv^v>>><<^<<<>^>^v^v<<<^^^<<<><><v<<>><^<vv<v<<v>v>^<<^v>^<^^^<>><vv^<>><v>>^^^>^^>v<>v^^<<v<v<<>^<<vvv^>^<<^>>v>^v<><>^<>^v<<v<v>^<><vv^>v^v^v><vvvv><vv<^>^vvv^v>v<^^v>^^<<v>>^^^^^^^^^v>^v>v<^^>v><<><<<v<<^><vvv<v^<^><v>^^<v^><<<^^v>^^vv>v^>^<><<^<^><>v^^>^<v^<>>v><v<<<<><<<v^><^<^>>^<>^><v><>^><><>^<<^^>v><^<>^>v<^v<>^^<v<^^^><<^>^v<v^^vvv<v>v^v^vvvv^v^^>^vv<^>^^v<v<^>^^v>>v>v<><^vv<><v^v<><^vv^<<^^<^^^>^>><v>^v><^>^<^<^>>^>v^^>^v<v^^vv^^>v^^^<>^v>>>>^v<<vv<^^v^v>^<v>^><vv^v<v<v<<<>vvv>v<>v<><<>^^>vv<v^<vv^<vv<^<<v><v>^<^<>>v><^<^^^>v^<v<^v><<^>vv>^v<<<^<v^^vv^v^<>><v<^v>>><<<v^^v><^^>^^^^v^>^^
<v<><vv<>v<vv>><<^^^<>>^^<>v^^vv^vv<v<vvv<<v<<>^>v<vv^>^<vv>>^>>v>><>>>^^v^^v<v><v<v<>>v>^<><v^^<v<^^^<v<vvv^^^vv^^<^>>^<^v<>>>v^<^>v<^vv^<vvv^v><<^<>v>>^^v^^v^^v^v><><vv^>vv>^<v<^^>^v<^^<v<v^^<>><vv><^>^^^>^^^>>v<v<><>v^^v<vvv<>v<^><^>>>>v^><^v>^^><^v<<v<>^><<^<<>>>^<^><<>vvv><^^<v>^<v^>^v^<<vv<^>>>^^v^^v><v^>>>>^vv<v<^v^<v<vv<v>>>vv<<^^<v^><^<^<>^>v<>^^v>>^vv^^<<>vvv<>><>vv^<^v<>^>v<>><<^>^<^<<><vvv^<<<><^vv<><^<^vv^^<<><v^>>^vvvv^>^^>><vv<^<^>^<v<^^v<<><>v><<^v<v^^>>>^<^v^vv>vv^v<v^^<>^vv<<v^<>^v<v^<v^<>^^<v>v<^>>^v<vv><<v>^^v>v^<>><^><v^v^>^<><>><^v^^<v^><>>^<vvv^^<^vv<>^v<^v>>^^><v>v^<^>v<<<^^v^^vv^v>^v>^>vvvv>^<^>v>>v<><<v<>v>^>^<>^>v<^><v>vv><<>v^<<v^<>^>^>v>^^<v^^>><^>^^>^<v<v>>>>^<<<<<>vvvv>vv^>v<vv><v<^<vv<<vv>^>>v^^<v^^^^^^><>>vv>^v^>v^<<^v>^>>><^^<v>^^>^vvv<>vvv^>^>>v^<><v><v^^^<^^<><^>>vvv^^>v<>>>>v^^>^<<vvv^v>v^<<<<><v>v^<<vvv^^<><v<^<>^v<><<^^>v<v<<>vv>^<^^^<vv^^vv<<^v><<<vv<><v>^<^<>>^<^<vv>vvv>>^><><<><>>>v<>>^^<>>v<<v^^v^>^<<^>><^<v><v<vvvv<>vv>><v^v^<v<^^^<vv<>><<><<
^<^<>><>>^^>v^>><>v<^<>^<<><^><>v^<v>>v<<><><>v<v>^v><^^>^^<v^><^<><>v>v>v<>>^<^>^>v>v^<vv^v<v^<^<^vv>v^^v<<<<><vvvv<^vvv>^^<><<^^>^>v><vvv^>^><>>>v>v<^v>>^^^<v>v<<v>^^v>^<<v^<vv><><^^v<>^v<^>v>^^>vv^v^v^<<>vvv<^^>v>><>v>>v^vv>><^^>^<>>^<^v>v^>>>>^^v>>^vvv<>vv<>v>>v><^^v<v>v>>v>>^<^^v<>v<>v>><v>v<>>>v^^v>v<^<vv>v^<>><vv<>><^^^vv>>v<v<v^v>v<>v>>^<v>^vv^<v>v^v<vv>>>v><v<^<^^<vv<<vvv<<^>vv>^^<^<^><<>vv<^>^v><^<vv>^^v^>>^>vv><>^<>v<v><^^^<v^^^>v^v<><<>>^vv>^v>>^>v<>v^<<^^>><<^><<v<<^<v>^^>^vv^v^>>^>^^^>>v^<^<><^>vv>^vv<<>v>>>v^^vv^><<^>>v>v<<>^<^^<<v<>><>^vv><>v>^<<>^^vv^^>v^v>>>^v^<vvv>^^vvv^^v^<^>^^v<<<v^v^^vv<><^>v>v^><<><v<>v<>>><v><><vv<<<v<<<v<<<<><><>>v><v<vv<v>v>^<>v^>^><<>>>^<<<^>>><>>>^v<><>^vvv<>^<<v><><>v>v>^v<<><>v<v>^<v<v^^>>^^^>v><<<>v^>>v<>^>^>^<vv>>v<v>>><<v^^^><^>>^vv<vv^>^v<^<<>>>>^v<<^>>vv><^v^^^v<vv<<<<>v>>v>>>v^>^>>^^>v^^vv^^v^^<v^<v>>v>><><>><^>>v<vv<<^<>v<v^>v^<v<>^^^>><<><v>^vv^^>^>><^>>v><>v^<<vv>v>v><>^vvvvv^>^^^^v<<v^^^<^>vvvv>^^^><>^<vv>^<v<^vv^<<><v^>>^v^<vv<>
>>^>>><v>v<v><>v^><v><<vvv<^vvv><v<v^^v>^^vv>v^>v>^v<>>v<v>>^v<^<<<^<<>vvv^v>^^<vvv>^<^>>>v<^>>^>^v^^>v>^<>v<<^^><^v<<^^><<><<><<^<v><^^><^><<^>>vvvv<<>v><>v^>^<^>v>^^^>><^vv<vv<^>^<vvv^<<v^<^v^v^>>^><v^<v<v^<<vvv<<>^<^<^v<><^<v><vv^<<<<^v<v<>^^v^v><^>>^<vv<^<^<vv>^><^<^^>vv^>v>>>v<>^v<vv<>v^^vv<>^vv^<>v<v>>^<vvvv>^v^>><v^v<>><^><>vv<<><^^>vv<^vv^<^<<^^>vv>>>>><vvv>^^<><<v>v^v>^>^<<v<<v>>>v<^vvv^v<<<^<<vv^<>^><<>^v<v<v^v^^^^<^<><<>v^^>>^<>v^vv><v^<^<<>><^v>>^^v^v>^>><<<v><><v^v<v<<v>><<>v>^><<<>>vvvvv^>vv^<><v^>v<v<v>v>v>>v><^v^v^>>v^>^v>^^<<^<v^v^^><<^^^vvv^<^^v^>v^vv^^>vvv^<>^<>v<<<>vv<><vvv^>v^>^<>^v>v^<v^<v<v<v>v<>^>^>>v><^v>^v^^<^>>v^><>^<v>^<^><<^<<vv<>^vv<<vv>v>>v<>v><<v>v^^^^><v<<vv><v>vv^vv>^v^>><<^>v^v^v>><^<v>^^<vv<^<<^>^^<vvvv<^>>^>>>^>^>vv<<^<><<^^<^v>v><v^^^^>v<>v^vv>><<<^<<>><v<v<^>>^<v^^<v>>^^<>v^vv<v<<v<<>v^v><<<>^vv<<^^<>>vv<^><^<>v>vv>><v<^vv^^><^<^^v<v^<^^v>^vv^>^^^<^^>>v><><v>^>>><<^>^^>v<<^><>>^^vv<<>>^<v>^><>v>>v^<^v^^v^vvv^^^^^v^<>>vv^^>^^<>>>^<>>>>^^^<^<<<v<<v^
v><<v><v<v<><^<><^>vv>>v>v>>>^>^v>v<v>^>^^<<v>^^v>^^><^v^<v<><v><v^>^^<v<^>^<^<vvv^v>>^>^>^v<^v^vv^vv>>>><v<><^v<<^><<>>v<<v><>v><>v><^v^^>v>^><v>><><<^<>>v>^>^v^^^v^<<v>^<^vv^><v^<>>^^<>><<>vvv>>^^v>>>^>>>^><><<^v><^^v>v^>v>^^<<>^v^v>><^v<><v^<vvv<^<v^^>^>^^<^>^>v>vv^<>^<>^<<<^<<^v<^>><v>><^v^v>^v^v>vv^<<<<>vv<^<>v><v^>>>>^^^<^>^v<<^<^><^<v>>>^^v<vv>vv^^>>>v^>vv^^>v^>v<<^v><<vv>>^<<^>vv^<^^>^v><<<^><v<><<vv><>v^^vv>>vvv>>>^>>^^vv<^<>>v^v^>>>v<>><v^><v^<<>><^v><<>vv>v>v^^vv>v^>^v<<><<<>>^^><^>>>v^^vv>>v><^>v>v^^v<<^>>^><>v^v<<<>v<^<>^<<<^v>^><^>^^v^^><>vv>v^^<v^^^^><^v<^><>^vv>v<v^^^^^^>^^v>>^v^<>>>vv>^>^>^v<<>^vv<<>v^^^v>><<<<v<<>>><>^<vv<<<v^^>^v<<<v^v^v>v^^^^^<><^<>>^^<<v<v<>>^<>v^>><^v^>^<^v^vv>v>>v<vvv<>v>><^v><<^<^^^^v<><v<>vv^>^><^>^<v<<>><<^><>^^v^^<><<<<>vv^v>^^><>^v^^vv^^>^v^>><v^^<^<^<<>^v<v<<>v>^^vvv^<^^^<>v<^^<v^v>vvv>>v^vvvv<><>^v<>><>v>^<^v<^v^><<^<>^>><v<^^>>v<>vv>>^^vv<>>>><<<><>><^^^v<<^><^<><<v<v<v^<v<<<<^v<><<<vv>v>><>v<>>><^<>^>>v^v<v^^v>v^vv<v><>^v^v>^<>^><>v>^^<<
"""

TEST = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

TEST2 = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

TEST3 = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""

x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")


grid, moves = x.split("\n\n")

grid = grid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")


grid = grid.split("\n")
grid = [list(row) for row in grid]
moves = list(moves.replace("\n", ""))

# To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:

# If the tile is #, the new map contains ## instead.
# If the tile is O, the new map contains [] instead.
# If the tile is ., the new map contains .. instead.
# If the tile is @, the new map contains @. instead.


def print_grid(g):
    for row in g:
        # print("".join(row))
        print("".join(row).replace("#", "█").replace(".", " ").replace("O", "○"))


print_grid(grid)

from copy import deepcopy


robot = None

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            robot = (i, j)
            break
    if robot:
        break


for move in tqdm(moves):
    # print(move)
    new_grid = deepcopy(grid)

    if move == "^":
        dir = (-1, 0)

    if move == "v":
        dir = (1, 0)

    if move == "<":
        dir = (0, -1)

    if move == ">":
        dir = (0, 1)

    new_pos = (robot[0] + dir[0], robot[1] + dir[1])

    # is there a box there?
    if grid[new_pos[0]][new_pos[1]] in "[]":
        # we have to move the cluster of boxes

        affected_positions = set()
        affected_positions.add(new_pos)

        e = len(affected_positions)
        cursor = new_pos
        # keep going in the direction dir until we hit a wall or empty space
        while grid[cursor[0]][cursor[1]] in "[]":
            affected_positions.add(cursor)
            cursor = (cursor[0] + dir[0], cursor[1] + dir[1])

        # now, we need to make sure we get all the affected positions
        # beacuse boxes can be 2 wide
        run_once = False
        while e != len(affected_positions) or not run_once:
            e = len(affected_positions)
            run_once = True
            for pos in list(affected_positions):
                # add the other side of the box
                t1, t2 = pos
                if grid[pos[0]][pos[1]] == "[":
                    affected_positions.add((pos[0], pos[1] + 1))
                if grid[pos[0]][pos[1]] == "]":
                    affected_positions.add((pos[0], pos[1] - 1))

                # if we go in the direction dir, we can hit another box
                if grid[t1 + dir[0]][t2 + dir[1]] in "[]":
                    affected_positions.add((t1 + dir[0], t2 + dir[1]))

        # now, can we move all the affected positions in the direction dir without hitting a wall?
        can_move = True
        for pos in affected_positions:
            temp = (pos[0] + dir[0], pos[1] + dir[1])
            if grid[temp[0]][temp[1]] == "#":
                can_move = False
                break

        if not can_move:
            continue

        print("Move", move, "affected", affected_positions, "positions")
        # we can move all the boxes
        if dir in [(-1, 0), (0, -1)]:  # Moving up or left
            sorted_positions = sorted(affected_positions, key=lambda x: (x[0], x[1]))
        else:  # Moving down or right
            sorted_positions = sorted(
                affected_positions, key=lambda x: (x[0], x[1]), reverse=True
            )

        for pos in sorted_positions:
            new_box_pos = (pos[0] + dir[0], pos[1] + dir[1])
            new_grid[new_box_pos[0]][new_box_pos[1]] = grid[pos[0]][pos[1]]
            new_grid[pos[0]][pos[1]] = "."

        new_grid[robot[0]][robot[1]] = "."
        robot = new_pos
        new_grid[robot[0]][robot[1]] = "@"

        # new_box_pos = (new_pos[0] + dir[0], new_pos[1] + dir[1])
        # while grid[new_box_pos[0]][new_box_pos[1]] == "O":
        #     new_box_pos = (new_box_pos[0] + dir[0], new_box_pos[1] + dir[1])

        # if grid[new_box_pos[0]][new_box_pos[1]] == ".":
        #     new_grid[new_box_pos[0]][new_box_pos[1]] = "O"
        #     new_grid[new_pos[0]][new_pos[1]] = "@"
        #     new_grid[robot[0]][robot[1]] = "."
        #     robot = new_pos
        # else:
        #     # can't move
        #     continue

    # we can just move there
    elif grid[new_pos[0]][new_pos[1]] == ".":
        new_grid[new_pos[0]][new_pos[1]] = "@"
        new_grid[robot[0]][robot[1]] = "."
        robot = new_pos

    grid = new_grid

    # print_grid(grid)
    # input()
print()

# for each box, get coords


score = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "[":

            score += 100 * i + j

print(score)
