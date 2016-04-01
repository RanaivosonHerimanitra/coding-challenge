#!/usr/bin/python
cd ..

#run first test
python ./src/average_degree.py ./insight_testsuite/tests/test-2-tweets-nohashtag/tweet_input/tweets.txt  ./insight_testsuite/tests/test-2-tweets-nohashtag/tweet_output/output.txt

#should get 0.00 (first tweet), 0.00 (first 02 tweets)
python ./insight_testsuite/check_tests.py ./insight_testsuite/tests/test-2-tweets-nohashtag/tweet_output/output.txt


