'''Exercise : Function and Objects Exercise-3'''
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(listt):
    '''Square function'''
    return listt**2
def apply_to_each(list1, func):
    '''Function for map'''
    return list(map(func, list1))

def main():
    '''Main Function'''
    data = input()
    data = data.split()
    list1 = list(map(int, data))
    # for j in l:
    #     list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()
