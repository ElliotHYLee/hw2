from functions import *
import sys, argparse

def decoder(msg, key):
    repeat = key[1]
    for i in range(0, repeat):
        msg = decrypt(msg, key)
    return msg

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--depth", dest ="depth", help="Depth", type = int)
    parser.add_argument("-r", "--repeat",dest = "repeat", help="Repeat", type = int)
    parser.add_argument("-m", "--msg", dest = "msg", help="Input Message")

    args = parser.parse_args()
    key = [args.depth, args.repeat]
    result = decoder(args.msg, key)
    print('\nkey:' + str(key) + '\n')
    print('input msg:\n' + args.msg + '\n')
    print('decrypted msg:\n' + result + '\n')
