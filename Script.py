class script(object):
    START_TXT = """šš²š¹š¹š¼ {}\n
 š° šš  <a href="https://t.me/AJmovieLINKS" >š£š¼šæš¶š»š·š šš¼š</a>\nššš ššš ššš ššššš šššš\n <a href="https://t.me/worldmoviesaj" >š š¢š©šš ššØš ššā¬ļøā¼ļøā¾ļøāŖļø</a>\nš¬š¼š šŗššš š·š¼š¶š» @AJmovieLINKS\n\nš š š¢šš»š²šæ š<a href="https://t.me/avataradorn" >š¼.š</a>"""
    HELP_TXT = """š·š“š {}
š·š“šš“ šøš šš·š“ š·š“š»šæ šµš¾š š¼š š²š¾š¼š¼š°š½š³š."""
    ABOUT_TXT = """āÆ š š š»š®šŗš²: {}
āÆ ššæš²š®šš¼šæ: <a href=url='https://t.me/avataradorn'>AJ</a>
āÆ šš¶šÆšæš®šæš: PYPROGRAM
āÆ šš®š»š“šš®š“š²: PYTHON
āÆ šš¢š§ š¦šš„š©šš„: @AJmovieLINKS
āÆ š š¬ šš„ššš” : v1.0.1 AJ"""
    SOURCE_TXT = """<b>NOTE:</b>
- AJ BOT is a open source project. 
- Source - url='https://t.me/worldmoviesaj'  

<b>DEVS:</b>
- <a href=url='https://t.me/worldmoviesaj'>AJ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. AJ BOT should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
ā¢ /filter - <code>add a filter in chat</code>
ā¢ /filters - <code>list all the filters of a chat</code>
ā¢ /del - <code>delete a specific filter in chat</code>
ā¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. AJ BOT supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
ā¢ /connect  - <code>connect a particular chat to your PM</code>
ā¢ /disconnect  - <code>disconnect from a chat</code>
ā¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
ā¢ /id - <code>get id of a specifed user.</code>
ā¢ /info  - <code>get information about a user.</code>
ā¢ /imdb  - <code>get the film information from IMDb source.</code>
ā¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
ā¢ /logs - <code>to get the rescent errors</code>
ā¢ /stats - <code>to get status of files in db.</code>
ā¢ /users - <code>to get list of my users and ids.</code>
ā¢ /chats - <code>to get list of the my chats and ids </code>
ā¢ /leave  - <code>to leave from a chat.</code>
ā¢ /disable  -  <code>do disable a chat.</code>
ā¢ /ban  - <code>to ban a user.</code>
ā¢ /unban  - <code>to unban a user.</code>
ā¢ /channel - <code>to get list of total connected channels</code>
ā¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ā šš¾šš°š» šµšøš»š“š: <code>{}</code>
ā šš¾šš°š» ššš“šš: <code>{}</code>
ā šš¾šš°š» š²š·š°šš: <code>{}</code>
ā ššš“š³ ššš¾šš°š¶š“: <code>{}</code> š¼šš±
ā šµšš“š“ ššš¾šš°š¶š“: <code>{}</code> š¼šš±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
