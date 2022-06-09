from decouple import config
import berserk
import os
from datetime import datetime, date, timedelta

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit

API_TOKEN = config("TOKEN")
API_LINK = "https://lichess.org/api/games/user/AdamGaffney96?tags=true&clocks=true&evals=false&opening=true&since=1653001200000&until=1654556400000&perfType=rapid"

session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)

unformatted_start = input("Please enter the start date in the format YYYY-MM-DD (Leave blank to download from last date): ")
unformatted_end = input("Please enter the end date in the format YYYY-MM-DD (Leave blank to take todays date): ")

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

start = berserk.utils.to_millis(datetime(start_year, start_month, start_day))
end = berserk.utils.to_millis(datetime(end_year, end_month, end_day))

downloaded_games = client.games.export_by_player("AdamGaffney96", since=start, until=end, max=300, as_pgn=True, perf_type="rapid", clocks=True, opening=True)

open(os.path.dirname(os.path.realpath(__file__))+"/last_pgn.pgn", "w").close()

with open(os.path.dirname(os.path.realpath(__file__))+"/last_pgn.pgn", "r+") as file:
    file.write("\n".join(downloaded_games).replace("AdamGaffney96", "Gaffney, Adam"))
    
with open(os.path.dirname(os.path.realpath(__file__))+"/last_export.txt", "r+") as file:
    file.write(str(date.today()))

os.startfile(os.path.dirname(os.path.realpath(__file__))+"/last_pgn.pgn")