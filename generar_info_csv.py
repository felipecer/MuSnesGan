import mido
import pandas as pd
from mido import MidiFile
import matplotlib.pyplot as plt
import instr_tools

trackNoteList = []
noteList = []
trackTimeList = []
timeList = []
trackNames = []

data = pd.read_csv("dataDesc.csv", encoding = 'cp1252')

songsWithInfo = pd.DataFrame(columns = ["game_name", "song_name", "is_4/4", "time_signature_count", "valid_tracks", "unique_valid_tracks"])

trackNames = dict()
validTracks = 0

for i in range(len(data.index)):

	if i % 100 == 0:
		print("EN", i, " DE ", len(data.index))
	try:
		mid = MidiFile("./td-dataset/" + data.loc[i][0] + "/" + data.loc[i][1])
	except:
		print("POSIBLE DIRECTORIO INVALIDO:" + "./raw_data/" + data.loc[i][0] + "/" + data.loc[i][1])
		continue

	newRow = [data.loc[i][0], data.loc[i][1]]

	isff = True
	tsCount = 0
	for track in mid.tracks:
		for msg in track:
			msgInfo = vars(msg)
			if msgInfo["type"] == "time_signature":
				tsCount += 1
				try:
					if msgInfo["numerator"] != 4 or msgInfo["denominator"] != 4:
						isff = False
				except:
					print("NADAAAAA")

	newRow.append(isff)
	newRow.append(tsCount)

	numVInstr, numUniqueVInstr = instr_tools.get_num_valid_instr(mid)

	newRow.append(numVInstr)
	newRow.append(numUniqueVInstr)

	songsWithInfo.loc[i] = newRow

songsWithInfo.to_csv("songs_info.csv")