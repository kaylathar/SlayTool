# SlayTool - Slay The Spire Save File Encoder/Decoder

SlayTool is a command-line utility for encoding and decoding Slay The Spire save files using XOR encryption with Base64 encoding.

## Usage

### Encoding a file

```bash
python slaytool.py encode <input_file> <output_file>
```

- `<input_file>`: Path to the file you want to encode (typically a Slay The Spire save file)
- `<output_file>`: Path where the encoded data will be saved

### Decoding a file

```bash
python slaytool.py decode <input_file> <output_file>
```

- `<input_file>`: Path to the file you want to decode (an encoded Slay The Spire save file)
- `<output_file>`: Path where the decoded data will be saved
