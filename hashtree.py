'''Noah Reuter-Gushow
Merkle Tree
Applied Crypto
'''
import hashlib
import sys
import os

'''opens the file and then computes the hash of file- returns hash'''
def compute_file_hash(filepath, algo='sha1'):
    hasher = hashlib.sha1() if algo == 'sha1' else hashlib.md5()
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

'''Build the merkle tree- only runs as many times as the total amount of hashes'''
def build_merkle_tree(hashes, algo='sha1'):
    if not hashes:
        return None
    while len(hashes) > 1:
        new_level = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i+1] if i+1 < len(hashes) else hashes[i]  # duplicate last if odd
            combined = left + right
            h = hashlib.sha1() if algo == 'sha1' else hashlib.md5()
            h.update(combined.encode())
            new_level.append(h.hexdigest())
        hashes = new_level
    return hashes[0]  # Top Hash
'''return hashes[0] - this returns the final hash value calulated from all hashes'''

'''main- this shows how to run the file, as well as calls the functions'''
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 hashtree.py <file1> <file2> ...")
        sys.exit(1)

    file_paths = sys.argv[1:]
    file_hashes = []

    print("Leaf Hashes:")
    for path in file_paths:
        if not os.path.isfile(path):
            print(f"Error: {path} is not a valid file.")
            sys.exit(1)
        file_hash = compute_file_hash(path)
        file_hashes.append(file_hash)
        print(f"{path}: {file_hash}")

    top_hash = build_merkle_tree(file_hashes)
    print("\nTop Hash:", top_hash)
'''Main runs'''
if __name__ == "__main__":
    main()