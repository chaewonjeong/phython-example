empty = []        # Create an empty list
print(len(empty))  # the length of a list
xs = [3, 1, 2]    # Create a list of length 3
print(len(xs))

print(xs[0])  # indexing
print(xs[1])
print(xs[2])

xs[0] = 5

print(xs[-1])     # Negative indices count from the end of the list; prints "2"
print(xs[-2])
print(xs[-3])

xs[2] = ['1', '2']
print(type(xs[0]))
