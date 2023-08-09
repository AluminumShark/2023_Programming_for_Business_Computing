hw, pbc = map(int, input().split(","))
hw_point = list(map(int, input().split(",")))
pbc_point = list(map(int, input().split(",")))

hw_t = 0
pbc_t = 0

for i in range(hw) :
    hw_t += hw_point[i]
for j in range(pbc) :
    pbc_t += pbc_point[j]

hw_e = hw_t / hw
pbc_e = pbc_t / pbc
out = 0

if hw_e > pbc_e :
    out = 1
elif hw_e < pbc_e :
    out = 2
elif hw_e == pbc_e :
    out = 0

print(out)