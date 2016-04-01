#!/usr/bin/python
import pandas as pd 
import numpy as np

### Function that correctly parse json format from tweets.txt using pandas ####
### and select field/entity of interests , here: "id","created_at" and "entities"
def read_json_tweets(pathname):
	# read the entire file into a python array
	with open(pathname, 'rb') as f:
		data = f.readlines()
	# remove the trailing "\n" from each line
	data = map(lambda x: x.rstrip(), data)
	data_json= "[" + ','.join(data) + "]";
	# now, load it into pandas
	data_json = pd.read_json(data_json);
	return data_json[['created_at','id','entities']]

###############################################################################
# process hashtags,date of creation into arrays:
# The idea is to have one list of hashtag per Id
# so for each Id, gather into a list all hashtags
def process_hashtags_into_array(df):
	#loop thru  id of users
	id_users= df['id']
	#store output (final)
	hashtags_text=[];
	#only store non empty hashtags
	non_empty_hashtags_content=[]
	for ids in id_users:
		for entity in df[df.id==ids]['entities']:
			# if type is dict and non empty
			if isinstance(entity,dict):
				if len(entity['hashtags'])>0:
					for content in entity['hashtags']:
						non_empty_hashtags_content.append(content['text'])
		#append hashtags this id and initialize list container for next Id:
		hashtags_text.append (non_empty_hashtags_content)
		non_empty_hashtags_content=[]
	return hashtags_text

########## select last 60 seconds of incoming hashtags using their date of creation 
# No matter time order of incoming hashtags within 60s window
# this function will always retain latest 60 seconds:
def select_last60_seconds(text_hashtags,time_hashtags):
	max_timestamp_value=np.max(time_hashtags)
	min_timestamp_value = max_timestamp_value - np.timedelta64(60, 's')
	#latest 60 hashtags:
	latest60_hashtags_text = []
	latest60_hashtags_time = []
	for i,(mytext,mytime) in enumerate(zip(text_hashtags,time_hashtags)):
		if mytime>=min_timestamp_value and mytime<=max_timestamp_value:
			latest60_hashtags_text.append(mytext)
			latest60_hashtags_time.append(mytime)
	return latest60_hashtags_text,latest60_hashtags_time

###############################################################################

################# transform hashtags into graph structure:####
############### then calculate average degree #############
def generate_graph(text_hashtags):
	mydict={} #to store graph
	for t in text_hashtags:
		if len(t)>0:
			#handle case where there is only one hashtag
			if len(t)==1:
				mydict[t[0]]=[] 
			#handle more than 02 hashtags(>=)	
			else:
				for x in t:
					#list elt expect current (x) elt:
					mylist= list ( set(t) -set([x]) )
					#handle if already present in the graph:
					if x in mydict.keys():
						#merge distinct elmnt:
						mydict[x]=list(set(mydict[x] + mylist))
					else:
						#otherwise append directly:
						mydict[x]= mylist							
	return mydict
############################## compute average degree ####################
def compute_average_degree(mydict):
	if len(mydict)==0:
		average_degree=0.00
	else:
		#loop thru all keys and count number of elmnt foreach key:
		for k in mydict.keys():
			mydict[k]=len(mydict[k])*1.00
		average_degree=np.nanmean( mydict.values() )*1.00
	return average_degree

###############################################################################
############### write average degree in output.txt #########################
def write_output(output_value):
	#open with append option:
	#'tweet_output/output.txt'==>sys.argv[2] (second argument, output)
	f = open(sys.argv[2], 'a')
	f.write(str(format(output_value, '.2f'))+'\n')
	f.close()
############### stream average degree of tweets hashtags as they come ######
def stream_average_degree (text_hashtags):
	for i in range(1,len(text_hashtags)+1):
		txt,_=select_last60_seconds(text_hashtags[:i],df['created_at'][:i])
		#generate graph (a dict that map each hashtag)
		graph=generate_graph(txt)
		#compute average degree of a node and store cumulated results 
		#as tweets come:
		average=compute_average_degree(graph) 
		print "rolling mean at " + str(i) + " is " + str(format(average, '.2f'))
		write_output(average)
##############################Main program########################################
import sys
#sys.argv[1]===>"tweet_input/tweets.txt" (first argument,input )
df=read_json_tweets(sys.argv[1])
text_hashtags=process_hashtags_into_array(df=df)
stream_average_degree(text_hashtags=text_hashtags)
