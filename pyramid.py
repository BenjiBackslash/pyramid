class Pyramid(object):
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
            yield Pyramid(self._row+1, col, self._vals)

vals = {
    0: { 0: 55},
    1: {0:94, 1:48},
    2: {0:95, 1:30, 2:28},
    3: {0:77, 1:71, 2:26, 3:28}
}

results = {}

def add_result(v):
    if v in results:
        results[v] +=1
    else:
        results[v] = 1

def calc(base, pyramid):
    base += pyramid.root_value()
    if pyramid.has_children():
        for child in pyramid.children():
            calc(base, child)
    else:
        add_result(base)



if __name__ == "__main__":
    pyramid = Pyramid(0,0,vals)
    calc(0, pyramid)
    print(results)


