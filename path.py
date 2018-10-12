class Pyramid(object):
    def __init__(self, vals):
        self._vals = vals
        self._path_sums = {}

    def add_result(self, v, trail=None):
        if v in self._path_sums:
            self._path_sums[v]["n"] +=1
            if trail is not None:
                self._path_sums[v]["trails"].append(trail)
        else:
            self._path_sums[v] = {"n":1, "trails": None if trail is None else [trail]}

    def _calc_path_sums(self, base_val, path, base_trail=None):
        base_val += path.root_value()
        _base_trail = None
        if base_trail is not None:
            _base_trail = list(base_trail)
            _base_trail.append(path.root_value())
        if path.has_children():
            for child in path.children():
                self._calc_path_sums(base_val, child, _base_trail)
        else:
            self.add_result(base_val, _base_trail)

    def calc_path_sums(self, include_trails=False):
        self._calc_path_sums(0, Path(0, 0, self._vals), base_trail=None if not include_trails else [])


class Path(object):
    def __init__(self, row, col, vals):
        self._col = col
        self._row = row
        self._vals = vals

    def root_value(self):
        return self._vals[self._row][self._col]

    def has_children(self):
        return not self._row+1 == len(self._vals)

    def children(self):
        for col in [self._col, self._col + 1]:
            yield Path(self._row + 1, col, self._vals)

vals = {
    0: { 0: 55},
    1: {0:94, 1:48},
    2: {0:95, 1:30, 2:28},
    3: {0:77, 1:71, 2:26, 3:28}
}

def vals_from_file(file_path):
    vals = {}
    row_idx = 0
    with open(file_path, "r") as fdr:
        for line in fdr:
            if line.startswith("#"):
                break
            vals[row_idx] = {}
            for col, x in enumerate([int(s) for s in line.split(" ")]):
                vals[row_idx][col] = x
            row_idx += 1

    return vals

def make_output(file_path, occur_dict):
    with open(file_path, "w") as fdw:
        for k,v in sorted(occur_dict.items()):
            output_line = "{} | {}\n".format(k,v["n"])
            if v["trails"] is not None:
                output_line += "  TRAILS: {}\n".format(v["trails"])
            fdw.write(output_line)


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-input", nargs='?', default="res/input.txt")
parser.add_argument("-output", nargs='?', default="res/output.txt")
parser.add_argument("--trails", action='store_true')
args = parser.parse_args()

# for trails mode
# --trails -output res/output_trails.txt

if __name__ == "__main__":
    vals = vals_from_file(args.input)
    pyramid = Pyramid(vals)
    pyramid.calc_path_sums(include_trails=args.trails)
    make_output(args.output, pyramid._path_sums)






