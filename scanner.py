import numpy as np
from itertools import permutations

NOROT = np.matrix('1 0 0; 0 1 0; 0 0 1')
ROT_X1 = np.matrix('1 0 0; 0 0 -1; 0 1 0')
ROT_X2 = np.matrix('1 0 0; 0 -1 0; 0 0 -1')
ROT_X3 = np.matrix('1 0 0; 0 0 1; 0 -1 0')
ROT_X = [NOROT, ROT_X1, ROT_X2, ROT_X3]
ROT_Y1 = np.matrix('0 0 1; 0 1 0; -1 0 0')
ROT_Y2 = np.matrix('-1 0 0; 0 1 0; 0 0 -1')
ROT_Y3 = np.matrix('0 0 -1; 0 1 0; 1 0 0')
ROT_Y = [NOROT, ROT_Y1, ROT_Y2, ROT_Y3]
ROT_Z1 = np.matrix('0 -1 0; 1 0 0; 0 0 1')
ROT_Z2 = np.matrix('-1 0 0; 0 -1 0; 0 0 1')
ROT_Z3 = np.matrix('0 1 0; -1 0 0; 0 0 1')
ROT_Z = [NOROT, ROT_Z1, ROT_Z2, ROT_Z3]


class Scanner:
    def __init__(self, number):
        self.number = number
        self.beacons = []
        self.rots = []
        self.matching = {}
        self.fixed = False
        self.trans_to_zero = (0, 0, 0)

    def __str__(self):
        return f"Scanner {self.number} with {len(self.beacons)} beacons."

    def get_id(self):
        return self.number

    def add_beacon(self, x, y, z):
        beacon = np.array([x,y,z])
        self.beacons += [beacon]

    def generate_rotations(self):
        bm = np.matrix(self.beacons)
        self.rots = []
        for x in ROT_X:
            for y in ROT_Y:
                for z in ROT_Z:
                    nm = bm.dot(x).dot(y).dot(z)
                    self.rots += [nm]

    def get_beacons(self):
        return self.beacons

    def get_beacon_list(self):
        result = []
        for b in self.beacons:
            result += [b.tolist()]
        return result

    def get_absolute_beacons(self):
        result = []
        for c in self.rots[0].tolist():
            result += [(c[0] + self.trans_to_zero[0], c[1] + self.trans_to_zero[1], c[2] + self.trans_to_zero[2])]
        return result

    def get_rotations(self):
        return self.rots

    def fix_rotation(self, rot):
        self.rots = [rot]
        self.fixed = True

    def get_overlapping2(self, scanner2):
        base = self.get_absolute_beacons()
        rots = scanner2.get_rotations()
        for rot in rots:
            matches = {}
            for b1 in base:
                for b2 in rot.tolist():
                    dx, dy, dz = b1[0] - b2[0], b1[1] - b2[1], b1[2] - b2[2]
                    matches[(dx, dy, dz)] = matches.get((dx, dy, dz), 0) + 1
            nb_match = max(matches.values())
            if nb_match >= 12:
                for k, v in matches.items():
                    if v >= 12:
                        # self.matching[scanner2.get_id()] = k
                        scanner2.set_trans_to_abs(*k)
                        scanner2.fix_rotation(rot)
                        return True, scanner2.get_absolute_beacons()
        return False, None

    def get_trans_to_abs(self):
        return self.trans_to_zero

    def set_trans_to_abs(self, dx, dy, dz):
        self.trans_to_zero = (dx, dy, dz)