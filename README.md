__1. Songs for Metal, Stone and Wood__

- The main file is 'songs004.py'
- Some functions are included in 'functions.py'
- Haiku generation function in 'haiku.py'
- The current submission has been developed and tested using Neoscore 1.01 running under Python 3.10.4
- This is a demo and I haven't taken the time to fully clean up the code or structure as yet
- As it stands it will not be possible for the percussionist to play the generated part, which are there primarily for demonstration purposes
- There is a pdf example of the output in the 'output' directory

__2. Running the score__
- cd to the score directory, e.g. "cd '/Users/rich/../neoscore-main/songs/'"
- Run "python3 songs004.py"
- If you want to test Open Sound Control (OSC) communication, download and install pyOSC3 from [https://pypi.org/project/pyOSC3/](https://pypi.org/project/pyOSC3/)
- Open the "neoscore-sc-osc.scd" file in SuperCollider and run the contents sequentially: 
	- s.boot
	- pause until the server bootsl
	- run the other code block: you should hear a tone
- Run "python3 songs004.py" and the frequency of the tone should change, showing successful OSC communication between neoscore and SuperCollider

__3. Flags__
- '-a' includes a variety of descriptive and (hopefully) helpful annotations in the score
- '-dy' includes a dynamic cursor
- e.g. "python3 songs004.py -ady" includes both annotations and dynamic cursor
- These flags must be a part of the first group of flags
- NB the first two flags here are strictly provisional in nature
- You can still use "--pdf", etc., flags, but they should be placed _after_ the first group, e.g. "python3 songs004.py -ady --pdf"

__4. Media__
- Video demonstration here: [https://youtu.be/7iZKA9W-Ci8](https://youtu.be/7iZKA9W-Ci8)
- pdf version here: [https://github.com/richardhoadley/songs/blob/main/songs/output/songs004_pdf.pdf](https://github.com/richardhoadley/songs/blob/main/songs/output/songs004_pdf.pdf)