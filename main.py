def find(data, index, arr, sm):
    if index < len(data):
        if data[index] is not None:
            arr.append(data[index])
            if sum(arr) == sm and find(data, index * 2 + 1, arr.copy(), sm) and find(data, index * 2 + 2, arr.copy(),
                                                                                     sm):
                print('->'.join([str(elem) for elem in arr]))
                return False
            else:
                find(data, index * 2 + 1, arr.copy(), sm)
                find(data, index * 2 + 2, arr.copy(), sm)
                return False
        else:
            return True
    else:
        return True


print("enter a string with node values:")
s = input()
print("enter a sum:")
n = int(input())
nodes = []
for el in s.split(','):
    if el == '':
        nodes.append(None)
    else:
        nodes.append(int(el))
ln = 1
ln1 = 1
for i in range(len(nodes)):
    if i == ln:
        ln1 *= 2
        ln += ln1
    if nodes[i] is None and i * 2 + 1 >= ln and len(nodes) > ln:
        nodes.insert(i * 2 + 1, None)
        nodes.insert(i * 2 + 2, None)
find(nodes, 0, [], n)
