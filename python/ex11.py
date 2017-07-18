import pprint
import collections

def main():
    file_input = input('filename : ')
    with open(file_input,'r') as info:
        count = collections.Counter(info.read().upper())
    
    value = pprint.pformat(count)
    print(value)

if __name__ == "__main__":
    main()