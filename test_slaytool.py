import os
import subprocess

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Command failed: {cmd}")
        print(f"Error output: {result.stderr}")
        return False
    return True

def test_slaytool():
    # Create a sample input file
    sample_content = "This is a test message for encryption and decryption."
    with open("sample.txt", "w") as f:
        f.write(sample_content)

    # Encode the file
    if not run_command("python slaytool.py encode sample.txt encoded.txt"):
        return False

    # Decode the file back
    if not run_command("python slaytool.py decode encoded.txt decoded.txt"):
        return False

    # Verify the decoded content matches the original
    with open("decoded.txt", "r") as f:
        decoded_content = f.read()

    if decoded_content != sample_content:
        print(f"Decoded content doesn't match original:")
        print(f"Original: {sample_content}")
        print(f"Decoded: {decoded_content}")
        return False

    # Clean up test files
    os.remove("sample.txt")
    os.remove("encoded.txt")
    os.remove("decoded.txt")

    print("All tests passed!")
    return True

if __name__ == "__main__":
    test_slaytool()