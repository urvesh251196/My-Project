
def write_file(path, data, info):
    with open(path, 'a') as f:
        f.write(info)
        f.write(data + '\n')