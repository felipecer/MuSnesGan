import mido
import os
from instr_tools import get_track_instrument
import matplotlib.pyplot as plt

tracksDict = {}
datasetPath = "./td-dataset/"

count = 0
for root, dirsArr, files in os.walk(datasetPath):
	for file in files:
		count += 1
		try:
			mid = mido.MidiFile(os.path.join(root, file))
		except:
			print("Posible archivo invalido en:", os.path.join(root, file))
		for track in mid.tracks:
			instr = get_track_instrument(track)
			if instr in tracksDict:
				tracksDict[instr] += 1
			else:
				tracksDict[instr] = 0

		if count % 100 == 0:
			print("Canciones procesadas:", count)

columns = []
freq = []
for col in tracksDict:
	if col == "None?":
		continue
	pltCol = col.replace(" ", "\n")
	columns.append(pltCol)
	freq.append(tracksDict[col])

zipped_lists = zip(freq, columns)
sorted_pairs = sorted(zipped_lists, reverse=True)
tuples = zip(*sorted_pairs)
freq, columns = [list(tup) for tup in  tuples]

plt.xlabel("Instrument family")
plt.ylabel("frequency")
plt.bar(columns, freq)
plt.show()