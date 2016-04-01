#!/usr/bin/python
import sys
dir1= "./insight_testsuite/tests/test-2-tweets-nohashtag/tweet_output/output.txt"
if dir1==sys.argv[1]:
	error=0;
	with open (sys.argv[1], 'r') as f :
		for i in f:
			if str(i.rstrip())=="0.00":
				print("test passed!")
			else:
				error=1
				print("test failed!")



