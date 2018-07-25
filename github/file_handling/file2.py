"""whether the files exist"""
import os, sys
if os.path.isfile("file2.py"):
    print("file is present")
else:
    print("not there bro")
    sys.exit()

