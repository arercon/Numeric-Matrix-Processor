def build_m():
    dim = input().split()
    matrix = []
    for i in range(int(dim[0])):
        row = input().split()
        row = list(map(int, row))
        matrix.append((row))
    return matrix

def sum_m():
    m1 = build_m()
    m2 = build_m()
    if len(m1[0]) == len(m2[0]):
        result = [[m1[i][j] + m2[i][j]  for j in range
        (len(m1[0]))] for i in range(len(m1))]
        for r in result:
            print(" ".join(map(str,r)))
    else:
        print("ERROR")



sum_m()
