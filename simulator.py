#! python3
"""Music test (music sample recognition) simulator"""

from random import randint, sample, randrange
from os import chdir, path, system as terminal
from math import floor
from glob import glob
from tempfile import TemporaryDirectory as TempDir
from time import time
from moviepy.editor import AudioFileClip as Audio
from configs import DURATION, DIRECTORY, NUM_OF_CHOICES, NUM_OF_QUESTIONS


def play(file_name, temp_dir):
	"""Plays a random audio sample of the file with the provided name"""
	audio = Audio(file_name)
	start = randint(0, floor(audio.duration - DURATION))
	file_path = path.join(temp_dir, str(time()) + '.mp3')
	audio.subclip(start, start + DURATION).write_audiofile(file_path, verbose=False, progress_bar=False)
	terminal(file_path)


def question(choices, temp_dir):
	"""Asks a question with multiple answers and returns the correct answer"""
	answer = randrange(len(choices))
	play(choices[answer], temp_dir)
	for i in range(len(choices)):
		name = choices[i]
		print('[{}] - {}'.format(i, name[:name.rindex('.')]))
	return answer


def main():
	"""Run the random music sampler (exam simulator)"""
	chdir(DIRECTORY)
	file_names = glob('*.mp3')
	score = 0
	with TempDir() as temp_dir:
		for i in range(NUM_OF_QUESTIONS):
			print('Question {}:'.format(i + 1))
			choices = sample(file_names, NUM_OF_CHOICES)
			answer = question(choices, temp_dir)
			key = input('Answer: ')
			if key == str(answer):
				print('[V] Correct!\n')
				score = score + 1
			else:
				correct = choices[answer]
				print('[X] Incorrect - {}\n'.format(correct[:correct.rindex('.')]))
	input('Total score {}%'.format(floor((score * 100) / NUM_OF_QUESTIONS)))


if __name__ == '__main__':
	main()
