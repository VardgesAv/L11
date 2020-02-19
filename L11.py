from contextlib import contextmanager

@contextmanager
def open_file(name):
    f =  open(name, "w")
    yield f
    f.close()

with open_file("example.txt") as f:
    f.write("hola!")