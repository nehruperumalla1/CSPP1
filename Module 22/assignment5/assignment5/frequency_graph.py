'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''Printing Frequency'''
    letter = '#'
    for index in sorted(dictionary.keys()):
        for _ in range(dictionary[index]):
            if isinstance(dictionary[index], int):
                dictionary[index] = letter
            else:
                dictionary[index] += letter
        print(index, '-', dictionary[index])

def main():
    '''main function'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
