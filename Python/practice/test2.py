import os

datum = []
data_sum = ['합계' if i == 0 else 0 for i in range(15)]
cnt = 0
with open('C:/Users/Harvey/Desktop/Codes/Python/practice/medical.csv', 'r', encoding='utf-8') as f:
    while 1:
        context = f.readline().strip()
        if cnt == 0:
            cnt += 1 # category pass
            continue
        if context == '':
            break
        data_list = context.split(',')
        #print(data_list)
        datum.append(data_list)
#print(datum)

for data in datum:
    for index, value in enumerate(data):
        if index == 0:
            continue
        else:
            if value == ' ':
                data_sum[index] += 0
            else:
                data_sum[index] += int(value)

datum.append(data_sum)
for data in datum:
    print(data)
for data in datum:
    for idx, value in enumerate(data):
        print(f'{value}', end = '\t')
    print()
        