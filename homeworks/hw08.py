"""
DSC 20 Homework 08
Name: Zehui Zhang
PID:  A16151490
"""

# Question 1
def counter_doctests():
    """
    Doctests for Counter and AlphanumericCounter.

    >>> counter = Counter()
    >>> counter.size()
    0
    >>> counter.add_items([123, 123, "abc", (10, 10), (10, 20)])
    >>> counter.size()
    5
    >>> counter.get_count(123)
    2
    >>> counter.get_count("dsc20")
    0
    >>> counter.get_all_counts()
    {123: 2, 'abc': 1, (10, 10): 1, (10, 20): 1}

    >>> an_counter = AlphanumericCounter()
    >>> an_counter.size()
    0
    >>> len(an_counter.counts)
    62
    >>> an_counter.add_items("DSC 20 (Marina Langlois)")
    >>> an_counter.size()
    19
    >>> an_counter.get_count("a")
    3
    >>> an_counter.get_count("?")
    0
    >>> an_counter.get_all_counts()
    {'0': 1, '2': 1, 'a': 3, 'g': 1, 'i': 2, 'l': 1, 'n': 2, 'o': 1, \
'r': 1, 's': 1, 'C': 1, 'D': 1, 'L': 1, 'M': 1, 'S': 1}

    >>> counter2= Counter()
    >>> counter2.size()
    0
    >>> counter2.add_items(['barry', 321, "abc", (1,3), (20,31)])
    >>> counter2.size()
    5
    >>> counter2.get_count(321)
    1
    >>> counter2.get_count("dsc20")
    0
    >>> counter2.get_all_counts()
    {'barry': 1, 321: 1, 'abc': 1, (1, 3): 1, (20, 31): 1}

    >>> counter2.add_items(['barry',122,321,(20,31)])
    >>> counter2.size()
    9
    >>> counter2.get_count(321)
    2
    >>> counter2.get_count("barry")
    2
    >>> counter2.get_all_counts()
    {'barry': 2, 321: 2, 'abc': 1, (1, 3): 1, (20, 31): 2, 122: 1}

    >>> counter2.add_items([12,33,'barry','DSC20',321,321,321])
    >>> counter2.size()
    16
    >>> counter2.get_count(321)
    5
    >>> counter2.get_count("barry")
    3
    >>> counter2.get_all_counts()
    {'barry': 3, 321: 5, 'abc': 1, (1, 3): 1, (20, 31): 2, 122: 1, 12: 1, \
33: 1, 'DSC20': 1}

    >>> an_counter2 = AlphanumericCounter()
    >>> an_counter2.size()
    0
    >>> len(an_counter2.counts)
    62
    >>> an_counter2.add_items("Fall2020 (Barry Zhang)")
    >>> an_counter2.size()
    18
    >>> an_counter2.get_count("a")
    3
    >>> an_counter2.get_count("r")
    2
    >>> an_counter2.get_all_counts()
    {'0': 2, '2': 2, 'a': 3, 'g': 1, 'h': 1, 'l': 2, 'n': 1, 'r': 2, 'y': 1, \
'B': 1, 'F': 1, 'Z': 1}

    >>> an_counter2.add_items("Winter2021(Zehui Zhang)")
    >>> an_counter2.size()
    38
    >>> an_counter2.get_count("a")
    4
    >>> an_counter2.get_count("n")
    3
    >>> an_counter2.get_all_counts()
    {'0': 3, '1': 1, '2': 4, 'a': 4, 'e': 2, 'g': 2, 'h': 3, 'i': 2, 'l': 2, \
'n': 3, 'r': 3, 't': 1, 'u': 1, 'y': 1, 'B': 1, 'F': 1, 'W': 1, 'Z': 3}

    >>> an_counter2.add_items("Spring2021(Zehui Zhang)")
    >>> an_counter2.size()
    58
    >>> an_counter2.get_count("a")
    5
    >>> an_counter2.get_count("n")
    5
    >>> an_counter2.get_all_counts()
    {'0': 4, '1': 2, '2': 6, 'a': 5, 'e': 3, 'g': 4, 'h': 5, 'i': 4, 'l': 2, \
'n': 5, 'p': 1, 'r': 4, 't': 1, 'u': 2, 'y': 1, 'B': 1, 'F': 1, 'S': 1, \
'W': 1, 'Z': 5}
    """
    return


class Counter:
    """
    A counter counts and stores the occurrences of provided items,
    and it allows you to query the count of a specific item in the counter.
    """

    def __init__(self):
        """
        0nitialize the following instance attributes
        """
        self.nelems = 0
        self.counts = {}

    def size(self):
        """
        Returns the total number of items stored in the counter.
        """
        return self. nelems

    def get_count(self, item):
        """
        Returns the count of an object item. If the item does not exist in
        the counter, return 0.
        """
        # check if the item already exist in the counts dictionary
        if item not in self.counts.keys():
            # if not return 0
            return 0
        else:
            # if so return its corresponding value
            return self.counts[item]

    def get_all_counts(self):
        """
        Returns a dictionary of all item to count pairs.
        """
        # return the dictionary
        return self.counts

    def add_items(self, items):
        """
        Takes an iterable object (like list) of objects (items) and adds them
        to the counter. Make sure to update both counts and nelems attributes.
        """
        # By using for loop to iterate
        for item in items:
            # check if the item already exist in the dictionary
            if item not in self.counts.keys():
                # if not the key should be paired with value 1
                self.counts[item] = 1
                # same as nelems
                self.nelems = self.nelems+1
            else:
                # if so add 1 to both nelems and its value
                self.counts[item] = self.counts[item]+1
                self.nelems = self.nelems+1


class AlphanumericCounter(Counter):
    """
    A counter for only Alphanumeric characters in strings.
    """

    def __init__(self):
        """
        Initialize the following instance attributes
        """
        max_len = 62
        self.nelems = 0
        self.counts = [0 for i in range(max_len)]

    def get_index(self, item):
        """
        Given an item, return its corresponding index (0-9 for digits,
        10-35 for lowercase letters, 36-61 for uppercase letters).
        If the item is not an alphanumeric character, return -1.
        """
        # magic numbers represent the bound
        num = 48
        lower = 87
        upper = 29
        # check if the item is upper case
        if item.isupper() == True:
            return ord(item) - upper
        # check if the item is lower case
        elif item.islower() == True:
            return ord(item) - lower
        # check if the item is numeric
        elif item.isnumeric() == True:
            return ord(item) - num
        else:
            return -1

    def get_char(self, idx):
        """
        Given an index (0-61), return the corresponding character.
        """
        # magic numbers represent bound
        num = 48
        lower = 87
        upper = 29
        bound1 = 9
        bound2 = 35
        bound3 = 61
        # check if the index in didits region
        if 0<=idx<=bound1:
            return chr(idx+num)
        # check if the index in lowercase letter region
        elif bound1+1<=idx<=bound2:
            return chr(idx+lower)
        # check if the index in uppercase letter region
        elif bound2+1<=idx<=bound3:
            return chr(idx+upper)

    def get_count(self, item):
        """
        Returns the count of a character item. If the item does not exist
        in the counter, return 0.
        """
        # check if the item exist
        if self.get_index(item) >= 0:
            # if so return the count
            return self.counts[self.get_index(item)]
        else:
            # if not return 0
            return 0

    def get_all_counts(self):
        """
        Returns a dictionary of all item to count pairs. You need to build
        the dictionary by iterating through the counts list and add all pairs
        with non-zero counts to the new dictionary. The dictionary should have
        characters as keys (instead of indices) and counts as values.
        """
        dic={}
        for i in range(len(self.counts)):
            if self.counts[i] != 0:
                # pair the character with counts
                dic[self.get_char(i)] = self.counts[i]
        return dic

    def add_items(self, items):
        """
        Takes a string items and adds each character to the counter.
        Note that you should not add non-alphanumeric characters to this
        counter. Make sure to update both counts and nelems attributes.
        """
        # By using the for loop to make the iteration
        for item in items:
            # check if the index is -1
            if self.get_index(item) == -1:
                # if so skip it and continue
                continue
            else:
                # if not update the data
                self.counts[self.get_index(item)]+=1
                self.nelems = self.nelems+1


# Question 2
def find_two_sums_rec(main, sub):
    """
    return the tuple contians two type of sum:
    1. Sum of intersection: the sum of all numbers in the main sequence
    that also appear in the sub sequence.
    2. Sum of differences: the sum of all numbers in the main sequence
    that do not appear in the sub sequence.

    >>> main_seq = [0, 1, 1, 2, 3, 3, 4, 5, 5]
    >>> find_two_sums_rec(main_seq, [])
    (0, 24)
    >>> find_two_sums_rec(main_seq, [1, 2])
    (4, 20)
    >>> find_two_sums_rec(main_seq, [3, 4, 5])
    (20, 4)

    >>> main_seq2 = [12,2,1,2,3,1,2,3,1]
    >>> find_two_sums_rec(main_seq2, [])
    (0, 27)
    >>> find_two_sums_rec(main_seq2, [2,1,3])
    (15, 12)
    >>> find_two_sums_rec(main_seq2, [2,1])
    (9, 18)

    >>> main_seq3 = [12,21,2,4,2,7,33,45,66,22,9]
    >>> find_two_sums_rec(main_seq3, [])
    (0, 223)
    >>> find_two_sums_rec(main_seq3, [33,45,66,9])
    (153, 70)
    >>> find_two_sums_rec(main_seq3, [12,21,7,9])
    (49, 174)

    >>> main_seq4 = []
    >>> find_two_sums_rec(main_seq4, [])
    (0, 0)
    >>> find_two_sums_rec(main_seq4, [33,45,66,9])
    (0, 0)
    """
    if len(main)==0:
        return (0,0)
    else:
        if main[0] in sub:
            return (main[0]+find_two_sums_rec(main[1:], sub)[0],\
            find_two_sums_rec(main[1:], sub)[-1])
        else:
            return (find_two_sums_rec(main[1:], sub)[0],\
            main[0]+find_two_sums_rec(main[1:], sub)[-1])

# Question 3
def compute_max_string(base, pattern):
    """
    a recursive function that takes a base string and a non-empty pattern
    string, and computes the length of the largest substring of the base that
    starts and ends with the pattern. If no match is found, return 0.

    >>> compute_max_string("jumpsjump", "jump")
    9
    >>> compute_max_string("hwhwhw", "hwh")
    5
    >>> compute_max_string("frontsdakonsakdna", "front")
    5
    >>> compute_max_string("life", "life")
    4

    >>> compute_max_string("tatatathshejtata", "ta")
    16
    >>> compute_max_string("BarryaB", "Ba")
    2
    >>> compute_max_string("zzszszsaaszzzszzs", "zzs")
    17
    """
    if len(base) == 0:
        return 0
    else:
        if base[0:len(pattern)] == pattern and base[-len(pattern):] == pattern:
            return len(base)
        elif base[0:len(pattern)] == pattern:
            return compute_max_string(base[:-1], pattern)
        elif base[-len(pattern):] == pattern:
            return compute_max_string(base[1:], pattern)
        else:
            return compute_max_string(base[1:], pattern)



# Question 4 (Extra Credit)
def group_summation(nums, target):
    """
    a recursive function that takes a list of positive integers
    (nums, not empty) and a positive integer target, and find whether it’s
    possible to pick a combination of integers from nums, such that their sum
    equals the target. Return True if we can pick such a combination of numbers
    from nums; otherwise, return False.

    >>> group_summation([3, 34, 4, 12, 5, 2], 9)
    True
    >>> group_summation([1, 1, 1], 9)
    False
    >>> group_summation([1, 10, 9, 8], 17)
    True

    >>> group_summation([22,11,44,22], 9)
    False
    >>> group_summation([22,11,44,22], 33)
    True
    >>> group_summation([211,32,1,3,5], 212)
    True
    """
    if len(nums) == 0:
        return False
    else:
        if nums[0] == target:
            return True
        elif nums[0] > target:
            return group_summation(nums[1:], target)
        else:
            if target - nums[0] not in nums[1:]:
                if group_summation(nums[1:], target - nums[0]) == True:
                    return True
                else:
                    return group_summation(nums[1:], target)
            else:
                return True
