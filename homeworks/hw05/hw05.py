"""
DSC 20 Homework 05
Name: Zehui Zhang
PID:  A16151490
"""

# Question 1
def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function.
    Do not add new doctests for this function.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    return [False, False, True, False, True, False, False, False, False, False]


# Question 2
def complexity_mc():
    """
    Write your answers to time complexity multiple-choice questions in this
    function.
    Do not add new doctests for this function.

    >>> answers = complexity_mc()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, int) and 1 <= ans <= 7 for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS #
    return [3,5,3,2,7,6,5,4,6,6]


# Question 3
def advanced_search(data, min_elem, max_elem, min_total, max_total):
    """
    # Create a filter function which could filter out all unqualified data
    # then store all qualified data into a new dictionary
    # return keys of new dictionary as a list
    >>> data = {"Marina": [10, 9.2, 11.4, 17.5, 13.8], \
        "Elvy": [3.2, 8.6, 9.1, 1.0, 2.3, 6.6], \
        "Yuxuan": [14.41, 12.21, 10.01, 13, 11.1], \
        "Simon": [84.82, 91.96, 31.32], \
        "Sean": [66.0112, 88.8888, 45.6789], \
        "Colin": [44.1214, 55.5663, 77], \
        "Jerry": [10, 20, 30, 80]}
    >>> advanced_search(data, 10, 20, 0, 300)
    ['Yuxuan']
    >>> advanced_search(data, 40, 100, 150.5, 279.9)
    ['Sean', 'Colin']
    >>> advanced_search(data, 10, 80, 130, 150)
    ['Jerry']
    >>> advanced_search(data, 5, 25, 30, 150)
    ['Marina', 'Yuxuan']
    >>> advanced_search(data, 0, 50, 30, 150)
    ['Marina', 'Elvy', 'Yuxuan']
    >>> advanced_search(data, 20, 30, 12, 250)
    []
    """
    # filter function which rid of all unqualified data from original dic
    filter_func = lambda x: min_elem<=min(x[1])<=max(x[1])<=max_elem \
    and min_total<=sum(x[1])<=max_total
    # new dic that store all qualified data
    dic = dict(filter(filter_func,data.items()))
    # return keys as a list
    return list(dic.keys())


# Question 4
def best_curve_function(scores, funcs):
    """
    # First write a function which could apply to all socres and then use filter
    # to find out the right function among funcs.Apply those to scores and
    # return curved socres

    >>> best1 = best_curve_function([80.0, 90.0, 100.0], \
        [lambda score: score + 4.55, lambda score: score * 1.05, 105.0])
    >>> best1(100.0)
    104.55
    >>> best2 = best_curve_function([80.0, 90.0, 100.0], \
        [lambda score: score + 100, lambda score: score * 0.95, 103.5])
    >>> best2(95.5)
    95.5
    >>> best3 = best_curve_function([80.0, 90.0, 100.0], \
        [100.0, 103.5, False])
    >>> best3(91.0)
    91.0
    >>> best4 = best_curve_function([77.0, 99.0, 88.0], \
        [lambda score: score + 4.50, lambda score: score * 1.03, 103.0])
    >>> best4(100.0)
    104.5
    >>> best5 = best_curve_function([80.0, 90.0, 100.0], \
        [lambda score: score + 180, lambda score: score * 3.1, 103.5])
    >>> best5(90.0)
    90.0
    >>> best6 = best_curve_function([80.0, 90.0, 100.0], \
        [lambda score: score + 3.21, lambda score: score * 1.1, 104])
    >>> best6(90.0)
    93.21
    """
    # magic numbers
    max_num = 100
    max_cur = 5
    # Assertions which make sure all inputs are in right form
    assert len(scores) != 0
    assert all([isinstance(i, float) and 0<=i<=max_num for i in scores])
    # filter out all disqualified functions
    func1 = lambda func: all([callable(func) \
    and 0<=func(i)-i<max_cur for i in scores])
    satisfied = list(filter(func1,funcs))
    # If no function is qualified, return original one
    if len(satisfied) == 0:
        return lambda a:a
    # sort tuples created
    lst = [(f(score),f)for f in satisfied for score in scores]
    lst.sort()
    return lst[-1][-1]



# Question 5 (Extra Credit)
def unique_data_generator(path):
    """
    # Open the file and then split all lines
    # Create a key list to store keys, if key repeated, skip it
    # store values in tuple and return key with value tuple as tuple
    >>> gen1 = unique_data_generator("infiles/data1.txt")
    >>> [next(gen1, None) for _ in range(3)]
    [('key1', ('val1', 'val2', 'val3')), ('key2', ('val1', 'val2')), \
('key3', ('val1', 'val2', 'val3', 'val4'))]
    >>> [next(gen1, None) for _ in range(5)]
    [('key4', ('val4', 'val5', 'val6')), \
('key5', ('val3', 'val4', 'val5', 'val6', 'val7')), None, None, None]
    >>> gen2 = unique_data_generator("infiles/data2.txt")
    >>> [next(gen2, None) for _ in range(5)]
    [('Colin', ('10-08-2020', '120')), ('James', ('10-08-2020', '100')), \
('Simon', ('10-09-2020', '115')), ('Jerry', ('10-09-2020', '120')), \
('Sean', ('10-10-2020', '150'))]
    """
    # open the file
    with open(path,'r') as f:
        key_lst = []
        for l in f:
            # omit all new lines and split them
            l=l.rstrip('\n')
            l=l.split(',')
            key = l[0]
        # if key repeated, skip it
        if key in key_lst:
            continue
        key_lst.append(key)
        # convert to tuple
        tup_lst = [x for x in l[1:]]
        # yield every tuple
        tuple=(key,tuple(tup_lst))
        yield tuple
