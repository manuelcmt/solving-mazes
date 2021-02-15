from maze import Maze
import pytest

@pytest.mark.parametrize("maze, goal",
                            [("maze1.txt", (0, 11)),
                             ("maze2.txt", (3, 3)),
                             ("maze3.txt", (0, 5)),
                             ("maze4.txt", (8, 13)),
                             ("maze5.txt", (2, 1)),
                             ("maze6.txt", (3, 2)),
                             ("maze7.txt", (4, 8)),
                            ])


def test_meta(maze, goal):
    m = Maze(maze)
    m.solve
    print(m.goal)
    assert m.goal == goal