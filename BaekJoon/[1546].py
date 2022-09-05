import sys

n = int(input())
score_list = list(map(int, sys.stdin.readline().split()))
max_score = max(score_list)

new_list = []

for i in score_list:
  new_list.append(i/max_score * 100)
  
test_avg = sum(new_list)/n

print(test_avg)

