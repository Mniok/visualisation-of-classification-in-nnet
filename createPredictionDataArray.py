from timeit import default_timer as timer
import itertools
step = 0.01

print('_______________________________________');
# 1 -------------
print('method 1: ---')
start1 = timer()

dataForPrediction = []
#step = 0.5
for i in range(int(-10*(1/step)), int(10*(1/step))+1):
    for j in range(int(-10*(1/step)), int(10*(1/step))+1):
        dataForPrediction.append([i*step, j*step]) # horrendously slow, replace
#print(dataForPrediction)
print(dataForPrediction[0:20])
print('...')
print(dataForPrediction[-20:])
print('length:', len(dataForPrediction))

end1 = timer();
print('time: ', end1 - start1)


# 2 -------------
print('method 2: ---')
start2 = timer()

dataForPrediction = [[i*step, j*step] for i in range(int(-10/step), int(10/step + 1)) for j in range(int(-10/step), int(10/step + 1))]  # I will use this one I think
print(dataForPrediction[0:20])
print('...')
print(dataForPrediction[-20:])
print('length:', len(dataForPrediction))

end2 = timer()
print('time: ', end2 - start2)


# 3 -------------
print('method 3: ---')
start3 = timer()

dataForPrediction = [[i[0]*step, i[1]*step] for i in itertools.product(range(int(-10/step), int(10/step + 1)), range(int(-10/step), int(10/step + 1)))]

print(dataForPrediction[0:20])
print('...')
print(dataForPrediction[-20:])
print('length:', len(dataForPrediction))

end3 = timer()
print('time: ', end3 - start3)


# --------
print('comparison:', end1-start1, end2-start2, end3-start3)
