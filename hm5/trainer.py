import pandas as pd


f = open('./p05ese_training.txt')
line = f.readline()
train = []
while line != '':
    name = line.replace('\n','')
    train.append(name)
    line = f.readline()

A = 0
G = 0
C = 0
T = 0
model = pd.read_table('./p05output_model_file_template.txt')

for j in range(len(train)):
    for i in range(6):
        if train[j][i] == 'A':
            A += 1
        elif train[j][i] == 'G':
            G += 1
        elif train[j][i] == 'C':
            C += 1
        else:
            T += 1
    
    totel = A+C+G+T

    for i in range(6):
        model[str(i+1)][0] = '{}/{}'.format(A, totel)
        model[str(i+1)][1] = '{}/{}'.format(C, totel)
        model[str(i+1)][2] = '{}/{}'.format(G, totel)
        model[str(i+1)][3] = '{}/{}'.format(T, totel)

model.to_csv('./out.txt', sep = '\t', index = False)
