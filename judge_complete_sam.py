import argparse

parser = argparse.ArgumentParser(description='Detect whether a sam file has been output complete or not')
parser.add_argument('-i', '--input', type=str, help='Input file name')
args = parser.parse_args()

input = [i for i in open(args.input)]

if len(input[-1].split('\t')) != len(input[-2].split('\t')):
    print('Incomplete... ', args.input.split('/')[-1].split('.')[0])
else:
    print('Complete! ', args.input.split('/')[-1].split('.')[0])
