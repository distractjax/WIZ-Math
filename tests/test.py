from os import path

def test():
    print(f"{path.expanduser('~')}")

if __name__ == '__main__':
    test()
