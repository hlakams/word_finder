# find all instances of given strings within input
def finder(input_string: str, to_find: list[str]) -> list[int]:
    instances = []
    input_string = input_string.lower()
    
    for current_string in to_find:
        current_string = current_string.lower()
        current_instances = []
        current_idx = 0

        while current_idx < len(input_string):
            if current_idx + len(current_string) <= len(input_string):
                if input_string[current_idx:current_idx+len(current_string)] == current_string:
                    current_instances.append(current_idx)
                current_idx += 1
            else:
                break
        
        instances.append(current_instances)

    return instances