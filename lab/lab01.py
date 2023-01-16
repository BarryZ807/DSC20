# DSC 20 Lab 01
# Name: Zehui Zhang
# PID:  A16151490

# Question 1
def password_1(first_name, last_name):
    """
    Return a password string constructed by concatenating the first 2
    characters of the first name and the last 2 characters of the last name,
    repeating this pattern twice, and appending the full last name at the end.
    If either name is shorter than 2 characters, concatenate the names and
    repeat this pattern three times.

    >>> password_1("Marina", "Langlois")
    'MaisMaisLanglois'
    >>> password_1("Donald", "Trump")
    'DompDompTrump'
    >>> password_1("Marina", "")
    'MarinaMarinaMarina'
    >>> password_1("","")
    ''
    >>> password_1("J", "Yo")
    'JYoJYoJYo'
    >>> password_1(" ", " ")
    '      '
    """
    if len(first_name) < 2 or len(last_name) < 2:
        return(first_name+last_name) * 3
    else:
        Step_1 = first_name[:2]
        Step_2 = last_name[-2:]
        Step_3 = (Step_1+Step_2)*2
        Step_4 = Step_3 + last_name
        return Step_4


# Question 2
def password_2(param1, param2, param3):
    """
    Return a password string constructed with the following rules:
        (1) If there are only 0 or 1 numeric among 3 parameters, concatenate
        the string form of all parameters directly.
        (2) If there are 2 numeric parameters, calculate the sum of 2 numeric
        values if they are both int, or calculate the product of them and round
        to 2 decimal places if any of them is float. Finally, append this
        sum/product to the string parameter.

    You may assume that there will be at least 1 string parameter.

    >>> password_2("Marina", "Langlois", "20")
    'MarinaLanglois20'
    >>> password_2("Marina", "Langlois", 20)
    'MarinaLanglois20'
    >>> password_2("Elvy", True, 20)
    'ElvyTrue20'
    >>> password_2(True, 20, "Elvy")
    'True20Elvy'
    >>> password_2(20, 40, "Elvy")
    'Elvy60'
    >>> password_2(20, "Elvy", 3)
    'Elvy23'
    >>> password_2(2, 3.333, "Elvy")
    'Elvy6.67'
    """
    def num_type(param):
        if type(param) == int or type(param) == float:
            return 1
        else:
            return 0

    s1 = list(map(num_type,[param1,param2,param3]))
    s2 = sum(s1)
    if s2 == 0 or s2 ==1:
        return (str(param1)+str(param2)+str(param3))
    elif s2 == 2:
        T1 = type(param1)
        T2 = type(param2)
        T3 = type(param3)
        if T1 != str and T2 != str:
            Determine_type1 = type(param1 + param2) == int
            if Determine_type1 == True:
                return param3 + str(param1 + param2)
            else:
                return param3 + str(round((param1 * param2),2))
        elif T1 != str and T3 != str:
            Determine_type2 = type(param1 + param3) == int
            if Determine_type2 == True:
                return param2 + str(param1 + param3)
            else:
                return param2 + str(round((param1 * param3),2))
        elif T2 != str and T3 != str:
            Determine_type3 = type(param2 + param3) == int
            if Determine_type3 == True:
                return param1 + str(param2 + param3)
            else:
                return param1 + str(round((param2 * param3),2))


# Question 3
def access(nickname, permission_lvl, super_access):
    """
    Return a string that shows the permissions associated with the person with
    given nickname. The possible permission levels are 0 (read), 1 (read and
    write), and 2 (read, write and invite). If super_access is set to True,
    this person ignores the permission level and has the full access. See the
    doctest for the output string format.

    You may assume that nickname is a string, permission_lvl is in (0, 1, 2),
    and super_access is a boolean value.

    >>> access("Marina", 2, True)
    'Marina, you have full access'
    >>> access("Sean", 1, True)
    'Sean, you have full access'
    >>> access("Jerry", 0, True)
    'Jerry, you have full access'
    >>> access("Elvy", 2, False)
    'Elvy, you are authorized to: read, write and invite'
    >>> access("Yuxuan", 1, False)
    'Yuxuan, you are authorized to: read and write'
    >>> access("Simon", 0, False)
    'Simon, you are authorized to: read'
    """
    if super_access == True:
        return nickname + ', you have full access'
    elif super_access == False:
        if permission_lvl == 0:
            return nickname + ', you are authorized to: read'
        elif permission_lvl == 1:
            return nickname + ', you are authorized to: read and write'
        else:
            return nickname + ', you are authorized to: read, write and invite'


# Question 4
def repeats(passwords, to_search, num_of_repeats):
    """
    A function that takes in a list of passwords (as strings), a password that
    needs to be checked (as a string), and an integer that represents the
    number of repetitions. If the given password occurs given number of times,
    return True, else return False.

    >>> repeats(["ma48", "ma28", "ma48"], "ma48", 2)
    True
    >>> repeats(["ma48", "ma28", "ma48"], "ma48", 3)
    False
    >>> repeats(["ma48", "ma28", "ma48", "ma28", "ma48"], "ma38", 2)
    False
    >>> repeats(["ma48", "ma28", "ma48", "ma38"], "ma48", 1)
    False
    """
    Result = passwords.count(to_search) == num_of_repeats
    return Result
