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
      
      - 
