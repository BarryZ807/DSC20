"""
DSC 20 Homework 02
Name: Zehui Zhang
PID:  A16151490
"""

# Question 1
def convert_to_tuples(courses, instructors):
    """
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

    >>> convert_to_tuples(['DSC90','DSC190'], [])
    [('DSC90','STAFF'), ('DSC190','STAFF')]

    >>> convert_to_tuples(['DSC10', 'DSC20', 'DSC30', 'DSC40B'],
    ... ['Justin Eldridge', 'Marina Langlois',
    ... 'Marina Langlois'])
    [('DSC10', 'Justin Eldridge'), ('DSC20', 'Marina Langlois'), \
('DSC30', 'Marina Langlois'), ('DSC40B','STAFF')

    >>> convert_to_tuples(['DSC102', 'DSC106'],
    ... ['Arun Kumar', 'Thomas Powell'])
    [('DSC102','Arun Kumar'), ('DSC106','Thomas Powell')]

    >>> convert_to_tuples(['DSC10','DSC20', 'DSC30','DSC40B'], [])
    [('DSC10','STAFF'), ('DSC20','STAFF'), ('DSC30','STAFF'), \
('DSC40B','STAFF')]
    """
    # creat a empty list storing the result
    result = []
    # create a loop to determine the max number of terms in the tuple
    for i in range(max(len(courses),len(instructors))):
        # Condition number of courses and instructors are same
        if len(courses) == len(instructors):
            tup = (courses[i], instructors[i])
        # Condition that some instructors are still undetermined
        if len(courses) > len(instructors):
            instructors.append('STAFF')
            tup = (courses[i], instructors[i])
        result.append(tup)
    return result


# Question 2
def convert_to_dict(tuples):
    """
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

    >>> convert_to_dict([('DSC90','STAFF'), ('DSC190','STAFF')])
    {'STAFF':['DSC90', 'DSC190']}

    >>> convert_to_dict([('DSC90', 'STAFF'), ('DSC190', 'STAFF'),
    ... ('DSC80','STAFF')])
    {'STAFF':['DSC90', 'DSC190','DSC80']}

    >>> convert_to_dict([('DSC102', 'Arun Kumar'),
    ... ('DSC106', 'Thomas Powell')])
    {'Arun Kumar':['DSC102'], 'Thomas Powell':['DSC106']}

    >>> convert_to_dict([('DSC10', 'Justin Eldridge'),
    ... ('DSC20', 'Marina Langlois'), ('DSC30', 'Marina Langlois'),
    ... ('DSC40B', 'Justin Eldridge'),('DSC180A', 'Aaron Fraenkel')])
    {'Justin Eldridge': ['DSC10', 'DSC40B'], \
'Marina Langlois':['DSC20', 'DSC30'], 'Aaron Fraenkel':['DSC180A']}
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
    >>> even_old_ops("Rand0mStr1NG")
    'NArDSM0Tn.Rg'
    >>> even_old_ops("d_s_c__20")
    '0._.c.s.d'
    >>> even_old_ops("0U1U2l3l4?5?6")
    '6u5u4L3L2.1.0'
    >>> even_old_ops('DAFsydvad133')
    '3adSvDyAF.D.'
    >>> even_old_ops('werhweh3238b.er')
    'rE.H8E2.h.wBrEw'
    >>> even_old_ops('wqr372hhwnvew./')
    '/Qw.v.wHhN7Er.w'
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
    >>> context_words(test_doc, "from", 2)
    [('from', 'fifty-two'),('from', 'units'),('from', 'lower-division'), \
('from', 'courses'),('from', 'sixty'),('from', 'units'), \
('from', 'upper-division'),('from', 'courses')]
     >>> context_words(test_doc, "courses", 3)
     [('courses', 'units'),('courses', 'from'),('courses', 'lower-division'), \
('courses', 'and'),('courses', 'sixty'),('courses', 'units'), \
('courses', 'units'),('courses', 'from'),('courses', 'upper-division')]
     >>> context_words(test_doc, "sixty", 1)
     [('sixty', 'and'), ('sixty', 'units')]
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
def flip_matrix(matrix_path):
    """
    Assumptions:
        The matrix will be represented as lines of space-seperated integers.
        The matrix will be N x M, where N and M >= 1.

    >>> flip_matrix("testfiles/matrix1.txt")
    >>> with open("testfiles/matrix1_flipped.txt", "r") as outfile1:
    ...     print(outfile1.read().strip())
    1   0   1   0   0
    0   1   0   1   0
    1   0   1   0   1
    0   1   0   1   0
    0   0   1   0   1
    >>> flip_matrix("testfiles/matrix2.txt")
    >>> with open("testfiles/matrix2_flipped.txt", "r") as outfile2:
    ...     print(outfile2.read().strip())
    7   6   5   4   3
    6   5   4   3   2
    5   4   3   2   1
    >>> flip_matrix("testfiles/matrix3.txt")
    >>> with open("testfiles/matrix3_flipped.txt", "r") as outfile3:
    ...     print(outfile3.read().strip())
    1 8   1 5 0 0 1   9 9
    7 1   1 3   2 4
    1   0 7 7   0 9
    2   1   8 8
    6 9   1 5   2 5
    0 9   2 1   5 0 1
    >>> flip_matrix("testfiles/matrix4.txt")
    >>> with open("testfiles/matrix4_flipped.txt", "r") as outfile4:
    ...     print(outfile4.read().strip())
    7   5 6   4 5   3 4   2 3
    1 6   1 5   1 4   1 3   1 2
    0 2   9 1   8 1   7 1   6 1
    5 1   4 1   3 1   2 1   1 1
    >>> flip_matrix("testfiles/matrix5.txt")
    >>> with open("testfiles/matrix5_flipped.txt", "r") as outfile5:
    ...     print(outfile5.read().strip())
    8   5   3   3
      2   6   5   3   3
    5   4   3   2   1
    >>> flip_matrix("testfiles/matrix6.txt")
    >>> with open("testfiles/matrix6_flipped.txt", "r") as outfile6:
    ...     print(outfile6.read().strip())
    3   5   9   8   7
      2   3   5   3   6   3
    """
    og_file = open(matrix_path,'r')
    new_file = open(matrix_path.replace('.txt','_flipped.txt'),'w')
    og_mat = og_file.readlines()
    og_mat = [og_mat[i][:-1] for i in range(len(og_mat))]
    og_line = [line.split(' ') for line in og_mat]
    og_file.close()
    new_mat = []
    for line in og_mat:
        new_line = line[::-1]
        new_line = ' '.join(new_line)
        new_mat.append(new_line)
    new_mat = '\n'.join(new_mat[::-1])
    new_file.write(new_mat)
    new_file.close()
    return


# Question 6.1
def parse_timelog(timelog_path):
    """
    Assumptions:
        The log will be sorted in chronological order.
        Each line of the time log will have name (str), date (str,
            MM-DD-YYYY), and minutes seperated by comma (",").
            For example: "Marina,09-30-2020,300".
        Each person will have only one entry per day.

    >>> parse_timelog("testfiles/timelog1.txt")
    {'Marina': [('09-30-2020', 300), ('10-01-2020', 300)], \
'Elvy': [('09-30-2020', 120), ('10-01-2020', 215)], \
'Yuxuan': [('09-30-2020', 185), ('10-01-2020', 90)]}
    >>> parse_timelog("testfiles/timelog2.txt")
    {'Colin': [('10-08-2020', 120), ('10-09-2020', 10), ('10-10-2020', 90), \
('10-11-2020', 30)], 'James': [('10-08-2020', 100), ('10-09-2020', 85)], \
'Simon': [('10-09-2020', 115)], 'Jerry': [('10-09-2020', 120)], \
'Sean': [('10-10-2020', 150)]}
    >>> parse_timelog("testfiles/timelog3.txt")
    {'Marina': [('09-12-2020', 122), ('10-01-2020', 310)], \
'Elvy': [('09-12-2020', 122), ('10-02-2020', 290)], \
'Yuxuan': [('09-12-2020', 200), ('10-03-2020', 200)]}
    >>> parse_timelog("testfiles/timelog4.txt")
    {'Barry': [('09-29-2020', 332)], 'Elvy': [('09-30-2020', 120), \
('10-01-2020', 212)], 'Tom': [('09-30-2020', 185)], \
'Yuxuan': [('10-01-2020', 201)], 'Marina': [('10-01-2020', 321)]}
    >>> parse_timelog("testfiles/timelog5.txt")
    {'Marina': [('09-30-2020', 320), ('10-01-2020', 217)], \
    'Elvy': [('09-30-2020', 210), ('10-01-2020', 221)], \
    'Yuxuan': [('09-30-2020', 212)], 'Barry': [('10-01-2020', 129)]}
    """
    dic = {}
    even_index = 2
    file = open(timelog_path,'r')
    for line in file:
        line = line.strip().split(',')
        item_1 = str(line[1])
        item_2 = int(line[even_index])
        if str(line[0]) not in dic.keys():
            dic[str(line[0])] = [(item_1,item_2)]
        else:
            dic[str(line[0])] = dic[str(line[0])]+[(item_1,item_2)]
    return dic


# Question 6.2
def extract_extreme_time(data, is_max):
    """
    Assumptions:
        When any comparison results a tie, keep the entry with earlier date.

    >>> data1 = parse_timelog("testfiles/timelog1.txt")
    >>> extract_extreme_time(data1, True)
    {'Marina': ('09-30-2020', 300), 'Elvy': ('10-01-2020', 215), \
'Yuxuan': ('09-30-2020', 185)}
    >>> extract_extreme_time(data1, False)
    {'Marina': ('09-30-2020', 300), 'Elvy': ('09-30-2020', 120), \
'Yuxuan': ('10-01-2020', 90)}
    >>> data2 = parse_timelog("testfiles/timelog2.txt")
    >>> extract_extreme_time(data2, True)
    {'Colin': ('10-08-2020', 120), 'James': ('10-08-2020', 100), \
'Simon': ('10-09-2020', 115), 'Jerry': ('10-09-2020', 120), \
'Sean': ('10-10-2020', 150)}
    >>> extract_extreme_time(data2, False)
    {'Colin': ('10-09-2020', 10), 'James': ('10-09-2020', 85), \
'Simon': ('10-09-2020', 115), 'Jerry': ('10-09-2020', 120), \
'Sean': ('10-10-2020', 150)}
    >>> data3 = parse_timelog("testfiles/timelog3.txt")
    >>> extract_extreme_time(data3, True)
    {'Marina': ('10-01-2020', 310), 'Elvy': ('10-02-2020', 290), \
'Yuxuan': ('09-12-2020', 200)}
    >>> extract_extreme_time(data3, False)
    {'Marina': ('09-12-2020', 122), 'Elvy': ('09-12-2020', 122), \
'Yuxuan': ('09-12-2020', 200)}
    >>> data4 = parse_timelog("testfiles/timelog4.txt")
    >>> extract_extreme_time(data4, True)
    {'Barry': ('09-29-2020', 332), 'Elvy': ('10-01-2020', 212), \
'Tom': ('09-30-2020', 185), 'Yuxuan': ('10-01-2020', 201), \
'Marina': ('10-01-2020', 321)}
    >>> extract_extreme_time(data4, False)
    {'Barry': ('09-29-2020', 332), 'Elvy': ('09-30-2020', 120), \
'Tom': ('09-30-2020', 185), 'Yuxuan': ('10-01-2020', 201), \
'Marina': ('10-01-2020', 321)}
    >>> data5 = parse_timelog("testfiles/timelog5.txt")
    >>> extract_extreme_time(data5, True)
    {'Marina': ('09-30-2020', 320), 'Elvy': ('10-01-2020', 221), \
'Yuxuan': ('09-30-2020', 212), 'Barry': ('10-01-2020', 129)}
    >>> extract_extreme_time(data5, False)
    {'Marina': ('10-01-2020', 217), 'Elvy': ('09-30-2020', 210), \
'Yuxuan': ('09-30-2020', 212), 'Barry': ('10-01-2020', 129)}
    """
    dic = {}
    if is_max:
        for x in data.keys():
            max = -float('inf')
            for ent in data[x]:
                if ent[1] > max:
                    max =ent[1]
                    max_tup = ent
            dic[x] = max_tup
        return dic
    else:
        for y in data.keys():
            min = float('inf')
            for ent in data[y]:
                if ent[1] < min:
                    min =ent[1]
                    min_tup = ent
            dic[y] = min_tup
        return dic
