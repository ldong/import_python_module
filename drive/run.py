import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from ldong.another.here import hello
from ldong.myprint import print_name

def main():
    # print_name("Hi");
    hello()


if __name__ == "__main__":
    main()
