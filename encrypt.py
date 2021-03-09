from functions import *
import sys, argparse

def encoder(msg, key):
    repeat = key[1]
    for i in range(0, repeat):
        msg = encrypt(msg, key)
    return msg

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--depth", dest ="depth", help="Depth", type = int)
    parser.add_argument("-r", "--repeat",dest = "repeat", help="Repeat", type = int)
    parser.add_argument("-m", "--msg", dest = "msg", help="Input Message")

    args = parser.parse_args()
    key = [args.depth, args.repeat]
    result = encoder(args.msg, key)
    print('\nkey:' + str(key) + '\n')
    print('input msg:' + args.msg + '\n')
    print('encrypted msg:' + result + '\n')








