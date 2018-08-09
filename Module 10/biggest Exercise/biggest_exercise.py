'''Exercise : Biggest Exercise'''
#Write a procedure, called biggest, which returns the key corresponding to the entry with the
#largest number of values associated with it. If there is more than one such entry,
#return any one of the matching keys.


def biggest(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    maximum = 0
    case = ''
    for value in adict:
        if len(adict[value]) > maximum:
            maximum = len(adict[value])
            case += value
    return case[-1]
def main():
    '''Main Function Biggest Exercise'''
    number = input()
    adict = {}
    for _ in range(int(number)):
        string = input()
        list1 = string.split()
        if list1[0][0] not in adict:
            adict[list1[0][0]] = [list1[1]]
        else:
            adict[list1[0][0]].append(list1[1])
    print(biggest(adict))


if __name__ == "__main__":
    main()
