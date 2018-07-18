가톨릭 성경 ebook format (epub) 만들기
======

## Goal
- 성경을 전자책(ex. 리디북스 페이퍼)에서도 읽을 수 있도록 여러 포맷(ex. epub, pdf)으로 생성한다  

### Feature
- 전체 성경책 내용을 웹에서 scraping 해준다.
- 명령어 실행으로 여러 전자책 포맷(ex. epub)을 생성한다. 

<a href="/images/ibooks_%EC%BB%A4%EB%B2%84.png" target="_blank">
<img src="/images/ibooks_%EC%BB%A4%EB%B2%84.png" width="340" /></a>
<a href="/images/ibooks_%EB%AA%A9%EC%B0%A8.png" target="_blank">
<img src="/images/ibooks_%EB%AA%A9%EC%B0%A8.png" width="340" /></a>
<a href="/images/ibooks_%EC%B0%BD%EC%84%B81%EC%9E%A5.png" target="_blank">
<img src="/images/ibooks_%EC%B0%BD%EC%84%B81%EC%9E%A5.png" width="340" /></a>

<a href="/images/ibooks_%EC%BB%A4%EB%B2%84.png" target="_blank">
<img src="/images/ibooks_%EC%BB%A4%EB%B2%84.png" width="340" /></a>
<a href="/images/ibooks_%EB%AA%A9%EC%B0%A8.png" target="_blank">
<img src="/images/ibooks_%EB%AA%A9%EC%B0%A8.png" width="340" /></a>
<a href="/images/ibooks_%EC%B0%A8%EB%A1%80.png" target="_blank">
<img src="/images/ibooks_%EC%B0%A8%EB%A1%80.png" width="340" /></a>
<a href="/images/ibooks_%EC%B0%BD%EC%84%B81%EC%9E%A5.png" target="_blank">
<img src="/images/ibooks_%EC%B0%BD%EC%84%B81%EC%9E%A5.png" width="340" /></a>


#### 코멘트
- 맥 시스템 기반으로 작성되었습니다.
  


#### 필요한 패키지 설치
##### 1. python 설치
- python3 설치


##### 2. gitbook관련 파일 설치
1. 먼저 node를 설치한다
~~~
$ brew install node
~~~
1. gitbook-cli 설치
- gitbook으로 여러 포맷을 생성하기 위해 먼저 gitbook 명령어를 설치한다.
~~~
$ npm i gitbook-cli -g
~~~
2. cablire 설치
- calibre는 ebook manager 
~~~
$ brew cask install calibre
~~~

#### 실행하기 
```
한글 성경 EPUB 파일로 만들기
Usage:  get_bible_content.py [-h|--help] [-f|--format] destination folder
   format : [epub, gitbook]

   -h,--help                 : help 메뉴
   -f,--format               : 생성하려는 포멧 (ex. epub, pdf, mob, gitbook
   * 참조: gitbook : scrape해서 markup으로 저장함 (1회성)

Examples: 
python3  get_bible_content.py -f epub ../

```
1. 성경 내용 scraping 하기
- 웹 서버에 많은 부하를 주지 않기 위해서 scraping 할때 time sleep을 줘서 전체 성경을 가져오는대는 시간이 걸린다. 
```bash
$ cd ./scripts
$ cd ./scripts
```
$ cd ./scripts
$ ./get_bible_content.py -f epub ../
~~~
2.성경 구약성경 epub으로 생성하기
~~~
$ cd ./scripts
$ ./get_bible_content.py -f epub ../
~~~
  
2.GITBOOK 사아트에서 성경을 읽을 수 있도록 개인 github에 업로드하기  

gitbook 서버 실행후 browser에서 보기 
~~~
$ gitbook serve 
~~~


#### Credit

