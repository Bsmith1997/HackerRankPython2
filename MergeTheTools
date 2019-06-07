def merge_the_tools(string, k):
    for part in zip(*[iter(string)] * k):
        dictionary = dict()
        print(''.join([ dictionary.setdefault(c, c) for c in part if c not in dictionary ]))

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    
