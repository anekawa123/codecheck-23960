import json


def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]


def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])


# split str so that each cell has n cells
def split(str, size):
    return [str[i:i+size] for i in range(0, len(str), size)]


# fill str as len(str) is multiple of size
def fill(str, filler='0', size=6):
    return str + filler * ((size - len(str) % size) % size)


def removeTrailingEquals(str):
    i = 0
    while str[-(i+1)] == '=' and i < len(str):
        i += 1
    return str[:-i]


def encode_line(str):
    # make binary
    binary = ''.join(string2bits(str))
    # separate in 6 digits
    splited = split(fill(binary, '0', 6), 6)
    # mapping
    with open("base64_encode_table.json", "r") as table:
        base64Dict = json.loads(table.read())
        mapped = ''.join([base64Dict[bi] for bi in splited])
    # concat and filling by '='
    return fill(mapped, "=", 4)


def decode_line(str):
    # remove trailing equals.
    no_equal = removeTrailingEquals(str)
    # decode per character.
    # concat 6-digits
    # remove trailing 0s so that len(str) is multiple of 8.
    # split in 8-digits and call chr().
    # return concatenated characters.
    return 'decoded.'


def decode_file(in_file, out_file):
    with open(in_file, 'r', encoding='utf-8') as fin, \
      open(out_file, 'w', encoding='utf-8') as fout:
        for row in fin:
            fout.write(decode_line(row))


def encode_file(in_file, out_file):
    with open(in_file, 'r', encoding='utf-8') as fin, \
      open(out_file, 'w', encoding='utf-8') as fout:
        for row in fin:
            fout.write(encode_line(row))


def main(args):
    if args.e or (not args.e and not args.d):
        encode_file(args.i, args.o)
    else:
        decode_file(args.i, args.o)
