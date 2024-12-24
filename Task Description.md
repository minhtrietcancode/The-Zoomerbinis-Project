# Define the content for the Task Description markdown

task_description = """
# Task Description

## Task 1: Decoding Attributes (3 marks)

Write a function `zbini_attrs(type_id)` that converts a Zoomerbini type ID to a tuple of strings representing the four underlying attributes in the following order: Hair/hat style, favourite colour, fashion accessory, and preferred social media platform. 

Here are the possible values (as string literals) for each attribute:
- Hair/Hat: "wavy", "curly", "cap", or "beanie"
- Colour: "red", "blue", "yellow", or "green"
- Accessory: "sneakers", "bowtie", "scarf", or "sunglasses"
- Social: "tiktok", "instagram", "snapchat", or "discord"

The parameter `type_id` may be assumed to be a numeric whole number value (integer). The returned attributes for a given ID should match those shown in the full mapping table in all cases. If a `type_id` outside the valid range is given, the function should instead return `None`.

**Hint**: There are multiple ways to solve this problem, but regardless of which one you pick, ensure that it is not overly redundant. In particular, you should be trying to identify pattern(s) in the way that type ID numbers map to Zoomerbini attributes and computing a result based on these in a concise and well-structured manner.

### Example Calls:

```python
>>> print(zbini_attrs(0))
('wavy', 'red', 'sneakers', 'tiktok')
>>> print(zbini_attrs(96))
('curly', 'yellow', 'sneakers', 'tiktok')
>>> print(zbini_attrs(351))
None

