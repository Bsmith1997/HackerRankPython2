def minion_game(string):
    string.upper()
    vowels = ('A', 'E', 'I', 'O', 'U')
    n = len(string)
    stuart_counter = 0
    kevin_counter = 0

    for i in range(n):
        if string[i] in vowels:
            kevin_counter += n - i
        else:
            stuart_counter += n - i

    if stuart_counter > kevin_counter:
        print "Stuart " + str(stuart_counter)
    elif kevin_counter > stuart_counter:
        print "Kevin " + str(kevin_counter)
    else: 
        print "Draw"

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
