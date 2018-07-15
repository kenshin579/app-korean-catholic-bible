#!/usr/bin/env python3
import json
import os
import shutil
import unittest
from time import sleep

import scripts.get_bible_content as bible


class BibleTest(unittest.TestCase):
    TESTAMENT_NAME_USED_FOR_CREATING_DIR = "테스트신약"
    ROOT_DIR = "./test"

    def setUp(self):
        pass

    def tearDown(self):
        if os.path.isdir(self.TESTAMENT_NAME_USED_FOR_CREATING_DIR):
            shutil.rmtree(self.TESTAMENT_NAME_USED_FOR_CREATING_DIR)

    def print_dir(self):
        for root, dirs, files in os.walk(self.TESTAMENT_NAME_USED_FOR_CREATING_DIR):
            print("root", root, "dirs", dirs, "files", files)

    def test_create_directory(self):
        with open("./test_bible_info_구약.json") as f:
            new_testment_json = json.loads(f.read())

            bible.create_directory_based_on_info(self.TESTAMENT_NAME_USED_FOR_CREATING_DIR, new_testment_json,
                                                 self.ROOT_DIR)
            self.print_dir()

            self.assertTrue(os.path.isdir(self.TESTAMENT_NAME_USED_FOR_CREATING_DIR))

    def test_create_bible_info(self):
        expected_total = 73
        testament_info = bible.create_testament_info("구약")
        old_testment_count = len(testament_info["BookInfo"].keys())

        testament_info = bible.create_testament_info("신약")
        new_testment_count = len(testament_info["BookInfo"].keys())

        self.assertEqual(expected_total, (old_testment_count + new_testment_count))

    def test_create_subcontents(self):
        with open("./test_bible_info_구약.json") as f:
            new_testment_json = json.loads(f.read())
            content_info = bible.create_subcontents(new_testment_json)
            print("content_info", content_info)

    def test_create_makeup_based_on_subcontent_info(self):
        with open("./test_subcontent_구약2.json") as s, open("./test_bible_info_구약.json") as b:
            testament_info = json.loads(b.read())
            subcontent_info = json.loads(s.read())
            bible.create_markup_based_on_subcontent_info(testament_info, subcontent_info, self.ROOT_DIR)

    def test_create_readme_file_for_testment(self):
        with open("./test_bible_info_구약.json") as b:
            testament_info = json.loads(b.read())
            bible.create_dir(os.path.join(self.ROOT_DIR, "구약"))
            bible.create_readme_file_for_testment(testament_info, self.ROOT_DIR)

    def test_create_summary_file_for_gitbook(self):
        with open("./test_bible_info_구약.json") as b:
            testament_info = json.loads(b.read())
            bible.create_summary_file_for_gitbook(testament_info, self.ROOT_DIR)

    def test_print_progress_bar(self):
        # bible.print_progress_bar()

        # A List of Items
        items = list(range(0, 57))
        l = len(items)

        # Initial call to print 0% progress
        bible.print_progress_bar(0, l, prefix='Progress:', suffix='Complete', length=50)
        for i, item in enumerate(items):
            # Do stuff...
            sleep(1)
            # Update Progress Bar
            bible.print_progress_bar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)

if __name__ == '__main__':
    unittest.main()
