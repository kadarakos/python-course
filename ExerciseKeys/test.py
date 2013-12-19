#!/usr/bin/env python

import re

def read_csv(fname):
	data = []
	f = open(fname, 'r')
	comma = re.compile(r"\s*\,\s*")
	for line in f:
		line = line.strip()
		items = comma.split(line)
		if len(items) != 4:
			continue
		data.append(items)
	f.close()
	print(data)
	return





