def calculate_structure_sum(data_structure):
    total = 0
    for item in data_structure:
        if isinstance(item, (int)):
            total += item
        elif isinstance(item, str):
            total += len(item)
        elif isinstance(item, (list, tuple, set)):
            total += calculate_structure_sum(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(key, (int)):
                    total += key
                elif isinstance(key, str):
                    total += len(key)
                if isinstance(value, (int)):
                    total += value
                elif isinstance(value, str):
                    total += len(value)
                elif isinstance(value, (list, tuple, dict)):
                    total += calculate_structure_sum([value])
    return total
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)