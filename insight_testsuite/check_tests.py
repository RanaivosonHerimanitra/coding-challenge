#!/usr/bin/python
import sys
dir1= "./insight_testsuite/tests/test-2-tweets-nohashtag/tweet_output/output.txt"
dir2="./insight_testsuite/tests/test-2-tweets-all-equal/tweet_output/output.txt"
if dir1==sys.argv[1]:
	error=0;
	with open (sys.argv[1], 'r') as f :
		for i in f:
			if str(i.rstrip())=="0.00":
				print("test passed!")
			else:
				error=1
				print("test failed!")
if dir2==sys.argv[1]:
	error=0;
	with open (sys.argv[1], 'r') as f :
		for i in f:
			if str(i.rstrip())=="1.00":
				print("test passed!")
			else:
				error=1
				print("test failed!")




