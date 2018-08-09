'''Exercise : how many'''
# write a procedure, called how_many, which returns the sum of the
# number of values associated with a dictionary.


def how_many(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    sum1 = 0
    values = adict.values()
    for index in values:
        sum1 += len(index)
    return sum1

def main():
    '''Main Function for Dictionary'''
    number = input()
    adict = {}
    for _ in range(int(number)):
        string = input()
        list1 = string.split()
        if list1[0][0] not in adict:
            adict[list1[0][0]] = [list1[1]]
        else:
            adict[list1[0][0]].append(list1[1])
    print(how_many(adict))
if __name__ == "__main__":
    main()
