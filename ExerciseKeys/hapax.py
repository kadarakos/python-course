#!/usr/bin/env python3

import string

def legomena(f):
	textF = open(f, 'rt')
	text_with_P = textF.read()
	textF.close()
	text = ""
	for char in text_with_P:
		if char not in string.punctuation:
			text+=char.lower()
	words = text.split()
	#print words[:50]
	freqs = {}
	for w in words:
		try:
			freqs[w]+=1
		except KeyError:
			freqs[w]=1
	hapaxes = []
	for w in freqs:
		if freqs[w] == 1:
			hapaxes.append(w)
	return hapaxes

def dislegomena(f):
	textF = open(f, 'rt')
	text_with_P = textF.read()
	textF.close()
	text = ""
	for char in text_with_P:
		if char not in string.punctuation:
			text+=char.lower()
	words = text.split()
	#print words[:50]
	freqs = {}
	for w in words:
		try:
			freqs[w]+=1
		except KeyError:
			freqs[w]=1
	hapaxes = []
	for w in freqs:
		if freqs[w] == 2:
			hapaxes.append(w)
	return hapaxes

def trislegomena(f):
	textF = open(f, 'rt')
	text_with_P = textF.read()
	textF.close()
	text = ""
	for char in text_with_P:
		if char not in string.punctuation:
			text+=char.lower()
	words = text.split()
	#print words[:50]
	freqs = {}
	for w in words:
		try:
			freqs[w]+=1
		except KeyError:
			freqs[w]=1
	hapaxes = []
	for w in freqs:
		if freqs[w] == 3:
			hapaxes.append(w)
	return hapaxes