# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.

def check_ten(n1,n2):
    # Code Here
        if n1+n2 == 10:
            return True
        else:
            return False

print(check_ten(5,5))
print(check_ten(4,5))
# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1,n2):
    # Code Here
    if n1 + n2 == 10:
        return True
    else:
        return n1 + n2

# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.

def first_upper(mystring):
    ret = mystring.upper()
    ret = ret[0]
    return ret


# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".

def last_two(mystring):
    if len(mystring) < 2:
        return "Error"
    else:
        length = len(mystring)
        retString = mystring[length-2:]
        return retString


# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.

def seq_check(nums):
    Sequence = [1,2,3]
    rightnow = []
    rightnow.append(nums[0])
    rightnow.append(nums[1])
    rightnow.append(nums[2])
    i1 = 0
    i2 = 1
    i3 = 2
    while i3 < len(nums)-1:
        if rightnow == Sequence:
            return True
        else:
            i1 += 1
            i2 += 1
            i3 += 1
            rightnow.clear()
            rightnow.append(nums[i1])
            rightnow.append(nums[i2])
            rightnow.append(nums[i3])
    return False

# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**

def compare_len(s1,s2):
    return abs(len(s1)-len(s2))


# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.

def sum_or_max(mylist):
    if len(mylist)%2==0:
        return sum(mylist)
    else: return max(mylist)


