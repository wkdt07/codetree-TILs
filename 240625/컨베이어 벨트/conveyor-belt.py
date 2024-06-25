N,t = map(int,input().split())

fst_arr = list(map(int,input().split()))
snd_arr = list(map(int,input().split()))
snd_arr.reverse()

def convey(arr1,arr2):
    left = arr2[0]
    right = arr1[-1]
    for i in range(N-1,0,-1):
        arr1[i]=arr1[i-1]
    for j in range(N-1):
        arr2[j] = arr2[j+1]
    arr2[N-1]=right
    arr1[0]=left

time = 0
while 1:
    convey(fst_arr,snd_arr)
    time += 1
    if time == t:
        break
print(*fst_arr)
snd_arr.reverse()
print(*snd_arr)