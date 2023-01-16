"""
DSC 20 Homework 02 Modified
Name: Zehui Zhang
PID:  A16151490
"""

# Question 1
def convert_to_tuples(courses, instructors):
    """
    The function that convert two list to a tuple, where the first element in
    the first tuple is the first element in the first list, and the second
    element in tuple is the first element in second list, and so on. If the
    elements in second list is not as much as first one, use "STAFF" as element.

    Assumptions:
        len(courses) >= len(instructors).

    >>> convert_to_tuples(['DSC10', 'DSC20', 'DSC30', 'DSC40B',
    ... 'DSC80', 'DSC180A'], ['Justin Eldridge', 'Marina Langlois',
    ... 'Marina Langlois', 'Justin Eldridge', 'Marina Langlois',
    ... 'Aaron Fraenkel'])
    [('DSC10', 'Justin Eldridge'), ('DSC20', 'Marina Langlois'), \
('DSC30', 'Marina Langlois'), ('DSC40B', 'Justin Eldridge'), \
('DSC80', 'Marina Langlois'), ('DSC180A', 'Aaron Fraenkel')]

    >>> convert_to_tuples(['DSC102', 'DSC106', 'DSC100'],
    ... ['Arun Kumar', 'Thomas Powell'])
    [('DSC102', 'Arun Kumar'), ('DSC106', 'Thomas Powell'), \
('DSC100', 'STAFF')]

    >>> convert_to_tuples(['DSC90', 'DSC190'], [])
    [('DSC90', 'STAFF'), ('DSC190', 'STAFF')]

    >>> convert_to_tuples([], [])
    []

    >>> convert_to_tuples(['DSC10', 'DSC20', 'DSC30', 'DSC40A','DSC80'],
    ... ['Justin Eldridge', 'Marina Langlois', 'Marina Langlois'])
    [('DSC10', 'Justin Eldridge'), ('DSC20', 'Marina Langlois'),\
 ('DSC30', 'Marina Langlois'), ('DSC40A', 'STAFF'), ('DSC80', 'STAFF')]

    >>> convert_to_tuples(['DSC102', 'DSC106', 'DSC100'],[])
    [('DSC102', 'STAFF'), ('DSC106', 'STAFF'), ('DSC100', 'STAFF')]
    """
    # creat a empty list storing the tuples created
    result = []
    # By using the for loop to create tuples containing course and instructor
    for i in range(len(courses)):
        # Condition number of courses and instructors are same
        if len(courses) == len(instructors):
            # create tuple containing course and corresponding instructor
            tup = (courses[i], instructors[i])
        # Condition that some instructors are still undetermined
        if len(courses) > len(instructors):
            # append staff if the instructor is not decided
            instructors.append('STAFF')
            tup = (courses[i], instructors[i])
        result.append(tup)
    return result


# Question 2
def convert_to_dict(tuples):
    """
    The function convert tuples into a dictionary where the keys are the second
    elements in the tuple and value is the first element in the tuple. If the
    keys are the same, append value to the same list.

    Assumptions:
        there aren't duplicate instructor names or course codes.

    >>> convert_to_dict([('DSC10', 'Justin Eldridge'),
    ... ('DSC20', 'Marina Langlois'), ('DSC30', 'Marina Langlois'),
    ... ('DSC40B', 'Justin Eldridge'), ('DSC80', 'Marina Langlois'),
    ... ('DSC180A', 'Aaron Fraenkel')])
    {'Justin Eldridge': ['DSC10', 'DSC40B'], \
'Marina Langlois': ['DSC20', 'DSC30', 'DSC80'], 'Aaron Fraenkel': ['DSC180A']}

    >>> convert_to_dict([('DSC102', 'Arun Kumar'),
    ... ('DSC106', 'Thomas Powell'), ('DSC100', 'STAFF')])
    {'Arun Kumar': ['DSC102'], 'Thomas Powell': ['DSC106'], \
'STAFF': ['DSC100']}

    >>> convert_to_dict([('DSC90', 'STAFF'), ('DSC190', 'STAFF')])
    {'STAFF': ['DSC90', 'DSC190']}

    >>> convert_to_dict(())
    {}

    >>> convert_to_dict([('DSC10', 'Justin Eldridge'),
    ... ('DSC20', 'Marina Langlois'), ('DSC30', 'Marina Langlois'),
    ... ('DSC40A', 'STAFF'), ('DSC80', 'STAFF')])
    {'Justin Eldridge': ['DSC10'], 'Marina Langlois': ['DSC20', 'DSC30'], \
'STAFF': ['DSC40A', 'DSC80']}

    >>> convert_to_dict([('DSC102', 'STAFF'), ('DSC106', 'STAFF'),
    ... ('DSC100', 'STAFF')])
    {'STAFF': ['DSC102', 'DSC106', 'DSC100']}
    """
    # sotrage variables
    dic = {}
    course_name = []
    instructor_name = []
    # using the loop to seperate the two items in the tuples
    for i in range(len(tuples)):
        course_name.append(tuples[i][0])
        instructor_name.append(tuples[i][1])
    # using the loop to create a new dictionary that required
    for x in range(len(instructor_name)):
        # Conditoin that the instructor appeared more than one times
        if instructor_name[x] in dic.keys():
            dic[instructor_name[x]].append(course_name[x])
        # Condition that the instructor is first appared
        else:
            dic[instructor_name[x]] = [course_name[x]]
    return dic


# Question 3
def even_old_ops(string):
    """
    A fucntion that reverse all elements at the even indices and change the
    uppercase to lower, change lowercase to upper for all elements at odd
    indices. If the elements at odd indices are not letter, change it to '.'

    >>> even_old_ops("Rand0mStr1NG")
    'NArDSM0Tn.Rg'
    >>> even_old_ops("d_s_c__20")
    '0._.c.s.d'
    >>> even_old_ops("0U1U2l3l4?5?6")
    '6u5u4L3L2.1.0'

    >>> even_old_ops("hse9uvth4w598h")
    '8S5.4VtHuWe.hH'
    >>> even_old_ops("54689tbfbeBUIHMesrg")
    'g.s.MTIFBEbubh9E6R5'
    >>> even_old_ops("")
    ''
    """
    # enpty variables for storing
    even_str = []
    odd_str = []
    even_num = 2
    result = ''
    # using loop the seperate the condition as even one and odd one
    for i,x in enumerate(string):
        # when even indices, append into even_str to prepare for reversing
        if i % even_num == 0:
            even_str.append(x)
        #when odd idices, append into odd_str to prepare for reversing
        if i % even_num != 0:
            odd_str.append(x)
    # reverse all elements in even_str
    even_str = even_str[::-1]
    # seperate odd indices to different conditions
    for m in range(len(odd_str)):
            # If the letter is a lowercase, convert it to uppercase
            if odd_str[m] >= 'a' and odd_str[m] <= 'z':
                odd_str[m] = odd_str[m].upper()
            # # If the letter is a uppercase, convert it to lowercase
            elif odd_str[m] >= 'A' and odd_str[m] <= 'Z':
                odd_str[m] = odd_str[m].lower()
            # Last condition for otherwise
            else:
                odd_str[m] = str('.')
    # steps for join two lit together to fit the requirement
    result = [None] * (len(odd_str)+len(even_str))
    result[::even_num] = even_str
    result[1::even_num] = odd_str
    return ''.join(result)


# Question 4
def context_words(document, target_word, window_size):
    """
    A function that could return all context words around targrt word with range
    window size as tuple

    Assumptions:
        `document` is always a string where words are seperated by spaces.
        `document` string will only have uppercase or lowercase letters,
            hyphens (only in compound words), and spaces.
        `target_word` will always exist in the `document`.

    >>> test_doc = "fifty-two UNITS from lower-division courses " + \
    "AND sixty UNITS from upper-division courses"
    >>> context_words(test_doc, "lower-division", 2)
    [('lower-division', 'units'), ('lower-division', 'from'), \
('lower-division', 'courses'), ('lower-division', 'and')]
    >>> context_words(test_doc, "upper-division", 2)
    [('upper-division', 'units'), ('upper-division', 'from'), \
('upper-division', 'courses')]
    >>> context_words(test_doc, "units", 1)
    [('units', 'fifty-two'), ('units', 'from'), ('units', 'sixty'), \
('units', 'from')]

    >>> my_test_doc = "I am writing this regrade homework on the flight" + \
    "to Dubai from Beijing so as to go back to the US"
    >>> context_words(my_test_doc, 'beijing', 2)
    [('beijing', 'dubai'), ('beijing', 'from'), ('beijing', 'so'), \
('beijing', 'as')]
    >>> context_words(my_test_doc, 'homework', 1)
    [('homework', 'regrade'), ('homework', 'on')]
    >>> context_words(my_test_doc, 'dubai', 1)
    [('dubai', 'flightto'), ('dubai', 'from')]
    """
    #  creat a empty list storing the result
    result = []
    # make sure every elements in documents is lowercase
    doc = document.lower().split(" ")
    # locate the target_word and store them
    for index, item in enumerate(doc):
        if item == target_word:
            lst_num = list(range(index - window_size,index)) + \
                list(range(1+index,window_size+1+index))
            for y in lst_num:
                if len(doc) > y >= 0:
                    result.append((target_word,doc[y]))
    return result

# Question 5
def multiply_matrix(mat_path1, mat_path2):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> multiply_matrix('files/mat1.txt', 'files/mat2.txt')
    >>> with open("files/mat1_multiplied_mat2.txt", "r") as outfile1:
    ...     print(outfile1.read().strip())
    -6 11
    -3 -3

    >>> multiply_matrix('files/mat3.txt', 'files/mat4.txt')
    >>> with open("files/mat3_multiplied_mat4.txt", "r") as outfile2:
    ...     print(outfile2.read().strip())
    5 27 -2 12
    -1 6 0 6

    >>> multiply_matrix('files/mat1.txt', 'files/mat4.txt')
    >>> with open("files/mat1_multiplied_mat4.txt", "r") as outfile3:
    ...     print(outfile3.read().strip())
    Matrices cannot be multiplied
    """
    name_out = mat_path1[:-4]+"_multiplied_"+mat_path2[6:-4]+'.txt'

    file1 = open(mat_path1,'r')
    file2 = open(mat_path2,'r')
    ele1 = []
    ele2 = []
    for line in file1:
        line.replace('\n','')
        line.replace(' ','')
        for i in line:
            temp = []
            temp.append(i)
            ele1.append(temp)

    for line in file2:
        line.replace('\n','')
        line.replace(' ','')
        for j in range(len(line)):
            temp = []
            for i in line:
                temp.append(i[j])
            ele2.append(temp)

    result = []
    for i in len(ele1):
        compute = list(zip(ele1,ele2))
        sum = 0
        for x in computed:
            mul = x[0] * x[1]
            sum += mul
        result[i] = sum

    output = ''
    for i in result:
        output += str(i) + ' '


    file1.close()
    file2.close()


    f_out = open(name_out, 'w')
    f_out.write(output)
    f_out.close()
    return



# Question 6.1
def parse_stocklist(stocklist_path):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> parse_stocklist('files/stocklist_1.txt')
    {'Newegg': {'RTX 3070': -40, 'RTX 3080': 25}, 'Amazon': {'PS5': 0}, \
'Best Buy': {'Xbox Series X': 50}, \
'Walmart': {'Ryzen 5600X': 10, 'Ryzen Threadripper': 20}}

    >>> parse_stocklist('files/stocklist_oversold.txt')
    {'B&H': {'G Pro Wireless': -5}, 'Amazon': {'Samsung TV': 0}}

    >>> parse_stocklist('files/empty.txt')
    {}
    """
    with open(stocklist_path, "r") as f:
        for line in f:
            splitted = line.split(',')
            

# Question 6.2
def find_best(data, find_product):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> data1 = parse_stocklist('files/stocklist_1.txt')
    >>> find_best(data1, True)
    {'RTX 3070': 'Newegg', 'RTX 3080': 'Newegg', 'PS5': 'Amazon', \
'Xbox Series X': 'Best Buy', 'Ryzen 5600X': 'Walmart', \
'Ryzen Threadripper': 'Walmart'}
    >>> find_best(data1, False)
    {'Newegg': 'RTX 3080', 'Amazon': 'PS5', 'Best Buy': 'Xbox Series X', \
'Walmart': 'Ryzen Threadripper'}

    >>> data2 = parse_stocklist('files/stocklist_oversold.txt')
    >>> find_best(data2, True)
    {'G Pro Wireless': 'B&H', 'Samsung TV': 'Amazon'}
    >>> find_best(data2, False)
    {'B&H': 'G Pro Wireless', 'Amazon': 'Samsung TV'}

    >>> data3 = parse_stocklist('files/empty.txt')
    >>> find_best(data3, True)
    {}
    >>> find_best(data3, False)
    {}
    """
    # YOUR CODE GOES HERE #
    return ...
