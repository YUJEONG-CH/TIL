# Python 기초





#### 컴퓨터 프로그래밍 언어

-  컴퓨터 (Computer) = Calculation + Remember

-  프로그래밍 (programming) 언어 : 컴퓨터에게 명령하기 위한 약속

  

### 파이썬 (Python)

- Expressive Language
  - 같은 작업에 대해서도 C나 Java로 작성할 때 보다 더 간결하게 작성 가능
- 크로서 플랫폼 언어
  - Windows, macOS, Linux, Unix 등 다양한 운영체제에서 실행 가능
- 인터프리터 언어 (Interpreter)
  - 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
  - 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음
- 객체지향 프로그래밍 (Object Oriented Programming)
  - 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음
    - 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것





### 파이썬 개발 환경

- 파이썬 기본 인터프리터 : IDLE

  - IDLE (Intergrated Development and Learning Environment)

    - 내장 프로그래밍으로 파이썬 설치 시 기본적으로 설치 -> 인터프리터가 대화형 모드로 동작함

      ​	> 여러 줄의 코드가 작성되는 경우 보조 프롬프트(...)가 사용됨

      ​	> 프롬프트(>>>)에 코드 작성하면 해당 코드 실행됨

    - Python이 설치된 환경에서는 기본적으로 활용 가능하나 디버깅 및 코드 편집, 반복 실행이 어려움

- 파이썬 스크립트 실행

  - IDE (예시: Pycharm), Text editor(예시: Visual Studio Code) 등에서 작성한 파이썬 스크립트 파일을 직접 실행





### 기초 문법

- 들여쓰기 (Identation)

  - Space Sensitive
    - 문장을 구분할 때,  들여쓰기를 사용
    - 들여쓰기를 할 때는 4칸(space 4번) 혹은 1탭(Tab 1번) 을 입력

- 변수(Variable)

  - 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름
  - 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에.
    즉, 참조하는 객체가 바뀔 수 있기 때문에 '변수'라고 불림
  - 변수는 할당 연산자(=)를 통해 값을 할당(assignment)
  - type()
    - 변수에 할당된 값의 타입
  - id()
    - 변수에 할당된 값(객체)의 고유한 아이덴티티값이며, 메모리주소

- 변수 연산

  ``` python
  i=5
  j=3
  i+j #8
  i-j #2
  
  s='파이썬'
  '안녕' + s #안녕파이썬
  s*3 #파이썬파이썬파이썬
  
  ```

- 변수 할당

  - 같은 값을 동시에 할당할 수 있음

    ``` python
    x=y=1004
    ```

  - 다른 값을 동시에 할당할 수 있음 (multiple assignment)

    ``` python
    x,y=1,2
    ```

    

  - 실습) x=10, y=20일 때, 각각 값을 바꿔서 저장하는 코드 작성하시오.

    ``` python
    #방법1 임시 변수 활용
    tmp=x
    x=y
    y=tmp
    print(x,y)
    
    #방법2 Pythonic!
    y,x = x,y
    print(x,y)
    ```

- 식별자 (Identifiers)

  - 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name)

  - 규칙

    - 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
    - 첫 글자에 숫자 불가
    - 길이제한 없고, 대소문자 구별
    - 다음의 키워드는 예약어로 사용할 수 없음
      - False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

  - 키워드 / 예약어

    ```python
    import keyword
    print(keyword.kwlist)
    ```

  - 내장함수나 모듈 등의 이름으로도 만들면 안됨

    - 기존의 이름에 다른 값을 할당하게 되므로 더 이상 동작하지 않음

      ```python
      print(5)
      print='hi'
      print(5) #내장함수 print가 아닌 식별자(변수명)가 print인 문자열 hi로 활용됨
      ```

- 사용자 입력

  - input([prompt])

    - 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수

    - 대괄호 부분에 문자열을 넣으면 입력 시, 해당 문자열을 출력할 수 있음

    - 반환값은 항상 문자열의 형태로 반환

      ``` python
      name=input('이름입력')
      print(name)
      
      type(name) #str
      ```

- 주석(Comment)

  - 코드에 대한 설명

    - 중요한 점이나 다시 확인하여야 하는 부분 표시
    - 컴퓨터는 인식하지 않음, 사용자만을 위한 것
    - 프로그램의 속도를 느리게 하지 않으며, 용량을 늘리지 않음

  - 가장 중요한 습관

    - 개발자에게 주석을 작성하는 습관은 매우 중요
    - 쉬운 이해와 코드의 분석 및 수정이 용이

  - 한 줄 주석

    `#` 입력

     - 한줄을 온전히 사용할 수도 있고, 그 줄 코드 뒷부분에 작성할 수 있음

       ```python
       #주석 입니다.
       #print('hello')
       print('hello') #주석
       ```





### 자료형(Datatype)

- 자료형 분류

  - Boolean Type

  - Numeric Type(수치형)
    - int (정수, integer)
    - float(부동소수점, 실수, floating point number)
    - complex(복소수, complex number)

  - String Type(문자열)

  - None

    

- None

  - 파이썬 자료형 중 하나

  - 파이썬에서는 값이 없음을 표현하기 위해 None타입 존재

  - 일반적으로 반환 값이 없는 함수에서 사용하기도 함

    ```python
    print(type(None)) #<class'NoneType'>
    a=None
    print(a) #None
    ```

- 불린형 (Boolean Type)

  - True/False 값을 가진 타입은 bool

  - 비교/논리 연산을 수행함에 있어서 활용됨

  - 0, 0.0, (), [], {}, ", None 은 모두 False로 반환됨

  - bool()함수

    - 특정 데이터가 True/False인지 검증

      ```python
      bool(0)  #False
      bool(1)  #True
      bool(-1) #True
      bool('') #False
      bool([]) #False
      bool([1,2,3]) #True
      ```

- 연산자 (Operator)

  - 논리 연산자 (Logical Operator)

    - 논리식을 판단하여 참 (True)과 거짓(False)를 반환

      | 연산자  |              내용              |
      | :-----: | :----------------------------: |
      | A and B |    A와 B 모두 True시, True     |
      | A or B  |    A와 B모두 False시, False    |
      |   Not   | True를 False로, False를 True로 |

    - and : 모두 참인 경우 참, 그렇지 않으면 거짓

      |  논리연산자and  | 내용  |
      | :-------------: | :---: |
      |  True and True  | True  |
      | True and False  | False |
      | False and True  | False |
      | False and False | False |

    

    - or : 둘 중 하나만 참이라도 참, 그렇지 않으면 거짓

      | 논리연산자 or  | 내용  |
      | :------------: | :---: |
      |  True or True  | True  |
      | True or False  | True  |
      | False or True  | True  |
      | False of False | False |

    

    - not : 참 거짓의 반대의 결과

      | 논리연산자 not | 내용  |
      | :------------: | :---: |
      |    not True    | False |
      |   not False    | True  |



- 수치형 (Numeric Type)

  - 정수(Int)

    - Python3부터는 long타입은 없고, 모두 int로 표기 됨
    - 여타 프로그래밍 언어, Python2에서는 OS기준 32/64비트

    - 

### 컨테이너



