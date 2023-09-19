lister = [1,4,4,3,4,6,1,2,3,3,3]
rank = {}
for vrs in lister:
	if vrs in rank.keys():
		rank[vrs] += 1
	else:
		rank[vrs] = 1


highest=list(rank.keys())[list(rank.values()).index(max(list(rank.values())))]
print(highest)