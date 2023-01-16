"""
DSC 20 Homework 04
Name: Zehui Zhang
PID:  A16151490
"""


# Utility Function
def is_iterable(obj):
    """
    A function that checks if `obj` is a iterable (can be iterated over
    in a for-loop).

    DO NOT MODIFY THIS FUNCTION. You don't need to add new doctests
    for this function.

    >>> is_iterable(1)
    False
    >>> is_iterable("DSC 20")
    True
    >>> is_iterable(["Fall", 2020])
    True
    """
    try:
        iter(obj)
        return True
    except TypeError:
        return False


# Question 1
def ucsd_spam_quarantine(emails, allowlist, blocklist):
    """
    # First define a function which it to check the end of emails
    # Then find the malicious emails
    # Remove all of them from the elails

    >>> emails = ["mlanglois@ucsd.edu", "istudents@ucsd.edu", \
    "jsmith@eng.ucsd.edu", "hello@gmail.com", "python@yahoo.com", \
    "phish@ucsd.edu"]
    >>> allowlist = ["hello@gmail.com"]
    >>> blocklist = ["phish@ucsd.edu"]
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['mlanglois@ucsd.edu', 'istudents@ucsd.edu', \
'jsmith@eng.ucsd.edu', 'hello@gmail.com']

    >>> emails = ["sean@ucsd.edu", "jojo@ucsd.edu", "dsc@ucsd.edu.us", \
    "tritons@outlook.com", "spam@ucsd.edu", "bad@ucsd.edu"]
    >>> allowlist = ["tritons@outlook.com", "no-reply@piazza.com"]
    >>> blocklist = ["spam@ucsd.edu", "bad@ucsd.edu", "phish@ucsd.edu"]
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['sean@ucsd.edu', 'jojo@ucsd.edu', 'tritons@outlook.com']

    >>> emails = ["barry@ucsd.edu", "zhang@ucsd.edu.us", "tritons@outlook.com", \
    "bad@ucsd.edu"]
    >>> allowlist = ["zhang@ucsd.edu.us"]
    >>> blocklist = ["bad@ucsd.edu"]
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['barry@ucsd.edu', 'zhang@ucsd.edu.us']

    >>> emails = ["barry@ucsd.edu", "zhang@ucsd.edu.us", "tritons@outlook.com", \
    "bad@ucsd.edu","Barryzhang@gmail.com"]
    >>> allowlist = ["zhang@ucsd.edu.us"]
    >>> blocklist = ["Barryzhang@gmail.com"]
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['barry@ucsd.edu', 'zhang@ucsd.edu.us', 'bad@ucsd.edu']

    >>> emails = ["zhang@ucsd.edu", "tritons@outlook.com", "bad@ucsd.edu"]
    >>> allowlist = ["zhang@ucsd.edu.us"]
    >>> blocklist = []
    >>> ucsd_spam_quarantine(emails, allowlist, blocklist)
    ['zhang@ucsd.edu', 'bad@ucsd.edu']
    """
    # Assertion to check all type of inputs
    assert type(emails)==list
    assert type(allowlist)==list
    assert type(blocklist)==list

    # function to check the end of every email
    def func(z):
        if z.endswith('ucsd.edu') != True:
            return z
    # to find out the malicious_email
    email = list(filter(lambda y: y not in allowlist,emails))
    email1 = list(filter(lambda x:x in blocklist,email))
    email2 = list(filter(func, email))
    malicious_email = email1+email2
    #remove all malicious_email from all emails
    result = list(filter(lambda m: m not in malicious_email,emails))
    return result



# Question 2
def create_dsc_email(students, years):
    """
    # First create the dic to store the college name, and then using functions
    # to narrow the range and change the data step by step
    >>> students = [ \
        ("First Middle Last", 2022, "revelle", "DS25"), \
        ("hi HELLO", 2022, "seventh", "DS25"), \
        ("Computer Science", 2021, "Warren", "CS25"), \
        ("longfirstname longlastname", 1990, "Marshall", "DS25") \
    ]
    >>> create_dsc_email(students, [2022])
    {'First Middle Last': 'firlast22rc@dsc.ucsd.edu', \
'hi HELLO': 'hihello22sv@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [1990, 2021])
    {'longfirstname longlastname': 'lonlongla90tm@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [])
    {}
    >>> create_dsc_email(students, [2021])
    {}
    >>> create_dsc_email(students, [1990])
    {'longfirstname longlastname': 'lonlongla90tm@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [2010])
    {}
    >>> students = [ \
        ("Math econ", 2022, "muir", "DS25"), \
        ("hi HELLO", 2022, "seventh", "DS25"), \
        ("Computer Science", 2000, "Warren", "CS25"), \
        ("Barry Zhang", 1990, "Marshall", "DS25") \
    ]
    >>> create_dsc_email(students, [2022])
    {'Math econ': 'matecon22mc@dsc.ucsd.edu', \
'hi HELLO': 'hihello22sv@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [1990])
    {'Barry Zhang': 'barzhang90tm@dsc.ucsd.edu'}
    >>> create_dsc_email(students, [1990,2022])
    {'Math econ': 'matecon22mc@dsc.ucsd.edu', \
'hi HELLO': 'hihello22sv@dsc.ucsd.edu', \
'Barry Zhang': 'barzhang90tm@dsc.ucsd.edu'}
    """
    mag1 = 3
    mag2 = 6
    mag3 = 2
    mag4 = 4
    # create a dic to store all college names
    college = {'muir':'mc','revelle':'rc','warren':'wc','roosevelt':'er', \
    'sixth':'sx','marshall':'tm','seventh':'sv'}
    # function that select data science students
    stu_dsc_func = lambda x : x[mag1] == 'DS25'
    #function that select the correct year
    year_func = lambda m : (m[1]in years)
    # name functions that change the name to required form
    fname_func = lambda y: y[0].split()[0][0:mag1] if len(y[0].split()[0]) \
    >mag1 else y[0].split()[0]
    lname_func = lambda z: z[0].split()[-1][0:mag2] if len(z[0].split()[-1]) \
    >mag2 else z[0].split()[-1]
    #function that collect all info together
    final_func = lambda o,p,q:(p.lower()+q.lower()+str(o[1])[mag3:mag4]+ \
    college.get(o[mag3].lower())+str('@dsc.ucsd.edu'))
    # list that all data science studnets
    stu_dsc = list(filter(stu_dsc_func,students))
    # list that all correct years
    year = list(filter(year_func,stu_dsc))
    # lists of all first name and last name
    fname = list(map(fname_func,year))
    lname = list(map(lname_func,year))
    # list that contains all required info of a student
    final = list(map(final_func,year,fname,lname))
    #convert ti to dictionary
    dic = dict(zip(list((map(lambda a:a[0],year))),final))
    return dic



# Question 3
def base_converter(target_base):
    """
    # Using the infinit whilt loop to help to create the inner function
    # which is to convert non-negative integers to target base as a string

    >>> binary_converter = base_converter(2)
    >>> [binary_converter(i) for i in range(10)]
    ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']
    >>> base_converter(16)(8200)
    '2008'
    >>> base_converter(36)(8200)
    '6BS'
    >>> base_converter(16)(820)
    '334'
    >>> base_converter(5)(820)
    '11240'
    >>> base_converter(26)(5567)
    '863'
    """
    assert callable(base_converter)
    assert type(target_base) == int
    assert 2<= target_base
    assert target_base <= 36
    # a string that contains all possible digits
    digit='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # def a inner function to find the remainders and store
    def inner(num):
        assert num>=0
        lst=[]
        str = ''
        while True:
            if num >= target_base:
                lst.append(num%target_base)
                num//=target_base
            else:
                lst.append(num%target_base)
                num//=target_base
                break
        lst=lst[::-1]
        # to find the corresponging digits
        for x in lst:
            str+=digit[x]
        return str
    return inner



# Question 4
def magic_sequence_generator(start0, start1, start2):
    """
    # Yield first three integers and then start the infinit loop
    # For the rest of term, substitude three terms before the ith term
    # yield abs(start0+start1-start2)

    >>> gen = magic_sequence_generator(10, 20, 30)
    >>> [next(gen) for _ in range(3)]
    [10, 20, 30]
    >>> next(gen)
    0
    >>> [next(gen) for _ in range(10)]
    [50, 20, 30, 40, 10, 60, 10, 60, 10, 60]
    >>> [next(gen) for _ in range(2)]
    [10, 60]
    >>> next(gen)
    10
    >>> [next(gen) for _ in range(8)]
    [60, 10, 60, 10, 60, 10, 60, 10]
    """
    # Assertion to check all types of inputs
    assert type(start0) == int
    assert type(start1) == int
    assert type(start2) == int
    # Yield first three integers
    yield start0
    yield start1
    yield start2
    # Start the infinit loop
    while True:
        # yield the later intefers
        Si = abs(start0+start1-start2)
        yield Si
        # substitude former integers
        start0=start1
        start1=start2
        start2=Si


# Question 5
def round_robin_generator(k, arg1, arg2, arg3):
    """
    # Put all three args into a list and then use loops one by one
    # to yield args in required order

    >>> arg1 = "abcdefgh"
    >>> arg2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> arg3 = (True, False, True, False, True, False)
    >>> gen = round_robin_generator(2, arg1, arg2, arg3)
    >>> [next(gen, None) for _ in range(14)]
    ['a', 'b', 1, 2, True, False, 'c', 'd', 3, 4, True, False, 'e', 'f']

    >>> gen = round_robin_generator(3, arg1, arg2, arg3)
    >>> [next(gen, None) for _ in range(14)]
    ['a', 'b', 'c', 1, 2, 3, True, False, True, 'd', 'e', 'f', 4, 5]

    >>> arg4 = "dsc"
    >>> arg5 = [2, 0]
    >>> arg6 = "fall"
    >>> gen = round_robin_generator(4, arg4, arg5, arg6)
    >>> [next(gen, None) for _ in range(10)]
    ['d', 's', 'c', None, 2, 0, None, None, 'f', 'a']

    >>> arg7 = 'fwefw'
    >>> arg8 = [4,2,3,21]
    >>> arg9 = 'Barry'
    >>> gen = round_robin_generator(2, arg7, arg8, arg9)
    >>> [next(gen, None) for _ in range(10)]
    ['f', 'w', 4, 2, 'B', 'a', 'e', 'f', 3, 21]

    >>> gen = round_robin_generator(3, arg7, arg8, arg9)
    >>> [next(gen, None) for _ in range(4)]
    ['f', 'w', 'e', 4]

    >>> gen = round_robin_generator(5, arg7, arg8, arg9)
    >>> [next(gen, None) for _ in range(12)]
    ['f', 'w', 'e', 'f', 'w', 4, 2, 3, 21, None, 'B', 'a']

    >>> arg10 = 'asdafwefwqfqwf'
    >>> arg11 = [4,2,3,True,False,'asdwe']
    >>> arg12 = 'Barry'
    >>> gen = round_robin_generator(5, arg10, arg11, arg12)
    >>> [next(gen, None) for _ in range(12)]
    ['a', 's', 'd', 'a', 'f', 4, 2, 3, True, False, 'B', 'a']

    >>> gen = round_robin_generator(3, arg10, arg11, arg12)
    >>> [next(gen, None) for _ in range(8)]
    ['a', 's', 'd', 4, 2, 3, 'B', 'a']

    >>> gen = round_robin_generator(7, arg10, arg11, arg12)
    >>> [next(gen, None) for _ in range(8)]
    ['a', 's', 'd', 'a', 'f', 'w', 'e', 4]

    >>> arg13 = ['wefr',True,False]
    >>> arg14 = [4,2,3,True,False,3,21,2,4,4,5]
    >>> arg15 = 'asdadwqfqwegfwrg'
    >>> gen = round_robin_generator(7, arg13, arg14, arg15)
    >>> [next(gen, None) for _ in range(8)]
    ['wefr', True, False, None, None, None, None, 4]

    >>> gen = round_robin_generator(8, arg13, arg14, arg15)
    >>> [next(gen, None) for _ in range(2)]
    ['wefr', True]

    >>> gen = round_robin_generator(8, arg13, arg14, arg15)
    >>> [next(gen, None) for _ in range(12)]
    ['wefr', True, False, None, None, None, None, None, 4, 2, 3, True]
    """
    # list of three arguments
    input = [iter(arg1),iter(arg2),iter(arg3)]
    # first loop to start infinit loop
    while True:
        # second loop to get into inputs
        for i in range(len(input)):
            # third loop to find certain part of a certain argument
            for j in range(k):
                yield next(input[i],None)



# Question 6
def make_generator(*args):
    """
    # based on the 3 different conditions, write 3 different parts of CODE
    # to satisfy all requirements

    >>> gen1 = make_generator(10, 20, 30)
    >>> [next(gen1, None) for _ in range(10)]
    [10, 20, 30, 0, 50, 20, 30, 40, 10, 60]
    >>> gen2 = make_generator([10, 20], "Sean", [True, False])
    >>> [next(gen2, None) for _ in range(10)]
    [10, 20, 'S', 'e', True, False, None, None, 'a', 'n']
    >>> gen3 = make_generator("Ev", 0, ["en"], ("DD",))
    >>> [next(gen3, None) for _ in range(10)]
    ['Ev', ['en'], 0, ('DD',), None, None, None, None, None, None]
    >>> gen4 = make_generator([10], "Sean", [True, False],'Barry')
    >>> [next(gen4, None) for _ in range(10)]
    [[10], [True, False], 'Sean', 'Barry', None, None, None, None, None, None]
    >>> gen5 = make_generator([10], [12,2,3,4,5,])
    >>> [next(gen5, None) for _ in range(10)]
    [[10], [12, 2, 3, 4, 5], None, None, None, None, None, None, None, None]
    >>> gen6 = make_generator(21,22,34)
    >>> [next(gen6, None) for _ in range(10)]
    [21, 22, 34, 9, 47, 4, 52, 1, 55, 2]
    """
    # magic numbers
    num_input = 3
    count_1 = 0
    count_2 = 0
    k = 2
    # empty list to store index
    odd_lst = []
    even_lst = []
    even_num = 2
    # seperate the args into 2 conditions
    if len(args) == num_input:
        for arg in args:
        # all args are non-negative integers
            if type(arg)==int and arg>=0:
                count_1 += 1
        # all args are iterable
            elif is_iterable(arg) == True:
                count_2 += 1
        if count_1 == num_input:
            yield from magic_sequence_generator(*args)
        if count_2 == num_input:
            yield from  round_robin_generator(k,*args)
    # Last condition that we should yield by even or odd
    else:
        for m in range(len(args)):
            # store all even index to a list
            if m%even_num==0:
                even_lst.append(m)
            # store all odd index to a list
            else:
                odd_lst.append(m)
        # yield all arguments at even indices
        for i in even_lst:
            yield args[i]
        # yield all arguments at odd indices
        for j in odd_lst:
            yield args[j]


# Question 7
def skip_increasing(iterable, k):
    """
    # By using for loop in to append every result to the final list and
    # every single step, we should add 1 to the skip_step,
    # finally end the loop when k is equal to 0 to reach the max volumn

    >>> skip_increasing(iter([1,2,3,4,5,6,7,8,9,10,11]), 5)
    [1, 2, 4, 7, 11]
    >>> skip_increasing(iter('ABcDefGhijKlmnoPqrs'), 10)
    ['A', 'B', 'D', 'G', 'K', 'P']
    >>> skip_increasing(iter((1, None, 3, 4, 5, 6, 7, 8)), 3)
    [1, None, 4]
    >>> skip_increasing(iter('sfqfbuUIHuibefubwqiub'), 5)
    ['s', 'f', 'f', 'U', 'i']
    >>> skip_increasing(iter([21,2,4,2,1,122,4]), 5)
    [21, 2, 2, 4]
    >>> skip_increasing(iter('ABCDessfeadefwe'), 3)
    ['A', 'B', 'D']
    """
    # create a empty list to store values in
    result = []
    # number of steps to skip
    skip_step = 0
    # loop and store in the list
    for i in range(k):
        try:
            result.append(next(iterable))
            # increase the skip_step every time
            for _ in range(skip_step):
                next(iterable)
            skip_step += 1
            k -= 1
        # stop the loop when k=0 reaching the max size of the list
        except:
            k=0
    return result
