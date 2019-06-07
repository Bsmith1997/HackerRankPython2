import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    string = wrapper.fill(text=string) 
    return string

    
if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
