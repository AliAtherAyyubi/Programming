
data=['pak',56,'India','g',56]
data2=['Afg',6,'Dubai','3']

# data.remove('pak')
count=data.count(56)
print(count)

data.append('Decision tree')
data.insert(5,'america')
print(data)

data.extend(data2)
print('after concatenation:',data)

