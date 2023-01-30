# Q1
'''
중간고사 기말고사 점수를 따로 받아 저장하는 클래스를 구현해보세요. 

1. 단, 생성자의 인스턴스는 private으로 선언되어야하며, 
2. 데코레이터를 이용해 데이터를 저장하고, 
3. 함수를 이용해 평균값을 출력해보세요.


- 자료형의 선언과 데코레이터를 이용해보세요.


---------------------------

class Score():
    # TODO
    
# 출력함수
score = Score(50, 75)
print((score.mid + score.final) / 2)

# 출력 예시
62.5
--------------------------

'''


'''
# 1) private 선언 + 함수 이용해 평균값 출력  ---> ok
class Score():
    def __init__(self, mid, final):
        self.__mid = mid
        self.__final = final
        
    def avg_calcultor(self):
        return (self.__mid + self.__final) / 2
    
    
# 출력함수
score = Score(50, 75)
result = score.avg_calcultor()
print(result)

'''
    
      
# 2) 안됨 ㅜㅜ
class Score():
    def __init__(self, mid, final):
        self.__mid = mid
        self.__final = final
 
        
def avg_calcultor(self):
    return (self.__mid + self.__final) / 2
    
    
# 출력함수
score = Score(50, 75)

@avg_calcultor(score)      # ---> 데코레이터 쓰는 거 잘 모르겠음
def result(score):
    print(score) 

result(score)