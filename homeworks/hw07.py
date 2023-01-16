"""
DSC 20 Homework 07
Name: Zehui Zhang
PID:  A16151490
"""

def doctests_go_here():
    """
    >>> available_time1 = [[1, 3, 21], [4, 6, 30], [9, 12, 8]]
    >>> ps1 = PersonalSchedule("Sun", "Curly", available_time1)
    >>> print(ps1)
    Curly Sun is available at [[1, 3, 21], [4, 6, 30], [9, 12, 8]].

    >>> available_time2 = [[1, 7, 20], [9, 10, 5], [11, 16, 8]]
    >>> ps2 = PersonalSchedule("Ran", "Sean", available_time2)
    >>> print(ps2)
    Sean Ran is available at [[1, 7, 20], [9, 10, 5], [11, 16, 8]].

    >>> t1 = Task(2, 5, 20, 1000, "Chopping potatoes")
    >>> t2 = Task(4, 5, 32, 2000, "Coding")
    >>> t3 = Task(11, 12, 8, 4000, "Playing League")
    >>> t4 = Task(1, 2, 21, 1200, "Gardening")
    >>> t5 = Task(11, 16, 6, 500, "Jogging")
    >>> t6 = Task(4, 6, 20, 1200, "Chopping potatoes")
    >>> t7 = Task(6, 9, 20, 1000, "Chopping potatoes")

    >>> print(t1)
    Task Chopping potatoes starts at 2, ends at 5, requires 20 focus level, \
and gives 1000 profit.

    >>> print(t2)
    Task Coding starts at 4, ends at 5, requires 32 focus level, and gives \
2000 profit.

    >>> print(t3)
    Task Playing League starts at 11, ends at 12, requires 8 focus level, \
and gives 4000 profit.

    >>> ps1.can_handle(t1)
    False
    >>> ps1.can_handle(t2)
    False
    >>> ps1.can_handle(t3)
    True
    >>> ps2.can_handle(t4)
    False
    >>> ps2.can_handle(t5)
    True

    >>> ps1.can_handle_task_sequence([t1, t2, t3])
    False
    >>> ps1.can_handle_task_sequence([t3, t4])
    True
    >>> ps2.can_handle_task_sequence([t3, t4])
    False
    >>> ps2.can_handle_task_sequence([t3, t5])
    True

    >>> t1.can_merge_task(t6)
    True
    >>> t1.can_merge_task(t7)
    False

    >>> merged_task1 = t1.merge_two_tasks(t6)
    >>> print(merged_task1)
    Task Chopping potatoes starts at 2, ends at 6, requires 20 focus level, \
and gives 2200 profit.
    >>> merged_task2 = t1.merge_two_tasks(t7)
    >>> print(merged_task2)
    None

    >>> task_sequences = [[t1, t2, t3], [t3, t4], [t3, t6]]
    >>> result1 = ps1.most_profitable_task_sequence(task_sequences)
    >>> result2 = ps1.most_profitable_task_sequence_recursion(task_sequences)
    >>> result1 == [[t3, t4], [t3, t6]]
    True
    >>> result1 == result2
    True

    >>> result3 = ps2.most_profitable_task_sequence_recursion([[t3], [t5]])
    >>> result3 == [[t3]]
    True

    >>> ps2.handle_two_tasks(t1, t6)
    True
    >>> ps2.handle_two_tasks(t1, t7)
    False
    >>> ps2.handle_two_tasks(t6, t7)
    False
    """
    return

def addition_doctests_go_here():
    """
    >>> available_time_1 = [[1, 6, 40], [3, 9, 30], [10, 12, 36]]
    >>> ps_1 = PersonalSchedule("Zhang", "Barry", available_time_1)
    >>> print(ps_1)
    Barry Zhang is available at [[1, 6, 40], [3, 9, 30], [10, 12, 36]].

    >>> available_time_2 = [[2, 6, 23], [3, 7, 33], [7, 8, 10]]
    >>> ps_2 = PersonalSchedule("Xu", "Lucy", available_time_2)
    >>> print(ps_2)
    Lucy Xu is available at [[2, 6, 23], [3, 7, 33], [7, 8, 10]].

    >>> available_time_3 = [[1, 3, 8], [7, 9, 20], [11, 12, 22]]
    >>> ps_3 = PersonalSchedule("Wang", "Allen", available_time_3)
    >>> print(ps_3)
    Allen Wang is available at [[1, 3, 8], [7, 9, 20], [11, 12, 22]].

    >>> t_1 = Task(2, 5, 12, 3000, "Fishing")
    >>> t_2 = Task(4, 6, 12, 100, "Fishing")
    >>> t_3 = Task(18, 20, 2, 2345, "Running")
    >>> t_4 = Task(6, 9, 20, 2334, "Chopping potatoes")
    >>> t_5 = Task(11, 12, 2, 1230, "Fighting")

    >>> print(t_1)
    Task Fishing starts at 2, ends at 5, requires 12 focus level, \
and gives 3000 profit.
    >>> print(t_2)
    Task Fishing starts at 4, ends at 6, requires 12 focus level, \
and gives 100 profit.
    >>> print(t_3)
    Task Running starts at 18, ends at 20, requires 2 focus level, \
and gives 2345 profit.
    >>> print(t_4)
    Task Chopping potatoes starts at 6, ends at 9, requires 20 focus level, \
and gives 2334 profit.
    >>> print(t_5)
    Task Fighting starts at 11, ends at 12, requires 2 focus level, \
and gives 1230 profit.

    >>> ps_1.can_handle(t_1)
    True
    >>> ps_1.can_handle(t_2)
    True
    >>> ps_3.can_handle(t_1)
    False
    >>> ps_2.can_handle(t_1)
    True
    >>> ps_3.can_handle(t_2)
    False
    >>> ps_2.can_handle(t_4)
    False

    >>> ps_1.can_handle_task_sequence([t_1, t_2, t_3])
    False
    >>> ps_1.can_handle_task_sequence([t_3, t_4])
    False
    >>> ps_3.can_handle_task_sequence([t_1, t_2])
    False
    >>> ps_1.can_handle_task_sequence([t_5])
    True

    >>> t_1.can_merge_task(t_2)
    True
    >>> t_2.can_merge_task(t_4)
    False
    >>> t_5.can_merge_task(t_2)
    False

    >>> merged_task_1 = t_1.merge_two_tasks(t_2)
    >>> print(merged_task_1)
    Task Fishing starts at 2, ends at 6, requires 12 focus level, \
and gives 3100 profit.

    >>> merged_task_2 = t_5.merge_two_tasks(t_4)
    >>> print(merged_task_2)
    None

    >>> task_sequences = [[t_1, t_3, t_5], [t_3, t_4], [t_2, t_4]]
    >>> result1 = ps_1.most_profitable_task_sequence(task_sequences)
    >>> result2 = ps_1.most_profitable_task_sequence_recursion(task_sequences)
    >>> result1 == [[t_3, t_4], [t_2, t_4]]
    False
    >>> result1 == result2
    True

    >>> result3 = ps_2.most_profitable_task_sequence_recursion([[t_3], [t_5]])
    >>> result3 == [[t_3]]
    False

    >>> ps_2.handle_two_tasks(t_1, t_2)
    True
    >>> ps_2.handle_two_tasks(t_1, t_5)
    False
    >>> ps_1.handle_two_tasks(t_2, t_5)
    False
    >>> ps_3.handle_two_tasks(t_3, t_5)
    False
    """
    return


class Task:
    """
    Implementation of a task.
    """

    def __init__(self, start_time, end_time, focus_level_required, \
                profit, task_description):
        """
        Constructor of Task.

        Requirement:
        Input validation

        Parameters:
        start_time (int): Start time of this task should be a non-negative integer.
        end_time (int): End time of this task should also be a non-nagative integer.
                        Start time should be strictly less than end time.
        focus_level_required (int): Focus level required for one person to handle
                        this task. It should be a positive integer.
        profit (int): A positive integer that represents how much value would
                        be made if the task is successfully handled.
        task_description (str): Description of this task.
        """
        # Assertions to check all inputs are vaild
        assert type(start_time)==int and type(end_time)==int
        assert start_time >= 0 and end_time>=0 and start_time<end_time
        assert type(focus_level_required)==int and focus_level_required > 0
        assert type(profit)==int and profit > 0
        assert type(task_description)==str
        # Set all variables
        self.start_time = start_time
        self.end_time = end_time
        self.focus_level_required = focus_level_required
        self.profit = profit
        self.task_description = task_description


    def get_start_time(self):
        """Getter for start_time attribute"""
        return self.start_time


    def get_end_time(self):
        """Getter for end_time attribute"""
        return self.end_time


    def get_focus_level_required(self):
        """Getter for focus_level_required attribute"""
        return self.focus_level_required


    def __str__(self):
        """
        String representation of Task.
        """
        return ("Task {} starts at {}, ends at {}, requires {} focus level, " + \
                "and gives {} profit.").format(self.task_description, \
                self.get_start_time(), self.get_end_time(), \
                self.get_focus_level_required(), self.profit)


    def can_merge_task(self, other_task):
        """
        Give another Task called other_task, this function determines whether
        we are able to merge the current task and other_task.

        Requirement:
        Input validation

        Parameters
        other_task (Task): The other task to be merged with this task.

        Returns:
        True if we are able to merge those two tasks, False otherwise.
        """
        # assertion to check the validation of input
        assert type(other_task)==Task
        # Check if focus_level_required and task_description are the same
        if self.get_focus_level_required() == \
        other_task.get_focus_level_required() \
        and self.task_description == other_task.task_description:
            # Check if there is the time overlap
            if other_task.get_start_time()<=self.get_end_time() \
            and self.get_start_time()<=other_task.get_end_time():
                # Both conditions are satisfied return True
                return True
        # if not return False
        return False


    def merge_two_tasks(self, other_task):
        """
        Merge two tasks if the merge is possible.

        Requirement:
        Input validation

        Parameters:
        other_task (Task): The other task to be merged with this task.

        Returns:
        The Task object after merging two tasks, where the new profit is the sum
        of two tasks' profit; otherwise, None is returned.
        """
        # assertion to check the validation of input
        assert type(other_task)==Task
        # By using the function we defined above to check whether other_task
        # can be merged
        if self.can_merge_task(other_task) == True:
            # Find out the new Parameters
            # new_start represents earlier time which is smaller number of
            # two start times
            new_start = min(self.get_start_time(),other_task.get_start_time())
            # new_end represents later time which is bigger number of
            # two end times
            new_end = max(self.get_end_time(),other_task.get_end_time())
            # new_profit is the sum of two progit
            new_profit = self.profit+other_task.profit
            # return the merged Task
            return Task(new_start, new_end, self.focus_level_required, \
                        new_profit, self.task_description)


class PersonalSchedule:
    """
    Implementation of a personal schedule.
    """

    def __init__(self, last_name, first_name, available_time):
        """
        Constructor of PersonalSchedule.

        Requirement:
        Input validation

        Parameters:
        last_name (str): Last name of this person. This string must have at least 2
                        characters.
        first_name (str): First name of this person. This string must have at least 2
                        characters.
        available_time (list[list]): A list of available intervals. Each interval has
                        three elements: [start_time, end_time, focus_level]. You
                        may assume that given intervals don't have overlaps with
                        one another.
        """
        # Assertions to check all inputs are vaild
        name_len = 2
        num_ele = 3
        assert type(last_name)==str and type(first_name)==str
        assert len(first_name) >= name_len and len(last_name) >= name_len
        assert type(available_time)==list
        assert all([isinstance(i, list) for i in available_time])
        assert len(available_time) > 0
        for i in available_time:
            assert i[1] > i[0] >= 0
            assert len(i) == num_ele
            assert all([isinstance(j, int) for j in i])
        # initialize all variables
        self.last_name = last_name
        self.first_name = first_name
        self.available_time = available_time


    def get_last_name(self):
        """Getter for last_name attribute"""
        return self.last_name


    def get_first_name(self):
        """Getter for first_name attribute"""
        return self.first_name


    def get_available_time(self):
        """Getter for available_time attribute"""
        return self.available_time


    def __str__(self):
        """
        String representation of PersonalSchedule.
        """
        return "{} {} is available at {}.".format(self.get_first_name(), \
                self.get_last_name(), self.get_available_time())


    def can_handle(self, task):
        """
        This function determines whether this person can handle the given task.

        Requirement:
        Input validation

        Parameters:
        task (Task): A task that this person needs to handle.

        Returns:
        True if there exists a time interval in the schedule that can properly
        handle the task with the required focus level, False otherwise.
        """
        # assertion to check the vaildation of input
        assert type(task)==Task
        # check whether conditions satisfied with Requirement
        for i in self.available_time:
            # check if there is an interval in avaliable_time where a peropsn
            # can deal with the given task
            if i[0]<=task.start_time and i[1]>= task.end_time:
                # check if the focus_level larger than required
                if i[-1]>=task.focus_level_required:
                    # all satisfied return True
                    return True
        # else return False
        return False


    def can_handle_task_sequence(self, task_sequence):
        """
        Given a list of tasks, this function determines whether this person
        can handle this task sequence.

        Requirement:
        Input validation

        Parameters:
        task_sequence (list[Task]): A list of tasks this person needs to handle.

        Returns:
        True if all tasks can be properly handled, False otherwise. To simplify
        the question, we assume that multitasking is possible, i.e., a person
        can handle multiple tasks in a single time interval.
        """
        # assertion to check the vaildation of input
        assert type(task_sequence)==list
        assert all([isinstance(i, Task) for i in task_sequence])
        # By using the function defined above to check if all tasks in the
        # task_sequence can be handled
        if all(self.can_handle(i) == True for i in task_sequence):
            # all tasks can be handled return True
            return True
        # else return False
        return False


    def most_profitable_task_sequence(self, task_sequences):
        """
        Given a list of task sequences, find all task sequences that give you
        the maximum profit.

        Requirement:
        Input validation

        Parameters:
        task_sequences (list[list]): A list of task sequences.

        Return:
        Sequence(s) of tasks (that a person can handle)  that gives you the most profit.
        """
        # assertion to check the vaildation of input
        assert type(task_sequences)==list
        # create the helper empty dictionary and empty list
        dic = {}
        result = []
        for i in task_sequences:
            # assertion to check the vaildation of input
            assert all([isinstance(i, list)])
            assert all([isinstance(ele, Task) for ele in i])
            # the start profit is 0
            profit = 0
            # check if the task in the list of task sequence can be handled
            if self.can_handle_task_sequence(i) == True:
                for j in i:
                    # if so add the profit and accumulate it
                    profit += j.profit
            # if not skip it
            else:
                continue
            # store all vaild ones into the helper dictionary
            dic[tuple(i)] = profit
        # Find out the max profit
        for key,value in dic.items():
            if value == max(list(dic.values())):
                result.append(list(key))
        # if there is no task_sequence can be completed, return all of them
        if len(result)==0:
            return task_sequences
        return result


    def most_profitable_task_sequence_recursion(self, task_sequences):
        """
        Given a list of task sequences, find all task sequences that give you
        the maximum profit.
        You MUST USE RECURSION in your solution.

        Requirement:
        Input validation

        Parameters:
        task_sequences (list[list]): A list of task sequences.

        Return:
        Sequence(s) of tasks (that a person can handle)  that gives you the most profit.

        """
        # assertion to check the vaildation of input
        assert type(task_sequences)==list
        for i in task_sequences:
            assert all([isinstance(i, list)])
            assert all([isinstance(ele, Task) for ele in i])
        # base case of recursive function indicates the time to stop
        if len(task_sequences) == 1:
            if self.can_handle_task_sequence(task_sequences[0]):
                return task_sequences
            else:
                return []
        # Check from last element to the first to find out the one satisfied
        # Condtion that there is no sequence any more
        if not self.\
            most_profitable_task_sequence_recursion(task_sequences[1:]):
            # condtion that we could handle the first one
            if self.can_handle_task_sequence(task_sequences[0]):
                return task_sequences[:1]
            else:
                return []
        else:
            # condition that  the first one can be handled
            if not self.can_handle_task_sequence(task_sequences[0]):
                return self.\
                    most_profitable_task_sequence_recursion(task_sequences[1:])
            # calculte final profits for both conditions
            profit1 = sum(i.profit for i in task_sequences[0])
            profit2 = sum(i.profit for i in self.\
                most_profitable_task_sequence_recursion(task_sequences[1:])[0])
            # compare them and return the bigger one
            if profit2 > profit1:
                return recursive_sequences
            elif profit2 < profit1:
                return task_sequences[:1]
            else:
                # condition that they are equal
                return task_sequences[:1] + self.\
                    most_profitable_task_sequence_recursion(task_sequences[1:])

    def handle_two_tasks(self, task1, task2):
        """
        Given two tasks, the function determines whether this personal can handle
        them together.

        Requirement:
        Input validation

        Parameters:
        task1 (Task): The first task.
        task2 (Task): The second task.

        Returns:
        True if and only if two tasks can be merged and handled by this PersonalSchedule,
        False otherwise.
        """
        # assertion to check the vaildation of input
        assert type(task1)==Task and type(task2)==Task
        # Check if two tasks can be merged
        if task1.can_merge_task(task2) == True:
            # if so merged these two tasks
            merge_task = task1.merge_two_tasks(task2)
            # check if the merged_task can be handled
            if self.can_handle(merge_task) == True:
                return True
        return False

# END OF FILE #
