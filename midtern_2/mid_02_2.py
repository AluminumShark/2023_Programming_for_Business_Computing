water_line = list(map(float, input().split(",")))
k1 = int(input())
k2 = int(input())
if k1 < 1 : k1 = 2
if k2 < 1 : k2 = 2

def find_trought(water_line, k1 = 2, k2 = 2):
    trought = []
    for i in range(k1, len(water_line) - k2 + 1):
        former = water_line[i - k1 : i + 1]
        later = water_line[i : i + k2 + 1]
        former_down = former == sorted(former, reverse=True)
        later_up = later == sorted(later)
        not_dupli = len(set(former)) == len(former) and len(set(later)) == len(later)
        if former_down and later_up and not_dupli and len(later) > 1:
            trought.append(i)
    
    return trought

output = find_trought(water_line, k1, k2)

if output == [] :
    print("NA")
else :
    for i in range(len(output)) :
        print(output[i])