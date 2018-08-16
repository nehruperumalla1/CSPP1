'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
# adict = {}
# def result(rank, hand):
#     global adict
#     if rank not in adict:
#         adict[rank] = [hand]
#     else:
#         adict[rank].append(hand)
#     print(adict)    
#     return adict
def func1(hand):
    '''Function call for one/two pair'''
    string = '--23456789TJQKA'
    rank_list = [num for num in string]
    #print(rank_list)
    set1 = set()
    for num, _ in hand:
        set1.add(rank_list.index(num))
    return set1
def is_onepair(hand):
    '''Function for One pair'''
    string = '--23456789TJQKA'
    rank_list = [num for num in string]
    #print(rank_list)
    set1 = set()
    l = []
    for num, _ in hand:
        l.append(rank_list.index(num))
        set1.add(rank_list.index(num))
    if len(set1) == 4:
        print(l)
        for index in set1:
            if l.count(index) == 2:
                return index/10
    return False
def is_twopair(hand):
    '''Function for twopair'''
    set1 = func1(hand)
    if len(set1) == 3:
        return True
    return False
def three_four(hand):
    '''Function call for Three/four kind, full house'''
    length = len(hand)
    yaar = []
    for index in range(length):
        if hand[index][0] == 'T':
            yaar.append(10)
        elif hand[index][0] == 'J':
            yaar.append(11)
        elif hand[index][0] == 'Q':
            yaar.append(12)
        elif hand[index][0] == 'K':
            yaar.append(13)
        elif hand[index][0] == 'A':
            yaar.append(14)
        else:
            yaar.append(int(hand[index][0]))
    yaar.sort()
    yaarcopy = yaar.copy()
    counter = []
    jindex = 0
    set1 = set(yaar)
    for jindex in set1:
        counter.append(yaar.count(jindex))
    return counter
def three_kind(hand):
    '''Function for three kind'''
    counter = three_four(hand)
    counter = max(counter)
    if counter == 3:
        return True
    return False
def four_kind(hand):
    '''Function for four_kind'''
    counter = three_four(hand)
    counter = max(counter)
    if counter == 4:
        return True
    return False
def fullhouse(hand):
    '''Function for FullHouse'''
    counter = three_four(hand)
    if 3 in counter:
        if 2 in counter:
            return True
    return False

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
'''
    length = len(hand)
    yaar = []
    for index in range(length):
        if hand[index][0] == 'T':
            yaar.append(10)
        elif hand[index][0] == 'J':
            yaar.append(11)
        elif hand[index][0] == 'Q':
            yaar.append(12)
        elif hand[index][0] == 'K':
            yaar.append(13)
        elif hand[index][0] == 'A':
            yaar.append(14)
        else:
            yaar.append(int(hand[index][0]))
    count = 0
    yaar.sort()
    for index in range(len(hand)-1):
        if yaar[index] == yaar[index+1]-1:
            count += 1
    if count == len(hand)-1:
        return True
    return False
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    l = []
    for num,suite in hand:
        l.append(suite)
        # if hand[index][1] != hand[index+1][1]:
        #     return False
    s = set(l)
    return len(s) == 1 

def high_card(hand):
    set1 = func1(hand)
    if len(set1) == 5 and not is_flush(hand):
        return max(set1)/100
    return False

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    # if is_straight(hand) and is_flush(hand):
    #   return
    if is_straight(hand) and is_flush(hand):
        #print(result(8, hand))
        #print(adict)
        return 8
    if four_kind(hand):
        #result(7, hand)
        return 7
    if fullhouse(hand):
        #result(6, hand)
        return 6
    if is_flush(hand):
        #result(5, hand)
        return 5
    if is_straight(hand):
        #result(4, hand)
        return 4
    if three_kind(hand):
        #result(3, hand)
        return 3
    if is_twopair(hand):
        #result(2, hand)
        return 2
    return is_onepair(hand)
        #result(1, hand)
    return high_card(hand)

    #return high_card(hand) and not (is_straight(hand) and is_flush(hand)) and not (four_kind(hand)) and not (fullhouse(hand))
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    # res = list(map(hand_rank,hands))
    # print(res)
    # for i in res:
    #     if res.count(i) > 1:
    #         print(i)
    #     res.remove(i)
    return max(hands, key=hand_rank)
if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
