import os.path
import subprocess

try:
  VERSION = subprocess.check_output(["git", "describe", "--tags", "--always"]).decode('ascii').strip()
except Exception:
  VERSION = ''

AUDIO_CACHE_PATH = os.path.join(os.getcwd(), 'audio_cache')
DISCORD_MSG_CHAR_LIMIT = 2000
