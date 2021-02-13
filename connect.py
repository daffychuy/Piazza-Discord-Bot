import os, discord, random, piazza
***REMOVED***

***REMOVED***
TOKEN = os.getenv['DISCORD_TOKEN']
GUILD = os.getenv['GUILD']
EMAIL = os.getenv['EMAIL']
PASSWD = os.getenv['PASSWD']

***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***

    # If message is a piazza link, call test.piazza_parse()
***REMOVED***
    if "piazza.com" in message.content:
        response = piazza.piazza_parse(message.content, EMAIL, PASSWD)
        await message.channel.send(response)
***REMOVED***
***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***