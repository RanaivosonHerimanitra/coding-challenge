Insight Data Engineering - Coding Challenge (my solution)
===========================================================

## Package dependencies:

You will need to install `numpy` and `pandas` :

* `pip install numpy`

* `pip install pandas`

## To run the script:
On the cli inside `coding-challenge` directory, enter: 

`bash run.sh` 
(ensure you have correct permission otherwise add `sudo` before `bash`)

## Unit Tests:

* Test for two consecutive tweets with no hashtag passed! Expected output `0.00`, `0.00`

* Test for two consecutive tweets with 02 hashtags with exactly the same hashtags passed! Expected output `1.00`, `1.00`

## Details implementation:

1. a function reads data from `tweets.txt` and parse it so that built-in function from `pandas` package can easily transform it into a dataframe.

2. a function  extracts hashtags for each tweet and store them in a `python list`. This `python list` has exactly the same length as the `timestamp list` to ensure time
consistency during streaming.

3. a third function handles streaming of tweets by calling 03 functions.

 * First tweet is processed then first 02 tweets then first three tweets and so on until the `n` tweets.

 * First function of this streaming process ensures that tweets currently processed belong to 60 seconds most recent tweets.

 * Second function of this streaming process generates graph (a dictionnary data structure in `python`) that corresponds to current tweets.

 * Third function of this streaming process calculates average degree of current nodes (each node corresponds to a `hashtag`, each node corresponds to a key of the dictionnary where values are list connected nodes ):

 * The idea of the calculation is to replace values of each key by their number(#) of elements then average the all. 



