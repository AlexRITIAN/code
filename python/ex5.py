import argparse

paser = argparse.ArgumentParser(description="this is description",epilog="thi is epilog")
paser.add_argument("ints",type=int,nargs="+")
paser.add_argument("-s",dest="sum",action="store_const",const=sum,default=max,help="sum the integres(default : find the max)")
args = paser.parse_args()
print(args.sum(args.ints))