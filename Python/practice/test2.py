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
# result
"""  
2012    849216  88251   77925   15506   180     10368   985     916     7739    5469    1346    322     0       448821
2013    835302  86973   73460   16988   150     10489   1574    966     8310    3816    1465    399     0       418979
2014    835700  86807   70710   16948   118     10339   117     1030    8932    3571    1606    835     0       404049
2015    880966  86675   67454   16691   79      10099           1075    9286    3634    1550    903             465855
2016    876938  85088   61361   16067   65      9758            1095    9608    3398    1472    701     0       443921
2017    879412  84255   58896   15482   58      9606    1496    1137    9912    3190    1350    604     0       420342
2018    899898  84216   56446   15616   47      9431    0       1158    10116   3030    1343    502     0       402868
2019    921201  84128   54861   15692   41      9239    3869    1205    10235   2808    697     428     0       384442
합계    6978633 686393  521113  128990  738     79329   8041    8582    74138   28916   10829   4694    0       3389277
"""        