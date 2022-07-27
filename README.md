__Songs for Metal, Stone and Wood__

- The main file is 'songs004.py'
- Some functions are included in 'functions.py'
- Haiku generation function in 'haiku.py'
- The current submission has been developed and tested using Neoscore 1.01 running under Python 3.10.4
- This is a demo and I haven't taken the time to fully clean up the code or structure as yet
- As it stands it will not be possible for the percussionist to play the generated part, which are there primarily for demonstration purposes
- There is a pdf example of the output in the 'output' directory

__Running the score__
- cd to the score directory, e.g. "cd '/Users/rich/../neoscore-main/songs/'"
- Run "python3 songs004.py"
- If you open the "neoscore-sc-osc.scd" file in SuperCollider and run the contents sequentially 
	- s.boot
	- pause until the server bootsl
	- run the other code block: you should hear a tone
- Run "python3 songs004.py" and the frequency of the tone should change, showing successful OSC communication between neoscore and SuperCollider

__Flags__
- '-a' includes a variety of descriptive and (hopefully) helpful comments in the score
- '-dy' includes a dynamic cursor
- e.g. "python3 songs004.py -ady" includes both annotations and dynamic cursor
- These flags must be a part of the first group of flags
- You can still use "--pdf", etc., flags, but they should be placed _after_ the first group, e.g. "python3 songs004.py -ady --pdf"