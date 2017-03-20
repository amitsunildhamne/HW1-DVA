#Python Version: 2.7
import csv
import json
import time
import tweepy

# You must use Python 2.7.x
# Rate limit chart for Twitter REST API - https://dev.twitter.com/rest/public/rate-limits

def loadKeys(key_file):
    # TODO: put in your keys and tokens in the keys.json file,
    #       then implement this method for loading access keys and token from keys.json
    # rtype: str <api_key>, str <api_secret>, str <token>, str <token_secret>

    # Load keys here and replace the empty strings in the return statement with those keys
    #data_file = ('/Users/vidyalankar/Desktop/Georgia_Tech/Sem_2/DVA/HW1-Dhamne-Amit/Q1/keys.json')
    with open('keys.json') as datafile:
    	data = json.load(datafile)
    api_key = data["api_key"]
    api_secret = data["api_secret"]
    token = data["token"]
    token_secret = data["token_secret"]
    return api_key,api_secret,token,token_secret

# Q1.b - 5 Marks
def getFollowers(api, root_user, no_of_followers):
    # TODO: implement the method for fetching 'no_of_followers' followers of 'root_user'
    # rtype: list containing entries in the form of a tuple (follower, root_user)
    primary_followers = []
    tup =()
    # Add code here to populate primary_followers
    for user in tweepy.Cursor(api.followers, screen_name= root_user).items(no_of_followers):
        try:
    	   tup = user.screen_name, root_user
    	   primary_followers.append(tup)
        except tweepy.TweepError, e:
            print "Private Follower hit. Pass"
            pass
    return primary_followers

# Q1.b - 7 Marks
def getSecondaryFollowers(api, followers_list, no_of_followers):
    # TODO: implement the method for fetching 'no_of_followers' followers for each entry in followers_list
    # rtype: list containing entries in the form of a tuple (follower, followers_list[i])    
    secondary_followers = []
    # Add code here to populate secondary_followers
    tup = ()
    for items in followers_list:
        try:
    	    for user in tweepy.Cursor(api.followers, screen_name = items[0]).items(no_of_followers):
                try:
    		        tup = user.screen_name, items[0]
    		        secondary_followers.append(tup)
                except tweepy.TweepError, e:
                    print "Private Follower hit. Pass"
                    pass
        except tweepy.TweepError,e:
            print "Private Follower. Pass"
            pass
    return secondary_followers

# Q1.c - 5 Marks
def getFriends(api, root_user, no_of_friends):
    # TODO: implement the method for fetching 'no_of_friends' friends of 'root_user'
    # rtype: list containing entries in the form of a tuple (root_user, friend)
    primary_friends = []
    # Add code here to populate primary_friends
    tup = ()
    for user in tweepy.Cursor(api.friends,screen_name = root_user).items(no_of_friends):
        try:
    	   tup  = user.screen_name,root_user
    	   primary_friends.append(tup)
        except tweet.TweepError, e:
            print "Private Friend. Pass"
            pass

    return primary_friends

# Q1.c - 7 Marks
def getSecondaryFriends(api, friends_list, no_of_friends):
    # TODO: implement the method for fetching 'no_of_friends' friends for each entry in friends_list
    # rtype: list containing entries in the form of a tuple (friends_list[i], friend)
    secondary_friends = []
    # Add code here to populate secondary_friends
    tup = ()
    for items in friends_list:
        try:
    	   for user in tweepy.Cursor(api.friends, screen_name = items[0]).items(no_of_friends):
              try:
    		       tup = user.screen_name,items[0]
    		       secondary_friends.append(tup)
              except tweepy.TweepError, e:
                   print "Private Friend. Pass"
                   pass
        except tweepy.TweepError, e:
            print "Private Friend. Pass"
            pass

    return secondary_friends

# Q1.b, Q1.c - 6 Marks
def writeToFile(data, output_file):
    # write data to output_file
    # rtype: None
    with open (output_file,'wb') as result_file:
    	wr = csv.writer(result_file)
    	wr.writerows(data)

    pass




"""
NOTE ON GRADING:

We will import the above functions
and use testSubmission() as below
to automatically grade your code.

You may modify testSubmission()
for your testing purposes
but it will not be graded.

It is highly recommended that
you DO NOT put any code outside testSubmission()
as it will break the auto-grader.

Note that your code should work as expected
for any value of ROOT_USER.
"""

def testSubmission():
    KEY_FILE = 'keys.json'
    OUTPUT_FILE_FOLLOWERS = 'followers.csv'
    OUTPUT_FILE_FRIENDS = 'friends.csv'

    ROOT_USER = 'PoloChau'
    NO_OF_FOLLOWERS = 10
    NO_OF_FRIENDS = 10


    api_key, api_secret, token, token_secret = loadKeys(KEY_FILE)

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)

    primary_followers = getFollowers(api, ROOT_USER, NO_OF_FOLLOWERS)
    secondary_followers = getSecondaryFollowers(api, primary_followers, NO_OF_FOLLOWERS)
    followers = primary_followers + secondary_followers

    primary_friends = getFriends(api, ROOT_USER, NO_OF_FRIENDS)
    secondary_friends = getSecondaryFriends(api, primary_friends, NO_OF_FRIENDS)
    friends = primary_friends + secondary_friends

    writeToFile(followers, OUTPUT_FILE_FOLLOWERS)
    writeToFile(friends, OUTPUT_FILE_FRIENDS)


if __name__ == '__main__':
    testSubmission()

