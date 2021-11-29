class Counter:
# 시계 클래스의 시, 분, 초를 나타낼 카운터 클래스

    def __init__(self, limit):
        #인스턴스 변수 limit, value 값을 설정
        self.limit = limit
        self.value = 0

    def set(self, new_value):
        #파라미터가 0이상, 최댓값 미만이면 value에 설정
        self.value = new_value if new_value > 0 else 0

    def tick(self):
        #value 1증가, limit에 도달하면 value 0, True 리턴
        self.value += 1

        if self.limit == self.value:
            self.value=0
            return True
        else:
            return False

    def __str__(self):
        return str(self.value).zfill(2)

counter = Counter(30)

print("1부터 5까지 카운트하기")
for i in range(5):
    counter.tick()
    print(counter)

print("카운터 값 0으로 설정하기")
counter.set(0)
print(counter)

print("카운터 값 27으로 설정하기")
counter.set(27)
print(counter)

print("카운터 값이 30이 되면 0으로 바뀝니다")
for i in range(5):
    counter.tick()
    print(counter)
