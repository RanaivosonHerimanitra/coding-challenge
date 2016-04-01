#!/usr/bin/python
cd ..

####################################### test 1 ###############################
#test for two tweets with no hashtag:
python ./src/average_degree.py ./insight_testsuite/tests/test-2-tweets-nohashtag/tweet_input/tweets.txt  ./insight_testsuite/tests/test-2-tweets-nohashtag/tweet_output/output.txt
#should get 0.00 (first tweet), 0.00 (first 02 tweets)
python ./insight_testsuite/check_tests.py ./insight_testsuite/tests/test-2-tweets-nohashtag/tweet_output/output.txt


###################################### test 2 ###############################
#test for two tweets with exactly the same tag:
python ./src/average_degree.py ./insight_testsuite/tests/test-2-tweets-all-equal/tweet_input/tweets.txt  ./insight_testsuite/tests/test-2-tweets-all-equal/tweet_output/output.txt
#should get 1.00 (first tweet), 1.00 (first 02 tweets)
python ./insight_testsuite/check_tests.py ./insight_testsuite/tests/test-2-tweets-all-equal/tweet_output/output.txt

###################################### test 3 ##############################
#test 02 tweets with more than 60 seconds difference in time:
python ./src/average_degree.py ./insight_testsuite/tests/test-2-tweets-morethan60s-timediff/tweet_input/tweets.txt  ./insight_testsuite/tests/test-2-tweets-morethan60s-timediff/tweet_output/output.txt
#should get 1.00 (first tweet), 3.00 (last tweet, first one should be evicted)
python ./insight_testsuite/check_tests.py ./insight_testsuite/tests/test-2-tweets-morethan60s-timediff/tweet_output/output.txt


