from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#consumer_key = 'd7RJDeV6M1TdKnXXdY29Zud5O'
#consumer_secret = '8LV35luiAco2mBnQ1W6erOnA8cbMwVgxblfHjP5zk5dmAXGwd6'
#access_token = '2206645458-9qlftwQ5eiovob7GCp21VrAoFRXi7AJLGt5ts3O'
#access_secret = 'Oc9ZKbHSL0reJhZYcU0Vk9UERbVvsTwerIfDUTwiRNGYf'

consumer_key = 'gIoZ2WuBQfPMuUADprHTjJNbA'
consumer_secret = 'sjbXcS9y5EJvWAakZZNOLgDrF61dI6mQnS39Xt0zsHdRIW36Er'
access_token = '1394623812499435520-PmKHJlTHunPjfMfon3Vf1C8dW6C9Ow'
access_secret = 'kFnxfF34vd3tD6S6mgJolnGFVkGVwM7CFb1Lux58x0u9w'



class StdOutListener(StreamListener):

    def on_data(self, data):
        with open('twitter_raw.txt','a') as tf:
            tf.write(data)
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':


    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    stream.filter(track=['depression', 'anxiety', 'mental health', 'suicide', 'stress', 'sad'])
