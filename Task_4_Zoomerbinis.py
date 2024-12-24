from hidden import possible_study_groups
from itertools import combinations

def is_valid(group_combination):
    """
    Takes group_combination (List[Tuple[int, ...]]) : A list of tuples 
    representing the group combination.

    Return boolen value with True if the given group combination is valid by 
    ensuring that each integer index appears only once across all tuples in 
    the combination and False otherwise 
    """
    # Flatten the group_combination into a list of individual elements
    flattened_group = [char for tup in group_combination for char in tup]

    # Check if the count of unique elements is equal to the
    # total count of elements
    count_element = len(flattened_group)
    count_unique_num = len(set(flattened_group))

    return count_element == count_unique_num

def three_smallest_indices(group_combination):
    """
    Takes group_combination (List[Tuple[int, ...]]) : A list of tuples 
    representing the group combination.

    Returns a list of three smallest integer indices present in the given group
    combination.
    """
    # Flatten the group_combination into a list of individual elements
    flattened_group = [char for tup in group_combination for char in tup]

    # Sort the flattened list and return the first three elements
    sorted_indices = sorted(flattened_group)
    return sorted_indices[:3]

def alloc_study_groups(zbinis):
    """
    Takes zbinis (List[Tuple[int, List[str]]]) : A list of tuples, where each 
    tuple contains an integer representing a zbini attribute and a list of 
    strings representing the subjects taken by that zbini.

    Allocates the best study groups for the given list of zbinis.

    Returns a list containing tuples of integer indices representing the best
    study groups based on its length, its socre and its three smallest indices
    """
    # Create a dictionary to store the score for each group Zbini type
    valid_group_score = {element[0]: element[1]
                         for element in possible_study_groups(zbinis)}

    # Get all of the valid group index : List[Tuple(ints)]
    valid_group = [element[0] for element in possible_study_groups(zbinis)]

    # Generate all unique combinations of tuples of valid group 
    possible_group_combinations = []

    # Get the maximum size of group combinations
    # based on the minimum group size (3)
    max_size_combinations = len(zbinis) // 3

    # Generating size of group combinations
    for combination_size in range(1, max_size_combinations + 1):
        # Creating combinations based on all valid groups and combination size
        for group_combination in combinations(valid_group, combination_size):
            # If the combination is valid, converting it to the possible group
            # combinations list
            if is_valid(group_combination):
                possible_group_combinations.append(list(group_combination))

    # If no valid groups can be formed, return an empty list
    if not possible_group_combinations:
        return []

    # Sorting groups by length and total score in decreasing order, after that
    # sorting groups based on three smallest indices
    possible_group_combinations.sort(key=lambda x:
                                    # Sorting based on length of combinations
                                    (-sum(len(tup) for tup in x),
                                     # Sorting based on score of combinations
                                     -sum(valid_group_score[tup] for tup in x),
                                     # Sorting based on three smallest indices
                                     three_smallest_indices(x)[0],
                                     three_smallest_indices(x)[1],
                                     three_smallest_indices(x)[2],))

    # Selecting the best group
    best_group = possible_group_combinations[0]

    return best_group