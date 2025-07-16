import argparse
from itertools import cycle
import base64

def xor(input_string, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(input_string, cycle(key)))

def process_file(input_file, output_file, key, encode=True):
    with open(input_file, 'r') as f:
        input_data = f.read()

    if encode:
        processed_data = base64.b64encode(xor(input_data, key).encode('utf-8'))
    else:
        decoded_bytes = base64.b64decode(input_data)
        processed_data = xor(decoded_bytes.decode("utf-8"), key)

    mode = 'wb' if encode else 'w'
    encoding = None if encode else "utf-8"

    with open(output_file, mode, encoding=encoding) as f:
        f.write(processed_data)

def main():
    parser = argparse.ArgumentParser(description='Encode or decode files using XOR encryption and Base64 encoding.')
    subparsers = parser.add_subparsers(dest='command')

    encode_parser = subparsers.add_parser('encode', help='Encode a file')
    encode_parser.add_argument('input_file', help='Input file to encode')
    encode_parser.add_argument('output_file', help='Output file to write encoded data')

    decode_parser = subparsers.add_parser('decode', help='Decode a file')
    decode_parser.add_argument('input_file', help='Input file to decode')
    decode_parser.add_argument('output_file', help='Output file to write decoded data')

    args = parser.parse_args()

    key = "key"

    if args.command == 'encode':
        process_file(args.input_file, args.output_file, key, encode=True)
    elif args.command == 'decode':
        process_file(args.input_file, args.output_file, key, encode=False)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
