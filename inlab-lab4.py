def recursiveMinimum(data):
        if len(data) == 0:
                return None
        if len(data) == 1:
                return data[0]
        return min(data[0], recursiveMinimum(data[1:]))

def recursiveMaximum(data):
        if len(data) == 0:
                return None
        if len(data) == 1:
                return data[0]
        return max(data[0], recursiveMaximum(data[1:]))

def recursiveRev(data):
        if len(data) <= 1:
                return data
        return recursiveRev(data[1:]) + [data[0]]

print(recursiveMinimum([30, 2, 43, 25, 78, 67,100,867,943]))
print(recursiveMaximum([30, 2, 43, 25, 78, 67,100,867,943]))
print(recursiveRev([30, 2, 43, 25, 78, 67,100,867,943]))

