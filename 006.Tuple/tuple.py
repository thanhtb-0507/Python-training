empty_tuple = ()
hmm = (1, 2, 3)

# hmm[-2:] = []
# print(hmm)
# 'tuple' object does not support item assignment

print(hmm[-2:3])
# (2, 3)

hmm = hmm * hmm[2]
print(hmm.count(1))
# 3

print(hmm.index(3))
# 2

print(1 in hmm)
# True

print(4 in hmm)
# False

umm = hmm, [1, 2, 3]
print(umm)
# ((1, 2, 3, 1, 2, 3, 1, 2, 3), [1, 2, 3])

umm[1][1] = 'hmm?'
print(umm)
# ((1, 2, 3, 1, 2, 3, 1, 2, 3), [1, 'hmm?', 3])

umm[1].append(4)
print(umm)
# ((1, 2, 3, 1, 2, 3, 1, 2, 3), [1, 'hmm?', 3, 4])

# umm[1] = []
# TypeError: 'tuple' object does not support item assignment

print("len(hmm) = ", len(hmm)) # = 9
print("len(umm) = ", len(umm)) # = 2

