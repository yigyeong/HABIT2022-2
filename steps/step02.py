# 2. 변수를 낳는 함수
'''
2.1 함수란
: 어떤 변수로부터 다른 변수로의 대응 관계를 정한 것

* 계산 그래프 : 노드와 에지로 구성된 데이터 구조
'''
import numpy as np

class Variable:
  def __init__(self, data):
    self.data = data

class Function:
  def __call__(self, input):
    x = input.data
    y = self.forward(x)
    ouput = Variable(y)
    return ouput

    def forward(sef, x):
      raise NotImplementedError()

class Square(Function):
  def forward(self, x):
    return x ** 2

x = Variable(np.array(10))
f = Square()
y = f(x)
print(type(y))  # <class '__main__.Variable'>
print(y.data) # 100