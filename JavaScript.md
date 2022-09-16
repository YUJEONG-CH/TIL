# JavaScript

### JavaScript의 필요성

- 브라우저를 조작할 수 있는 유일한 언어

- 브라우저 화면을 동적으로 만들기 위함

### DOM (Document Object Model)

- #### 브라우저에서 할 수 있는 일
  
  - DOM 조작 - 문서(html) 조작
  
  - BOM 조작 - navigator, screen, location, frames, history, XHR
  
  - JavaScript Core (ECMAScript) - Data Structure(Object, Array), Conditional Expression, Iteration   <- 프로그래밍 문법

- #### DOM 이란?
  
  - HTML, XML 과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
  
  - 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취금하여 다루는 논리적 트리 모델
  
  - 문서가 구조화되어 있으며 각 요소는 객체로 취급
  
  - 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
  
  - 주요객체
    
    - window: DOM을 표현하는 창, 가장 최상위 객체 (작성 시 생략 가능)
    
    - document: 페이지 컨텐츠의 Entry Point 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함
    
    - naviagtor, location, history, screen

- #### DOM 조작
  
  - Document는 문서 한장(HTML) 에 해당하고 이를 조작
  
  - Dom 조작 순서
    
    - 1. 선택 (Select)
      
      2. 변경 (Manipulation)
  
  - 메서드
    
    - document. <mark>querySelector</mark>(selector)
      
      - 제공한 선택자와 일치하는 <mark>element 하나</mark> 선택
      
      - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null)
    
    - document<mark>.querySelectorAll</mark>(selector)
      
      - 제공한 선택자와 일치하는 여러 element를 선택
      
      - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 css selector를 인자(문자열)로 받음
      
      - 지정된 셀렉터에 일치하는<mark> NodeList </mark>반환
    
    - getElementById(id)
    
    - getElementsByTagName(name)
    
    - getElementsByClassName(names)
    
    - ##### querySelector(), querySelectorAll()을 사용하는 이유
      
      - id, class, tag선택자 등을 모두 사용가능하므로, 더 구체적이고 유연하게 선택 가능
        
        - ex) document.querySelector('#id') , document.querySelectAll('.class')
  
  -    DOM 변경
    
    - 변경 관련 메서드 (Creation)
      
      - document.createElement()
        
        - 작성한 태그 명의 HTML요소를 생성해 반환
    
    - 변경 관련 메서드 (append DOM)
      
      - Element.append()
        
        - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
        
        - 여러 개의 Node 객체, DOMString 을 추가할 수 있음
        
        - 반환 값이 없음
      
      - Node.appendChild()
        
        - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능)
        
        - 한번에 오직 하나의 Node만 추가할 수 있음
        
        - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동
    
    - 변경 관련 메서드 (property)
      
      - Node.innerText
        
        - Node객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text) (사람이 읽을 수 있는 요소만 남김)
        
        - 즉, 줄바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
      
      - Element.innerHTML
        
        - 요소(element) 내에 포함된 HTML 마크업을 반환
        
        - XSS 공격에 취약하므로 사용 시 주의
  
  - XSS (Cross-site Scripting)
    
    - 공격자가 입력요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
    
    - 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함
  
  - DOM 삭제 관련 메서드
    
    - ChildNode.remove()
      
      - Node가 속한 트리에서 해당 Node를 제거
    
    - Node.removeChild()
      
      - DOM에서 자식 Node를 제거하고 제거된 Node를 반환
      
      - Node는 인자로 들어가는 자식Node의 부모Node
  
  - DOM 속성 관련 메서드
    
    - Element.setAttribute(name, value)
      
      - 지정된 요소의 값을 설정
      
      - 속성이 이미 존재하면 값을 갱신, 존재 않으면 지정된 이름과 값으로 새 속성을 추가
    
    - Element.getAttribute(attributeName)
      
      - 해당 요소의 지정된 값(문자열) 반환
      
      - 인자 (attributeName)는 값을 얻고자 하는 속성의 이름



### 변수와 식별자

- 식별자는 변수를 구분할 수 있는 변수명을 말함

- 식별자는 반드시 문자, 달러$, 또는 밑줄_로 시작

- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작

- 예약어 사용 불가능 ex) for, if, function 등

- 선언 : 변수를 생성하는 행위 또는 시점

- 할당 : 선언된 변수에 값을 저장하는 행위 또는 시점

- 초기화: 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```javascript
let foo //선언
console.log(foo) //undefined
foo = 11 //할당
console.log(foo) //11

let bar = 0 //선언+할당 
console.log(bar) //0
```

- **let, const**
  
  - let - 재할당 가능,  재선언 불가능
    
    ```javascript
    let number = 10 //선언 및 초기값 할당
    number = 10     //재할당
    console.log(number) //10
    
    ```
    
    ```javascript
    let number = 10
    let number = 50  >재선언 불가능 >에
    ```
  
  - const - 재할당 불가능, 재선언 불가능
    
    ```javascript
    const number = 10 //1.선언 및 초기값 할당number = 10 
    number = 10       //2.재할당 불가능 에러
    
    ```
    
    ```javascript
    const number = 10
    const number = 50
    
    >재선언 불가능 > 에러 
    ```
  
  - 블록 스코프
    
    - if, for, 함수 등의 중괄호 내부를 가리킴
    
    - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
      
      ```javascript
      let x = 1
      if (x===1){
          let x = 2
          console.log(x)  //2
      }
      console.log(x) //1
      ```

- **var**
  
  - var로 선언한 변수는 재선언 및 재할당 모두 가능
  
  - ES6 이전에 변수를 선언할 때 사용되던 키워드
  
  - 호이스팅 되는 특성으로 인해 예기치 못한 문제 발생 가능
    
    - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
  
  - 함수 스코프
    
    - ```javascript
      var number = 10
      var number = 50 //재할당
      console.log(number) //50
      ```
  
  - **호이스팅**(hoisting)
    
    - 변수를 선언 이전에 참조할 수 있는 현상
    
    - 변수 선언 이전의 위치에서 접근 시 undefined를 반환
    
    - 자바스크립트는 모든 선언을 호이스팅한다.
    
    - 즉 var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생하여 일시적 사각지대가 존재하지 않는다.
      
      ```javascript
      console.log(username) //undefined
      var username = '홍길동'
      
      console.log(email) //Uncaught ReferenceError
      let email = 'gildong@gmail.com'
      
      
      console.log(age) //Uncaught ReferenceError
      const age = 50
      
      
      ```

- ***let, const, var 비교***

| 키워드   | 재선언 | 재할당 | 스코프   | 비고       |
| ----- | --- | --- | ----- | -------- |
| let   | X   | O   | 블록스코프 | ES6부터 도입 |
| const | X   | X   | 블록스코프 | ES6부터 도입 |
| var   | O   | O   | 함수스코프 | 사용x      |





### 데이터 타입

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐

- 크게 원시 타입과 참조 타입으로 분류됨 (Primitive type / Reference type)



- #### 원시타입
  
  - 객체가 아닌 기본 타입
  
  - 변수에 해당 타입의 값이 담김
  
  - 다른 변수에 복사할 때 실제 값이 복사됨
    
    ```javascript
    let message = '안녕하세요' //1.message 선언 및 할당
    
    
    let greeting = message //2. greeting 에 message 복사
    console.log(greeting) //3. '안녕하세요'출력
    
    
    message = 'Hello' //4.재할당
    console.log(greeting) //5.안녕하세요출력
    
    //즉 원시타입은 실제 해당 타입의 값을 변수에 저장한다.
    ```

- #### 참조타입
  
  - 객체 타입의 자료형
  
  - 변수에 해당 객체의 참조 값이 담김
  
  - 다른 변수에 복사할 때 참조 값이 복사됨
    
    ```javascript
    const msg = ['안녕하세여'] //1. msg선언 및 할당
    const greeting = message //2.복사
    console.log(greeting) //3.['안녕하세여']출력
    
    msg[0] = 'hello world' //4.재할당
    console.log(greeting) //5.['Hello world']출력
    //즉, 참조 타입은 해당 객체를 참조할 수 있는 참조 값을 저장한다.
    ```

- #### 숫자 타입
  
  - 정수, 실수 구분 없는 하나의 숫자 타입
  
  - 부동소수점 형식을 따름
  
  - NaN (Not-A-Number)
    
    - 계산 불가능한 경우 반환되는 값
    
    - ex) 'Angel'/1004
      
      const a = 13 //양의 정수
