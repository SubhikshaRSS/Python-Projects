''' Take sys arguments '''
import sys
print("File name:", sys.argv[0])
print("First argument:", sys.argv[1])

''' Take arg parse '''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("adv")
args = parser.parse_args()
print("Hello", args.adv)

