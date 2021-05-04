score = {'1학기':100, '2학기':50, '3학기':88, '4학기':99}
print(score['2학기'])

for x in score:
    if score[x] >= 85:
        print(x, score[x])