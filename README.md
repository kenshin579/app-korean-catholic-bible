가톨릭 성경 ebook format (epub) 만들기
======

목표
- 성경을 전자책(ex. 리디북스 페이퍼)에서도 읽을 수 있도록 여러 포멧(ex. epub, pdf)을 생성한다.  

Feature
- 명령어 실행으로 전자책 포맷(ex. epub) 생성하기  

필요한 패키지 설치
1.gitbook-cli 설치
~~~
$ npm i gitbook-cli -g
~~~
2.cablire 설치
- calibre는 ebook manager 
~~~
$ brew cask install calibre
~~~

실행하기 
1.성경 구약성경 epub으로 생성하기
~~~
$ cd ./scripts
$ gitbook epub ../ ../_build/bible.epub
~~~
  
2.GITBOOK 사아트에서 성경을 읽을 수 있도록 개인 github에 업로드하기  

gitbook 서버 실행후 browser에서 보기 
~~~
$ gitbook serve 
~~~
