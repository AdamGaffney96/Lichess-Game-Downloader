# LICHESS GAME DOWNLOADER

## ABOUT
I tend to play a lot of rapid+ time control games on Lichess, and also own Chessbase. As someone who always prefers just having a physical copy of my data always on my personal drives I would always download my games into various databases on my local Chessbase application. However it was always pretty tedious going through the GUI for Lichess downloads, so I decided to write a quick Python script for downloading games from Lichess into a single PGN file, and then opening that in Chessbase automatically to let me move the games as necessary. I personally have a button on my Streamdeck that runs this script with one press, so it's essentially a 3-press download of games (when you take into account the two user input prompts in the script). 
I thought I would anonymise this and upload in case anyone else wanted a quick script for doing this and didn't want to write it themselves.

## Installation
All you require are a clone of this repository and then a Python install. Also this is specifically for Windows only as I haven't tested how this works on Mac or Linux and don't intend to. I built this on Python 3.9.2 so can't testify to how this works on any other version.

## USAGE
Just download this repo to a folder on your PC, and run the "download.py" file with Python and a CMD prompt should pop up for you. 

### GAME TYPE
The only edits that could need made are if you want to download a different time control. At the moment this only does rapid and doesn't have a variable for changing this easily. however in the function on line 62 you should see `perf_type="rapid"`. This can be changed to the word version of whatever time control you want to search for (rapid, bullet, blitz etc). Also the default max download is currently 300 games, if you want to do an initial big dump then this will need changed. But for semi-regular downloads 300 games should generally be enough.

### START DATE
The first prompt is asking for a start date for download in the format YYYY-MM-DD (e.g. 2022-02-20). This is inclusive i.e. The start date should be the first day you want to download from, as games from that day will be included also. Included in this repo is also a text file called "last_export.txt". This is updated every time the script runs successfully to todays date, however this will default to whatever the date is that I actually uploaded this repo (currently 2022-06-09). 
    *On your first run, be sure to enter a start date, however every subsequent run will start from the date in last_export.txt, i.e. the date you last exported games successfully.*
All this to say, if you just want to export from the last date exported onwards, leave this blank and hit Enter.

### END DATE
The next user prompt is asking for an end date in the same format as the last. If you just want all the games from the chosen start date until today, leave this blank also and hit enter. Otherwise enter the end date in the correct format.

And that's it! After that if all is alright then the download should carry out, and the PGN file should open in your default PGN reader. If there's any issues let me know and I'll try resolve them, but as this is just a simple script for my needs I'm not planning on making a bunch of different changes, it's pretty much in it's final incarnation. I hope you find some use from it.
