'''Exercise : Odd Tuples'''
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as
# input and returns a tuple in which contains odd index values in the input tuple
def oddtuples(atup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    return atup[::2]
def main():
    '''Main Function for printing odd places'''
    data = input()
    data = data.split()
    atup = tuple(data)
    # for j in range(len(data)):
    #     atup += ((data[j]),)
    print(oddtuples(atup))
if __name__ == "__main__":
    main()
