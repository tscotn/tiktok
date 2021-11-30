#from TikTokApi import TikTokApi
#
#api = TikTokApi()
#n_videos = 10
#username = 'washingtonpost'
#
#user_videos = api.byUsername(username, count=n_videos)
#
#print(user_videos)


from TikTokApi import TikTokApi

verifyFp="verify_kwmpj4r7_AB6PqQ5V_gaPf_4NqC_Agl5_6ujdR4nJOFJB"


def print_tiktok(tiktok):
    print(tiktok['desc'])
    print("\nnumber of likes:", str(tiktok['stats']['diggCount']))
    print("\nnumber of shares:", str(tiktok['stats']['shareCount']))
    print("\nnumber of comments:", str(tiktok['stats']['commentCount']))
    print("\nnumber of plays:", str(tiktok['stats']['playCount']))

api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
results = 10
username = 'brunchwithbabs'

user_results = api.by_username(username=username, count=results, custom_verifyFp=verifyFp)
print(type(user_results))
for tiktok in user_results:
    print_tiktok(tiktok)

#    search_results = api.by_hashtag(count=results, hashtag=hashtag)
#    for tiktok in search_results:
#        print(tiktok['video']['playAddr'])
