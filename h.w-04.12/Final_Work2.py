# Ex 8:
student = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'],
}


# 1.
def print_student_data(student: dict) -> None:
    """
    Prints all the properties of the student object.
    Each property is displayed on a new line.

    Param:
    student - The student object containing properties to print.
    """
    for key, value in student.items():
        print(f"{key}: {value}")


print_student_data(student)


# 2.
def add_hobby(student: dict, hobby: str) -> None:
    """
    Adds a new hobby to the student's hobbies list.
    If the hobby already exists in the list, it will not be added again.

    Param:
    student - The student object containing a 'hobbies' list.
    hobby - The hobby to add to the hobbies list.
    """
    if hobby not in student['hobbies']:
        student['hobbies'].append(hobby)


# 3.
"""
Adding a new hobby and printing student data
"""
add_hobby(student, 'dancing')
print_student_data(student)


# 4.
def delete_hobby(student: dict, hobby: str) -> None:
    """
    Removes a specific hobby from the student's hobbies list.
    If the hobby does not exist in the list, no changes are made.

    Parameters:
    student - The student object containing a 'hobbies' list.
    hobby - The hobby to remove from the hobbies list.
    """
    if hobby in student['hobbies']:
        student['hobbies'].remove(hobby)


# 5.
"""
Deleting a hobby and printing student data
"""
delete_hobby(student, 'reading')
print_student_data(student)

# 6.
"""
Adding a new property to the student object: family_name and adding a value
"""
student['family_name'] = 'shaham'
print_student_data(student)


# Ex 9:
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]


def print_matrix(matrix: list) -> None:
    """
    Prints all the elements of a 2D list (matrix) in a single line.

    Param:
    matrix (list): A 2D list (list of lists) containing the matrix elements.

    Returns:
    None
    """
    for list in matrix:
        for item in list:
            print(item, end=" ")
    print()


print_matrix(matrix)


# Ex 10:
matrix = [
    [0, 1, 1],
    [0, 1, 0],
    [1, 0, 0]
]


def zero_count(matrix: list) -> int:
    """
    Counts how many zeros appear in the 2D matrix.

    Param:
    matrix (list): A 2D list (list of lists) containing the matrix elements.

    Returns:
    int: The count of zeros in the matrix.
    """
    count = 0
    for list in matrix:
        for num in list:
            if num == 0:
                count += 1
    return count


print(zero_count(matrix))


# Ex 11:
arr = [4, 2, 34, 4, 1, 12, 1, 4]


def find_dup(arr: list) -> list:
    """
    Returns an array of elements that are repeated more than once in the given array.

    Param:
    arr (list): The input array to check for repeated elements.

    Returns:
    list: A list of elements that appear more than once in the array.
    """
    count = {}
    dupl = []

    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num, nums in count.items():
        if nums > 1:
            dupl.append(num)

    return dupl


print(find_dup(arr))


# Ex 12:
arr = [43, "what", 9, True, "cannot", False, "be", 3, True]


def reverse_array(arr: list) -> list:
    """
    Returns a new array with the elements from the given array in reverse order.

    Param:
    arr (list): The input array to reverse.

    Returns:
    list: A new array with the elements in reverse order.
    """
    reversed_arr = []

    for element in arr:
        reversed_arr.insert(0, element)

    return reversed_arr


print(reverse_array(arr))


# Ex 13:
first_array = [4, 6, 7]
second_array = [8, 1, 9]


def sum_arrays(first_array: list, second_array: list) -> list:
    """
    Adds up each element from the two given arrays at the same position
    and returns a new array containing the sum of each pair.

    Param:
    first_array (list): The first input array of integers.
    second_array (list): The second input array of integers.

    Returns:
    list: A new array containing the sum of elements at each position.
    """
    summed_array = []

    for x, y in zip(first_array, second_array):
        summed_array.append(x + y)

    return summed_array


print(sum_arrays(first_array, second_array))


# Ex 14:
first_str = "racecar"
second_str = "Java"


def tail_head(word: str = ' ') -> bool:
    """
    Checks if a string is a palindrome.

    A palindrome is a word or phrase that reads the same backward as forward.

    Param:
    word : str
        The word to check (default: an empty string).

    Returns:
    bool
        True if the word is a palindrome, otherwise False.
    """
    reverse_word = word[::-1]
    return word == reverse_word


print(tail_head(first_str))
print(tail_head(second_str))


# Ex 15:
counter = 1

while counter < 100:
    print(counter, end=' ')
    counter += counter
print()


# Ex 16:
counter = 900000

while counter > 50:
    print(f'{counter:.2f}', end=', ')
    counter = counter / 2
    if counter < 51:
        break
print()


# Ex 17:
words = ["apple", "apple", "danny", "apple", "danny", "danny", "apple"]


def find_duplicates(words: list) -> list:
    """
   get a list of words
   create a dict
   iterate over all of the words:
   each word check if exist in the dict
   "danny", "apple", "danny"
      if not -> store in the dict {key-word: value-counter}
              counter = 1
      if word already exist in the dict then + 1 its counter
   final result:  { "danny": 2, "apple": 1}
    { "danny": 2, "apple": 1 }

    -- [("apple", 1), ("danny", 2)]
    result = []
    for key, value in dict_counter.items():
      if value > 1:
        result.append(key)
    """
    dict_counter = {}
    i = 0
    while i < len(words):
        word = words[i]
        if word in dict_counter:
            dict_counter[word] += 1
        else:
            dict_counter[word] = 1
        i += 1

    result = []
    for key, value in dict_counter.items():
        if value > 1:
            result.append((key, value))

    return result


result = find_duplicates(words)
print(result)
