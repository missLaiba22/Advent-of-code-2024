#puzzle  1
from collections import Counter
with open("/content/day1.txt","r") as file:
  left_list=[]
  right_list=[]

  for line in file:
    left,right=map(int,line.split())
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()
total_distance= sum(abs(l-r)for l, r in zip(left_list, right_list))
print("total distance",total_distance)

#puzzle  2
right_counts=Counter(right_list)
similarity_score = sum(num * right_counts.get(num, 0) for num in left_list)

# Print the similarity score
print("Similarity Score:", similarity_score)
