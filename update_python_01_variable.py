print("=" * 200)
print("Hello \nPython")
print("Hello \tPython")
print("=" * 200)

# \n : 새 줄 변환, \t : tab(8칸 띄움)

# 자료형(문자형, 정수형, 실수형, 논리형) -> 외울 것

# Java와 Python에서의 정수형 차이점
# - Java : byte, short, int, long 등 다양한 종류의 자료형을 사용
# - Python : int 1개만 사용 : 기술의 발전, 메모리 넘쳐나게 씀
# 만들어진지 오래 된 언어들의 경우 대부분 다양한 종류의 자료형이 사용됨 : 메모리를 효율적으로 사용하기 위해서
# 자료형은 담을 수 있는 크기의 범위가 지정되어 있음(byte, short, int, long 등 담을 수 있는 범위가 모두 다름)

# Python은 동적 타이핑 언어 -> Python이 실행될 때 Type을 지정해 준다.
# type() 함수 제공 : 괄호 안의 값의 type(int, float, string, bool)이 무엇인지를 알려줌

print(type("ABC"))
print(type(123))
print(type(1.4))
print(type(False))

print("=" * 200)

# Type Casting(형변환)
# - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능함
# 1) int() : 정수형으로 변환
# 2) float() : 실수형으로 변환
# 3) str() : 문자열형으로 변환
# float("Hello"), int("Hello")는 형변환 불가

print(int("3"))
print(float("3"))
# print(int("3.14")) 문자열 실수형 -> 정수형 변환은 불가능
print(float("3.14"))
print(float(3))
print(str(3))
print(int(3.14))
print(str(3.14))

print("=" * 200)  # 코드 옆에 주석 달 때에는 2칸 띄우고 작성하는 것이 개발자들의 관례임

# None
# 아무런 값을 갖지 않을 때 사용, 일반적으로 변수가 초기값을 갖지 않게 변수만 생성하고 싶을 때 사용
# 다른 언어의 Null과 같은 의미로 사용함
# e.g) value = None
# 그러나 사용하지 않는 것이 적극 권장됨(절대 사용 금지)
# value = "" 이라고 쓰는 것(빈 공간)을 추천함 : "Null Pointer Exception"이라는 에러를 피하기 위해서

# C언어 변수 생성 -> int a; : 변수는 생성되었으나 변수 내의 값은 존재하지 않음, int로 처음부터 자료형 정해줌
# Python 변수 생성 -> a : 변수 생성이 아닌 변수 호출 기능, 동적 타이핑 언어이기 때문(자료형을 안 정해줌)

# 기본자료형(Primitive Type) : 변수에 값이 저장됨
# 객체자료형(Reference Type) : 변수에 값의 "주소"가 저장됨
# Java : 기본, 객체 자료형을 모두 사용함
# Python : 객체 자료형만 사용

# 변수(Variable) - 하나의 값을 저장할 수 있는 메모리 공간
print("=" * 200)

num = 4
num = 10
print(num)  # 결과 10 출력 : 하나의 값만 저장됨

# 변수 생성 및 초기화
num = 5 # 컴퓨터 구조상 원래 있는 값을 초기화하고 새로운 변수 값을 집어 넣음

# 대입 연산자(=) : 우측의 값을 좌측 변수에 저장함 - 동등 연산자 : ==(=을 2개씀 : for Numerical Comparison)

print("=" * 200)

# name 변수 생성 - "Joonsu Han" 값을 name 변수에 담기

name = "Joonsu Han"
print(name)

# 명명규칙(Naming Rule) : 변수, 함수, 클래스 등의 사용자 정의 이름을 붙일 때 사용(C, Python, Java 등에서 모두 사용)
# 명확하고 알아보기 쉽게 짓는 것이 좋음

# 1. 영문 대소문자, 숫자, _(언더바)만 사용해야함
# 2. 변수명이 숫자로 시작할 수 없음
# 3. 영어 대소문자를 구분함
# 4. 예약어 사용 불가능 : 파이썬 자체적으로 미리 선점하여 사용중인 키워드(e.g : print, for, while, if, else, et cetera)
# 4가지 사항은 암기해야 함

# Naming Method(명명기법) - Naming Rule =/= Naming Method
# 변수, 함수, 클래스 등의 사용자 정의 이름에 사용하는 기법 : 프로그래밍 언어별로 Method가 다르다
# 1. snake_case : 소문자만 사용, 합성어는 언더바(_)를 사용하여 붙임(e.g. student_name) -> Python에서 주로 사용됨
# 2. camelCase : 첫글자 소문자, 합성어의 첫글자는 대문자 사용(e.g. studentName)
# 3. PascalCase : 첫글자와 합성어 첫글자 모두 대문자 사용(e.g. StudentName)

# Python, Java, C 비교
#                          변수                함수              클래스
# Java, C               camelCase           camelCase()         PascalCase
# Python                snake_case          snake_case()        PascalCase

# 함수는 괄호()가 붙어있음 - 변수와 함수를 구분하는 방법
# Naming Rule / Naming Method 시험 출제 확률 높음

print("=" * 200)

# 동적 출력
student_num = 20182594
student_name = "Joonsu Han"

# 원하는 출력 예시 : 조선대학교 20182594, Joonsu Han 입니다.

print("조선대학교 20182594, Joonsu Han 입니다.")  # 원하는 대로 출력은 되지만, 하드 코딩은 지양해야 함

# 1. format() 함수를 사용 - 변수 갯수가 많아지면 헷갈림, 과거에 주로 쓰던 방법
print("조선대학교 {}, {} 입니다.".format(student_num, student_name))

# 2. f-string - 새로 쓰는 방법(괄호 맨 앞에 f를 작성, {}안에 변수 집어넣기)
print(f"조선대학교 {student_num}, {student_name} 입니다.")

# 간단한 사칙연산
# + : 더하기, - : 빼기, * : 곱하기, / : 나누기, // : (나누기)몫, % : (나누기)나머지, ** : 제곱

print(5/2)  # 2.5(float 형태로 출력)
print(5//2)  # 2
print(5%2)  # 1