def det(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError
    m = matrix
    r = 0
    if len(matrix) == 2:
        return ((m[0][0]) * (m[1][1])) - ((m[1][0]) * (m[0][1]))
    else:
        u = 1
        for x in range(len(m)):
            smaller = []
            for y in range(1, len(m)):
                sa = []
                for z in range(len(m)):
                    if z != x:
                        sa.append(m[y][z])
                smaller.append(sa)
            r = r + u*det(smaller)*m[0][x]
            u = u*-1
    return r


