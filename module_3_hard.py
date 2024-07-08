def calculate_structure_sum(structure):
    count = 0
    if isinstance(structure, int):
        count += structure
    if isinstance(structure, float):
        count += structure
    if isinstance(structure, str):
        count += len(structure)
    if isinstance(structure, list):
        for i in range(0, len(structure)):
            count += calculate_structure_sum(structure[i])
    if isinstance(structure, tuple):
        for i in range(0, len(structure)):
            count += calculate_structure_sum(structure[i])
    if isinstance(structure, set):
        listed_structure = list(structure)
        for i in range(0, len(listed_structure)):
            count += calculate_structure_sum(listed_structure[i])
    if isinstance(structure, dict):
        listed_dict = list(structure.items())
        for i in range(0, len(listed_dict)):
            count += calculate_structure_sum(listed_dict[i])
    return count


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))


