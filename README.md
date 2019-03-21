# AnnouncementBot

I participate in a Reddit community that has most of its announcements posted in its associated Discord, thereby making it much harder to participate for anyone who doesn't want to install Discord. This bot remedies that by automatically sending any messages in a Discord channel to a subscription list on reddit, directly messaging the users to ensure that they are notified. This community will be using this to enable Reddit-only users to also read the announcements put out on Discord and therefore improving their participation.

# How to use the bot

The Reddit-side bot is subscribed to by sending a message containing "!subscribe" in its body, and can be unsubscribed with "!unsubscribe". 

# Configuration

The program requires a Reddit account's information put in praw.ini, and a Discord client secret in discordID.txt

The Discord-side bot must be configured by putting the id's for the announcement channel(s) in the array on line 34. 

# Usage

This program is fine for use by anyone not in the community it was created for. However, due to the competetive nature of the community this is made for, if you are in said community (you know who you are), I do not give you permission to use this code, modify this code, copy this code or otherwise. I have no legal backing for this, but just don't do it. 
