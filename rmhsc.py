#!/usr/bin/env python

import argparse
import binascii
import itertools
import pickle
import random
import sys
import time

from array import *


def genmaps(_):
    print('Generating mapping file...')

    maps = [''.join(i) for i in itertools.product(list('espinoza'), repeat=8)]
    random.shuffle(maps)

    states = [''.join(i) for i in itertools.product(['1', '0'], repeat=8)]

    map_dict = {}
    for s in states:
        s_index = states.index(s)
        map_dict[s] = maps[65536*s_index:65536*(s_index+1)]

    with open('mapping.p', 'wb') as f:
        pickle.dump(map_dict, f)


def encryption(params):
    input_file, output_file = params
    print('Encrypting file...')

    with open('mapping.p', 'rb') as f:
        map_dict = pickle.loads(f.read())

    ciphertext = ''
    with open(input_file, 'rb') as f:
        while True:
            byte = f.read(1)
            if not byte:
                break
            b = bin(int.from_bytes(byte, 'little'))[2:].zfill(8)
            ciphertext += random.choice(map_dict[b])

    with open(output_file, 'w') as f:
        f.write(ciphertext)


def decryption(params):
    input_file, output_file = params
    print('Decrypting file...')

    with open('mapping.p', 'rb') as f:
        map_dict = pickle.loads(f.read())

    with open(input_file) as f:
        ciphertext = f.read()

    enc_letters = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]

    def search_mapping(c):
        for k, vals in map_dict.items():
            for v in vals:
                if v == c:
                    return k

    bin_array = array('B')
    for c in enc_letters:
        b = search_mapping(c)
        bin_array.append(int(b, 2))
    f = open(output_file, 'wb')
    bin_array.tofile(f)
    f.close()


def timeit(func, params):
    start_time = time.time()
    out = func(params)
    print('Completed {0} in {1:.2f} seconds.'.format(func.__name__, time.time() - start_time))
    return out


def get_parser():
    parser = argparse.ArgumentParser(description='rich man\'s homophonic substitution cipher')
    parser.add_argument('-g', '--genmaps',
                        help='generate mapping file', action='store_true')
    parser.add_argument('-e', '--encrypt',
                        help='encrypt a file', action='store_true')
    parser.add_argument('-d', '--decrypt',
                        help='decrypt a file', action='store_true')
    parser.add_argument('-i', '--input',
                        help='input file', type=str)
    parser.add_argument('-o', '--output',
                        help='output file', type=str)

    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if not (args['genmaps'] or args['encrypt'] or args['decrypt']):
        parser.print_help()
        return

    if args['genmaps']:
        timeit(genmaps, params=None)
        return

    if not args['input']:
        print('Input file not supplied.')
        return
    if not args['output']:
        print('Output file not supplied.')
        return

    if args['encrypt']:
        timeit(encryption, params=[args['input'], args['output']])
        return
    if args['decrypt']:
        timeit(decryption, params=[args['input'], args['output']])
        return


if __name__ == '__main__':
    main()
