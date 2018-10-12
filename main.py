from pyramid import Pyramid

import argparse


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

# for trails mode
# --trails -output res/output_trails.txt


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-input", nargs='?', default="res/input.txt")
    parser.add_argument("-output", nargs='?', default="res/output.txt")
    parser.add_argument("--trails", action='store_true')
    args = parser.parse_args()

    vals = vals_from_file(args.input)
    pyramid = Pyramid(vals)
    pyramid.calc_path_sums(include_trails=args.trails)
    make_output(args.output, pyramid._path_sums)
