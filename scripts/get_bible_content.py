#!/usr/bin/env python3
import getopt
import os
import sys
from urllib.request import urlopen

from bs4 import BeautifulSoup

################################################
# TODO LIST
# 1...
################################################


################################################
# Constants
#
################################################
oldTestmentUrl = "http://maria.catholic.or.kr/bible/read/bible_list.asp?m=1"
newTestmentUrl = "http://maria.catholic.or.kr/bible/read/bible_list.asp?m=2"
gitBookUrl = "https://openair.gitbook.io/korean-catholic-bible"


def create_epub(bibleName):
    """
    gitbook 명령어로 epub 만듬

    :param bibleName:
    :return:
    """
    print("created epub file : " + bibleName + ".epub")

    if bibleName == "신약":
        html = urlopen(newTestmentUrl)
        bsObj = BeautifulSoup(html, "html.parser")
    if bibleName == "구약":
        pass
    if bibleName == "성경":
        pass


def create_bible_info():
    """
    create directory based on bibleInfo

    :return:
    """
    bibleInfo = {}
    # 신약

    html = urlopen(newTestmentUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    titleList = bsObj.findAll("td", {"class": "l_tit"})

    # for titleName in titleList:
    #     print("titleName", titleName.get_text())

    for tableRow in bsObj.find("table").tr.next_siblings:
        print(tableRow)

    # print("bookList", bookList)

    # 구약

    return {}


def create_irectory(bibleInfo):
    pass


def create_git_book(bibleName):
    """
    웹사이트에 접속해서 전체 성경을 scrape해서 gitbook으로 만듬

    :param bibleName:
    :return:
    """
    print("created gitbook")
    print("gitBookUrl: ", gitBookUrl)

    bibleInfo = create_bible_info()
    create_irectory(bibleInfo)


def scrape_bible(formatType, bibleName):
    print("formatName", formatType, "bibleName", bibleName)

    if formatType == "epub":
        print("epub")
        create_epub(bibleName)

    if formatType == "gitbook":
        print("gitbook")
        create_git_book(bibleName)


def usage():
    print("한글 성경 EPUB 파일로 만들기")
    print("Usage: ", os.path.basename(sys.argv[0]),
          "[-h|--help] [-n|--name] [-n|--name]")
    print("   name: [성경, 구약, 신약]")
    print("   format : [epub, gitbook]")
    print()
    print("   -h,--help                 : help 메뉴")
    print("   -n,--name                 : 생성하려는 성경이름 (ex. 성경, 구약, 신약)")
    print("   -f,--format               : 생상하려는 포멧 (ex. epub, pdf, mob, gitbook")
    print("   * 참조: gitbook : scrape해서 markup으로 저장함 (1회성)")
    print()
    print("Examples: ")
    print("python3 ", os.path.basename(sys.argv[0]), "-n new -f epub")


################################################
# Main function
#
################################################

def main():
    print("sys.argv", sys.argv[-1])
    if len(sys.argv) <= 4:
        usage()
        sys.exit(0)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:f:", ["help", "name=", "format="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    bible_name = "성경"
    format_type = "epub"

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)

        elif opt in ("-n", "--name"):
            bible_name = arg
        elif opt in ("-f", "--format"):
            format_type = arg
        else:
            assert False, "unhandled option"

    scrape_bible(format_type, bible_name)


if __name__ == "__main__":
    sys.exit(main())
