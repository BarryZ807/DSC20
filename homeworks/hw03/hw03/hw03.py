"""
DSC 20 Homework 03
Name: Zehui Zhang
PID:  A16151490
"""


# Question 1
def assert_playground(num, lst, *args, **kwargs):
    """

    # Make several assert statements that chek all the condtion one by one
    # If all assert statements passed, return the num

    >>> assert_playground(1.5, [9.5, 1], -3.1, -9.2, s1="sS", s2="DSC20")
    1.5
    >>> assert_playground(15, [9.5, 1], -3.1, -9.2, s1="sS", s2="DSC20")
    Traceback (most recent call last):
    AssertionError
    >>> assert_playground(1.5, [0, 1], -3.1, -9.2, s1="sS", s2="DSC20")
    Traceback (most recent call last):
    AssertionError
    >>> assert_playground(1.2, [8.7,2], -0.1, -4.9, s1="SS", s2="DSC20")
    1.2
    >>> assert_playground(1.3, [1], -0.1,-4,2, s1="SS")
    Traceback (most recent call last):
    AssertionError
    >>> assert_playground(12.1, [9.5, 1], -3.1, -9.2, s1="sS", s2="DSC20")
    12.1
    """
    lower_range = -5.0
    upper_range = -1.0
    # assertion to check if num is a positive float
    assert type(num) == float
    assert num > 0
    # assertion to check if the sum of list is greater than 10
    # if not, They may smaller than 10
    # and the list may conclude strings
    assert sum(lst) > 10
    # the assertion to check if all args are float
    # and any one of it in the region
    assert all(isinstance(i,float)for i in args)
    assert lower_range<=any(args)>=upper_range
    # assertion to check if all kwargs are strings and contain 'S' as required
    assert all(isinstance(x,str)for x in kwargs)
    assert len(kwargs) > 1
    assert [y[1] == str('S') for y in kwargs.values()]
    return num


# Question 2
def various_types(lst):
    """

    # First check whether the lst input is the list by an assertion
    # By writing a one-line list comprehension to check the type of element
    # And do the certain changes for them
    # Connect them with 'for' and 'else'

    >>> various_types(['Hello', 4, ['A', 'B', 'C'], True])
    ['olleH', 16, 3, False]
    >>> various_types([])
    []
    >>> various_types([False, 0, 1, [], 'olleH', ('a', 'b')])
    [True, 0, 1, 0, 'Hello', None]
    >>> various_types(['Barry', 'Zhang', ['A', 'B', 'C'], 20])
    ['yrraB', 'gnahZ', 3, 400]
    >>> various_types(['Barry', [1,2,3,4,5,6,7], '20'])
    ['yrraB', 7, '02']
    >>> various_types(['homework is supper difficult'])
    ['tluciffid reppus si krowemoh']
    >>> various_types('homework is supper difficult')
    Traceback (most recent call last):
    AssertionError
    """
    squ_int = 2
    #Assertion checks the input type
    assert type(lst)==list
    # to check whether the element is boolean, if is, change it to opposite
    return [not x if isinstance(x,bool) \
    ## to check whether the element is string, if is, change it to reverse
    else x[::-1] if isinstance(x,str) \
    ## to check whether the element is integer, if is, change it to its square
    else x**squ_int if isinstance(x,int) \
    # to check whether the element is list, if is, count its length
    else len(x) if isinstance(x,list) \
    # if the element is other type, change it to None
    else None for x in lst]


# Question 3
def find_greatest_divisor(lower, upper):
    """

    # First make sure the inputs are integers and upper is larger than lower
    # Using dictionary comprehension as return of the function

    >>> find_greatest_divisor(20, 27)
    {20: 5, 21: 7, 22: 2, 23: 1, 24: 8, 25: 5, 26: 2, 27: 9}
    >>> find_greatest_divisor(1, 10)
    {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 5}
    >>> find_greatest_divisor(11, 19)
    {11: 1, 12: 6, 13: 1, 14: 7, 15: 5, 16: 8, 17: 1, 18: 9, 19: 1}
    >>> find_greatest_divisor(98, 25)
    Traceback (most recent call last):
    AssertionError
    >>> find_greatest_divisor(7,17)
    {7: 7, 8: 8, 9: 9, 10: 5, 11: 1, 12: 6, 13: 1, 14: 7, 15: 5, 16: 8, 17: 1}
    >>> find_greatest_divisor(21,7)
    Traceback (most recent call last):
    AssertionError
    >>> find_greatest_divisor(21,21)
    Traceback (most recent call last):
    AssertionError
    """
    # the variable to avoid magic number meaning the upper region for y
    divisor_int=10
    # Assertion to chek if the input are integer
    assert type(lower)==int and type(upper)==int
    # Assertion to chek if lower smaller than upper integer
    assert lower < upper
    # x represents the key in dic and y is the value
    return {x:y for x in range(lower,upper+1) \
    for y in range(1,divisor_int) if x%y==0}


# Question 4
def best_player(**player_scores):
    """

    # Write a one-line list comprehension including for loop
    # Sorted the final score by soted()
    # derive the key with largest value

    >>> best_player(marina=[9.6, 9, 9.8, 9.9], yuxuan=[9.0, 9.5, 9.9],
    ... elvy=[10.0, 9.8, 10.0, 9.5, 9.6])
    'elvy'
    >>> best_player(sean=[100, 99.99, 100])
    'sean'
    >>> best_player(james=[3.8, 3.5, 3.2], simon=[4.0, 3.6, 3.0])
    'simon'
    >>> best_player(Barry=[9.6, 9.9, 9.8, 9.9,10],
    ... elvy=[10.0, 9.8, 10.0, 9.5, 9.6])
    'Barry'
    >>> best_player(Barry=[9.6, 9.9, 9.8, 9.9,10],
    ... Tommy =[10.0, 9.8, 10.0, 9.6],Amy = [10,8,10,9.7])
    'Tommy'
    >>> best_player(Barry=[8,10,9,9.9],Tommy =[9.9,8,9,10])
    'Tommy'
    """
    # assertion check all values are list
    assert all(map(lambda x: isinstance(x,list), player_scores.values()))
    # assertion check all keys are exactly string
    assert all(map(lambda y: isinstance(y,str), player_scores.keys()))
    # assertion check all elements in list is integers
    assert [type(z) == int for z in player_scores.values()]
    # first sorted and calculate the final score for every one
    return sorted([(sum(sorted(lst)[1:-1])/len(sorted(lst)[1:-1]),key) \
    # derive the key that with highest value
    for key,lst in player_scores.items()])[-1][-1]


# Question 5
def deserialize(outpath, patterns, *serialized_lines):
    """
    # break out the serialized_lines, and append it the new string created

    >>> deserialize("outfiles/out1.txt", ["**", "Marina"],
    ... [1,1,1], [0,5], [3,3,0,3,3])
    >>> with open("outfiles/out1.txt", "r") as outfile1:
    ...     print(outfile1.read().strip())
    **Marina**
    MarinaMarinaMarinaMarinaMarina
    ******MarinaMarinaMarinaMarinaMarinaMarina******

    >>> deserialize("outfiles/out2.txt", ["__", "()", "??"],
    ... [2,4,0,2], [1,2,0,2,2,0,1], [0,2,0,4,2,0], [0,1,0,6,1,0])
    >>> with open("outfiles/out2.txt", "r") as outfile2:
    ...     print(outfile2.read().strip())
    ____()()()()____
    __()()____()()__
    ()()________()()
    ()____________()

    >>> deserialize("outfiles/out3.txt", ["##", "__"],
    ... [2,3,2,2,2,1,2,3,1,1], [1,1,1,1,1,3,1,5,1,1,1,1,1],
    ... [1,1,1,2,1,2,1,4,1,2,1,1,1], [1,1,1,3,1,1,1,3,1,3,1,1,1],
    ... [2,2,2,3,2,1,3,2,1,1])
    >>> with open("outfiles/out3.txt", "r") as outfile3:
    ...     print(outfile3.read().strip())
    ####______####____####__####______##__
    ##__##__##______##__________##__##__##
    ##__##____##____##________##____##__##
    ##__##______##__##______##______##__##
    ####____####______####__######____##__
    """
    # Open the file to write
    f_out = open(outpath,"w")

    # put *serialized_lines to a list
    # Then we can use len to get its length
    tmplist = [*serialized_lines]

    # Go through *serialized_lines
    for l in tmplist:
        tmpindex = 0
        tmpstring = ''
        for ele in l:
            tmpstring += ele * patterns[tmpindex]
            tmpindex += 1
            if tmpindex == len(patterns):
                tmpindex = 0

        # write into the file
        f_out.write(tmpstring + '\n')
    f_out.close()


# Question 6
def sequential_apply(nums, *instructions):
    """

    # Baied on 6 different instructions
    # write code for each of them to make the change

    Examples of all instructions:
    [1, 2, 3, 4], ('add', 1) -> [2, 3, 4, 5]
    [1, 2, 3, 4], ('multiply', 2) -> [2, 4, 6, 8]
    [1, 2, 3, 4], ('insert', 1, 100) -> [1, 100, 2, 3, 4]
    [1, 2, 3, 4], ('remove', 1) -> [1, 3, 4]
    [1, 2, 3, 4], ('mean',) -> [2.5, 2.5, 2.5, 2.5]
    [1, 2, 3, 4], ('range',) -> [3, 3, 3, 3]

    >>> sequential_apply([1, 2, 3, 4], ('add', 1))
    [2, 3, 4, 5]
    >>> sequential_apply([3.3, 6.6, 7.7],
    ... ('insert', 1, 5.5), ('insert', 1, 4.4))
    [3.3, 4.4, 5.5, 6.6, 7.7]
    >>> sequential_apply([9.9, 1.3, 8.2, 4, 10],
    ... ('remove', 0), ('mean',), ('range',), ('add', 10))
    [10.0, 10.0, 10.0, 10.0]
    >>> sequential_apply([9.9, 1.3, 8.2, 4, 10,12,21],
    ... ('remove', 0), ('range',), ('add', 10))
    [29.7, 29.7, 29.7, 29.7, 29.7, 29.7]
    >>> sequential_apply([10,12,21],('remove', 0), ('add', 10))
    [22, 31]
    >>> sequential_apply([1, 2, 3, 4], ('multiply', 12.1))
    [12.1, 24.2, 36.3, 48.4]
    """
    pos_ind = 2
    for i,y in enumerate(instructions):
        # add specific number to each element
        if y[0] =='add':
            nums = [x+y[1] for x in nums]
        # multiply the specific number to each element
        elif y[0] == 'multiply':
            nums = [x*y[1] for x in nums]
        # insert a number to specific position
        elif y[0] == 'insert':
            nums.insert(y[1],y[pos_ind])
        # remove specific element
        elif y[0] == 'remove':
            del nums[y[1]]
        # replace all elements to its avergae
        elif y[0] == 'mean':
            avg = float(sum(nums)/len(nums))
            nums = [avg]*len(nums)
        # replace all elements to its range
        else:
            range = max(nums)-min(nums)
            nums = [range]*len(nums)
    return nums
