fname = "hello-world.txt"

with open(fname, "w") as f:
    f.write("Hello World")

with open(fname, "r") as f:
    print(f.read())  