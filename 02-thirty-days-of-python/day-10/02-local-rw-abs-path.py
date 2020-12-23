import os

this_file_path = os.path.abspath(__file__)
print("This file's absolute path", this_file_path)

BASE_DIR = os.path.dirname(this_file_path)
print("This file's absolute directory", BASE_DIR)

DATA_DIR = os.path.join(BASE_DIR, "data")
if(not os.path.exists(DATA_DIR)):
    print("Data directory doesn't exist, creating!!")
    os.makedirs(DATA_DIR, exist_ok=False)
else:
    print("Data directory exists, not creating")

for i in range(10):
    file_name = os.path.join(DATA_DIR, f"file-{i}.txt")
    with open(file_name, "w") as f:
        f.write(f"Hello world, this is file number {i}")

print(f"Wrote 10 files to data directory {DATA_DIR}")
