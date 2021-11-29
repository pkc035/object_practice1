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


class Clock:
    #시계 클래스

    HOURS = 24 
    MINUTES = 60
    SECONDS = 60

    def __init__(self, hour, minute, second):
        #시, 분, 초를 나타내는 카운터 인스턴스 정의
        self.hour = hour
        self.minute = minute
        self.second = second

    def set(self, hour, minute, second):
        #현재 시간 설정
        self.hour = hour
        self.minute = minute
        self.second = second

    def tick(self):
        #초 카운터 값 1 증가
        self.second += 1

        if self.second == self.SECONDS:
            self.second = 0
            self.minute += 1
        
        if self.minute == self.MINUTES:
            self.minute = 0
            self.hour +=1

        if self.hour == self.HOURS:
            self.hour = 0

    def __str__(self):
        #시:분:초 형식으로 리턴
        return "{}:{}:{}".format(str(self.hour).zfill(2), str(self.minute).zfill(2), str(self.second).zfill(2))


print("시간을 1시 30분 48초로 설정합니다")
clock = Clock(1, 30, 48)
print(clock)

print("13초가 흘렀습니다")
for i in range(13):
    clock.tick()
print(clock)

print("시간을 2시 59분 58초로 설정합니다")
clock.set(2, 59, 58)
print(clock)

print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)

print("시간을 23시 59분 57초로 설정합니다")
clock.set(23, 59, 57)
print(clock)

print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)