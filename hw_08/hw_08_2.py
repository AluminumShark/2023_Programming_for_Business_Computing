class Point:
    def __init__(self, cardlist) -> None:
        self.cardlist = cardlist
        pass
    def destring(self):
        for i in range(len(self.cardlist)):
                if self.cardlist[i][1] == "A":
                    self.cardlist[i][1] = 1
                elif self.cardlist[i][1] == "J":
                    self.cardlist[i][1] = 11
                elif self.cardlist[i][1] == "Q":
                    self.cardlist[i][1] = 12
                elif self.cardlist[i][1] == "K":
                    self.cardlist[i][1] = 13
                else:
                    self.cardlist[i][1] = int(self.cardlist[i][1])
        return self.cardlist
    def count(self):
        (self.cardlist).sort(key=lambda x : x[1])
        the_card = 0
        rule_a = 0
        for i in range(len(self.cardlist)):
            if self.cardlist[i][1] == 1:
                rule_a += 1
        rule_b = 0
        for i in range(len(self.cardlist)):
            for j in range(len(self.cardlist)):
                if i < j and self.cardlist[i][1] == self.cardlist[j][1]:
                    rule_b += 1
        rule_c = True
        for i in range(len(self.cardlist)):
            if i == 0:
                the_card = self.cardlist[i]
            elif self.cardlist[i][0] == the_card[0]:
                the_card = self.cardlist[i]
            else:
                rule_c = False
        rule_d = True
        for i in range(len(self.cardlist)):
            if i == 0:
                the_card = self.cardlist[i]
            elif self.cardlist[i][1] == 1 and the_card == 13:
                the_card = self.cardlist[i]
            elif self.cardlist[i][1] == the_card[1] + 1:
                the_card = self.cardlist[i]
            else:
                rule_d = False
        rule_d_test = []
        for i in range(len(self.cardlist)):
            rule_d_test.append(self.cardlist[i][1])
        rule_d_test.sort()
        if rule_d_test == [1, 10, 11, 12, 13] or rule_d_test == [1, 2, 11, 12, 13]\
            or rule_d_test == [1, 2, 3, 12, 13] or rule_d_test == [1, 2, 3, 4, 13]:
            rule_d = True
        rule_e = True
        rule_e_count1 = 0
        rule_e_count2 = 0
        for i in range(len(self.cardlist)):
            if self.cardlist[0][1] == self.cardlist[i][1]:
                rule_e_count1 += 1
            elif self.cardlist[-1][1] ==  self.cardlist[i][1]:
                rule_e_count2 += 1
        if not ((rule_e_count1 == 3 and rule_e_count2 == 2) \
                or (rule_e_count1 == 2 and rule_e_count2 == 3)):
            rule_e = False
        rule_f = False
        rule_f_test = []
        for i in range(len(self.cardlist)):
            rule_f_test.append(self.cardlist[i][1])
        rule_f_test = list(set(rule_f_test))
        if len(rule_f_test) <= 2:
            count1 = 0
            count2 = 0
            for i in range(len(self.cardlist)):
                if rule_f_test[0] == self.cardlist[i][1]:
                    count1 += 1
                elif rule_f_test[1] == self.cardlist[i][1]:
                    count2 += 1
            if count1 == 4 or count2 == 4:
                rule_f = True
            elif count1 == 5 or count2 == 5:
                rule_f = 5
        rule_g = True
        if rule_c == False or rule_d == False:
            rule_g = False
        print_count = 5 * rule_a + rule_b * 10 + rule_c * 30 + rule_d * 50 + rule_e * 80\
        + rule_f * 100 + rule_g * 300
        return print_count
    
def Card(strings):
    suit = strings[0]
    rank = strings[1 : ]
    the_card = [suit, rank]
    return the_card

players = int(input())
players_list = []
for i in range(players):
    player = input().split(",")
    for j in range(len(player)):
        player[j] = Card(player[j])
    players_list.append(player)

count = []
for i in range(len(players_list)):
    point = Point(players_list[i])
    point.destring()
    point = point.count()
    count.append([i, point])
count.sort(key=lambda x : -x[1])
champ = []
for i in range(len(count)):
    if count[i][1] == count[0][1]:
        champ.append(count[i][0] + 1)

champ.sort()
champ = list(map(str, champ))
print(",".join(champ))