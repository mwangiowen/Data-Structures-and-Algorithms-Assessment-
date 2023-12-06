def remove_dup(sequence):
    seen = set()
    result = []

    for element in sequence:
        if element not in seen:
            result.append(element)
            seen.add(element)

    return result


input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_dup(input_sequence)
print(result)  
