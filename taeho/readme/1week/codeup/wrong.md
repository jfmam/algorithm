# 틀린 문제

## 1012

### 틀린이유 및 해결방법

c언어와 같은 서식 문자가 존재하며 % 기호로 서식 문자와 포멧할 데이터를 구분한다

```py
number = 10
print("%d" % number)
```

## 1013

### 틀린이유 및 해결방법

변수를 만드는 여러가지 방법이 있으며 구조를 분해 후 할당도 가능하다

```py
a = 'hi'
a, b = ('hello', 'world')
a, b = ['hello', 'world']
(a, b) = 'hello', 'world'
[a, b] = ['hello', 'world']
a = b = '하나의 값으로'
```
