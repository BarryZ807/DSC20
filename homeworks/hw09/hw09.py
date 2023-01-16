"""
DSC 20 Homework 09
Name: Zehui Zhang
PID:  A16151490
"""


# Question 1
def check_inputs(input1, input2):
    """
    Check the input validation one by one by using raise error

    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'

    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1

    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type

    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric

    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type

    >>> check_inputs([], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type

    >>> check_inputs([2,1,3,4,12], 8)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1

    >>> check_inputs([3,4,12], 3)
    'Input validated'
    """
    # check if the input1 is a list
    if not isinstance(input1,list):
        raise TypeError('input1 is not the correct type')
    for index, element in enumerate(input1):
        # check if the values in input1 is numeric
        if not isinstance(element,(int,float)):
            raise TypeError('The element at index {} is not numeric'.\
            format(index))
    # check if the input2 is numeric
    if not isinstance(input2,(int,float)):
        raise TypeError('input2 is not the correct type')
    # check if input2 is in input1
    if input2 not in input1:
        raise TypeError('input2 not in input1')
    return 'Input validated'


# Question 2
def load_file(filename):
    """
    Check the correctness of a given filepath and its corresponding file
    one by one by using raise error

    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string

    >>> load_file('files/ten_words.txt')
    10

    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty

    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist

    >>> load_file('files/addition1.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty

    >>> load_file('files/addition2.txt')
    4

    >>> load_file('files/addition3.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/addition3.txt does not exist
    """
    # check if the filepath is a string
    if not isinstance(filename,str):
        raise TypeError('filename is not a string')
    # check the existness of file
    try:
        f = open(filename,'r')
    except IOError:
        raise FileNotFoundError('{} does not exist'.format(filename))
    else:
        # count the words
        words = f.read().split()
        counts = len(words)
        # check if the file is empty
        if len(words) == 0:
            raise ValueError('File is empty')
        return counts


# Question 3
def q3_doctests():
    """
    Q3 doctests go here.

    >>> h = Nonmetal("H")
    >>> h
    Nonmetal("H")
    >>> print(h)
    Nonmetal name: H, atomic number: 8, period: 2, group: 2
    >>> h.get_mass()
    66

    >>> f = Metal("F")
    >>> f
    Metal("F")
    >>> print(f)
    Metal name: F, atomic number: 6, period: 1, group: 6
    >>> f.get_mass()
    78

    >>> f == h
    False
    >>> f != h
    True
    >>> f > h
    True
    >>> f < h
    False

    >>> water = Compound("H2O1")
    >>> water
    Compound("H2O1")
    >>> print(water)
    H2O1
    >>> water.elements
    {'H': 2, 'O': 1}
    >>> water.get_compound_mass()
    255

    >>> yummy_metal = Compound("U1")
    >>> dsc2 = Compound("D2S2C2")
    >>> dsc3 = Compound("D3S3C3")
    >>> cse = Compound("C7S8E9")
    >>> lava = Compound("H3O4")
    >>> obsidian = Compound("H5O5")
    >>> smelly_gas = Compound("H2")

    >>> water == yummy_metal
    True
    >>> water <= yummy_metal
    True
    >>> water > dsc2
    False

    >>> dsc2 + dsc3
    Compound("C5D5S5")
    >>> water - smelly_gas
    Compound("O1")
    >>> dsc2 + cse
    Traceback (most recent call last):
    ...
    ValueError
    >>> water - lava
    Traceback (most recent call last):
    ...
    ValueError
    >>> water + lava == obsidian
    True
    """
    return

def my_doctest():
    """
    >>> l = Metal("L")
    >>> l
    Metal("L")
    >>> print(l)
    Metal name: L, atomic number: 12, period: 2, group: 6
    >>> l.get_mass()
    150

    >>> y = Nonmetal("Y")
    >>> y
    Nonmetal("Y")
    >>> print(y)
    Nonmetal name: Y, atomic number: 25, period: 5, group: 1
    >>> y.get_mass()
    205

    >>> y == l
    False
    >>> y > l
    True

    >>> A = Compound("A1B1")
    >>> A
    Compound("A1B1")
    >>> print(A)
    A1B1
    >>> A.elements
    {'A': 1, 'B': 1}
    >>> A.get_compound_mass()
    26

    >>> B = Compound("B1C1")

    >>> A == B
    False
    >>> A >= B
    False

    >>> A+B
    Compound("A1B2C1")
    """
    return


LIST_METAL = "FKLPQRUVWXZ"


class Element:
    """
    A class represents each element in the periodic table.
    """

    def __init__(self, name):
        """
        Constructor of Element

        Input validation is required

        Parameter:
        name (str): a single uppercase character from 'A' to 'Z' that
                    represents the name of the element
        """
        # check the validation of the name
        if isinstance(name,str) == False:
            raise ValueError('invalid argument')
        # Initialize arguments
        upper = 29
        num_letter = 26
        num_digit = 9
        num_group = 6
        self.name = name
        self.atomic_num = ord(self.name) - upper - num_letter - num_digit
        if self.atomic_num % num_group == 0:
            self.period = self.atomic_num // num_group
            self.group = num_group
        else:
            self.period = self.atomic_num // num_group + 1
            self.group = self.atomic_num % num_group

    def get_mass(self):
        """
        Returns atomic mass of this element

        This method is a placeholder to avoid style check errors in some
        editors or tools. You will overwrite this method in the subclasses.
        """
        # DO NOT MODIFY #
        raise NotImplementedError("must be implemented in the subclasses")

    def __eq__(self, other_elem):
        """
        Returns True when two Elements are equal.
        Equality is determined by their atomic mass
        """
        # check if the mass of two elements are equal
        if self.get_mass() == other_elem.get_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __ne__(self, other_elem):
        """ Returns True when two Elements are not equal """
        # check if the mass of two elements are not equal
        if self.get_mass() != other_elem.get_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __gt__(self, other_elem):
        """ Returns True when this Element is greater than the other """
        # check if the mass of element is greater than other
        if self.get_mass() > other_elem.get_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __ge__(self, other_elem):
        """
        Returns True when this Element is greater than or
        equal to the other
        """
        # check if the mass of element is greater or equal to other
        if self.get_mass() >= other_elem.get_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __lt__(self, other_elem):
        """ Returns True when this Element is less than the other """
        # check if the mass of element is less than other
        if self.get_mass() < other_elem.get_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __le__(self, other_elem):
        """
        Returns True when this Element is less than or
        equal to the other
        """
        # check if the mass of element is less or equal to other
        if self.get_mass() <= other_elem.get_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __repr__(self):
        """ Returns object representation of this Element """
        # uncomment the following code
        # repr_form = "{0}(\"{1}\")"
        class_name = self.__class__.__name__
        # repr_form = repr_form.format(...)
        return "{0}(\"{1}\")".format(class_name,self.name)


class Nonmetal(Element):
    """
    # TODO: add class docstring #
    """

    def get_mass(self):
        """ Returns atomic mass of this Nonmetal element """
        # magic numbers
        mass_constant = 8
        # calculate the atomic mass
        atomic_mass = (mass_constant * self.atomic_num) + self.period
        return atomic_mass

    def __str__(self):
        """ Returns string representation of this Nonmetal element """
        # uncomment the following code
        # str_form = \
        #    "Nonmetal name: {}, atomic number: {}, period: {}, group: {}"
        return "Nonmetal name: {}, atomic number: {}, period: {}, group: {}".\
        format(self.name,self.atomic_num,self.period,self.group)


class Metal(Element):
    """
    # TODO: add class docstring #
    """

    def get_mass(self):
        """ Returns atomic mass of this Metal element """
        # magic number
        mass_constant = 12
        # calculate the atomic mass
        atomic_mass = (mass_constant * self.atomic_num) + self.group
        return atomic_mass

    def __str__(self):
        """ Returns string representation of this Metal element """
        # uncomment the following code
        # str_form = "Metal name: {}, atomic number: {}, period: {}, group: {}"
        return "Metal name: {}, atomic number: {}, period: {}, group: {}".\
        format(self.name,self.atomic_num,self.period,self.group)


class Compound:
    """
    # TODO: add class docstring #
    """

    def __init__(self, name):
        """
        Constructor of Compound

        Input validation is required

        Parameter:
        name (str): a string that represents the name of the compound
        """
        # check the validation of the name
        if isinstance(name,str) == False:
            raise ValueError('invalid argument')
        # Initialize the arguments
        self.name = name
        # helper empty list to store the elements and number of atoms
        ele = []
        num = []
        # for loop to seperate the elements and atoms into two lists
        for i in range(len(self.name)):
            if i % 2 == 0:
                ele.append(self.name[i])
            else:
                num.append(int(self.name[i]))
        # Initialize the element as the dictionary
        self.elements = dict(zip(ele,num))

        # the initial mass is 0
        mass = 0
        # for loop to calculate differnt compound mass based on the class of
        # element
        for key,value in self.elements.items():
            if key in LIST_METAL:
                mass+=Metal(key).get_mass()*value
            else:
                mass+=Nonmetal(key).get_mass()*value
        self.compound_mass = mass

    def get_compound_mass(self):
        """ A simple getter of compound_mass """
        # return the compound mass calculated above
        return self.compound_mass

    def __eq__(self, other_comp):
        """
        Returns True when two Compounds are equal.
        Equality is determined by their compound mass
        """
        # check if two compounds have same mass
        if self.get_compound_mass() == other_comp.get_compound_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __ne__(self, other_comp):
        """ Returns True when two Compounds are not equal """
        # check if two compounds have different mass
        if self.get_compound_mass() != other_comp.get_compound_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __gt__(self, other_comp):
        """ Returns True when this Compound is greater than the other """
        # check if the mass of compound is greater than other
        if self.get_compound_mass() > other_comp.get_compound_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __ge__(self, other_comp):
        """
        Returns True when this Compound is greater than or
        equal to the other
        """
        # check if the mass of compound is greater or equal to other
        if self.get_compound_mass() >= other_comp.get_compound_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __lt__(self, other_comp):
        """ Returns True when this Compound is less than the other """
        # check if the mass of compound is less than other
        if self.get_compound_mass() < other_comp.get_compound_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __le__(self, other_comp):
        """
        Returns True when this Compound is less than or
        equal to the other
        """
        # check if the mass of compound is less or equal to other
        if self.get_compound_mass() <= other_comp.get_compound_mass():
            # if so return true
            return True
        else:
            # else return False
            return False

    def __add__(self, other_comp):
        """
        Synthesize a new Compound by adding this Compound with another

        Exception:
        ValueError will be raised if the product is invalid
        """
        # for loop going through the element and number of it one by one
        for name,num in other_comp.elements.items():
            # if the element in other compound is in the first compund
            if name in self.elements.keys():
                # update the number of element
                self.elements[name] = self.elements[name] + num
            else:
                # else create new one
                self.elements[name] = num
        # check if all number of elements fits the requirements
        for key,value in self.elements.items():
            # if not raise the error
            if value < 0 or value > 9:
                raise ValueError()
        # sorted the dictionary
        sort_lst = sorted(self.elements)
        result = ''
        # append all to the result
        for i in sort_lst:
            result = result + i + str(self.elements[i])
        return Compound(result)

    def __sub__(self, other_comp):
        """
        Decompose this Compound by subtracting another from it. A new product
        is returned after decomposition

        Exception:
        ValueError will be raised if the product is invalid
        """
        # for loop going through the element and number of it one by one
        for name,num in other_comp.elements.items():
            # if the element of other compound is not appear in the first one
            if name not in self.elements.keys():
                # raise error
                raise ValueError()
            else:
                # else update the number of elements
                self.elements[name] = self.elements[name] - num
        del_lst = []
        # check if all number of elements fits the requirements
        for key,value in self.elements.items():
            if value < 0 or value > 9:
                raise ValueError()
            if value == 0:
                # append all elements that reduced to 0 into the helper list
                del_lst.append(key)
        for i in del_lst:
            # remove all elements reduced to 0
            del self.elements[i]
        # sort the dictionary
        sort_lst = sorted(self.elements)
        result = ''
        # append all to the result
        for i in sort_lst:
            result = result + i + str(self.elements[i])
        return Compound(result)

    def __str__(self):
        """ Returns string representation of this Compound """
        return self.name

    def __repr__(self):
        """ Returns object representation of this Compound """
        # uncomment the following code
        # repr_form = "{0}(\"{1}\")"
        class_name = self.__class__.__name__
        # repr_form = repr_form.format(...)
        return "{0}(\"{1}\")".format(class_name,self.name)
