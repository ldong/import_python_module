import os.path, sys
# sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
sys.path.append(os.path.abspath(__file__ + "/../../../"))


from ldong.another.here import hello

def main():
    # print_name("Hi");
    hello()


if __name__ == "__main__":
    main()
