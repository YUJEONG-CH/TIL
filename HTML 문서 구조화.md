웹 05_ 0905  복습

# HTML 문서 구조화

- table의 영역을 <thead>, <tbody>, <tfoot> 요소로 표현
  
  | ID  | Name | Major    | <mark>thead</mark> |
  | --- | ---- | -------- | ------------------ |
  | 1   | 홍길동  | computer | <mark>tbody</mark> |
  | 2   | 김철수  | business |                    |
  | 총계  |      | 2명       | <mark>tfoot</mark> |

- <tr>로 가로 줄 구성, 내부는 <th> 또는 <td>로 셀 구성

- colspan, rowspan 속성을 활용해 셀 병합 ```colspan="2"```

- <caption>을 통해 표 설명 또는 제목을 나타냄

- table 태그 기본 구성
  
  - thead
    
    - tr > th
  
  - tbody
    
    - tr > td
  
  - tfoot
    
    - tr > td
  
  - caption            

- ```html
  
          </thead>
          <tbody>
              <tr>
                  <td>1</td>
                  <td>홍길동</td>
                  <td>computer</td>
              </tr>
              <tr>
                  <td>2</td>
                  <td>김철수</td>
                  <td>비즈니</td>
              </tr>
          </tbody>
          <tfoot>
             <tr>
                  <td>총</td>
                  <td colspan="2">2명</td>
              </tr>
          </tfoot>
          <caption> 1 반 학생명
           </table>
  </body>        
  ```

# form

- <form>은 데이터를 서버에 제출하기 위해 사용하는 태그

- 기본속성
  
  - action : form을 처리할 서버의 URL (데이터를 보낼 곳)
  
  - method: form을 제출할 때 사용하는 HTTP메서드 (GET 혹은 POST)
  
  - enctype: method가 post인 경우 데이터의 유형
    
    - application/x-www-form-urlencoded: 기본값
    
    - multipart/form-data: 파일 전송시 (input type이 file인 경우)

- ```html
  <form action="/search" method="GET">
  </form>
  ```

# input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

- <input> 대표적인 속성
  
  - name: form control에 적용되는 이름 (이름/값 페어로 전송됨)
  
  - value: form control에 적용되는 값 (이름/값 페어로 전송됨)
  
  - required, readonly, autofocus, autocomplete, disabled 등

- ```html
  <form action="/search" method="GET">
      <input type="text" name="q">
  </form>
  ```

``` https://www.google.com/search?q=HTML```

# input label

- label을 클릭해 input 자체에 초점을 맞추거나 활성화 시킬 수 있음
  
  - 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일(터치) 환경에서 편하게 사용할 수 있음label과 input입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인 할 수 있도록 함

- <input>에 id 속성을, <label>에는 for속성을 활용해 상호연관을 시킴

- ```html
  <label for="agreement">개인정보 수집에 동의함</label>
  <input type="checkbox" name="agreement" id="agreement">
  ```

# input 유형 - 일반

- 일반적으로 입력을 받기 위해 제공되며 타입별로 html 기본 검증 혹은 추가 속성을 활용할 수 있음
  
  - text: 일반 텍스트 입력
  
  - password: 입력 시 값이 보이지 않고 문자를 특수기호로(*)로 표현
  
  - email: 이메일 형식이 아닌 경우 form 제출 불가
  
  - number: min, max, step 속성을 활용해 숫자 범위 설정 가능
  
  - file: accept 속성을 활용해 파일 타입 지정 가능

# input 유형 - 항목 중 선택

- 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함

- 동일 항목에 대해서는 name 을 지정하고 선택된 항목에 대한 value를 지정해야 함
  
  - checkbox: 다중선택
  
  - radio : 단일 선택
    
    ```html
    <div>
        <p> checkbox </p>
        <input id="html" type="checkbox" name="language" value="html">
        <label for="html"> HTML </label>
        <input id ="python" type="checkbox" name="language" value="python">
        <label for="python">파이썬</label>
    </div>
    ```

# input  유형 - 기타

- 다양한 종류의 input을 위한 picker 제공
  
  - color: color picker
  
  - date: date picker

- hidden input을 활용해 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  
  - hidden: 사용자에게 보이지 않는 input







# Bootstrap 활용하기

- **CDN** (Content Delivery (Distribution) Network)
  
  -  컨텐츠 (CSS, JS, Image, Text 등) 을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템
  
  - 개별 end-user 의 가까운 서버를 통해 빠르게 전달 가능 (지리적 이점)
  
  - 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

- **spacing** (margin and padding)
  
  - {property}{sides}-{size}
    
    ``mt-3``
  
  - ```html
    <div class="mt-3 ms-5"> bootstrap-spacing </div>
    ```
  
  - **<mark>{property}</mark>**{sides}-{size}
    
    - **m**- for classes that set **margin**
    
    - **p**- for classes that set **padding**
  
  - {property}**<mark>{sides}</mark>**-{size}
    
    - **t**- for classes that set **margin top** or **padding top**
    
    - **b**- for classes that set **margin-bottom** or **padding-bottom**
    
    - **s**-(start) for classes that set **margin-left** or **padding-left** in LTR, **margin-right** or** padding-right** in RTL
    
    - **e**-(end) for classes that set **margin-right** or **padding right** in LTR, **margin-left** or** paddin-left** in RTL
    
    - **x** - for classes that set both ***-left** and ***-right**
    
    - **y** - for classes that sest both ***-top** and ***-bottom**
    
    - blank - for classes that set a **margin**or **padding** on all 4 sides of the element
  
  - {property}{sides}**<mark>-{size}</mark>**
    
    - **0** - for classes that **eliminate the margin or padding**by setting it to 0
    
    - **1** - (by default) for classes that set the **margin** or **padding** to **$spacer *.25**
    
    - **2 - (by default) for classes that set the **margin** or **padding** to **$spacer*.5**
    
    - 3** - (by default) for classes that set the **margin** or **padding** to **$spacer**
    
    - **4 - (by default) for classes that set the **margin** or **padding** to **$spacer *1.5**
    
    - **5** - (by default) for classes that set the **margin** or **padding** to **$spacer *.3**
    
    - **auto** - for classes that set the **margin** to auto
  
  - **<mark><정리></mark>**
  
  - | class name | rem  | px  |
    |:----------:|:----:|:---:|
    | m-1        | 0.25 | 4   |
    | m-2        | 0.5  | 8   |
    | m-3        | 1    | 16  |
    | m-4        | 1.5  | 24  |
    | m-5        | 3    | 48  |
    
    
  
  - **.mx-0 ?**  : 가로(왼쪽, 오른쪽) margin 이 0
    
    ```css
    .mx-0{
        margin-right: 0 !important;
        margin-left: 0 !important;
    }
    ```
  
  - **.mx-auto** : 블록 요소 수평중앙정렬, 가로 가운데 정렬
    
    ```css
    .mx-auto{
        margin-right: auto !important;
        margin-left: auto !important;
    }
    ```
  
  - **.py-0** : 위 아래 padding이 0
    
    ```css
    .py-0{
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }     
    ```
