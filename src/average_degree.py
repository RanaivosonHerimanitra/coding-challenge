#!/usr/bin/python
import pandas as pd 
import numpy as np

### Function that correctly parse json format from tweets.txt using pandas ####
### and select field/entity of interests , here: "created_at" and "entities"
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
def process_hashtags_into_array(df):
	#loop thru  id of users
	id_users= df['id']
	#store output (final)
	hashtags_text=[];
	#hashtags_time=[]
	#only store non empty hashtags
	non_empty_hashtags_content=[]
	for ids in id_users:
		for entity in df[df.id==ids]['entities']:
			# if type is dict and non empty
			if isinstance(entity,dict):
				if len(entity['hashtags'])>0:
					for content in entity['hashtags']:
						non_empty_hashtags_content.append(content['text'])
		#append both timestamp and hashtags
		hashtags_text.append (non_empty_hashtags_content)
		#hashtags_time.append (df[df.id==ids]['created_at'])
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
def gen_graph_and_compute_average_degree(text_hashtags):
	mydict={} #to store graph
	L=[] #to store degree of each node
	for t in text_hashtags:
		if len(t)>0:
			#handle case where there is only one hashtag
			if len(t)==1:
				mydict[t[0]]=[]
				L.append(0.0)
			#more than 02 hashtags(>=)
			else:
				L.append(len(list(set(t[1:])))*1.0)
				first_element_array_of_t=t[0]
				if first_element_array_of_t in mydict.keys():
					mydict[first_element_array_of_t]=list(set(mydict[first_element_array_of_t])) + list(set(t[1:]))
				else:
					mydict[first_element_array_of_t]=list(set(t[1:]))
	#avoid nan during mean calculation
	average_degree=np.nanmean(L) 
	return mydict,average_degree

############### stream average degree of tweets hashtags as they come ######
def stream_average_degree (text_hashtags):
	for i in range(1,len(text_hashtags)+1):
		txt,_=select_last60_seconds(text_hashtags[:i],df['created_at'][:i])
		graph,average=gen_graph_and_compute_average_degree(txt)
		print average
##############################Main program########################################
df=read_json_tweets("tweet_input/tweets.txt")
text_hashtags=process_hashtags_into_array(df=df)
stream_average_degree(text_hashtags=text_hashtags)
