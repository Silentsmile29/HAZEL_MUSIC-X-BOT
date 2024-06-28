from HAZELMUSIC.core.bot import HAZEL
from HAZELMUSIC.core.dir import dirr
from HAZELMUSIC.core.git import git
from HAZELMUSIC.core.userbot import Userbot
from HAZELMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = HAZEL()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
