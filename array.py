# 配列の操作
list_a = ['dog', 'cat', 'tiger', 'horse', 'monkey']
print(list_a[2:4])
# ['tiger', 'horse']

list_a[3] = 'elephant'
print(list_a)

list_b = ['dog', 'cat', 'tiger']
list_b.append('house')
list_b.append('monkey')
print(list_b)

# delete elements
list_b[1:3]=[]
print(list_b)

list_c = [[2, 4, 6], ['dog', 'cat', 'tiger']]
print(len(list_c))
# 2
print(list_c[1][2])
# tiger
list_d = [[2, 4, 6], ['dog', 'cat', 'tiger', [100, 200, 300]]]
print(list_d[1][3][2])
# 300



