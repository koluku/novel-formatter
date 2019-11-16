import sys
import re


def main(args):
    input_file = args[1]

    with open(input_file, "r") as f:
        body = f.read()
        body = re.sub(r"(?<![。」])(\n)+", "\n", body)

    with open(input_file, "w") as f:
        f.write(body)


if __name__ == "__main__":
    args = sys.argv
    main(args)
