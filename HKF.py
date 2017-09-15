path='D:/urvesh/Project/Program/2.csv'

def write_file(data, info):
    with open(path, 'a') as f:
        f.write(info)
        f.write(data + '\n')
