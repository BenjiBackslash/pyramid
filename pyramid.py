class Pyramid(object):
    def __init__(self, vals):
        self._vals = vals
        self._path_sums = {}

    def add_result(self, v, trail=None):
        if v in self._path_sums:
            self._path_sums[v]["n"] += 1
            if trail is not None:
                self._path_sums[v]["trails"].append(trail)
        else:
            self._path_sums[v] = {"n": 1, "trails": None if trail is None else [trail]}

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





