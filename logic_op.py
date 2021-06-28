print(2<3 and 5>2 and 6<89)
print(all([2<3,5>2,6<89]))
print(all([2<3,5>2,6==89]))

print(2<3 or 5==2 or 6<89)
print(2==3 or 5==2 or 6==89)
print(any([2<3,5>2,6==89]))

print(not all([2<3,5>2,6==89]))
print(not any([2<3,5>2,6==89]))
