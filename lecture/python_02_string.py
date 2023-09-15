# 문자열(String)의 이해

# 1. 문자열 인덱스
# 문자열은 각 문자마다 순서(인덱스)가 있음
# 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
# 인덱스 시작은 0(첫 문자열의 인덱스 = 0)
# 인덱스는 공백을 포함

print("=" * 200)

# 2. 문자 추출 - 인덱스를 통해서 문자 추출, 인덱스 범위 벗어난 경우 오류(index out of range) 발생
lang = "Python"
print(lang[0])
print(lang[2])
#  print(lang[9]) - IndexError: string index out of range

print("=" * 200)

# -1 인덱스(Reverse Index)
# 우측에서부터 좌측으로 인덱스를 붙임
# 최초 값 : -1 (0이 아님)

print(lang[-1])
print(lang[-3])

print("=" * 200)

# 3. 문자열 슬라이싱
# lang[3] -> 문자 1개만 추출
# 슬라이싱 : 부분 문자열을 추출하고 싶은 경우
# 시작 인덱스 : 끝 인덱스 2개가 필요함
# 끝 인덱스 번호 : +1 해줘야 함(e.g. [0:6] -> 0번 인덱스부터 5번 인덱스까지 출력)

msg = "Python is all you need"
print(msg[0:6])
print(msg[:6])  # 시작 인덱스 생략 -> 처음 인덱스(0번)부터 시작
print(msg[3:])  # 끝 인덱스 생략 -> 끝 인덱스(-1)까지 슬라이싱
print(msg[:]) # 시작/끝 인덱스 생략 -> 전체 출력

print("=" * 200)

print(msg[18:])  # 정방향 인덱스
print(msg[-4:])  # 역방향 인덱스