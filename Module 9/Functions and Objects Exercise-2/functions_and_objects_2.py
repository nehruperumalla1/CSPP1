'''Exercise : Function and Objects Exercise-2'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def inc(listt):
    '''Function for squaring a number'''
    return listt+1


def apply_to_each(list1, _):
    '''Function for map'''
    return list(map(inc, list1))


def main():
    '''Main function for input data'''
    data = input()
    data = data.split()
    list1 = list(map(int, data))
    print(apply_to_each(list1, inc))


if __name__ == "__main__":
    main()
