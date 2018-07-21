가톨릭 성경 ebook format (epub) 만들기
======
성경을 전자책(ex. 리디북스 페이퍼)에서도 읽을 수 있도록 여러 포맷(ex. epub, pdf)으로 생성한다  

## 목차
   * [가톨릭 성경 ebook format (epub) 만들기](#가톨릭-성경-ebook-format-epub-만들기)
      * [Features](#features)
      * [추가 작업목록 - 2차 (누구나 참여 가능합니다)](#추가-작업목록---2차-누구나-참여-가능합니다)
      * [필요한 패키지 설치](#필요한-패키지-설치)
         * [1. python 설치](#1-python-설치)
         * [2. gitbook 관련 파일 설치](#2-gitbook-관련-파일-설치)
         * [3. 실행하기](#3-실행하기)


## Features
- 전체 성경책 내용을 웹에서 scraping 해준다.
- 명령어 실행으로 여러 전자책 포맷(ex. epub)을 생성한다. 

<a href="/images/ibooks_%EC%BB%A4%EB%B2%84.png" target="_blank">
<img src="/images/ibooks_%EC%BB%A4%EB%B2%84.png" width="200" /></a>
<a href="/images/ibooks_%EB%AA%A9%EC%B0%A8.png" target="_blank">
<img src="/images/ibooks_%EB%AA%A9%EC%B0%A8.png" width="200" /></a>
<a href="/images/ibooks_%EC%B0%BD%EC%84%B81%EC%9E%A5.png" target="_blank">
<img src="/images/ibooks_%EC%B0%BD%EC%84%B81%EC%9E%A5.png" width="200" /></a>
<br>
<a href="/images/ridibooks_%EC%BB%A4%EB%B2%84.jpg" target="_blank">
<img src="/images/ridibooks_%EC%BB%A4%EB%B2%84.jpg" width="200" /></a>
<a href="/images/ridibooks_%EB%AA%A9%EC%B0%A8.jpg" target="_blank">
<img src="/images/ridibooks_%EB%AA%A9%EC%B0%A8.jpg" width="200" /></a>
<a href="/images/ridibooks_%EC%B0%A8%EB%A1%80.jpg" target="_blank">
<img src="/images/ridibooks_%EC%B0%A8%EB%A1%80.jpg" width="200" /></a>
<a href="/images/ridibooks_%EC%B0%BD%EC%84%B81%EC%9E%A5.jpg" target="_blank">
<img src="/images/ridibooks_%EC%B0%BD%EC%84%B81%EC%9E%A5.jpg" width="200" /></a>

## 추가 작업목록 - 2차 (누구나 참여 가능합니다)
- [ ] 영어 성경도 스크래핑하기 (여러 버전이 많음)
  - gitbook에서 multi 언어 지원을 하고 있음 (참고: https://toolchain.gitbook.com/languages.html)
- [ ] 공동성서도 스크래핑하기
- [ ] epub cover image 추가하기 (참고 : https://toolchain.gitbook.com/ebook.html#cover)  

## 필요한 패키지 설치
- 실행 환경은 mac 기반으로 작성되었습니다.  

### 1. python 설치
- script 실행을 위해 python3을 설치한다
~~~
$ brew install python3
~~~

### 2. gitbook 관련 파일 설치
1.먼저 node를 설치한다
~~~
$ brew install node
~~~
2.gitbook-cli 설치
- gitbook으로 여러 포맷을 생성하기 위해 global로 gitbook 명령어를 설치한다.
~~~
$ npm i gitbook-cli -g
~~~
3.cablire 설치
- calibre는 gitbook에서 pdf로 렌더링할 때 필요한 프로그램이다. 
~~~
$ brew cask install calibre
$ ln -s /Applications/calibre.app/Contents/MacOS/ebook-convert /usr/local/bin
~~~

### 3. 실행하기 
```
$ cd scripts
$ ./get_bible_content.py -h
한글 성경 EPUB 파일로 만들기
Usage:  get_bible_content.py [-h|--help] [-f|--format] destination folder
   format : [epub, gitbook]

   -h,--help                 : help 메뉴
   -f,--format               : 생성하려는 포멧 (ex. epub, pdf, mob, gitbook
   * 참조: gitbook : scrape해서 markup으로 저장함 (1회성)

Examples: 
python3  get_bible_content.py -f epub ../

```
1.성경 내용 scraping 하기
- 웹 서버에 많은 부하를 주지 않기 위해서 scraping 할때 time sleep을 주기 때문에 전체 성경을 가져오는 대는 시간이 걸린다. 
~~~
$ cd ./scripts
$ ./get_bible_content.py -f gitbook ../
~~~
2.웹 스크래핑한 성경을 epub나 pdf로 생성하기 
~~~
$ cd ./scripts
$ ./get_bible_content.py -f epub ../
$ open ../build/bible.epub

$ ./get_bible_content.py -f pdf ../
$ open ../build/bible.pdf
~~~ 
3.웹 스크래핑한 내용을 로컬 서버에서 실행해서 브라우져에서 확인하기
- 웹 스크래핑한 내용을 github에 commit하면 gitbook.com 사이트에서도 확인이 가능하다
~~~
$ gitbook serve 
~~~
<a href="/images/gitbook_serve.png" target="_blank">
<img src="/images/gitbook_serve.png" width="350" /></a>
