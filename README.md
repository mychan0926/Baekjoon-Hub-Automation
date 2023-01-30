# Baekjoon-Hub-Automation 백준 허브 자동화 프로그램
<br>
<img src="https://user-images.githubusercontent.com/98321404/215512190-9f9ec73c-ffc5-4f92-aa82-b62c0e7f6813.png" width="150" height="150">
<br>

## 제작 계기
2023년도 소프트 웨어 마에스트로를 지원 하면서 백준 허브를 통해 백준의 풀이를 깃허브로 옮기는 작업을 하였으나, 적용 이전 문제는 업로드 되지 않는 것을 확인함.
그래서 그 이전 문제를 자동으로 업로드 하고자, 백준 허브 자동화 프로그램을 제작하게 되었음.
<br><br>
## 사용 라이브러리 및 프레임 워크
pyqt5, selenium
<br><br>
## 실행 과정
<br><br>
![깃허브용](https://user-images.githubusercontent.com/98321404/215518946-2b144c40-589b-4e9a-a75b-9f93fe4505c5.png)
<br><br>
프로그램에서 사용자에게 받은 Id, Pw를 selenium을 통해 백준 사이트에 입력 후, 해결 문제 목록 가져옴.
그 후, 해결 문제 목록을 주소로 변환, 사이트로 이동 후, 백준 허브를 통해 문제 정보를 GitHub에 입력.
<br><br>
## 사용시 주의 사항
