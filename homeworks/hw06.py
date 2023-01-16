"""
DSC 20 Homework 06
Name: Zehui Zhang
PID:  A16151490
"""


# Question 1
def hate_f(word):
    """
    # Create a string containning f and F
    # Write a base case that when word is ''
    # Check if every first latter in word is f or F
    # If the lecture is f or F, remove it and do recresion else do recresion

    >>> hate_f('FabFxx')
    'abxx'
    >>> hate_f('FfFf')
    ''
    >>> hate_f('ABCde')
    'ABCde'
    >>> hate_f('Barry')
    'Barry'
    >>> hate_f('MoDFDsffdunfg')
    'MoDDsdung'
    >>> hate_f('as~!efFFunfg')
    'as~!eung'
    """
    # the string containning f and F
    f_letter= 'fF'
    # base case that show the time to stop the recresion
    if word == '':
        return ''
    # Check if the first letter is in f_letter
    else:
        # Condition that the letter is F or f
        if word[0] in f_letter:
            # remove the f or F
            new_str = word.replace(word[0],'')
            return hate_f(new_str)
        # Conditin that the letter is not F or f
        else:
            return word[0]+hate_f(word[1:])


# Question 2
def encode(mapping, plaintext):
    """
    # Stop the recresion when plaintext is ''
    # store the output from the mapping dictionary which keys are plaintext

    >>> mapping = {'z': 'not', 'r': 'ece', 't': 'dsc'}
    >>> encode(mapping, 'zzr')
    'notnotece'
    >>> encode(mapping, 'zzt')
    'notnotdsc'
    >>> encode(mapping, 'ttzrr')
    'dscdscnoteceece'

    >>> mapping2 = {'z': 'not', 'r': 'ece', 't': 'dsc',\
    'a':'First','b':'Second','c':'Final'}
    >>> encode(mapping2, 'abbzcr')
    'FirstSecondSecondnotFinalece'
    >>> encode(mapping2, 'abzzrt')
    'FirstSecondnotnotecedsc'
    >>> encode(mapping2, 'ccrt')
    'FinalFinalecedsc'
    """
    # base case which is the time to stop the recresion
    if plaintext == '':
        return ''
    else:
        # smaller input
        smaller = plaintext[1:]
        # return the value as string and do the recresion
        return str(mapping[plaintext[0]]) + encode(mapping,smaller)


# Question 3
def climb_stair(n_steps):
    """
    # Write the base case which stop the recresion when n_steps less than one
    # Sum the number of ways when climb one step and two steps

    >>> climb_stair(2)
    2
    >>> climb_stair(5)
    8
    >>> climb_stair(8)
    34
    >>> climb_stair(7)
    21
    >>> climb_stair(9)
    55
    >>> climb_stair(20)
    10946
    """
    # magic number represent the step number 2
    num_step = 2
    # base case which indicates the time to stop when steps left less than one
    if n_steps<=1:
        return 1
    else:
        # number of ways when climb one step + numbers when climb two steps
        return climb_stair(n_steps-1)+climb_stair(n_steps-num_step)


# Question 4
def add_all_digits(num):
    """
    # Write a base case stoping recresion as sum of digits become a single-digit
    # Sum all digits
    # check  if sum is single-digit

    >>> add_all_digits(41)
    5
    >>> add_all_digits(567)
    9
    >>> add_all_digits(999777)
    3
    >>> add_all_digits(122311)
    1
    >>> add_all_digits(876872)
    2
    >>> add_all_digits(876)
    3
    """
    # Magic numbers
    single_dig = 10
    # Base case that stops the recresion
    if num<single_dig:
        return num
    else:
        # find out the sum of all digits
        sum =int(str(num)[0])+ add_all_digits(int(str(num)[1:]))
        # if the sum is single digit return it
        if sum < single_dig:
            return sum
        # if not put the sum as input to the function again until end
        else:
            return add_all_digits(sum)


# Question 5
def find_max_recursive(lst):
    """
    # Base case that stop the recresion when one element left in input
    # Compare the first two element in list
    # Remove the smaller one from the list and then continue the recresion

    >>> find_max_recursive([1, 2, 3, 4, 5])
    5
    >>> find_max_recursive([10, 11, 5, 0, -10, 1])
    11
    >>> find_max_recursive(['b', 'c', 'z', 'y', 'a', 'e'])
    'z'
    >>> find_max_recursive([121,23,12121,456,322])
    12121
    >>> find_max_recursive(['b', 'c','a','r','s'])
    's'
    >>> find_max_recursive([1021, 111, 5000, 0, -110, 1])
    5000
    """
    # base case stop the recresion when only one element left
    if len(lst)==1:
        return lst[0]
    else:
        # compare the first two elements in the list
        if lst[0]> lst[1]:
            # remove the smaller element
            del lst[1]
            # continue the recresion
            return find_max_recursive(lst)
        else:
            return find_max_recursive(lst[1:])


# Question 6
def skip_then_swap(string, n_skip, n_swap):
    """
    # When n_skip and n_swap reduce to 0, that is the time to stop the recresion
    # Similarly if the length of the string are odd, as reduced to one element
    # the recresion should be stoped
    # The base case shows the time to stop the recresion
    # Then shorten the string one step by one step until the end

    >>> skip_then_swap('kkkABXXXXCDkkk', 3, 2)
    'kkkDCXXXXBAkkk'
    >>> skip_then_swap('DSC20', 1, 2)
    'D2CS0'
    >>> skip_then_swap('skip_then_swap', 4, 3)
    'skip_neht_swap'
    >>> skip_then_swap('asdADACBABAdsa', 3, 2)
    'asdABACBADAdsa'
    >>> skip_then_swap('Barry_Zhang', 2, 2)
    'Baahy_Zrrng'
    >>> skip_then_swap('cccXYzzzMNddd', 3, 2)
    'cccNMzzzYXddd'
    """
    # the base case that represent the time to stop the recresion
    if n_skip==0 and n_swap==0 or len(string)==1:
        return string
    else:
        # First skip the character until the n_skip to 0
        if n_skip > 0:
            return string[0]+\
            skip_then_swap(string[1:-1], n_skip-1, n_swap)+string[-1]
        # swap the character for certain times until n_swap to 0
        elif n_swap >0:
            return string[-1]+\
            skip_then_swap(string[1:-1], n_skip, n_swap-1)+string[0]


# Question 7
def flatten_dict(nested_dict):
    """
    # Check the type of value in nested_dict
    # If it is a dictionary apply the func to it
    # store the result in the dic created at the beginning

    >>> flatten_dict({'A': 1, 'B': 2})
    {'A': 1, 'B': 2}
    >>> flatten_dict({'Hi': True, 'Hello': {'World': 'Java',
    ... 'Kitty': 'Python'}})
    {'Hi': True, 'HelloWorld': 'Java', 'HelloKitty': 'Python'}
    >>> flatten_dict({'A': {'B': 1, 'C': 2, 'D': {'E': 3, 'F': 4}},
    ... 'G': 5, 'H': 6})
    {'AB': 1, 'AC': 2, 'ADE': 3, 'ADF': 4, 'G': 5, 'H': 6}
    >>> flatten_dict({'First': 'a', 'Second': {'Name': 'Barry','Age': 20}})
    {'First': 'a', 'SecondName': 'Barry', 'SecondAge': 20}
    >>> flatten_dict({'A': {'a':'A','b':'B','c':'C'},'B': {'1':1,'2':2}})
    {'Aa': 'A', 'Ab': 'B', 'Ac': 'C', 'B1': 1, 'B2': 2}
    >>> flatten_dict({'A': {'a':'A','b':{'aa':'a','bb':'b'},'c':'C'},\
    'B': {'1':1,'2':2}})
    {'Aa': 'A', 'Abaa': 'a', 'Abbb': 'b', 'Ac': 'C', 'B1': 1, 'B2': 2}
    """
    # Create a new dictionary to store the result
    dic = {}
    # Base case
    if len(nested_dict) == 0:
        return dic
    else:
        for key1,value1 in nested_dict.items():
            # check the type of value in nested_dict
            if type(value1)==dict:
                new=flatten_dict(value1)
                # flatten the inner dictionary
                for key2,value2 in new.items():
                    dic[key1+key2] = value2
            else:
                dic[key1]=value1
        # return the dic created with result
        return dic
