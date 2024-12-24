from hidden import zbini_attrs

def count_common_elements(subjects):
    """
    Takes a list of lists, each list represents the subjects that a Zoomerbini
    learns, and returns an integer which is the number of common subjects that 
    all the lists have.
    """
    # Creating the intersection of the sets of all subject lists
    common_elements = set.intersection(*(set(lst) for lst in subjects))
    return len(common_elements) if common_elements else 0

def extract_group_attributes(zbinis, group):
    """
    Extracts attributes for each Zbini in the group.
    
    Args:
    - zbinis: a list of tuples, each tuple contains an integer representing 
      the type_id of a Zoomerbini and a list of subjects learned by that Zoomerbini.
    - group: a tuple containing integers which are the indices of Zoomerbinis.
    
    Returns:
    - A list of attribute lists for each Zbini in the group.
    """
    return [zbini_attrs(zbinis[idx][0]) for idx in group]

def extract_group_subjects(zbinis, group):
    """
    Extracts subjects for each Zbini in the group.
    
    Args:
    - zbinis: a list of tuples, each tuple contains an integer representing 
      the type_id of a Zoomerbini and a list of subjects learned by that Zoomerbini.
    - group: a tuple containing integers which are the indices of Zoomerbinis.
    
    Returns:
    - A list of subject lists for each Zbini in the group.
    """
    return [zbinis[idx][1] for idx in group]

def check_same_or_different_attributes(group_attrs):
    """
    Checks if each of the four attributes in all Zoomerbinis is the same or different.
    
    Args:
    - group_attrs: A list of attribute lists for each Zbini in the group.
    
    Returns:
    - A boolean indicating whether all attributes are either the same or different.
    """
    attr_lists = [[attr[attr_idx] for attr in group_attrs] for attr_idx in range(4)]
    return all(len(set(attr_list)) in (1, len(attr_list)) for attr_list in attr_lists)

def check_valid_group_size(group):
    """
    Checks if the group size is 3 or 4.
    
    Args:
    - group: a tuple containing integers which are the indices of Zoomerbinis.
    
    Returns:
    - A boolean indicating whether the group size is valid.
    """
    return len(group) in (3, 4)

def check_common_subjects(group_subjects):
    """
    Checks if there is at least one common subject among the group.
    
    Args:
    - group_subjects: A list of subject lists for each Zbini in the group.
    
    Returns:
    - A boolean indicating whether there is at least one common subject.
    """
    return count_common_elements(group_subjects) != 0

def check_no_duplicates(group):
    """
    Checks if there are no duplicate Zbini IDs in the group.
    
    Args:
    - group: a tuple containing integers which are the indices of Zoomerbinis.
    
    Returns:
    - A boolean indicating whether there are no duplicate Zbini IDs.
    """
    return len(set(group)) == len(group)

def valid_study_group(zbinis, group):
    """
    Takes zbinis: a list of tuples, each tuple contains an integer representing 
    the type_id of a Zoomerbini and a list of subjects learned by that 
    Zoomerbini, and group: a tuple containing integers which are the indices 
    of Zoomerbinis.

    Returns a tuple containing a bool value indicating whether the group is
    valid, and the number of common subjects if the group is valid, or None
    otherwise.
    """
    group_attrs = extract_group_attributes(zbinis, group)
    group_subjects = extract_group_subjects(zbinis, group)

    same_or_different_attrs = check_same_or_different_attributes(group_attrs)
    valid_group_size = check_valid_group_size(group)
    has_common_subjects = check_common_subjects(group_subjects)
    no_duplicates = check_no_duplicates(group)

    valid = (same_or_different_attrs and valid_group_size
             and has_common_subjects and no_duplicates)

    if valid:
        return (True, count_common_elements(group_subjects))
    else:
        return (False, None)
