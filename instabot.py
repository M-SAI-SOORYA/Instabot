#import the instabot module
from instabot import Bot
bot=Bot()
#you should enter your username and password inside  the quotation marks
bot.login(username='',password='')

# you can follow anyone no need to write specifically according to this code
bot.follow('chrishemsworth') 

# you can unfollow anyone no need to write specifically according to this code
bot.unfollow('robertdowneyjr') 

#you can upload any photo just copy the path of the photo and paste in the parethesis
bot.upload_photo('') 

followers=bot.get_user_followers('')# <--- you should type your username here inside the parenthesis 

#HERE you can get your followers data and information
for i in followers:
    print(bot.get_user_info(i))

following=bot.get_user_following('')# <--- you should type your username here inside the parenthesis 

#HERE you can get information about who you follow in instagram.....
for i in following:
    print(bot.get_user_info(i))


#Here you can send messages to any instagram_users by typing the message or text 
#And you can send the same message to multiple persons by creating a list of their usernames
bot.send_message('Hi , How are you!',['chrishemsworth','robertdowneyjr'])

#########------------------END---------------------------#########
