import time
import math


n = int(input('판별하고자 하는 수를 입력하세요: '))
 
start = time.time()
# 소수 판별
def isPrime(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0 :
            return False
    return True

# 소수 찾기
def findPrimes(x):
    primes = []
    for i in range(2, x+1):  # for i in range(2, (n//2)+1) 로 개선 가능
        if isPrime(i):
            primes.append(i)
    return primes

# 소인수 분해 1
def factorize(x):
    factors = []
    primes = findPrimes(x)  # n의 소수 리스트를 추출
    for i in primes:
        while (x % i == 0):  # 소수 중 나누어 떨어지는(약수) 수를 찾는다
            factors.append(i)
            x = x // i
    return factors

p_list = factorize(n-1)

a_list = list(range(2,n,1))


# temp_p= 0
temp_a = []

for i in a_list:
    if ((i**(n-1))-1)%n == 0:
        temp_a.append(i)
    
if temp_a == []:
    print('소수 아님')
    end1 = time.time()
    print(f"걸린시간은 {end1 - start:.5f} sec")
    exit()
    

endpoint= 0
for i in temp_a:
    temp = 0
    for j in p_list:
        if (i**int(((n-1)/j))-1)%n != 0:
            temp+=1
        else:
            continue
        
        
    if temp==len(p_list):
        print('소수입니다')
        end2 = time.time()
        print(f"걸린시간은 {end2 - start:.5f} sec")
        exit()
    
    else:
        endpoint +=1
        continue
        
        
if endpoint == len(temp_a) :
    print('소수 아닙니다') 
    end3 = time.time()
    print(f"걸린시간은 {end3 - start:.5f} sec")
    exit()

    
