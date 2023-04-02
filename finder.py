# find all instances of given strings within input
def finder(input_string: str, to_find: list[str], to_verify: list[bool]) -> list[int]:
    # all found positions, grouped by word
    instances = []
    input_string = input_string.lower()

    # iterate over all words to find
    for idx, current_string in enumerate(to_find):
        # account for all foung instances for current word
        current_string = current_string.lower()
        current_instances = []
        current_idx = 0

        # loop over all indices in input string
        while current_idx < len(input_string):
            # current word to find is valid
            if current_idx + len(current_string) - 1 < len(input_string):
                # word is found
                if input_string[current_idx:current_idx+len(current_string)] == current_string:
                    # if word can be substring, add found index
                    if to_verify[idx] is False:
                        current_instances.append(current_idx)
                    # if word cannot be substring, verify independence + add found index
                    else:
                        if verify_word(input_string, current_string, current_idx):
                            current_instances.append(current_idx)

                # go to next position
                current_idx += 1
            # invalid word
            else:
                break

        # add found indices for current word to ledger
        instances.append(current_instances)

    # done!
    return instances


# check if word is separated
def verify_word(input_string: str, current_string: str, current_idx: int) -> bool:
    # boundary conditions: word is at start, middle, or end (all cases, by itself)
    # check start idx
    if current_idx == 0:
        # start and end match
        if len(input_string) == len(current_string):
            return True
        # start matches, end doesn't:
        elif input_string[current_idx+len(current_string)] == ' ':
            return True
    # start idx is not 0 (check before and after word)
    else:
        # string is set apart at end, and portion after is valid
        if input_string[current_idx - 1] == ' ':
            # portion of string afterwards is followed by space
            if current_idx + len(current_string) < len(input_string):
                # space found
                if input_string[current_idx+len(current_string)] == ' ':
                    return True
            # end of input string
            else:
                return True

    # invalid condition, some boudary condition failed
    return False
