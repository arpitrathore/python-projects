import os

def create_dir(dir_name):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(BASE_DIR, dir_name)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path

def create_binary_file(base_dir, file_name, content):
    file_path = os.path.join(base_dir, file_name)
    
    with open(file_path, "wb") as f:
        f.write(content)
        print("Binary file created. Path : ", file_path)