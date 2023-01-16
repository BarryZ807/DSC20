# DSC 20 Homework 01
# Name: Zehui Zhang
# PID:  A16151490

# Question 1
def older_tutor(first_name, first_age, second_name, second_age):

    """
    A function that returns the name of the older tutor given their names (as
    strings) and ages (as positive integers). If they happen to be of the same
    age, return a string: 'Same Age'.

    >>> older_tutor("Aaron", 22, "James", 21)
    'Aaron'
    >>> older_tutor("Elvy", 18, "Yuxuan", 20)
    'Yuxuan'
    >>> older_tutor("Simon", 999, "Sean", 999)
    'Same Age'
    >>> older_tutor('Barry', 20, 'Peter', 20)
    'Same Age'
    >>> older_tutor('David', 19, 'Justin', 21)
    'Justin'
    >>> older_tutor('Xin', 31, 'Gao',19)
    'Xin'
    """

    if first_age > second_age:
        return first_name
    if first_age < second_age:
         return second_name
    else:
        return 'Same Age'


# Question 2
def older_tutor_year_month(f_name, f_year, f_month, s_name, s_year, s_month):

    """
    A function that that returns the name of the older tutor, given their
    names (as strings), years (as positive integers), and months (0 to 11).
    If they happen to be the same age return a string: 'Same Age'.

    You can reuse the function from the first question when needed.

    >>> older_tutor_year_month("Aaron", 22, 10, "James", 22, 5)
    'Aaron'
    >>> older_tutor_year_month("Elvy", 18, 11, "Yuxuan", 18, 11)
    'Same Age'
    >>> older_tutor_year_month("Simon", 10, 11, "Sean", 30, 3)
    'Sean'
    >>> older_tutor_year_month('Barry', 20, 8, 'Petter', 20, 8)
    'Same Age'
    >>> older_tutor_year_month('David', 19, 7, 'Justin', 21, 2)
    'Justin'
    >>> older_tutor_year_month('Xin', 31, 2, 'Gao', 19, 11)
    'Xin'
    """

    if older_tutor(f_name, f_year, s_name, s_year) == 'Same Age':
        if f_month > s_month:
            return f_name
        if f_month < s_month:
            return s_name
        else:
            return 'Same Age'
    elif older_tutor(f_name, f_year, s_name, s_year) != 'Same Age':
        return older_tutor(f_name, f_year, s_name, s_year)


# Question 3
def message(name, dow, time):

    """
    A function that takes in (name, day of the week, time) and returns
    Sharmi's invitation to her discussion session. Check the doctest
    for the output string format.

    Note:
        <BLANKLINE> denotes a blank line in doctest.
        DO NOT append this token to the returned string.

    >>> print(message("Marina", "Friday", "4:00 PM"))
    Dear Marina,
    Please join our discussion on Friday at 4:00 PM.
    <BLANKLINE>
    Sharmi
    >>> print(message("Barry", "Monday", "2:00 PM"))
    Dear Barry,
    Please join our discussion on Monday at 2:00 PM.
    <BLANKLINE>
    Sharmi
    >>> print(message("Tommy", "Tuesday", "4:00 AM"))
    Dear Tommy,
    Please join our discussion on Tuesday at 4:00 AM.
    <BLANKLINE>
    Sharmi
    >>> print(message("David", "Thursday", "7:00 PM"))
    Dear David,
    Please join our discussion on Thursday at 7:00 PM.
    <BLANKLINE>
    Sharmi
    """

    f_line = 'Dear ' + name +','
    s_line = 'Please join our discussion on ' + dow + ' at ' + time + '.'
    t_line = 'Sharmi'
    sep_line = '\n'
    return f_line+sep_line+s_line+sep_line+sep_line+t_line


# Question 4
def larger_room(
        first_name,
        first_room_length,
        first_room_width,
        second_name,
        second_room_length,
        second_room_width,
):
    """
    A function that returns the name of the tutor living in a larger room,
    given their names (as strings), and their room dimensions (height and
    width as positive integers). If they happen to have the same room area,
    return a string: "Same Area".

    You may assume that their rooms are rectangular.

    >>> larger_room("Aaron", 22, 5, "James", 22, 10)
    'James'
    >>> larger_room("Elvy", 18, 11, "Yuxuan", 20, 3)
    'Elvy'
    >>> larger_room("Simon", 30, 3, "Sean", 2, 45)
    'Same Area'
    >>> larger_room('Barry', 17, 10, 'Petter', 15, 8)
    'Barry'
    >>> larger_room('David', 12, 8, 'Justin', 13, 10)
    'Justin'
    >>> larger_room('Xin', 22, 10, 'Gao',20 , 11)
    'Same Area'
    """

    area1 = first_room_length * first_room_width
    area2 = second_room_length * second_room_width
    if area1 > area2:
        return first_name
    if area1 < area2:
        return second_name
    else:
        return 'Same Area'


# Question 5
def multi_lst(lst):

    '''
    This is a function find the product of all elements in the given list.

    >>> multi_lst([2,3,4])
    24
    >>> multi_lst([3,8,9])
    216
    >>> multi_lst([2,4,3,7])
    168
    '''

    result = 1
    for i in lst:
        result = result * i
    return result

def larger_multidim_room(
    first_name, first_room_dims, second_name, second_room_dims
):
    """
    A function that returns the name of the tutor living in a larger room,
    given their names (as strings), and their room dimensions (as a list of
    positive integers). If they happen to have the same room volume,
    return a string: "Same Volume".

    You may assume two rooms have the same number of dimensions.

    >>> larger_multidim_room("Aaron", [22, 5, 7, 11], "James", [10, 11, 2, 9])
    'Aaron'
    >>> larger_multidim_room("Elvy", [11, 8, 1], "Yuxuan", [3, 5, 20])
    'Yuxuan'
    >>> larger_multidim_room("Simon", [20, 9], "Sean", [18, 10])
    'Same Volume'
    >>> larger_multidim_room('Barry', [17,10,3,6], 'Petter', [15,8,3,7])
    'Barry'
    >>> larger_multidim_room('David', [3,8,6], 'Justin', [13,10,4])
    'Justin'
    >>> larger_multidim_room('Xin', [25,7], 'Gao',[5,35])
    'Same Volume'
    """

    if multi_lst(first_room_dims) > multi_lst(second_room_dims):
        return first_name
    if multi_lst(first_room_dims) < multi_lst(second_room_dims):
        return second_name
    else:
        return 'Same Volume'


# Question 6
def larger_room_subspace(
    ndim, first_name, first_room_dims, second_name, second_room_dims
):
    """
    A function that returns the name of the tutor living in a larger room with
    larger subspace (calculated using only the first `ndim` dimensions), given
    their names (as strings), and their room dimensions (as a list of positive
    integers). If they happen to have the same room volume, return a string:
    "Same Volume".

    You may assume two rooms have the same number of dimensions, and `ndim`
    won't exceed the number of dimensions of both rooms.

    >>> larger_room_subspace(2, "Aaron", [2, 4, 6, 7, 8],
    ...                         "James", [4, 2, 8, 10, 3])
    'Same Volume'
    >>> larger_room_subspace(3, "Aaron", [2, 4, 6, 7, 8],
    ...                         "James", [4, 2, 8, 10, 3])
    'James'

    >>> larger_room_subspace(5, "Aaron", [2, 4, 6, 7, 8],
    ...                         "James", [4, 2, 8, 10, 3])
    'Aaron'

    >>> larger_room_subspace(3,'Justin', [9,3,6,4,2,5,7],
    ...                        'Barry', [9,12,3,2,9,8,5])
    'Barry'

    >>> larger_room_subspace(5,'Justin', [9,3,6,4,2,5,7],
    ...                        'Barry', [9,12,3,2,1,8,5])
    'Justin'
    >>> larger_room_subspace(4,'Justin', [9,3,6,4,2,5,7],
    ...                        'Barry', [9,12,3,2,9,8,5])
    'Same Volume'
    """

    num_dim = ndim
    f_room_dim = first_room_dims[:num_dim]
    s_room_dim = second_room_dims[:num_dim]
    if multi_lst(f_room_dim) > multi_lst(s_room_dim):
        return first_name
    if multi_lst(f_room_dim) < multi_lst(s_room_dim):
        return second_name
    else:
        return 'Same Volume'


# Question 7
def larger_room_subspace_unbounded(
    ndim, first_name, first_room_dims, second_name, second_room_dims
):
    """
    A function that returns the name of the tutor living in a larger room with
    larger subspace (calculated using only the first `ndim` dimensions), given
    their names (as strings), and their room dimensions (as a list of positive
    integers). If they happen to have the same room volume, return a string:
    "Same Volume".

    If the given dimensions `ndim` exceeds the number of dimensions of both
    rooms, you should apply the following procedure to each room:
        (1) Find the dimensions with maximum and minimum length
        (2) Take the square root of the product of the max and min found
        (3) Truncate this number to only keep the 3 digits after the decimal
        point
    Then, compare the truncated numbers of two rooms, and return the name of
    the tutor associated with a larger truncated number, or "Same Volume"
    if two numbers are equal.

    You may assume two rooms have the same number of dimensions.

    >>> larger_room_subspace_unbounded(10, "Yuxuan", [2, 8, 6, 8, 9],
    ...                                    "James", [4, 1, 18, 15, 6])
    'Same Volume'
    >>> larger_room_subspace_unbounded(10, "Aaron", [2, 4, 6, 7, 8],
    ...                                    "James", [4, 2, 8, 10, 3])
    'James'
    >>> larger_room_subspace_unbounded(10, "Jerry", [9, 7, 1, 2, 11],
    ...                                    "Colin", [8, 5, 8, 3, 12])
    'Jerry'
    >>> larger_room_subspace_unbounded(8,'Barry',[9,12,3,2,9,8,5],
    ...                                  'Justin', [9,3,6,4,2,5,7])
    'Barry'
    >>> larger_room_subspace_unbounded(4,'Barry',[9,12,3,2,9,8,5],
    ...                                  'Justin', [9,3,6,4,2,5,7])
    'Same Volume'
    >>> larger_room_subspace_unbounded(10,'Barry',[2, 4, 6, 7, 8],
    ...                                   "Justin", [4, 2, 8, 10, 3])
    'Justin'
    """

    first_dim = len(first_room_dims)
    second_dim = len(second_room_dims)
    product1 = min(first_room_dims) * max(first_room_dims)
    product2 = min(second_room_dims) * max(second_room_dims)
    num_of_root = 1/2
    num_of_round = 3
    if first_dim and second_dim >= ndim:
        return larger_room_subspace(ndim,
                                    first_name,
                                    first_room_dims,
                                    second_name,
                                    second_room_dims)
    else:
        f_v = round(product1**num_of_root, num_of_round)%1
        s_v = round(product2**num_of_root, num_of_round)%1
        if f_v > s_v:
            return first_name
        if f_v < s_v:
            return second_name
        else:
            return 'Same Volume'


# Question 8
def odd_even_list(names):
    """
    A function that returns a list, where each name in the names list is
    replaced with the string "Even" if the name has even length, or "Odd"
    otherwise. If the names list is empty, return a list with the string
    "Empty list was given" in it.

    >>> odd_even_list(["Marina", "Elvy", "James", "Sharmi"])
    ['Even', 'Even', 'Odd', 'Even']
    >>> odd_even_list(["Yuxuan", "Simon", "Sean"])
    ['Even', 'Odd', 'Even']
    >>> odd_even_list([])
    ['Empty list was given']
    >>> odd_even_list(['Barry','Marry','Lucy'])
    ['Odd', 'Odd', 'Even']
    >>> odd_even_list(['Lucy','David','Beezy','Tommy'])
    ['Even', 'Odd', 'Odd', 'Odd']
    >>> odd_even_list([])
    ['Empty list was given']
    """

    even_index = 2
    name_lst = []
    if len(names) != 0:
        for name in names:
            if len(name)%even_index == 0:
                name_lst.append('Even')
            else:
                name_lst.append('Odd')
    else:
        return ['Empty list was given']
    return name_lst


# Question 9
def is_james_more_than_aaron(names):
    """
    A function that returns whether the name 'James' occurs more often than
    the name 'Aaron' in the input list of names. Return True if the above
    statement is true.

    >>> is_james_more_than_aaron(["James", "Aaron", "James"])
    True
    >>> is_james_more_than_aaron(["Aaron", "Aaron"])
    False
    >>> is_james_more_than_aaron(["Aaron", "Marina", "Yuxuan", "James"])
    False
    >>> is_james_more_than_aaron(['Aaron', 'Aaron', 'Barry', 'James'])
    False
    >>> is_james_more_than_aaron(['James', 'James', 'James'])
    True
    >>> is_james_more_than_aaron(['Aaron'])
    False
    """

    freq_Aaron, freq_James = 0, 0
    for i in names:
        if i == 'Aaron':
            freq_Aaron += 1
        if i == 'James':
            freq_James += 1
    if freq_Aaron < freq_James:
        return True
    else:
        return False


# Question 10
def string_sum(lst):
    """
    A function that calculates the sum of all integers in the input list. All
    integers in the input list are given in string format, and the returned
    sum should also be a string.

    >>> string_sum(["1", "2", "3"])
    '6'
    >>> string_sum(["111", "205", "377"])
    '693'
    >>> string_sum(["777", "-999"])
    '-222'
    >>> string_sum(["3", "7"])
    '10'
    >>> string_sum(["824", "111", "222"])
    '1157'
    >>> string_sum(["921", "221", "12"])
    '1154'
    >>> string_sum([])
    '0'
    """

    num_sum = 0
    if len(lst) == 0:
        return '0'
    else:
        for i in lst:
            num_sum = num_sum +int(i)
        return str(num_sum)
