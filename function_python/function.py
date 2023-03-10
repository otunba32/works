def greet(name):
    '''
    greet salutes the name passed to it
    '''
    print('Good day {}!'.format(name))

def count_to(number):
    '''
    counts from 1 to the 'number' given
    '''
    number = int(number)
    for i in range(1, number+1):
        print(i, end=' ')
    print()

if __name__ == '__main__':
    greet('Maleek')
    count_to(10)
