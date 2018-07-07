#!/usr/bin/env python3
import json
import os
import shutil
import unittest
from time import sleep

import scripts.get_bible_content as bible


class BibleTest(unittest.TestCase):
    BIBLE_NAME_USED_FOR_CREATING_DIR = "테스트신약"

    def setUp(self):
        pass

    def tearDown(self):
        if os.path.isdir(self.BIBLE_NAME_USED_FOR_CREATING_DIR):
            shutil.rmtree(self.BIBLE_NAME_USED_FOR_CREATING_DIR)

    def print_dir(self):
        for root, dirs, files in os.walk(self.BIBLE_NAME_USED_FOR_CREATING_DIR):
            print("root", root, "dirs", dirs, "files", files)

    def test_create_directory(self):
        with open("./test_bible_info_구약.json") as f:
            new_testment_json = json.loads(f.read())

            bible.create_directory_based_on_info(self.BIBLE_NAME_USED_FOR_CREATING_DIR, new_testment_json)
            self.print_dir()

            self.assertTrue(os.path.isdir(self.BIBLE_NAME_USED_FOR_CREATING_DIR))

    def test_create_bible_info(self):
        expected_total = 73
        bible_info = bible.create_bible_info("구약")
        old_testment_count = len(bible_info["BookInfo"].keys())

        bible_info = bible.create_bible_info("신약")
        new_testment_count = len(bible_info["BookInfo"].keys())

        self.assertEqual(expected_total, (old_testment_count + new_testment_count))

    def test_create_subcontents(self):
        with open("./test_bible_info_구약.json") as f:
            new_testment_json = json.loads(f.read())
            bible.create_subcontents(new_testment_json)
            self.assertTrue(True)

    def test_create_makeup_based_on_subcontent_info(self):
        with open("./test_마태.json") as f:
            contents = json.loads(f.read())
            print(contents)

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
        pass

if __name__ == '__main__':
    unittest.main()
