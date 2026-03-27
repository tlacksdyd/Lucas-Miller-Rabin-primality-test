import random as r
import time
import numpy

repu = int(input('반복하고자 하는 횟수를 입력하세요: '))
N = int(input('판별하고자 하는 수(짝수제외): '))
percent = 0

if N%2 == 0:
    print('그거 짝수잖아')
    exit()

t_list = []
temp = N-1

for i in range(0,repu,1):
    start = time.time()
    count = 0
    def division(x):
        global count
        while x%2 == 0:
            count +=1
            x= x//2
            return division(x)
        return x
    d = division(temp)

    N_list = list(range(1,N,1))
    a = r.choice(N_list)

    if count-1 == 0:
        r1_list=[0]
    else:
        r1_list = list(range(0,count,1))
    
    for i in r1_list:
        if (a**d-1)%N ==0 or (a**((2**i)*d)+1 )%N==0 :
            percent += 1
            print('r이',i,'일 때 N은 확률적 소수입니다')    
        else: 
            print('r이',i,'일 때 N은 합성수입니다')

    end = time.time()
    t = end - start
    t_list.append(t)

prime_rate = ( percent/(repu*len(r1_list)) ) * 100
composite_rate = 100 - prime_rate
avg = numpy.mean(t_list)


print('입력한 소수:', N)
print('d = ', d)
print('s = ', count)
print('계산 반복 횟수:',len(r1_list)*repu)
print('소수일 확률:',prime_rate,'%')
print('합성수일 확률:',composite_rate,'%')
print('평균 걸린 시간:',avg,'sec')

