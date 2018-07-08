#!/usr/bin/env python3
import getopt
import os
import re
import sys
from random import randint
from time import sleep
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

################################################
# TODO LIST
# 1...
################################################


################################################
# Constants
#
################################################
base_url = "http://maria.catholic.or.kr/bible/read/"
old_testment_url = "http://maria.catholic.or.kr/bible/read/bible_list.asp?m=1"
new_testment_url = "http://maria.catholic.or.kr/bible/read/bible_list.asp?m=2"
git_book_url = "https://openair.gitbook.io/korean-catholic-bible"
MAX_SLEEP_TIME = 15


def create_epub(testament_name):
    """
    gitbook 명령어로 epub 만듬

    :param testament_name:
    :return:
    """
    print("created epub file : " + testament_name + ".epub")

    if testament_name == "신약":
        html = urlopen(new_testment_url)
        bsObj = BeautifulSoup(html, "html.parser")
    if testament_name == "구약":
        pass
    if testament_name == "성경":
        pass


def request(url):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "close"
    }

    return session.get(url, headers=headers)


def create_bible_info(testament_name):
    """
    url에 접속해서 bibleInfo를 생성함. 한번만 실행하면 그이후에는 따로 할필요는 없음.

    bibileInfo = {
        "구약": {},
        "신약": {
            "ListOfContents": ["복음서", "사도행전", "서간", "묵시록"],
            "ListOfSubContents": {
                "복음": ["마태", "마르"],
                "사도행전": ["사도행전"],
                "서간": ["로마", ...],
            },
            "Books": {
                "마태": {"NumOfChapters": 28, "Url": "bible_read.asp?m=2&amp;n=147&amp;p=1"},
                "마르": {"NumOfChapters": 28, "Url": "bible_read.asp?m=2&amp;n=147&amp;p=1"}
            }
        }
    }

    :return:
    """
    bsObj = BeautifulSoup(request(old_testment_url if testament_name == "구약" else new_testment_url).content, "html.parser")

    rows = bsObj.find("table").find_all("tr")

    new_testment_list_of_contents = []
    new_testment_list_of_subcontents = {}
    new_testment_list_of_books = []
    new_testment_list_of_book_info = {}

    for row in rows:
        name_of_content = row.find("td", class_="l_tit")
        if name_of_content is not None:
            if len(new_testment_list_of_books) != 0:
                new_testment_list_of_subcontents[new_testment_list_of_contents[-1]] = new_testment_list_of_books
            new_testment_list_of_contents.append(name_of_content.get_text())
            new_testment_list_of_books = []

        book_info_list = row.find_all("td", class_="")

        index = 0
        chapter_info = {}
        for bookInfo in book_info_list:
            if bookInfo.a:
                if len(new_testment_list_of_books) == 0:
                    new_testment_list_of_subcontents[new_testment_list_of_contents[-1]] = []
                new_testment_list_of_books.append(bookInfo.get_text())
                chapter_info["Url"] = bookInfo.a['href']

            if index == 2:
                m0 = re.match(r".*\s+([0-9]+)", bookInfo.get_text())
                if m0:
                    chapter_info["TotalNumOfChapters"] = m0.group(1)
                new_testment_list_of_book_info[new_testment_list_of_books[-1]] = chapter_info

                index = 0
                chapter_info = {}
            else:
                index = index + 1

    if len(new_testment_list_of_books) != 0:
        new_testment_list_of_subcontents[new_testment_list_of_contents[-1]] = new_testment_list_of_books

    return {

        "ListOfContents": new_testment_list_of_contents,
        "ListOfSubContents": new_testment_list_of_subcontents,
        "BookInfo": new_testment_list_of_book_info
    }


def create_dir(name_dir):
    if not os.path.exists(name_dir):
        os.makedirs(name_dir)


def create_directory_based_on_info(parent_dir_name, bible_info):
    """
    bible_info 정보기반으로 폴더를 생성함

    :param parent_dir_name:
    :param bible_info:
    :return:
    """
    create_dir(parent_dir_name)

    content_count = 1
    for content_dir_name in bible_info["ListOfContents"]:
        content_path = os.path.join(parent_dir_name, str(content_count) + "_" + content_dir_name)
        create_dir(content_path)
        content_count = content_count + 1

        subcontent_count = 1
        for subcontent_dir_name in bible_info["ListOfSubContents"][content_dir_name]:
            subcontent_path = os.path.join(content_path, str(subcontent_count) + "_" + subcontent_dir_name)
            create_dir(subcontent_path)
            subcontent_count = subcontent_count + 1


def sleep_randomly():
    rand_value = randint(1, MAX_SLEEP_TIME)
    # print("sleeping for", rand_value, "secs.")
    sleep(rand_value)


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def create_subcontents(bible_info):
    """

    contents_info = {
        "창세": [
            # chap1
            [
                "t: 예수 그리스도의 족보 (루카 3,23-38)", "1 다윗의 자손이시며 아브라함의 자손이신 예수 그리스도의 족보.", "2 ..", "3 ...",
                "t: sdfsf", "1 ...", "2..."
            ],
            # chap2
            [
                "t: 예수 그리스도의 족보 (루카 3,23-38)", "1 다윗의 자손이시며 아브라함의 자손이신 예수 그리스도의 족보.", "2 ..", "3 ...",
                "t: sdfsf", "1 ...", "2..."
            ]
        ]
    }

    :param bible_info:
    :return:
    """

    contents_info = {}

    # 오경, 역사서 ...
    for content in bible_info["ListOfSubContents"]:
        print("===", content, "===")

        # 창세, 탈출 ...
        for subcontent in bible_info["ListOfSubContents"][content]:
            print("-", subcontent, "-")

            total_chapters = int(bible_info["BookInfo"][subcontent]["TotalNumOfChapters"])
            print("total_chapters", total_chapters)
            print_progress_bar(0, total_chapters, prefix='Progress:', suffix='Complete', length=50)
            # for chapter_index in range(1, total_chapters + 1):
            for chapter_index in range(1, randint(2, 4)):
                url = re.sub(r"p=1", "p=" + str(chapter_index), bible_info["BookInfo"][subcontent]["Url"])
                # print("url", url)

                sleep_randomly()

                bsObj = BeautifulSoup(request(base_url + "/" + url).content, "html.parser")
                rows = bsObj.find("table").find_all("tr")

                contents_list = []

                for row in rows:
                    # print("row", row)
                    texts = row.find_all("td", class_="al tt")
                    for text in texts:
                        # print("text", text.get_text())
                        if text.get("id") == "j":
                            contents_list.append("t:" + text.get_text().strip().replace(u'\xa0', u' '))
                        else:
                            contents_list.append(text.get("id")[1:] + " " + text.get_text().strip())

                # print("contents_list", contents_list)
                print_progress_bar(chapter_index + 1, total_chapters, prefix='Progress:', suffix='Complete', length=50)

            contents_info[subcontent] = contents_list
            # print("contents_info", contents_info)

    # print("contents_info", contents_info)
    return contents_info


def create_readme_file_for_gitbook():
    pass


def create_summary_file_for_gitbook(bible_info):
    print("bible_info", bible_info)
    with open("SUMMARY.MD", "w") as f:
        f.write("# Summary\n")
        testament_name = get_testament_name(bible_info)
        print("testament_name", testament_name)
        f.write("* [" + testament_name + "성경](" + testament_name + "/README.md)\n")
        for each_subcontent in bible_info["BookInfo"]:
            print("each_subcontent", each_subcontent)
            path = get_full_path_based_on_subcontent_name(bible_info, each_subcontent)
            print("path", path)
            f.write("\t * [" + each_subcontent + "] (" + path + ")\n")
            total_count = get_total_chapter(bible_info, each_subcontent)
            print("total_count", total_count)
            for index in range(1, total_count + 1):
                f.write("\t\t ** [Chapter" + str(index) + "](" + path + "/chap" + str(index) + ".md)\n")
        pass


def write_makeup(title, content):
    if title == "README":
        print("readme", content)
    if title == "":
        print("content", content)


def find_content_based_on_subcontent_name(bible_info, subcontent_name):
    for content_name in bible_info["ListOfSubContents"]:
        for each_subcontent in bible_info["ListOfSubContents"][content_name]:
            if each_subcontent == subcontent_name:
                return content_name


def write_readme_for_each_chapter(bible_info, subcontent_name, total_chapter, file_path):
    """
    # 마태
    {% include "./chap1.md" %}
    {% include "./chap2.md" %}
    ...

    :param bible_info:
    :param subcontent_name:
    :param total_chapter:
    :param file_path:
    :return:
    """
    content_name = find_content_based_on_subcontent_name(bible_info, subcontent_name)
    print("content_name", content_name)
    with open(file_path, "w") as f:
        f.write("# " + subcontent_name + "\n")
        for index in range(1, int(total_chapter) + 1):
            f.write("{% include ./chap" + str(index) + ".md %}\n")


def is_old_testment(bible_info):
    if "창세" in bible_info["BookInfo"]:
        return True
    else:
        return False


def get_full_path_based_on_subcontent_name(bible_info, subcontent_name):
    return get_testament_name(bible_info) + "/" + find_content_based_on_subcontent_name(bible_info,
                                                                                       subcontent_name) + "/" + subcontent_name


def get_total_chapter(bible_info, subcontent_name):
    return int(bible_info["BookInfo"][subcontent_name]["TotalNumOfChapters"])


def get_testament_name(bible_info):
    return "구약" if is_old_testment(bible_info) else "신약"


def create_makeup_based_on_subcontent_info(bible_info, subcontent_info):
    """
    creating makeup 파일
        1_복음서/1_마태/chap#.md
        1_복음서/1_마태/REAMDME.md

    :param subcontent_info:
    :return:
    """
    # print("subcontent_info", subcontent_info)
    print("bible_info", bible_info)

    for subcontent_name in subcontent_info:
        print("subcontent_name", subcontent_name)
        file_path = get_full_path_based_on_subcontent_name(bible_info, subcontent_name)
        print("file_path", file_path)

        create_dir(file_path)

        write_readme_for_each_chapter(bible_info, subcontent_name, get_total_chapter(bible_info, subcontent_info),
                                      file_path + "/README.md")

        for index, chapter in enumerate(subcontent_info[subcontent_name]):
            print((index + 1), "chapter", chapter)
            with open(file_path + "/chap" + str(index + 1) + ".md", "w") as f:

                for line in chapter:
                    if re.search("t:", line):
                        f.write("### " + line.split(":")[1].lstrip() + "\n")
                    else:
                        f.write(line + "\n")

def create_readme_file_for_testment(bible_info):
    print("bible_info", bible_info)
    testament_name = get_testament_name(bible_info)
    print("testament_name", testament_name)

    with open(testament_name + "/README.md", "w") as f:
        f.write("# " + testament_name + " 성경\n")
        for content_name in bible_info["ListOfContents"]:
            f.write("## " + content_name + "\n")
            for chapter in bible_info["ListOfSubContents"][content_name]:
                print("chapter", chapter)
                full_path = get_full_path_based_on_subcontent_name(bible_info, chapter)
                f.write("* [" + chapter + "](" + full_path + "/README.md)\n")

def create_makeup_files(bible_info, subcontent_info):
    # readme for root
    create_summary_file_for_gitbook(bible_info)

    # readme for testment
    create_readme_file_for_testment(bible_info)

    # subcontent
    create_makeup_based_on_subcontent_info(bible_info, subcontent_info)


def create_gitbook(testament_name):
    """
    웹사이트에 접속해서 전체 성경을 scrape해서 gitbook으로 만듬

    :param testament_name:
    :return:
    """
    print("testament_name", testament_name)
    bible_info = create_bible_info(testament_name)
    create_directory_based_on_info(testament_name, bible_info)
    subcontent_info = create_subcontents(bible_info)
    create_makeup_files(bible_info, subcontent_info)


def scrape_bible(format_type):
    print("format_type", format_type)

    if format_type == "epub":
        print("epub")
        # create_epub(testament_name)

    if format_type == "gitbook":
        print("gitbook")
        create_gitbook("구약")
        create_gitbook("신약")


def usage():
    print("한글 성경 EPUB 파일로 만들기")
    print("Usage: ", os.path.basename(sys.argv[0]),
          "[-h|--help] [-f|--format]")
    print("   format : [epub, gitbook]")
    print()
    print("   -h,--help                 : help 메뉴")
    print("   -f,--format               : 생성하려는 포멧 (ex. epub, pdf, mob, gitbook")
    print("   * 참조: gitbook : scrape해서 markup으로 저장함 (1회성)")
    print()
    print("Examples: ")
    print("python3 ", os.path.basename(sys.argv[0]), "-f epub")


################################################
# Main function
#
################################################

def main():
    print("sys.argv", sys.argv)
    if len(sys.argv) <= 2:
        usage()
        sys.exit(0)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:f:", ["help", "name=", "format="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    format_type = "epub"

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)

        elif opt in ("-f", "--format"):
            format_type = arg
        else:
            assert False, "unhandled option"

    scrape_bible(format_type)


if __name__ == "__main__":
    sys.exit(main())
