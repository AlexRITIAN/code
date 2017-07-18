import argparse

def getSum(n1,n2,n3):
    s = n1 * 1 + n2 * 2 + n3 * 3
    return s

def getParse():
    parse = argparse.ArgumentParser(description="sum the integers")
    parse.add_argument("n1",type=int,nargs=1)
    parse.add_argument("n2",type=int,nargs=1)
    parse.add_argument("n3",type=int,nargs=1)
    return parse

def main():
    parse = getParse()
    args = parse.parse_args()
    args = vars(parse.parse_args())
    n1 = args['n1'][0]
    n2 = args['n2'][0]
    n3 = args['n3'][0]
    print(getSum(n1,n2,n3))
if __name__ == "__main__":
    main()