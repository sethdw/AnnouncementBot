# Work with Python 3.6
# THIS IS NOT LISCENSED FOR USE BY ANY PERSONS FROM /R/FLAIRWARS WITHOUT EXPRESSED PERMISSION FROM THE AUTHOR

import discord, praw, threading, pickle
from datetime import datetime
global subscribers

client = discord.Client()

# Decomment to wipe subscribers at start of program
# p = open("subs","wb")	
# pickle.dump([],p)
# p.close()

p = open("subs","rb")	
subscribers = pickle.load(p)
p.close()

print (subscribers)

messageEnd = "\n\n---\n\nI am a bot, please message /u/REDDIT_USERNAME if you have any issues.\n\nTo unsubscribe, reply with !unsubscribe"

# assumes praw.ini with reddit logon info and discordID.txt with discord token
bot = praw.Reddit("bot01")
f = open("discordID.txt","r")
discordID = f.readline()
f.close()

############## Discord bit ##############
@client.event
async def on_message(discordMessage):
	#								  Announcement channel ID's
	if discordMessage.channel.id in ["557229087735676930","523151352755388438","538038411991449600"]:
		text = discordMessage.content + "\n\nPlease message " + discordMessage.author.display_name +" if you have any further questions." + messageEnd
		print("Sent announcement:\n" + text + "\n")
		for un in subscribers:
			bot.redditor(un).message('New announcement!', text)

############## Reddit bit ##############
def checkYellow(user):
	Yellow = False
	fwCommentExists = False
	try:
		for fwComment in user.comments.new(limit=100):
			if fwComment.subreddit == "flairwars":
				fwCommentExists = True
				if "Yellow" in fwComment.author_flair_text:
					Yellow = True
					return "Yellow"
				else:
					return fwComment.author_flair_text
	except e:
		print (e)

	# if Yellow:
	# 	if user.link_karma > 100 and (datetime.utcnow() - user.created_utc) > 5259486

	return "noFWComment"

# Reads all incoming messages and acts on them
def ReadMessages():
	global subscribers
	print("opened reddit thread")
	while True:
		for message in bot.inbox.unread(limit=None):

			# Subscribe
			if "!subscribe" in message.body:
				flair = checkYellow(message.author)
				if flair == "Yellow":
					if message.author.name in subscribers:
						message.reply("You are already subscribed to yellow's announcements" + messageEnd)
					else:
						subscribers += [message.author.name]
						message.reply("You have subscribed to yellow's announcements!" + messageEnd)
						print(message.author,"subscribed")
						p = open("subs","wb")
						pickle.dump(subscribers,p)
						p.close()

				elif flair == "noFWComment":
					message.reply("I could not find your flair! Please make a comment [somewhere on flairwars](https://www.reddit.com/r/flairwars/comments/9n0394/comment_to_gain_a_team_megathread/) and send the command again")

				elif flair not in ["Yellow","noFWComment"]:
					message.reply("Either you're not a yellow, or something went horribly wrong. Please contact /u/REDDIT_USERNAME if you think this is an error.")	

			# Unsubscribe
			if "!unsubscribe" in message.body:
				if message.author.name in subscribers:
					subscribers.remove(message.author.name)
					message.reply("You have succesfully unsubscribed from yellow's announcements :(" + messageEnd)
					print(message.author + " unsubscribed")
				else:
					message.reply("You aren't subscribed to yellow's announcements!" + messageEnd)

			# mark message as read
			bot.inbox.mark_read([message])

# Start threads
messagesThread = threading.Thread(target=ReadMessages,args=[])
messagesThread.start()
client.run(discordID)