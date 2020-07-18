import sys
import add

if __name__ == "__main__":
    print(sys.argv)
    if sys.argv[1] == 'add':
        v = [int(i) for i in sys.argv[2:]]
        print(add.add(*v))
