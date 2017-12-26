import sys
from app.main import main
import argparse

parser = argparse.ArgumentParser(description="argparser")
parser.add_argument("-i", type=str, help="input file name", required=True)
parser.add_argument("-o", type=str, help="output file name", required=True)
parser.add_argument('-e', action='store_true')
parser.add_argument('-d', action='store_true')

args = parser.parse_args()
main(args)
