# Python 

### 제어문

- 파이썬은 위에서 아래로 순차적 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요
- 제어문은 순서도(flow chart) 로 표현 가능



	#### 		조건문

- 참/거짓을 판단할 수 있는 조건식과 함께 사용

- expression에는 참/거짓에 대한 조건식

  - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭 실행

  - 이외의 경우 else이후 들여쓰기 되어있는 코드 블럭 실행

    - else는 선택적

      ```python
      if <expression> :
          #Run this Code block
      else:
          #Run this Code block
      ```

  - 복수 조건문

    - ```python
      if <expression>:
          #Code block
      elif <expression>:
          #Code block
      elif <expression>:
          #Code block
      else:
          #Code block
      ```

  - 중첩 조건문

    - 조건문은 다른 조건문에 중첩되어 사용될 수 있음

    - 들여쓰기 유의

    - ``` python
      if <expression>:
          #Code block
          if <expression>:
              #Code block
      else:
          #Code block
      ```

  - 조건 표현식 (Conditional Expression)

    - 조건 표현식을 일반적으로 조건에 따라 값을 할당할 때 활용

    - ``` python
      <true인 경우 값> if <expression> else <false인 경우 값>
      value = num if num>=0 else -num
      #절대값을 저장하기 위한 코드
      ```

    

​		

#### 		반복문 (Loop Statement)

- 특정 조건을 도달할 때 까지, 계속 반복되는 일련의 문장
- while 문
  - 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
- for 문
  - 반복가능한 객체를 모두 순회하면 종료(별도의 종료조건이 필요 없음)
- 반복제어
  - break, continue, for-else



- while
  - while문은 조건식이 참인 겨





























