N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

# print(arr)

max_v = 0
for i in range(N):
    for j in range(N): # 시작지점 잡기
        # 시작지점 잡고 나서 3*3 처리하면 된다.
        if i+3<N+1 and j+3<N+1: # 범위 내에 존재한다면
            cnt = 0
            for ni in range(3):
                for nj in range(3):
                    if arr[i+ni][j+nj]:
                        cnt += 1
            max_v = max(max_v, cnt)

print(max_v)