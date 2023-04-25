unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    print_value = unprinted_designs.pop()
    completed_models.append(print_value)
    print(print_value)

print(completed_models)
