#!/usr/bin/python
import sys

## here are directories of each test:
dir1= "./insight_testsuite/tests/test-2-tweets-nohashtag/tweet_output/output.txt"
dir2="./insight_testsuite/tests/test-2-tweets-all-equal/tweet_output/output.txt"
dir3="./insight_testsuite/tests/test-2-tweets-morethan60s-timediff/tweet_output/output.txt"

## here is the program to test 02 tweets with no hashtag
if dir1==sys.argv[1]:
	error=0;
	with open (sys.argv[1], 'r') as f :
		for i in f:
			if str(i.rstrip())=="0.00":
				print("test passed!")
			else:
				error=1
				print("test failed!")

## here is the program to test 02 tweets with all equal hashtags
if dir2==sys.argv[1]:
	error=0;
	with open (sys.argv[1], 'r') as f :
		for i in f:
			if str(i.rstrip())=="1.00":
				print("test passed!")
			else:
				error=1
				print("test failed!")

## here is the program to test 02 tweets (with no empty hashtags) spaced with more
## than 60 seconds interval:			
if dir3 ==sys.argv[1]:
	output_value=[]
	with open(sys.argv[1],'r') as f:
		for i in f:
			output_value.append(str(i.rstrip()))
	expected_output_value = ["1.00","3.00"]
	for p,q in zip(output_value,expected_output_value):
		if p==q:
			print ("test passed!")
		else:
			print("test failed!")





