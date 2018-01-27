#!python3

from moviepy.editor import AudioFileClip as Audio
from random import randint
from os import system, chdir
from math import floor
from glob import glob
from random import choice

# TODO: output configs file
# TODO: save as a temp file
# TODO: change temp file name to add uniqueness
# TODO: call clipper as a subprocess to repress verbosity
# TODO: turn into (iterative) random sampling
# TODO: add 4 possible answers + grade

def randomPlay(filename):
	length = 30
	audio = Audio(filename)
	duration = audio.duration
	start = randint(0, floor(duration - length))
	audio.subclip(start, start + length).write_audiofile('~out.mp3')
	system('~out.mp3')
	system('del ~out.mp3')

	
def main():
	chdir('./Library')
	filenames = glob('*.mp3')
	loop = True
	while loop:
		selection = choice(filenames)
		randomPlay(selection)
		key = input('Press Q to quit...')
		loop = (key != 'q'and key != 'Q')
		print('***** {} *****'.format(selection[0:-4]))
	input()
	
if __name__ == '__main__':
	main()
