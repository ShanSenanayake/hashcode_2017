import sys


def main(args):
    with open(args[0], 'r') as f:
        print(f.readline())

if __name__ == "__main__":
    main(sys.argv[1:])
