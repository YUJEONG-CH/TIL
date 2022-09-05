# HTML & CSS



### HTML ?

- HyperText Markup Language

- 우리가 보는 웹페이지가 어떻게 구조화되어 있는지 브라우저로 하여금 알 수 있도록 하는 마크업 언어

- 웹을 이루는 가장 기초적인 구성 요소로, 웹 콘텐츠의 의미와 구조를 정의할 때 사용

-  웹 브라우저에 표시되는 글과 이미지 등 다양한 콘텐츠를 표시하기 위해 마크업을 사용

- HTML은 [elements](https://developer.mozilla.org/ko/docs/Glossary/Element)로 구성되어 있으며, 이들은 적절한 방법으로 나타내고 실행하기 위해 각 컨텐츠의 여러 부분들을 감싸고 마크업 합니다. [tags](https://developer.mozilla.org/ko/docs/Glossary/Tag) 는 웹 상의 다른 페이지로 이동하게 하는 하이퍼링크 내용들을 생성하거나, 단어를 강조하는 등의 역할을 함

- HTML 마크업에서 사용하는 다양한 요소(element)

[`<head>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/head), [`<title>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/title), [`<body>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/body), [`<header>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/header), [`<footer>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/footer), [`<article>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/article), [`<section>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/section), [`<p>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/p), [`<div>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div), [`<span>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/span), [`<img>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/img), [`<aside>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/aside), [`<audio>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/audio), [`<canvas>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/canvas), [`<datalist>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/datalist), [`<details>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/details), [`<embed>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/embed), [`<nav>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/nav), [`<output>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/output), [`<progress>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/progress), [`<video>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Video), [`<ul>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ul), [`<ol>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ol), [`<li>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/li)



### HTML 요소 (Element)의 구조

- **Element** : 여는 태그, 닫는 태그, 내용을 통틀어 요소라고 함

- **여는 태그**  <

- **닫는 태그** / >

- **내용(Content)** 요소의 내용, 이 경우 단순한 텍스트



### HTML의 두가지 요소

- **블럭 레벨 요소**
  
  - 웹페이지 상에 블록(Block)을 만드는 요소
  
  - 앞뒤 요소 사이에 새로운 줄(Line)을 만들고 나타납니다. 즉 블록 레벨 요소 이전과 이후 요소사이의 줄을 바꿉니다. 블록 레벨 요소는 일반적으로 페이지의 구조적 요소를 나타낼 때 사용됩니다. 예를 들어 개발자는 블록 레벨 요소를 사용하여 단락(Paragraphs), 목록(lists), 네비게이션 메뉴(Navigation Menus), 꼬리말(Footers) 등을 표현할 수 있습니다. 블록 레벨 요소는 인라인 요소(Inline elements)에 중첩될(Nested inside)수 없습니다. 그러나 블록 레벨 요소는 다른 블록 레벨 요소에 중첩될 수 있습니다.
    
    ```html
    <p>fourth</p><p>fifth</p><p>sixth</p>
    ```
    
    ```textile
    fourth
    
    fifth
    
    sixth
    
    ```

- **인라인 요소**
  
  - 항상 블록 레벨 요소내에 포함되어 있습니다. 인라인 요소는 문서의 한 단락같은 큰 범위에는 적용될 수 없고 문장, 단어 같은 작은 부분에 대해서만 적용될 수 있습니다. 인라인 요소는 새로운 줄(Line)을 만들지 않습니다. 즉 인라인 요소를 작성하면 그것을 작성한 단락내에 나타나게 됩니다. 예를 들어, 인라인 요소에는 하이퍼링크를 정의하는 요소인 [`<a>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/a) , 텍스트(Text)를 강조하는 요소인 [`<em>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/em),[`<strong>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/strong) 등이 있습니다.
    
    ```html
    <em>first</em><em>second</em><em>third</em>
    
    
    ```
    
    ```textile
    firstsecondthird
    ```

- **빈 요소**
  
  - 여는 태그, 내용, 닫는 태그 패턴을 따르는 것은 아닙니다. 주로 문서에 무언가를 첨부하기 위해 단일 태그(Single tag)를 사용하는 요소도 있습니다. 예를 들어 [`<img>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/img) 요소는 해당 위치에 이미지를 삽입하기 위한 요소
    
    ```html
    <img src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/firefox-icon.png">
    ```

### 속성

- 속성은 요소에 실제론 나타내고 싶지 않지만 추가적인 내용을 담고 싶을 때 사용
  
  ```html
   <a href="https://www.mozilla.org/</a>
  ```

- 속성을 사용할 때에는 아래 내용을 지켜야 합니다:
  
  1. 요소 이름 다음에 바로 오는 속성은 요소 이름과 속성 사이에 공백이 있어야 되고, 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백이 있어야 합니다.
  2. 속성 이름 다음엔 등호(=)가 붙습니다.
  3. 속성 값은 열고 닫는 따옴표로 감싸야 합니다.

 




















































