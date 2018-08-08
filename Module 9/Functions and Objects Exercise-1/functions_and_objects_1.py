'''Exercise : Function and Objects Exercise-1'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(list2, func):
    '''Function in which mapping occurs'''
    return list(map(func, list2))
def main():
    '''Main function of converting negative to positive'''
    data = input()
    data = data.split()
    list1 = list(map(int, data))
    #list1 = []
    # print(list1)
    # for j in data:
    #     list1.append(int(j))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
