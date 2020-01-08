

def dec(f):
    # This function is what we "replace" hello with
    def wrapper(*first):
        print('....')
        print(first)
        if first:
            return f('hello', 'young man')  # Call hello
        else:
            return f('login', '')
    return wrapper