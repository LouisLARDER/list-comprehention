'''
list comprehension
'''
# squares = []
# for x in range(10):
#    squares.append(x ** 9)

# print(squares)  

# print ([x ** 2 for x in range (10)])


'''
conditionals in list comprehension
'''
# combs = []
# for x in [1,2,3]:
#    for y in [3,2,5]:
#       if x != y:
#          combs.append((x,y))

# print(combs)

# print([(x,y) for x in [1,2,3] for y in  [3,2,5] if x !=y])

'''
nested list comprehension
'''

# matrix = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]

# res = [[row[i]for row in matrix] for i in range(4)]
# print(res)

#=====================================

# matrix = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]

# res = []
# for i in range(4):
#    res.append([row[i] for row in matrix])

# print(res)

# matrix = [
#   [1,2,3,4,8],
#   [5,6,7,8,9],
#   [9,10,11,12,56]
# ]

# res = []
# for k in range(5):
#    res_row = []
#    for row in matrix:
#       res_row.append(row[k])
#    res.append(res_row)

# print(res)