# Package import
from decouple import config
import berserk
import os
from datetime import datetime, date, timedelta

# Exception handler
def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit

# Fetch API token, Player Name and formatted player name from .env file in the same folder
API_TOKEN = config("TOKEN")
PLAYER_NAME = config("PLAYER_NAME")
# I added this as I like all my games to link up to my real name in Chessbase (e.g. Smith, J rather than my lichess username)
PLAYER_NAME_FORMATTED = config("PLAYER_NAME_FORMATTED")

# Uses berserk to connect to the session
session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)

# Takes the user input for start and end dates. Leave blank to take export from the last date in last_export.txt to todays date
unformatted_start = input("Please enter the start date in the format YYYY-MM-DD (Leave blank to download from last date): ")
unformatted_end = input("Please enter the end date in the format YYYY-MM-DD (Leave blank to take todays date): ")

# Formats the correct start date depending on the user input
if (unformatted_start == ""):
    with open(os.path.dirname(os.path.realpath(__file__))+"/last_export.txt", "r+") as file:
        start_date = file.readline()
else:
    start_date = unformatted_start

start_date_split = start_date.split("-")
start_year = int(start_date_split[0])
start_month = int(start_date_split[1])
start_day = int(start_date_split[2])
print(start_year, start_month, start_day)

# Formats the correct end date depending on the user input
if (unformatted_end == ""):
    end_date = date.today() + timedelta(1)
    end_date_split = end_date.strftime("%Y-%m-%d").split("-")
else:
    end_date = unformatted_end
    end_date_split = end_date.split("-")

end_year = int(end_date_split[0])
end_month = int(end_date_split[1])
end_day = int(end_date_split[2])
print(end_year, end_month, end_day)

# Converts the dates to milliseconds as required by the Lichess API
start = berserk.utils.to_millis(datetime(start_year, start_month, start_day))
end = berserk.utils.to_millis(datetime(end_year, end_month, end_day))

# The function that downloads from the API. Each argument can be changed to whatever is necessary, these are just my preferred settings.
downloaded_games = client.games.export_by_player(PLAYER_NAME, since=start, until=end, max=300, as_pgn=True, perf_type="rapid", clocks=True, opening=True)

# Clears the PGN of previous games to prevent duplicates
open(os.path.dirname(os.path.realpath(__file__))+"/last_pgn.pgn", "w").close()

# Adds games in PGN format to file and then adds todays date to last_export.txt
with open(os.path.dirname(os.path.realpath(__file__))+"/last_pgn.pgn", "r+") as file:
    file.write("\n".join(downloaded_games).replace(PLAYER_NAME, PLAYER_NAME_FORMATTED))
    
with open(os.path.dirname(os.path.realpath(__file__))+"/last_export.txt", "r+") as file:
    file.write(str(date.today()))

# Opens the PGN file. If Chessbase (or equivalent database app) is default for PGN files this should open the file in that software.
os.startfile(os.path.dirname(os.path.realpath(__file__))+"/last_pgn.pgn")