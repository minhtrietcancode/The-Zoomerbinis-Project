from itertools import combinations
from hidden import valid_study_group

def calculate_group_score(group_size, num_common_subjects):
    """
    Calculates the score for a group based on its size and the number of common subjects.
    
    Args:
    - group_size: An integer representing the size of the group.
    - num_common_subjects: An integer representing the number of common subjects in the group.
    
    Returns:
    - An integer representing the score of the group.
    """
    return num_common_subjects * 3 + (1 if group_size == 3 else 2)

def possible_study_groups(zbinis):
    """
    Takes a list of tuples, each tuple contains an integer representing a zbini
    attribute and a list of strings representing the subjects taken by that 
    zbini.

    Returns a list of tuples, where each tuple contains a tuple of integer 
    indices representing a valid study group, and an integer score for 
    that group.

    The returned list is sorted by the group score in descending order, and 
    then by the group indices in ascending order.
    """
    possible_groups = []

    # Generate all combinations of indices with lengths 3 or 4
    for group_size in range(3, 5):
        for group_index in combinations(range(len(zbinis)), group_size):
            # Check if the combination forms a valid study group
            valid, num_common_subjects = valid_study_group(zbinis, group_index)
            if valid:
                # Calculate the score for the group
                score = calculate_group_score(group_size, num_common_subjects)
                # Convert the valid group and its score to possible_groups list 
                possible_groups.append((group_index, score))

    # Sort the possible groups by score in descending order
    possible_groups.sort(key=lambda x: (-x[1], x[0]))

    return possible_groups
