# MerkleHash

# Merkle Tree Hasher

This project implements a Merkle Hash Tree for verifying the integrity of files. It accepts any number of file paths, hashes each file, constructs a Merkle Tree using SHA1 or MD5, and outputs the final Top Hash. Modifying any of the input files will result in a different Top Hash, demonstrating file integrity verification.

---

## Files
- hashtree.py: Main Python script to compute Merkle Tree and Top Hash.

---

## Features
- Supports any number of input files 
- Uses SHA1 or MD5 for hashing (default: SHA1)
- Efficiently builds a binary Merkle Tree
- Detects file modifications by observing Top Hash changes

---

## Usage

### Run the script:

python hashtree.py file1.txt file2.txt file3.txt ...


### Example Output:

Leaf Hashes:
file1.txt: 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12
file2.txt: 3a7bd3e2360a3d80a5b1b902458b0f53c360f722


Top Hash: 867f70cf1ade02cff3752599a3a53dc4af34b0c8


---

## Notes
- If an odd number of file hashes exists at a tree level, the last hash is duplicated to form a pair.
- Default hash algorithm is SHA1. You can modify the code to use MD5 if preferred.

---

## Example Test
1. Run the script on a set of files.
2. Modify one file.
3. Run the script again — observe that the Top Hash Changes, showing the integrity check works.

---

## Why Use a Merkle Tree?
Merkle Trees allow efficient and secure verification of data integrity. They are used in blockchain, distributed systems, and secure file storage.

---

## Author
Built by Noah Reuter-Gushow
