
def hello():
    print 'Hello world'
    
def add(*args):
    sum = 0
    for val in args:
        sum += val
    return sum

def meaning(the_meaning = 42):
    print 'The meaning to life, the universe, and ' + \
    'everything is %d' % the_meaning
    
def multiples_less_than(value, max_value):
    add = value
    multiples = list()
    while value < max_value:
        multiples.append(value)
        value += add
    return multiples

def find_max(number_list):
    max_val = number_list.pop()
    for val in number_list:
        if val > max_val:
            max_val = val
    return max_val