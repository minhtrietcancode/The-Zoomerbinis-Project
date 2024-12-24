from itertools import combinations

def get_type_id(type_id):
    """
    Converts the type_id of a Zoomerbini into a list of four type identifiers.
    
    Args:
    - type_id: An integer representing the type_id of a Zoomerbini.
    
    Returns:
    - A list of integers, each representing one of the four type identifiers.
    """
    type_ids = []
    for _ in range(4):
        rm = type_id % 4
        type_ids.append(rm)
        type_id //= 4
    return type_ids

def check_valid_group_ids(group, zbinis):
    """
    Checks if the given group of Zoomerbinis has valid type identifiers.
    
    Args:
    - group: A tuple containing the indices of Zoomerbinis in the group.
    - zbinis: A list of tuples, each tuple contains an integer representing 
      the type_id of a Zoomerbini and a list of subjects learned by that Zoomerbini.
    
    Returns:
    - A boolean indicating whether the group has valid type identifiers.
    """
    c = ["" for _ in range(4)]
    valid_lists = ["0000", "1111", "2222", "3333", "0123", "000", "111", 
                   "222", "333", "012", "013", "023", "123"]
    for idx in group:
        type_id = zbinis[idx][0]
        type_ids = get_type_id(type_id)
        for i in range(4):
            c[i] += str(type_ids[i])
    for pattern in c:
        if ''.join(sorted(pattern)) not in valid_lists:
            return False
    return True

def calculate_group_score(group):
    """
    Calculates the score for a group based on its size and the number of common subjects.
    
    Args:
    - group: A tuple containing the indices of Zoomerbinis in the group.
    
    Returns:
    - An integer representing the score of the group.
    """
    return len(group) * 3 + (1 if len(group) == 3 else 2)

def alloc_study_groups(zbinis):
    """
    Allocates Zoomerbinis into valid study groups.
    
    Args:
    - zbinis: A list of tuples, each tuple contains an integer representing 
      the type_id of a Zoomerbini and a list of subjects learned by that Zoomerbini.
    
    Returns:
    - A list of tuples, each tuple contains the indices of Zoomerbinis in a valid study group.
    """
    output = []
    checked_ids = set()
    subjects = {}

    # Create a dictionary where keys are subjects and values are lists of zbini indices
    for zbini_id, zbini in enumerate(zbinis):
        for subject in zbini[1]:
            if subject not in subjects:
                subjects[subject] = []
            subjects[subject].append(zbini_id)

    # Sort subjects based on the number of zbini indices (smallest to largest)
    subjects = dict(sorted(subjects.items(), key=lambda item: len(item[1])))

    for subject in subjects:
        id_list = subjects[subject]
        id_set = set(id_list)
        for idx in id_list:
            if idx in checked_ids:
                id_set.remove(idx)
        if len(id_set) <= 2:
            continue

        id_list = list(id_set)
        
        # Check for valid groups of size 4
        for group in combinations(id_list, 4):
            if all(idx not in checked_ids for idx in group) and check_valid_group_ids(group, zbinis):
                checked_ids.update(group)
                output.append(group)

        # Check for valid groups of size 3
        for group in combinations(id_list, 3):
            if all(idx not in checked_ids for idx in group) and check_valid_group_ids(group, zbinis):
                checked_ids.update(group)
                output.append(group)

    return output
