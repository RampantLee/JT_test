# encoding: utf-8
import os


def print_directory_contents(spath):
    for schild in os.listdir(spath):
        sChildPath = os.path.join(spath, schild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents("D:\\test_script\\Test_script_summary\\9.X_trans_test")