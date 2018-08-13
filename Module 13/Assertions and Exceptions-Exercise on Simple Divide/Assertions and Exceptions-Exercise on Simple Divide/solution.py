'''define the simple_divide function here'''
def simple_divide(item, denom):
    '''Division Try Except Block'''
    # start a try-except block
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

def fancy_divide(list_of_numbers, index):
    '''Denom Function'''
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]

def main():
    '''Main Function For Division'''
    data = input()
    line = data.split()
    line1 = []
    for jindex in line:
        line1.append(float(jindex))
    num = input()
    index = int(num)
    print(fancy_divide(line1, index))
if __name__ == "__main__":
    main()
