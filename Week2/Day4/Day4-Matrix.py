def clean_input(matrix_input):
    # We don't know what the input looks like, let's make sure it's valid.
    cleaned_intput = []
    for line in matrix_input.split("\n"):
        clean_line = line.lstrip()
        if clean_line != "":
            cleaned_intput.append(clean_line)

    return "\n".join(cleaned_intput)


def create_matrix(matrix_input_string):
    # Assuming we have a valid input, convert it into a matrix (list of lists)
    matrix_input_string = clean_input(matrix_input_string)
    rows = matrix_input_string.split("\n")
    real_matrix = []
    for num in range(3):
        real_matrix.append([char[num] for char in rows])
    return real_matrix


def decode_matrix(matrix_input_string):
    #
    real_matrix = create_matrix(matrix_input_string)
    result = []
    last_token = ""
    for column in real_matrix:
        for char in column:
            if char.isalpha():
                # one of two could happen:
                # 1. Last token was a group of non-alpha, so we add space and add our char
                # 2. Last token was start of string/alpha/non-alpha - all the same. We just add the char.
                if last_token == "group-of-non-alpha":
                    result.append(" ")
                    result.append(char)
                else:
                    result.append(char)
                last_token = "alpha"
            else:
                if last_token == "group-of-non-alpha":
                    # last was a group, for example: ($#), and now ^. Last token didn't change.
                    last_token = "group-of-non-alpha"
                elif last_token == "non-alpha":
                    # last was a single token: ($) and now #. Last token should change to group.
                    last_token = "group-of-non-alpha"
                else:
                    # last was either char or start of string: ("") and now 7, or (r) and then 3
                    last_token = "non-alpha"

    return "".join(result)


if __name__ == "__main__":
    data = """
    7i3
    Tsi
    h%x
    i #
    sM 
    $a 
    #t%
    ^r!
    """
    data = clean_input(data)
    print(decode_matrix(data))
