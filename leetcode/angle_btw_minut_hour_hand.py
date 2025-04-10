def angle(hour, mint):
    a = abs((5.5*mint - 30*hour))
    return min(a, 360-a)

print(angle(12,0))
print(angle(12,30))
print(angle(9,15))
print(angle(0,30))
print(angle(6,0))
