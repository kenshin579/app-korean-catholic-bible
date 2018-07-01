가톨릭 성경 ebook format (epub) 만들기 
======

목표
- 성경을 전자책(ex. 리디북스 페이퍼)에서 읽을 수 있도록 EPUB 포멧을 생성한다. 

Feature
- 명령어 실행으로 EPUB을 생성
  * 옵션 : 구약따로, 신약 따로 아니면 전체 성경 생성가능 
- 온라인 상에서 성경 읽기 (GITBOOK) 
  * 이건 한번한 하면 된다

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
3.(옵션) pandoc 설치
- pandoc은 한 markup 포멧에서 다른 포멧(ex.docx)으로 변환할때 사용함
~~~
$ brew install pandoc
~~~

실행하기 
 

1.성경 구약성경 epub으로 생성하기
~~~
$ gitbook epub ./ _build/bible.epub
~~~
2.전자책에 업로드
 * SD 카드로 복사해서 사용하시면 될 것 같습니다.  
  
3.GITBOOK에서 읽을 수 있도록 개인 github에 업로드하기  

환경에서 실행
~~~
$ gitbook serve 
~~~
