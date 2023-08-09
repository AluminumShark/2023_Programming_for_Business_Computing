m_work1_work2 = input().split(",")
bird = input().split(",")
trad = input().split(",")
employ = list()
output_str = str()

for i in range(len(m_work1_work2)) :
    m_work1_work2[i] = int(m_work1_work2[i])
for j in range(len(bird)) :
    bird[j] = int(bird[j])
    trad[j] = int(trad[j])

for k in range(len(bird)) :
    pine = (bird[k] * 4) + (trad[k] * 3)
    egg = (bird[k] * 2) + (trad[k] * 3)
    empoly_t = (pine // m_work1_work2[1]) + (egg // m_work1_work2[2]) + bool(pine % m_work1_work2[1]) + bool(egg % m_work1_work2[2])
    employ.append(empoly_t)

for m in range(len(employ)) :
    if (m + 1) == len(bird) :
        output_str += str(employ[m])
    else :
        output_str += str(employ[m]) + ","

print(output_str)