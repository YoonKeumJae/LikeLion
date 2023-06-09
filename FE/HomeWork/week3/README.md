# React를 활용한 웹페이지

React를 활용한 간단한 웹페이지입니다.

홈 화면이 존재하고, 리스트의 항목을 누르면 설명을 읽을 수 있습니다. 

항목의 생성과 업데이트 또한 가능합니다. 

<br>

# 코드 리뷰: 강병준님

### 1. 고칠 사항

- `setTopics([...topics, { id: nextId, title, body }]);` 를 `setTopics((prevTopics)=>[...prevTopics, { id: nextId, title, body }]); `의 형식으로 고치는게 좋습니다. 간단한 코드의 경우 문제가 없지만, 조금 더 복잡한 코드의 경우에는 문제가 생길 수 있습니다. 이전 상태의 값을 매개변수로 가져와서 새로운 정보들을 추가하는 방식으로 코드를 작성하는 것이 좋습니다.

- 세미콜론(;)을 붙이는 것이 좋습니다. 자바스크립트는 세미콜론을 붙이지 않아도 동작하지만, 세미콜론을 붙이지 않으면 코드가 동작하지 않는 경우가 생길 수 있습니다. 따라서 세미콜론을 붙이는 것이 좋습니다.

- WELCOME, CREATE 등의 모드를 상수로 정해주는 것이 좋습니다. 오타가 발생할 확률이 줄어들고 단축키를 사용할 수 있습니다.

- input태그 대신 form태그를 사용하는 것이 좋습니다. 지금 당장은 문제가 없지만, 백엔드와 함께 작업할 때 데이터를 넘겨줘야 하기 때문입니다. 

- 간단한 화살표 함수는 굳이 개행하기 보다는 한줄로 쓰는게 좋습니다. 

- 사용자가 입력하는 칸에 공백을 입력하는 경우에 대해 예외처리를 해주는 것이 좋습니다.

- props보다 구조분해할당을 사용하는 것이 좋습니다. 꼭 그래야 하는 것은 아니지만, 코드의 가독성을 좋게 해줍니다. 

- `import React from 'react'`는 더이상 사용하지 않아도 됩니다. 

### 2. 질문한 사항

- `@param`의 뜻이 무엇인가요? 

-> 주석과 같은 역할을 합니다. 함수의 매개변수를 설명할 때 사용합니다.

- id를 selectedId로 바꾼 이유가 무엇인가요?

-> 더 직관적이고 가독성이 좋습니다. 

- Form.js를 사용한 이유가 무엇인가요?

-> 코드의 중복을 줄일 수 있니니다. 

- || 연산자의 의미가 무엇인가요?

-> 연산자 앞의 값이 false일 경우 뒤의 값을 사용합니다.