NGROK_AUTH_TOKEN = "1o2x2fXqS5F6mHJ7HokT4r6eQaZ_3vJGno1MHHz8xESah33pb"
# copy the auth token from https://dashboard.ngrok.com/get-started/your-authtoken

CONSUMER_KEY = "RycypWy8QGDi4BVraaf5lM76F"
CONSUMER_SECRET = "Mic5nJ3LuC5BlCGm5KAI0OYnWR0jgaHNGqalSqT5fGCthtyyIT"
ACCESS_KEY = "1380157138861953025-3qGUUIdEItAkhznnE6tLtjIn0K4uO3"
ACCESS_SECRET = "v69SocQgoNQ7Bz0DelTZnPTuJIEdX5G9JN52SmyrOV9AB"
ENV_NAME = "autobase"
# create Account Activity API (AAPI) dev env on https://developer.twitter.com/en/account/environments
# ENV_NAME is the same as Dev environment label
# Check your AAPI subcription renewal date on https://developer.twitter.com/en/account/subscriptions

Admin_id = [""] # list of str
# Admin id is like sender id. To check it, send a menfess from your admin account.
# or you can use api.get_user(screen_name="usernameoftheaccount")
# IF YOU WANT TO TEST THE CONFIG, REMEMBER THIS! USERS IN ADMIN_ID PASS ALL USER'S FILTERS, you should delete your id on Admin_id

Timezone = 7

Notify_queue = True
# bool, True: Send the menfess queue to sender
# The first tweet in queue won't be notified to sender (the delay is very quick).
Notify_queueMessage = "Menfess kamu berada pada urutan ke-{}, akan terkirim sekitar pukul {}"
# Please keep the "{}" format -> .format(queue, time)

Notify_sent = True
# bool, True: Send menfess tweet link to sender when menfess sent
Notify_sentMessage = "Yeay! Menfess kamu telah terkirim! https://twitter.com/{}/status/"
# Please keep the "{}" format -> .format(bot_username) + postid

Notify_sentFail1 = "Maaf ada kesalahan pada sistem :( \ntolong screenshot & laporkan kepada admin"
# Used when error is happened in system

Interval_perSender = True # bool
Interval_time = 5 # int
# Interval time (in minutes) of sending menfess per sender, Admin pass this filter
Notify_intervalPerSender = "Mengirim menfess dibatasi! silakan coba lagi setelah pukul {}"
# Please keep the "{}".format(time)

Delay_time = 36 # int, seconds
# Twitter API limits user to post tweet. System will delay 36s per/tweet. You can add it by input
# seconds in Delay_time. e.g Delay_time = 60, it means system will delay 96 seconds per tweet

# Welcome message to new followers
Greet_newFollower = True
Notif_newFollower = "Makasih yaa udah follow base ini :)"

Keyword_deleter = False # Trigger word deleter
# bool, True: Delete keyword from menfess before uploaded

# send notif to user that followed by bot
Greet_followed = True
Notif_followed = "Yeay! kamu udah difollow base ini. Jangan lupa baca peraturan sebelum mengirim menfess yaa!"

Minimum_lenMenfess = 0 # length of the menfess
Maximum_lenMenfess = 1120
Notify_lenMenfess = f"Maksimum jumlah karakter: {Maximum_lenMenfess}, Minimum jumlah karakter {Minimum_lenMenfess}"

Sender_requirements = True
# bool, True: sender should passes the following requirements:   (admin pass this filter)
Only_followed = False
Notif_notFollowed = "Hmm, kamu belum difollow base ini. Jadi ga bisa ngirim menfess dehh :("
# Minimum_followers and Minimum_day is (automatically) required when Sender_requirements is True.
Minimum_followers = 0 # int
# Minimum-account-created-at
Minimum_day = 1 # e.g 100, it means sender account must be created at 100 days ago
Notify_senderRequirements = f"Kamu harus punya {Minimum_followers} followers dan umur akun kamu harus\
     lebih dari {Minimum_day} hari biar bisa ngirim menfess :("

Private_mediaTweet = False
# bool, True: Delete username on the bottom of the attached video tweet.
# Usually when sender want to attach video (from tweet), they will attach a media url
# But the username of the (VIDEO) OWNER is mentioned on the bottom of video. With this
# when sender attach (media and/or media tweet) and if total of media ids are more than
# 4 or the space is not available, THE REST OF THE MEDIA WILL BE ATTACHED TO THE
# SUBSEQUENT TWEETS IN SORTED ORDER.

Watermark = False
# bool, True: Add watermark text to sender's photo
Watermark_image = "twitter_autobase/watermark/photo.png" # bool or str
# bool, True: Add watermark using default image. str, file_path e.g 'twitter_autobase/watermark/photo.png'
# Watermark image's size must be square
Watermark_text = "lorem ipsum"
# If you won't to add text, fill str() or "" to Watermark_text.
# You can add enter "\n", maximum: 2 lines
Watermark_font = "twitter_autobase/watermark/FreeMono.ttf"
Watermark_textColor = (100,0,0,1)
Watermark_textStroke = (0,225,225,1)
# RGBA color format, you can search it on google
Watermark_ratio = 0.15 # float number under 1 , ratio between watermark and sender's photo
Watermark_position = ('right', 'bottom') # (x, y)
# x: 'left', 'center', 'right'
# y: 'top', 'center', 'bottom'


Database = False
# bool, True: Using database (Make json file in local)
Github_database = False # Push json file to Github every midnight
# bool, True: using github to save database, False: database only in local
# Github_token and Github_repo are not required when Github_database is False
# You can directly update Github database using '/db_update' command from DM
Github_token = ""
# get it from https://github.com/settings/tokens , set allow for editing repo
Github_repo = "username/your_repo"
# Make a repository first, then fill the Github_repo
# use another repo instead of primary repo

Account_status = True
# bool, True: Turn on the automenfess. If it turned into False, this bot won't
# post menfess. You can switch it using '/switch on/off' command from DM
Notify_accountStatus = "Automenfess sedang dimatikan oleh admin, silakan cek tweet terbaru atau \
hubungi admin untuk informasi lebih lanjut"

Off_schedule = False
# schedule automenfess to turned off
Off_scheduleData = {
    'start'         : ('21', '06'), # ('hour', 'minute')
    'different_day' : True,
    'end'           : ('04', '36'), # ('hour', 'minute')
}
Off_scheduleMsg = f"Automenfess dimatikan setiap pukul {Off_scheduleData['start'][0]}:{Off_scheduleData['start'][1]} \
sampai dengan pukul {Off_scheduleData['end'][0]}:{Off_scheduleData['end'][1]}"

Trigger_word = ["wkly!", "wkly!"]
Notify_wrongTriggerUser = True # Will be sent to user
Notify_wrongTriggerAdmin = False # Will be sent to admin
Notify_wrongTriggerMsg = "Trigger menfess tidak terdeteksi"

Sensitive_word = "/sensitive"
# Used when sender send sensitive content, order them to use this word
# But I advise against sending sensitive content, Twitter may ban your account,
# And using this bot for 'adult' base is strictly prohibited.
Blacklist_words = ['porn', 'politik'] 
# hashtags and mentions will be changed into "#." and "@." in clean_dm_autobase.py to avoid ban
Notify_blacklistWords = "di menfess kamu terdapat blacklist words, jangan lupa baca peraturan base yaa!"
Notify_blacklistWordsAdmin = False # Will be sent to admin

# Please set Admin_cmd and User_cmd in lowercase
# Read README.md for the DMs examples
# You can move Admin_cmd to User_cmd and vice versa

Admin_cmd = {
    '/add_blacklist'    : 'DMCmd.add_blacklist(arg)',
    '/rm_blacklist'     : 'DMCmd.rm_blacklist(arg)',
    '/display_blacklist': 'DMCmd.display_blacklist(sender_id) #no_notif',
    '/db_update'        : 'DMCmd.db_update()',
    '/who'              : 'DMCmd.who(selfAlias, sender_id, urls) #no_notif',
    '/add_admin'        : 'DMCmd.add_admin(arg)',
    '/rm_admin'         : 'DMCmd.rm_admin(arg)',
    '/switch'           : 'DMCmd.switch(arg)',
}
# #no_notif is an indicator to skip send notif to admin
# db_update is not available when Github_Database set to False
# who is only available for one day (reset every midnight or heroku dyno cycling)


User_cmd = {
    '/delete'           : 'DMCmd.delete(selfAlias, sender_id, urls)',
    '/unsend'           : 'DMCmd.unsend(selfAlias, sender_id)',
}
# delete and unsend is not available for user when bot was just started and user id not in db_sent
# delete & db_sent are only available for one day (reset every midnight or heroku dyno cycling)
Notify_DMCmdDelete = "Yeay! Menfess kamu sudah berhasil dihapus"
Notify_DMCmdDeleteFail = "Duh! Menfess ini ngga bisa kamu hapus :("
# Notify above are only for user
