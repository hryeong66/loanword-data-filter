# 외래어 1차 작업 필터 사용법

1. 먼저 readxlsxenv 폴더로 이동해주세요
2. `source bin/activate` 명령어를 입력하여 가상환경을 실행시켜주세요
<img width="647" alt="image" src="https://user-images.githubusercontent.com/59547116/147374402-7682cf1d-f7d9-4c8f-bc34-8913279d50bd.png">
가상환경이 실행되면 사진처럼 뜰거에요!

3. `pip3 install pandas` , `pip3 install openxlpy` 명령어를 입력하여 필요한 라이브러리를 설치해주세요
여기까지 하면 프로그램 돌릴 준비가 되었습니다!


### ▶️ 프로그램 돌리기 전, 엑셀 파일에 사전작업을 조금 해야합니다😥
<img width="344" alt="image" src="https://user-images.githubusercontent.com/59547116/147374426-e67a4dc0-2842-4f44-b2d5-379a112b1db0.png">
엑셀에서 문장이 있는 열 맨 위에 '스크립트' 라느 단어를 꼭 넣어주셔야합니다!   

그리고 만약 시트가 여러 개라면 첫번때 있는 시트에 데이터를 옮겨놓아주세요 :)

그 후 작업할 엑셀 파일을 data 폴더 안으로 이동시켜주세요

<img width="205" alt="image" src="https://user-images.githubusercontent.com/59547116/147374447-7cae462c-9931-43fe-be06-1ab6cfb440b9.png">
사진처럼 파일명을 한글을빼고 영어+숫자 조합으로 파일명을 변경하는게 터미널에서 파일명을 입력했을때 오류가 덜납니다!
(그냥 복붙하는 경우에는 괜찮습니다! 터미널에서 입력할 때는 잘 안되더라구여,,)

여기까지가 사전작업입니다!

### ▶️ 프로그램 실행

`python3 source.py` 명령어를 입력하며 프로그램이 돌아갑니다

<img width="646" alt="image" src="https://user-images.githubusercontent.com/59547116/147374544-21f967f8-ce29-4ceb-ba6c-d10e4705d7a0.png">

사진과 같은 문구가 터미널에 뜨기 전까지 조금만 기다려주세요:)

이제 파일명을 입력해주시며 됩니다!


<img width="649" alt="image" src="https://user-images.githubusercontent.com/59547116/147374556-08f82254-6660-4cd4-9bec-31e584abd4da.png">

사진처럼 뒤에 .xlsx 확장하는 제외하고 파일명만 입력해주시면 됩니다!

<img width="535" alt="image" src="https://user-images.githubusercontent.com/59547116/147374725-49114480-afcd-4417-9afa-5da71aadd4d2.png">


해당 파일의 작업이 끝나면 다음 파일명을 입력하라는 문구가 뜨는데요, 다음 작업할 파일명을 입력해주시면 됩니다!

작업을 끝내시려면 `q`를 눌러주시면됩니다.

### ▶️ 가상환경 종료
`deactivate`를 입력하시면 가상환경이 종료됩니다


### ▶️ 마지막으로
작업하시기 전에 `dictionary.xlsx` 파일은 최신화 시키는걸 추천드립니다!

그리고 해당 프로그램은 외래어 작업을 조금이라도 돕기 위해 만들어진 것이니

1. 현재 있는 단어 외에 다른 외래어가 있다면 최대한 그 외래어로 하기
2. 꼼꼼한 검수는 필수 이건 정말 아주 간단한 1차 작업정도로만 생각하기

이 2가지를 꼭 지켜주시길 부탁드립니다!


다들 행복작업하세요 :)

