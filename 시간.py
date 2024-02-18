h = int(input())

count = 0

# 시간 만들기
# 결론적으로 매 초 마다 시간을 만들어서 3이 있는지 여부를 확인한다.
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 만든 시간 안에 3이 포함되어있으면.
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
