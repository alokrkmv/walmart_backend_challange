# Parse the input filr and create a dictionary of input data
def parse_file(filereader):
    """
    Parse a file and return a list of lines.
    """
    input_dict = {}
    for line in filereader:
        line = line.strip()
        if line:
            key, value = line.split(' ')
            input_dict[key] = int(value)
    return input_dict