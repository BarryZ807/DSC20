"""
DSC 20 Lab 02
Name: Zehui Zhang
PID:  A16151490
"""

# Question 1
def check_Blackjack(player1, player2):
    """
    Returns a list of results of the Blackjack game between player1 and
    player 2. For the i-th round, the i-th index of player1 list represents
    the sum of all cards of player1, and the i-th index of player2 list
    represents player2's card sum. The i-th index of the returned list should
    be the winner's card sum. If the card sum is closer to 21 but not going
    over it, that player wins. If both players' card sum go over 21 in a
    round, we put 0 for that round instead.

    Parameters:
        player1 (List[int]): card sums for player 1
        player2 (List[int]): card sums for player 2

    Returns:
        (List[int]): game results judged with the rule above

    Assumptions:
        player1 and player2 will always have the same length

    >>> check_Blackjack([19, 21, 22], [21, 19, 3])
    [21, 21, 3]
    >>> check_Blackjack([17, 21, 22, 29], [15, 19, 3, 4])
    [17, 21, 3, 4]
    >>> check_Blackjack([], [])
    []
    """
    result = []
    for i in range(len(player1)):
        if player1[i] > 21 and player2[i] > 21:
            result.append(0)
        elif player1[i] <= 21 and player2[i] > 21:
            result.append(player1[i])
        elif player1[i] >21 and player2[i] <= 21:
            result.append(player2[i])
        elif player1[i] <= 21 and player2[i] <= 21:
            result.append(max([player1[i],player2[i]]))
    return result


# Question 2
def majority_element(nums):
    """
    Returns the majority element in the `nums` list. The majority element
    is the element that appears more than ⌊ n/2 ⌋ times, where n is the length
    of `nums` list.

    Parameters:
        nums (List[int]): the list of integers to apply this function

    Returns:
        (int) the majority element found

    Assumptions:
        `nums` list is non-empty
        A majority element always exists in `nums` list

    >>> majority_element([3,2,3])
    3
    >>> majority_element([2,2,1,1,1,2,2])
    2
    >>> majority_element([1,1,2,2,2])
    2
    """
    index = -1
    num_count = 0
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count +=1
            if count > num_count:
                num_count = count
                index = i
            if num_count > len(nums)//2:
                return nums[index]


# Question 3
def remove_vowels(string):
    """
    Removes vowels (a, e, i, o, u) from `string` and returns the resulted
    string. Capitalized vowel letters should also be removed.

    Parameters:
        string (str): the string to apply this function

    Returns:
        (str): the string with vowel letters removed

    >>> remove_vowels('Hello')
    'Hll'
    >>> remove_vowels('')
    ''
    >>> remove_vowels('Hi how are...you?')
    'H hw r...y?'
    """
    for i in string:
        for j in 'aeiou':
            if i == j:
                string = string.replace(j,'')
    return string


# Question 4
def pig_latin(string):
    """
    Returns `string` translated into Pig Latin. Please read the write-up
    for specific rules of translating a string into Pig Latin.

    However, for whatever reason we are afraid of 8 letter words. If we
    encounter a 8 letter word, we will immediately stop translating and
    return what we have translated so far.

    Parameters:
        string (str): the string to translate

    Returns:
        (str): the translated string

    Assumptions:
        there will be no punctuation in `string`.
        all words will only be separated by one space.
        all words will have at least one vowel.

    >>> pig_latin('Hi how are you')
    'iHay owhay areyay ouyay'
    >>> pig_latin('Absolute')
    ''
    >>> pig_latin('When words begin with consonant clusters')
    'enWhay ordsway eginbay ithway onsonantcay'
    """
    outcome = []
    vowel='aeiouAEIOU'
    str_1 = string.split()
    for i in str_1:
        if len(i) == 8:
            break
        if i[0] in vowel:
            outcome.append(i+'yay')
        if i[0] not in vowel:
            n = 0
            for x in i:
                if x in vowel:
                    temp1 = i[n:]+i[:n]+'ay'
                    outcome.append(temp1)
                    break
                n += 1
    temp2 = ''
    for n in outcome:
        temp2 = temp2+n+' '
    temp2 = temp2[:-1]
    return temp2
