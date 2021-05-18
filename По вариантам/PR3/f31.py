import struct


def f31(x):
    return {'A1': {'B1': [{'C1': (struct.unpack("1B", x[5:6])[0]), 'C2': (struct.unpack("<1Q", x[6:14])[0])},
                          {'C1': (struct.unpack("1B", x[14:15])[0]), 'C2': (struct.unpack("<1Q", x[15:23])[0])},
                          {'C1': (struct.unpack("1B", x[23:24])[0]), 'C2': (struct.unpack("<1Q", x[24:32])[0])},
                          {'C1': (struct.unpack("1B", x[32:33])[0]), 'C2': (struct.unpack("<1Q", x[33:41])[0])}],
                   'B2': (struct.unpack("1B", x[41:42])[0]),
                   'B3': (struct.unpack("<1Q", x[42:50])[0]),
                   'B4': (struct.unpack("<1f", x[50:54])[0])},
            'A2': (struct.unpack("<1d", x[54:62])[0]),
            'A3': (struct.unpack("<1H", x[62:64])[0]),
            'A4': (struct.unpack("<8s", x[64:72])[0]).decode('utf-8'),
            'A5': {'D1': [(struct.unpack("1b", x[72:73])[0]),
                          (struct.unpack("1b", x[73:74])[0]),
                          (struct.unpack("1b", x[74:75])[0]),
                          (struct.unpack("1b", x[75:76])[0]),
                          (struct.unpack("1b", x[76:77])[0]),
                          (struct.unpack("1b", x[77:78])[0])],
                   'D2': [(struct.unpack("1b", x[78:79])[0]),
                          (struct.unpack("1b", x[79:80])[0]),
                          (struct.unpack("1b", x[80:81])[0])]}}
