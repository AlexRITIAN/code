'''test file.read()'''

import collections
import pprint

def read():
    '''read file'''
    file_name = "123.txt"
    with open(file_name, 'r') as info:
        file_list = info.readlines()
        value = collections.Counter(file_list)
    value = pprint.pformat(value)
    print(value)


if __name__ == "__main__":
    read()
