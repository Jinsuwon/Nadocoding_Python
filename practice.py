# #boolean=참 거짓

# '''print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5>10)) 
# '''
# animal="강아지"
# name="연탄이"
# age=4
# hobby="산책"
# is_adult=age>=3

# print("우리집 강아지의 이름은 연탄입니다")
# print("연탄이는 4살이며, 산책을 아주 좋아해요")
# print("연탄이는 어른일까요? True")

# print("우리집" + animal + "의 이름은" + name + "에요")
# hobby="공놀이"
# #print(name + "는 " + str(age) + "살이며, "+ hobby + "을 아주 좋아해요")
# print(name,"는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요?" + str(is_adult))

# #퀴즈
# station1="사당" 
# station2="신도림"
# station3="인천공항"

# station4, station5, station6="서면", "전포", "광안리"

# print(station1,"행 열차가 들어오고 있습니다")
# print(station2,"행 열차가 들어오고 있습니다")
# print(station3,"행 열차가 들어오고 있습니다")

# print(station4,"행 열차가 들어오고 있습니다")
# print(station5,"행 열차가 들어오고 있습니다")
# print(station6,"행 열차가 들어오고 있습니다")

# ment="행 열차가 들어오고 있습니다"
# print(station1,ment)

# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3) # 2^3=8
# print(5%3) # 나머지구하기 이므로 2
# print(5//3) # 몫 구하기이므로 1

# print(10>3) #True
# print(4>=7) #False
# print(10<3) #False
# print(5<=5) #True

# print(3==3) #True
# print(4==2) #False
# print()
# print(1 !=3) #True
# print(not 1!=3) #False

# print((3>0) and (3<5)) #True
# print((3>0) & (3<5)) #True

# print((3>0) or (3>5)) #True
# print((3>0) | (3>5)) #True

# print(5>4>3) #True
# print(5>4>7) #False

# print(2+3 * 4) #14
# print((2+3) * 4) #20
# number=2+3*4 #14
# print(number)
# number=number+2 #16
# print(number) 
# number +=2 #18
# print(number)
# number *=2 #36
# print(number)
# number /=2 #18
# print(number)
# number -=2 #16
# print(number)

# number %=2 #0
# print(number)

# print(abs(-5)) # 5(절댓값)
# print(pow(4,2)) # 4^2 (제곱)
# print(max(5,12)) # 12 (최댓값)
# print(min(5,12)) # 5 (최솟값)
# print(round(3.14)) # 3 (반올림)
# print(round(4.99)) # 5 

# from math import * # math 라이브러리안에 모든 함수를 사용하겠다
# print(floor(4.99)) # 4, 내림
# print(ceil(3.14)) # 4, 올림
# print(sqrt(16)) # 4, 제곱근

#from random import *

# print(random()) # 0.0~1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0~10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0부터 10미만의 정수 생성

# print(int((random()*10)+1)) #0부터 10 이하의 정수 생성
# print(int((random()*10)+1))
# print(int((random()*10)+1))
# print(int((random()*10)+1))
# print(int((random()*10)+1))
# print(int((random()*10)+1))

# print(int((random()*45)+1)) # 1~45 이하의 임의의 값 생성, 로또 번호 생성
# print(int((random()*45)+1))
# print(int((random()*45)+1))
# print(int((random()*45)+1))
# print(int((random()*45)+1))
# print(int((random()*45)+1))
# print()
# print(randrange(1,46)) # 1~45 미만의 임의의 값 생성
# print()
# print(randint(1,45)) # 1~45 이하의 임의의 값 생성
# from random import *

# print("오프라인 스터디 모임 날짜는 매월", randrange(4,29), "일로 선정되었습니다")

# #유튜브 구문
# date=randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 "+ str(date) + "일로 선정되었습니다")

# sentence="나는 소년입니다"
# print(sentence)
# sentence2="파이썬은 쉬워요"
# print(sentence2)
# sentence3="""
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3) # 

#슬라이싱: 문자열 중에 필요한 값만 가져온다
# jumin="990120-1234567"

# print("성별: "+ jumin[7])
# print("연 : " + jumin[0:2]) # 0부터 2직전까지
# print("월 : " + jumin[2:4]) # 
# print("일 : ", jumin[4:6])

# print("생년월일: " + jumin[:6]) # 처음부터 6직전까지
# print("뒤 7자리" + jumin[7:14])
# print("뒤 7자리" + jumin[7:]) #7부터 끝자리까지
# print("뒤 7자리 (뒤에부터): "+ jumin[-7:-1]) # 맨끝자리가 '-1' 이므로 출력은 1~6까지 됨
# print("뒤 7자리 (뒤에부터): "+ jumin[-7:]) 


#문자열 처리 함수
# python="Python is Amazing"
# print(python.lower()) # 문자열을 모두 소문자로
# print(python.upper()) # 문자열을 모두 대문자로
# print(python[0].isupper()) # 문자열의 첫번째가 대문자인가?를 확인해주는 함수, 출력은 True or False
# print(len(python)) # 문자열의 길이를 반환
# print(python.replace("Python", "Java")) # Python이라는 문자열을 Java로 바꿔줌

# index=python.index("n") # n이 위치한 인덱스를 출력: 5
# print(index)
# index=python.index("n", index+1) # n이 나온 이후(+1) 또 n이 나오는 인덱스를 출력: 15
# print(index)

# print(python.find("n")) # n이 포함된 위치를 알려줌, 출력: 5
# print(python.find("Java")) # Java는 포함되어 있지 않음, 출력: -1
# #print(python.index("Java")) # index에서는 없으면 오류를 내고 프로그램을 종료함

# print(python.count("n")) # n이 몇번 나오는지 세어줌, 출력: 2

#문자열 포맷
# print("a" + "b") 
# print("a", "b")

# 방법 1
# print("나는 %d살입니다" % 20) # %d: 정수
# print("나는 %s를 좋아해요" % "파이썬") # %s: 문자열
# print("Apple은 %c로 시작해요" % "A") # %c: 문자

# print("나는 %s살입니다" %20) # %d때랑 똑같은 출력이 나옴, 만능이죠?

# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간")) #파란:0, 빨간:1로 처리해서 중괄호 안에 넣어준다

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# 방법 4 (version 3.6 이상부터 가능)
# age=20
# color="빨간"
# print(f"나는 {age} 살이며, {color}색을 좋아해요")
#실제 변수의 저장된 값을 중괄호 안으로 가져다 쓸 수 있다


#탈출문자
# print("백문이 불여일견\n백견이 불여일타")

# #저는 "나도코딩"입니다
# print("저는 \"나도코딩\"입니다")
# print("저는 '나도코딩'입니다")
# print('저는 "나도코딩"입니다')

# # \\: 문장 내에서는 \로 취급됨
# print("C:\\Users\\jinso.JINSUWON")

# # \r: 커서를 맨앞으로 이동
# print("Red Apple\rPine") #PineApple
# print("Red Apple\rPine123") #Pine123le

# # \b: 백스페이스 (한 글자 삭제)
# print("Redd\bApple") #RedApple

# \t: 키보드 tab을 치는 것과 똑같음
#print("Red\tApple") #Red    Apple

#print("Redd\b\b\b\bApple") #RedApple

# ex1="http://naver.com"

# cond12=ex1[7:12]
# cond3=cond12[0:3]
# print("{}{}{}{}".format(cond3, len(cond12), cond12.count("e"), "!"))


# 리스트[]

#지하철 칸별로 10명, 20명, 30명
# subway1=10
# subway2=20
# subway3=30

# subway=[10,20,30]
# print(subway)

# subway=["유재석", "조세호", "박명수"]
# print(subway)

# #조세호씨가 몇 번쨰 칸에 타고 있는가?
# print(subway.index("조세호")) # 출력: 1

# #하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# #정형돈씨를 유재석 - 조세호 사이에 태워봄
# subway.insert(1, "정형돈") # 1번 인덱스에 정형돈을 삽입
# print("정형돈인덱스", subway)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print("팝 기능", subway.pop())
# print(subway)

# print("팝 기능", subway.pop())
# print(subway)

# print("팝 기능", subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# #정렬도 가능
# num_list=[5,2,4,3,1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print("해치웠나?", num_list)

#다양한 자료형과 함께 사용
#mix_list=["조세호", 20, True]
#print(mix_list)
#num_list=[5,2,4,3,1]

#리스트 확장
#num_list.extend(mix_list)
#print(num_list)


#사전
#cabinet={3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(5)) # 출력: None
# print(cabinet.get(5, "사용 가능")) # 출력: 사용 가능
# print("hi")

#print(3 in cabinet) # True
#print(5 in cabinet) # False 

# cabinet={"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"]) #출력: 유재석
# print(cabinet["B-100"]) #출력: 김태호

# # 새 손님
# print(cabinet)
# cabinet["C-20"]= "조세호" # 출력: C-20에 조세호를 추가
# cabinet["A-3"]="김종국" # 출력: 유재석을 대체
# print(cabinet)

# # 떠나간 손님
# del cabinet["A-3"] # A-3 삭제
# print(cabinet)

# # key들만 출력
# print(cabinet.keys()) #출력: dict_keys(['B-100', 'C-20'])

# #value들만 출력
# print(cabinet.values()) #출력: dict_values(['김태호', '조세호'])

# #key, value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점, { } 안에 모든 값을 삭제
# cabinet.clear()
# print(cabinet)


#튜플: 리스트와 달리 추가 삭제와 같은 수정이 불가하지만 속도가 빠르다
# menu=("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# #menu.add("생선까스") # 코드 오류

# name="김종국"
# age=20
# hobby="코딩"
# print(name, age, hobby)

# (name, age, hobby)=("유재석", 25, "독서")
# print(name,age,hobby)


#집합(set)
#중복 안됨, 순서 없음
# my_set={1,2,3,3,3}
# print(my_set) #출력: 1,2,3

# #집합을 만드는 두가지 방식
# java={"유재석", "김태호", "양세형"}
# python=set(["유재석", "박명수"])

# #교집합 (java와 python을 모두 할 수 있는 개발자
# print(java&python) # 교집합, 출력: 유재석
# print(java.intersection(python)) # 교집합, 출력: 유재석

# #합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
# print(java|python)
# print(java.union(python))

# #차집합(java는 할 수 있지만 python은 못하는 개발자)
# print(java-python)
# print(java.difference(python))

# # python을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 까먹음
# java.remove("김태호")
# print(java)


# 자료구조의 변경
# # 커피숍
# menu={"커피", "우유", "주스"}
# print(menu, type(menu)) #출력: type='set

# menu=list(menu)
# print(menu, type(menu)) #출력: type='list'

# menu=tuple(menu)
# print(menu, type(menu)) #출력: type='tuple'

# menu=set(menu)
# print(menu, type(menu)) #출력: type='set'


#활용 예제
# from random import *
# lst=[1,2,3,4,5]
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

# from random import *

# arr1=[0]*20
# for i in range(20):
#     arr1[i]=i+1
# '''#유튜브 내용
# users=range(1,21)
# print(type(users)) #출력: 'range' 라 list함수를 사용할 수 없음
# users=list(users) #
# print(type(users)) #출력: 'list'
# ''' 

# shuffle(arr1)
# first_winner=sample(arr1,1)
# print("치킨 당첨자: ", first_winner)
# arr1.remove(first_winner[0])
# print("커피 당첨자: ",sample(arr1,3))

# java.remove("김태호")
# del cabinet["A-3"] # A-3 삭제

# weather=input("오늘 날씨는 어떄요?: ") # 문장 출력후 str형태로 받음
# if weather=="비" or weather=="눈":
#     print("우산을 챙기세요")

# elif weather=="미세먼지":
#     print("마스크를 챙기세요")

# else: 
#     print("준비물 필요없음")

# temp=int(input("기온은 어떄요? "))
# if 30<=temp:
#     print("너무 더워요.")
# elif 10<=temp and temp<30:
#     print("괜찮은 날씨에요")

# elif 0<=temp and temp<10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요")

# print("대기번호: 1")
# print("대기번호: 2")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호: {0}".format(waiting_no))

# for waiting_no2 in range(5): #0,1,2,3,4
#     print("대기번호: {0}".format(waiting_no2))

# starbucks=["아이어맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비 됨".format(customer))


#while
# customer="토르"
# index=5
# while index>=1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
#     index -=1
#     if index==0:
#         print("커피는 폐기처분되었습니다")

# customer="아이언맨"
# index=1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출{1} 회".format(customer, index))
#     index+=1

# customer="토르"
# person="Unknown"

# while person!=customer:
#     print("{0}, 커피가 준비 되었습니다".format(customer))
#     person=input("이름이 어떻게 되세요?: ")

# absent=[2,5] #결석
# no_book=[7] #책을 깜빡했음
# for student in range(1,11):
#     if student in absent: # student가 리스트 absent에 포함되어 있다면
#        continue
#     elif student in no_book:
#         print("오늘 수업은 여기까지, {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student)) 

# 한줄 for문
# # 출석번호가 1 2 3 4, 에서 100을 붙이기로 함 => 101 102 103 104
# students=[1,2,3,4,5]
# print(students)
# students=[i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students=["Iron man", "Thor", "groot"]
# students=[len(i) for i in students]
# print(students)

# 학생이름을 대문자로 변환

# students=["Iron man", "Thor", "groot"]
# students=[i.upper() for i in students]
# print(students)

''' 혼자 고민
2. 왜 메서드가 필요할까?
객체지향 프로그래밍은 **데이터(객체)**와 **그 데이터를 처리하는 함수(메서드)**를 한 덩어리로 묶어 다룹니다.
그래서 어떤 데이터(객체)는 자신만의 고유한 기능(메서드)을 갖고 있어요.

예를 들어, 문자열(str) 객체는 대문자로 바꾸는 upper()라는 메서드를 갖고 있고,
리스트(list) 객체는 요소를 추가하는 append()라는 메서드를 갖고 있죠.
'''

# from random import *
# # print(randint(1,45)) # 1~45 이하의 임의의 값 생성
# count=0

# for customer in range(1,51):
#     be_timed=randint(5,50)
#     if (be_timed >=5 and be_timed <=15):
#         print("[o] {}번째 손님 (소요시간: {}분)".format(customer, be_timed))
#         count+=1
#     else:
#         print("[ ] {}번째 손님 (소요시간: {}분)".format(customer, be_timed)) 
# print("총 탑승 승객: ",count)


'''
def open_account():
    print("새로운 계좌가 생성되었습니다")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {}입니다.".format(balance+money))
    return balance+money

balance=0 #잔액
balance=deposit(balance, 1000)
print(balance)

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {}원입니다.".format(balance))
        return balance
    

def withdraw_night(balance, money): #저녁에 출금, 수수료발생
    commission=100 #수수료 100원
    return commission, balance-money-commission

balance=0
balance=deposit(balance, 1000)
#balance=withdraw(balance, 500)
commission, balance=withdraw_night(balance, 500)
print("수수료 {}원이며, 잔액은 {}원입니다.".format(commission, balance))
'''

# def profile(name, age, main_lang):
#     print("이름: {0} \t 나이: {1} \t 주 사용 언어: {2}"\
#           .format(name, age,main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#키워드 값
# 같은 학교,학년,반,수업 => 이름 말고 다 같음

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0} \t 나이: {1} \t 주 사용 언어: {2}"\
#           .format(name, age,main_lang))
    
# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20 )
# profile(main_lang="자바", age=25, name="김태호")

# def profile(name, age, lang1,lang2,lang3,lang4,lang5):
#     print("이름: {0} \t나이: {1}".format(name,age), end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)


#가변 인자
# def profile(name, age, *language):
#     print("이름: {0} \t나이: {1}".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python", "java", "c", "c++", "c#", "JS")
# profile("김태호", 25, "kotiln", "swift")


#전역변수

# gun=10

# def checkpoint(soldiers): #경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun=gun-soldiers
#     print("[함수 네] 남은 총: {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun=gun-soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun


# print("전체 총: {0}".format(gun))
# #checkpoint(2) # 2명이 경계근무 나감
# gun=checkpoint_ret(gun,2)
# print("남은 총: {0}".format(gun))


#퀴즈
# def std_weight(height, gender):
#     if gender=="남자":
#         weight=height**2*0.0001*22
#         print("키: {0}cm 남자의 표준 체중은 {1:.2f}kg입니다.".format(height, weight))
    
#     elif gender=="여자":
#         weight=height**2*0.0001*21
#         print("키: {0}cm 여자의 표준 체중은 {1:.2f}kg입니다.".format(height, weight))

# height= float(input("키를 입력해주세요: "))
# gender= str(input("성별을 입력해주세요: "))


# std_weight(height, gender)

# import sys
# print("Python", "Java", file=sys.stdout) #표준 출력
# print("Python", "Java", file=sys.stderr) #표준 오류

# 시험 성적
# scores={"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003 ...
# for num in range(1,21):
#     print("대기번호: " + str(num).zfill(3))

# answer=input("아무 값이나 입력하세요: ") # 문자열 형태로 변수에 저장한다
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")
'''
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0:>10}".format(500)) # 출력:        500
# 양수일 때 +로 표시, 음수일 때 -로 표시
print("{0:>+10}".format(500)) # 출력:       +500
print("{0:>+10}".format(-500)) # 출력:       -500
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500)) # 출력: +500______

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000)) # 출력: 100,000,000,000
# 3자리마다 콤마를 찍어주기, +,- 부호도 붙이기
print("{0:+,}".format(100000000000)) # 출력: +100,000,000,000
print("{0:,}".format(-100000000000)) # 출력: -100,000,000,000
# 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니깐 빈 자리는 ^^로 채워주기
print("{0:^<+30,}".format(100000000000000))
# 소수점 출력, 둘째 자리까지 출력
print("{0:.2f}".format(5/3))
'''

# score_file=open("score.txt", "w", encoding="utf8") # w: write 쓰기 전용
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# score_file=open("score.txt", "a", encoding="utf8") # a: append 끝에 추가하기
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

# score_file=open("score.txt", "r", encoding="utf8") # r: read, 읽기 전용
# print(score_file.read())
# score_file.close()
      
# score_file=open("score.txt", "r", encoding="utf8") # r: read, 읽기 전용
# print(score_file.readline(), end="") # 한 줄만 읽어오고, 커서는 다음 줄로
# print(score_file.readline()) # 한 줄만 읽어오고, 커서는 다음 줄로
# print(score_file.readline()) # 한 줄만 읽어오고, 커서는 다음 줄로
# print(score_file.readline()) # 한 줄만 읽어오고, 커서는 다음 줄로
# score_file.close()

# score_file=open("score.txt", "r", encoding="utf8")
# while True:
#     line=score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file=open("score.txt", "r", encoding="utf8")
# lines=score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# 피클
# import pickle
# # profile_file=open("profile.pickle", "wb") # wb: 바이너리, 피클을 쓰기 위해서는 항상 바이너리를 설정해줘야한다
# # profile={"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# # profile_file.close()

# profile_file=open("profile.pickle", "rb") # rb: 바이너리, 피클을 쓰기 위해서는 항상 바이너리를 설정해줘야한다
# profile=pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle

# with open("profile.pickle", "rb") as profile_files:
#     print(pickle.load(profile_files))
# # close 해줄 필요가 없다

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 배우고 있다")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

#퀴즈
# for i in range(1,51):
#     with open("{}주차 주간보고.txt".format(i), "w", encoding="utf8") as report_file:
#         report_file.write("--{}주차 주간보고--".format(i))
#         report_file.write("\n{0:<6}".format("부서: "))
#         report_file.write("\n{0:<6}".format("이름: "))    
#         report_file.write("\n{0:<6}".format("업무 요약: "))









