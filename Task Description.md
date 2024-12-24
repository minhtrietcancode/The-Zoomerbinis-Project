## Task 1: Decoding Attributes (3 marks)

Write a function `zbini_attrs(type_id)` that converts a Zoomerbini type ID to a tuple of strings representing the four underlying attributes in the following order: Hair/hat style, favourite colour, fashion accessory and preferred social media platform.

Here are the possible values (as string literals) for each attribute:
- **Hair/Hat**: "wavy", "curly", "cap" or "beanie"
- **Colour**: "red", "blue", "yellow" or "green"
- **Accessory**: "sneakers", "bowtie", "scarf" or "sunglasses"
- **Social**: "tiktok", "instagram", "snapchat" or "discord"

**Mapping Table**: The valid mappings for the attributes are available in the [Zoomerbini Mapping Table](https://2024s1-comp10001-d7ccc59f4734fd6399530ec2572d0fddd929b27d8ca441.pages.gitlab.unimelb.edu.au/). Refer to this table for the corresponding values.

The parameter `type_id` may be assumed to be a numeric whole number value (integer). The returned attributes for a given ID should match those shown in the full mapping table in all cases.
If a `type_id` outside the valid range is given, the function should instead return `None`.

*Hint*: There are multiple ways to solve this problem, but regardless of which one you pick, ensure that it is not overly redundant. In particular, you should be trying to identify pattern(s) in the way that type ID numbers map to Zoomerbini attributes and computing a result based on these in a concise and well structured manner.

### Example Calls:
```python
>>> print(zbini_attrs(0))
('wavy', 'red', 'sneakers', 'tiktok')

>>> print(zbini_attrs(96))
('curly', 'yellow', 'sneakers', 'tiktok')

>>> print(zbini_attrs(351))
None
```

## Task 2: Checking Group Validity (3 marks)

While Zoomerbinis are usually quite amicable with one another, they have a rather specific set of preferences when it comes to forming study groups! Specifically, a study group is valid if for each of the four attributes:
- All members have the same attribute value, or;
- All members have unique attribute values, i.e., no two members share the same attribute value.

Additionally:
- A valid group can only have either 3 or 4 members, and;
- Each member must study at least one subject in common with every other member of the group.

Write a function `valid_study_group(zbinis, group)` that computes the validity of a given study group of Zoomerbinis, as per the above definition.

The parameter `zbinis` will be a list of Zoomerbinis, each represented as a `(type_id, subjects)` tuple, where `type_id` is a Zoomerbini type ID (0 to 255 inclusive) and `subjects` is a list of non-empty strings denoting the subjects the respective Zoomerbini is studying.

The parameter `group` will be a tuple of indices into the `zbinis` list and reflects the group of Zoomerbinis being checked for validity (`zbinis` may be of a different length to `group`). Note that while Zoomerbinis in a group may share the same type IDs, they must be distinct individuals in `zbinis`. In other words, if an index appears more than once in `group`, the group is invalid.

Your function should return a tuple containing two elements:
1. A boolean value denoting the validity of the respective group (`True` if the group is valid or `False` if not).
2. A positive integer representing the number of subjects all members of the group share in common with one another, or otherwise `None` if the group is not valid.

A working version of the `zbini_attrs(type_id)` function from Task 1 has been provided to help you with this task.

### Example Calls:
```python
>>> example_zbinis = [(0, ['FoC', 'Calc 1', 'Logic']), 
                      (108, ['FoA', 'Calc 2', 'Logic']), 
                      (148, ['FoC', 'Calc 1', 'Logic']), 
                      (248, ['FoC', 'Calc 1', 'Logic']), 
                      (0, ['Calc 2', 'History', 'Politics']), 
                      (108, ['FoC', 'Calc 1', 'Logic'])]

>>> valid_study_group(example_zbinis, (0, 1, 3))
(True, 1)

>>> valid_study_group(example_zbinis, (0, 1, 5))
(False, None)

>>> valid_study_group(example_zbinis, (0, 1, 2, 3))
(True, 1)

>>> valid_study_group(example_zbinis, (1, 2, 3, 4))
(False, None)
```

## Task 3: Possible Study Groups (4 marks)

Write a function `possible_study_groups(zbinis)`. The parameter `zbinis` is a list of Zoomerbinis of the same form as in Task 2.

The function should return a list representing all the possible ways a valid study group could be chosen from `zbinis`. Each element is a tuple where:
1. The first element is a tuple of indices representing a group. This tuple should contain exactly three or four unique indices into the `zbinis` list in ascending order.
2. The second element is a score for the group, derived using a "points" system (described below).

For example, if `zbinis` was of length four, there could be up to five tuples of indices in the result with the first element in each being: (0, 1, 2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), and (1, 2, 3).

Each group's score (the second element in each returned tuple) is derived using a "points" system according to the following rules:
- Add three points for each subject shared by all members of the group, and;
- Add one point if the group has three members, or two points if the group has four members.

The returned groups should be sorted in descending order using the above scoring system, that is, higher scored groups should come before lower scored groups in the resulting list.

If there is ever a tie in scores, the group's indices should be used as a tiebreaker. Each index should be considered in turn (left to right) until one facilitates a tiebreak. For example, the grouping (0, 2, 3) should come before (1, 2, 3), and (0, 1, 2) should come before (0, 1, 3).

Groups that are invalid as per the same rules as in Task 2 should be excluded from the returned list altogether. A working version of the respective `valid_study_group(zbinis, group)` function has been provided to help you with this task.

### Example Calls:
```python
>>> print(possible_study_groups([(198, ['FoC']), (138, ['FoC', 'Calc 1']), (14, ['FoC', 'Calc 1']), (66, ['Calc 1'])]))
[((0, 1, 2), 4), ((1, 2, 3), 4)]

>>> print(possible_study_groups([(198, ['FoC']), (138, ['FoC', 'Calc 1']), (14, ['FoC']), (66, ['FoC'])]))
[((0, 1, 2, 3), 5), ((0, 1, 2), 4), ((0, 1, 3), 4), ((0, 2, 3), 4), ((1, 2, 3), 4)]

>>> print(possible_study_groups([(198, ['FoC']), (138, ['Calc 1']), (14, ['Calc 1']), (66, ['FoC'])]))
[]
```

## Task 4: Allocating Study Groups (5 marks)

In this task, you will finally allocate the Zoomerbinis to their study groups!

Write a function `alloc_study_groups(zbinis)` where the parameter `zbinis` is a list of Zoomerbinis, each represented as a `(type_id, subjects)` tuple (this is again of the same form as in the previous two tasks). The function should compute a set of groups of zbinis such that the number of Zoomerbinis without a group is minimised. We call this an optimal grouping.

The return value must be a list of tuples of indices into the `zbinis` list, where each tuple corresponds to a valid group in descending score order (following the same ordering rules as in Task 3). Importantly, a Zoomerbini cannot be allocated to more than one group, that is, any index in the result should appear at most once.

In the case that there are multiple optimal groupings, the grouping with the highest combined score out of these should be returned. This score is computed by summing up all the individual group scores that make up a given grouping (each group should be scored using the same points system as described in Task 3).

If there is still a tie between optimal groupings after considering combined scores, your function should preference the grouping with the smallest minimum index. For example, in the grouping `[(2, 3, 4), (6, 7, 9)]` the minimum index is 2, and hence should be preferred over `[(3, 4, 5), (6, 7, 9)]` which has a minimum index of 3. If more than one optimal grouping has the same minimum index, the second-to-minimum index should be used to tiebreak instead (or the third-to-minimum if there's a tie on both the minimum and second-to-minimum indices, etc). No further tiebreaking beyond this point is required.

Since this is a computationally expensive problem to solve, you may assume the length of `zbinis` will be at most 10. A working version of the `possible_study_groups(zbinis)` function has been provided to help you with this task.

### Example Calls:
```python
>>> print(alloc_study_groups([(198, ['FoC']), (198, ['FoC']), (138, ['FoC']), (14, ['FoC'])]))
[(0, 2, 3)]

>>> print(alloc_study_groups([(198, ['FoC']), (138, ['FoC', 'Calc 1']), (14, ['FoC', 'Calc 1']), (66, ['FoC', 'Calc 1'])]))
[(0, 1, 2, 3)]

>>> print(alloc_study_groups([(198, ['FoC', 'Logic']), (138, ['Calc 1']), (14, ['Calc 1']), (66, ['FoC', 'Logic']), (10, ['FoC', 'Logic']), (142, ['FoC', 'Logic']), (66, ['Calc 1'])]))
[(0, 3, 4, 5), (1, 2, 6)]
```

## Bonus: Many (More) Study Groups

**Note**: This question is optional and for bonus marks only! You can obtain full marks for this project without attempting this question. It is considerably more difficult than the previous questions and intended for students who would like to challenge themselves. 

You may have already discovered that computing an optimal grouping of Zoomerbinis using a naive "brute force" approach (as in Task 4) does not generalise well to larger inputs. This is due to the combinatorial nature of the problem – significantly more time is required for each additional Zoomerbini that is considered.

In this bonus activity, you are tasked with writing an "improved" version of the `alloc_study_groups(zbinis)` function that is able to handle a much higher bound on the possible size of `zbinis` – at least in the hundreds and as many as one thousand!

While all groups must be valid as per the rules outlined in the previous tasks, you do not need to produce an optimal grouping here, since in theory this will be very difficult (if not impossible) without unlimited time. In other words, your function may allocate fewer Zoomerbinis to groups than is theoretically possible for a given input list and still be in the running for bonus marks.

### Assessment Summary
To score your work, a class-wide tournament will be run. Your function will be ranked based on:
- The number of Zoomerbinis successfully allocated to valid groups (more is better).
- The combined scores of the groups returned will be used to break ties.
- If there are further ties, the time taken to compute the result will be used (less time is better).

To be eligible for 2 bonus marks, you need to rank in the top 50 submissions. For 1 bonus mark, you need to rank in the next 150 submissions. Submissions not in the top 200 will not receive any bonus marks.

There is a five-second time limit on an input list of 1000 hidden Zoomerbinis. See the tournament submission page for more detailed information, including submission instructions.
