def zbini_attrs(type_id):
    """
    Take type_id: an integer and returns a tuple of four attributes of 
    the Zoomerbinis with that type_id 
    """
    # Check if type_id is out of the valid range
    if type_id < 0 or type_id > 255:
        return None

    # Define the attribute options
    attributes = [
        # Hair/hat
        ["wavy", "curly", "beanie", "cap"],
        # Colour
        ["red", "blue", "yellow", "green"],
        # Accessory
        ["sneakers", "bowtie", "sunglasses", "scarf"],
        # Social
        ["tiktok", "instagram", "discord", "snapchat"]
    ]

    # Calculate the indices for each attribute
    indices = [(type_id // (4 ** (3 - i))) % 4 for i in range(4)]

    # Retrieve the attributes using the calculated indices
    return tuple(attributes[i][index] for i, index in enumerate(indices))