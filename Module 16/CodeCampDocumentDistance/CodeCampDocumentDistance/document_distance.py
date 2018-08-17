'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def delete_stopwords(adict):
    stopwords = load_stopwords("stopwords.txt")
    for words in stopwords:
        if words in adict:
            del adict[words]
    return adict
def format(adict):
    lower = adict.lower()
    form = re.sub('[^a-z\ ]', '', lower)
    return form

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    # for word in
    newdict1 = format(dict1)
    #newdict2 = format(dict2)
    newdict1 = newdict1.strip().split()
    newdict2 = newdict2.strip().split()
    adict1 = {}
    adict2 = {}
    list1=[]
    for word1 in newdict1:
        if word1 not in adict1:
            adict1[word1] = 1
        else:
            adict1[word1] += 1
    for word2 in newdict2:
        if word2 not in adict2:
            adict2[word2] = 1
        else:
            adict2[word2] += 1
    adict1 = delete_stopwords(adict1)
    adict2 = delete_stopwords(adict2)
    numerator = []
    denominator1 = []
    denominator2 = []
    for word in adict1:
        #print(adict1)
        if word in adict2:
            #print(adict2.keys)
            numerator.append(adict1[word] * adict2[word])
    for word in adict1:
            denominator1.append(adict1[word]**2)
    for word in adict2:
            denominator2.append(adict2[word]**2)
    numerator = sum(numerator)
    denominator = math.sqrt(sum(denominator1))*math.sqrt(sum(denominator2))
    return numerator/denominator
    # for word 
    #print(mul)
    #print(sum(mul))

def load_stopwords(stopwords):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords1 = []
    with open(stopwords, 'r') as wordsstop:
        for line in wordsstop:
            stopwords1.append(line.strip())
    return stopwords1

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
