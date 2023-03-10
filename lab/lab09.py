"""
DSC 20 Lab 09
Name: Zehui Zhang
PID:  A16151490
"""


# Question 1
def polynomial_doctests():
    """
    >>> p1 = Polynomial({0: 8, 1: 2, 3: 4})
    >>> p2 = Polynomial({0: 8, 1: 2, 2: 8, 4: 4})
    >>> p3 = Polynomial({0: 8, 1: 2, 3: 4, 2: 0})
    >>> print(p1)
    8 + 2 x + 4 x^(3)
    >>> p2
    {0: 8, 1: 2, 2: 8, 4: 4}
    >>> print(p3)
    8 + 2 x + 4 x^(3)
    >>> print(p1 + p2)
    16 + 4 x + 8 x^(2) + 4 x^(3) + 4 x^(4)
    >>> print(p1 * p2)
    64 + 32 x + 68 x^(2) + 48 x^(3) + 40 x^(4) + 40 x^(5) + 16 x^(7)
    >>> p1 == p1
    True
    >>> p1 == p2
    False
    >>> p1 == p3
    True
    """
    return


class Polynomial:
    """
    A class that abstracts polynomial expressions.
    """

    def __init__(self,dictionary):
        self.dic = dictionary

    def __str__(self):
        exp = ''
        newlist = [i for i in self.dic.keys()]
        newlist.sort()
        for i in newlist:
            if i == 1:
                exp+=str(self.dic[i])+ ' x' + ' + '
            elif i == 0:
                exp+=str(self.dic[i])+ ' + '
            else:
                if self.dic[i] == 0:
                    continue
                else:
                    if newlist.index(i) == (len(newlist)-1):
                        exp+=str(self.dic[i])+ ' x' + '^' +'(' + str(i)+')'
                    else:
                        exp+=str(self.dic[i])+ ' x'+'^' +'(' + str(i)+')'+' + '
        return '{}'.format(exp)

    def __repr__(self):
        return '{}'.format(self.dic)

    def __add__(self,new_term):
        newdic1 = {}
        for i in new_term.dic.keys():
            if i in newdic1.keys():
                newdic1[i] += new_term.dic[i]
            else:
                newdic1[i] = new_term.dic[i]
        for i in self.dic.keys():
            if i in newdic1.keys():
                newdic1[i] += new_term.dic[i]
            else:
                newdic1[i] = new_term.dic[i]
        return Polynomial(newdic1)

    def __mul__(self,new_term):
        newdic2 = {}
        for m in self.dic.keys():
            for n in new_term.dic.keys():
                if m+n in newdic2.keys():
                    newdic2[m+n] += self.dic[m]*new_term.dic[n]
                else:
                    newdic2[m+n] = self.dic[m]*new_term.dic[n]
        return Polynomial(newdic2)

    def __eq__(self,new_term):
        for i in self.dic.keys():
            if i not in new_term.dic.keys():
                if self.dic[i]!=0:
                    return False
            else:
                if new_term.dic[i] == self.dic[i]:
                    continue
                else:
                    return False
        for j in new_term.dic.keys():
            if j not in self.dic.keys():
                if new_term[j]!=0:
                    return False
                else:
                    if new_term.dic[j] == self.dic[j]:
                        continue
                    else:
                        return False
        return True


# Question 2.1
def fix_1(lst1, lst2):
    """
    Divide all of the elements in `lst1` by each element in `lst2`
    and return the values in a list.

    >>> fix_1([1, 2, 3], [0, 1])
    [1.0, 2.0, 3.0]
    >>> fix_1([], [])
    []
    >>> fix_1([10, 20, 30], [0, 10, 10, 0])
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    """
    out = []
    for div in lst2:
        for num in lst1:
            try:
                out.append(num / div)
            except ZeroDivisionError as e:
                continue
    return out


# Question 2.2
def fix_2(*filepaths):
    """
    Open all of the files in `filepaths` and PRINT a string for each file
    that indicates if this file can be opened or not.

    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found

    >>> fix_2('docs.txt')
    docs.txt not found
    """
    for filepath in filepaths:
        try:
            cur_file = open(filepath, "r")
            print('{} opened'.format(filepath))
            cur_file.close()
        except FileNotFoundError as e:
            print('{} not found'.format(filepath))


# Question 2.3
def fix_3(lst):
    """
    For each element in `lst`, add it with its following element
    in the list. Returns all of the summed values in a list.

    >>> fix_3([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []

    >>> fix_3([1, 2, 3, 4])
    <class 'IndexError'>
    [3, 5, 7]

    >>> fix_3([])
    []
    """
    sum_of_pairs = []
    for i, _ in enumerate(lst):
        try:
            sum_of_pairs.append(lst[i] + lst[i + 1])
        except IndexError as i:
            print(type(i))
        except TypeError as e:
            print(type(e))
    return sum_of_pairs
