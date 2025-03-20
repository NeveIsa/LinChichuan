from itertools import permutations as perm
import numpy as np
import json
from fire import Fire


class Tile:
    def __init__(self, length, width):
        self.l = length
        self.w = width
        self.area = length * width
        self.perimeter = 2 * (length + width)

    def __add__(self, tile):
        if tile.w == tile.w:
            return Tile(self.l + tile.l, self.w)

        else:
            return Tile(0, 0)

    def __mul__(self, tile):
        if tile.l == self.l:
            return Tile(self.l, self.w + tile.w)
        else:
            return Tile(0, 0)

    def __repr__(self):
        return f"| {self.l} x {self.w} |"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, tile):
        return (self.l == tile.l) and (self.w == tile.w)

    def __lt__(self, tile):
        return self.area < tile.area

    # def __ge__(self, tile):
    # return not self.__le__(tile)


def main(tilesfile, ntiles):
    # shapes = [(24, 24), (30, 24), (30, 30)]
    shapes = json.load(open("tiles.json"))
    tiles = list(map(lambda x: Tile(*x), shapes))

    all = list(perm(tiles, ntiles))

    valid = [np.sum(_) for _ in all] + [np.sum(_) for _ in all]

    valid = [x for x in valid if x != Tile(0, 0)]

    valid = np.unique(valid)

    print(f"Permuted {ntiles} tiles\n", valid, "\n\n")


if __name__ == "__main__":
    Fire(main)
