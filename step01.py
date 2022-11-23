# 1.1 상자로서의 변수
'''
'상자' = '변수'
- 상자와 데이터는 별개
- 상자에는 데이터가 할당
- 상자 속을 들여다 보면 데이터 참조 가능
'''

class Variable:
  def __init__(self, data):
    self.data = data

import numpy as np

data = np.array(1.0)
x = Variable(data)
print(x.data) # 1.0

'''
x는 Variable 인스턴스
실제 데이터는 x 안에 담겨있음
x는 데이터 자체가 아니라 데이터를 담은 상자


머신 러닝 시스템 기본 데이터 구조 : 다차원 배열
'''

x.data = np.array(2.0)
print(x.data) # 2.0

'''
* 넘파이의 다차원 배열
0차원 매열 : 스칼라
1차원 배열 : 벡터
2차원 배열 : 행렬
'''