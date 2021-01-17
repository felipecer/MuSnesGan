import pypianoroll as pypi
import mido
import pandas as pd
import numpy as np
from instr_tools import merge_tracks
import os

data = pd.read_csv("song_filtrado_mas_mejor_este_si.csv")

pathPre = "./td_dataset_preprocesado"
pathData = "./td-dataset"

if not os.path.isdir(pathData):
	raise Exception("No existe el directorio del dataset:" + pathData)

if not os.path.isdir(pathPre):
	os.mkdir(pathPre)

for i in range(len(data.index)):

	if i % 100 == 0:
		print("EN", i, " DE ", len(data.index))

	try:
		mm = pypi.read("./td-dataset/" + data.loc[i][1] + "/" + data.loc[i][2])
	except:
		print("Posible error" + data.loc[i][1] + "/" + data.loc[i][2])
		continue

	mm = merge_tracks(mm)

	if not os.path.isdir(pathPre + "/" + data.loc[i][1]):
		try:
			os.mkdir(pathPre + "/" + data.loc[i][1])
		except:
			print("Posible nombre del directorio invalido:" + pathPre + "/" + data.loc[i][1])

	songName = data.loc[i][2][:-3] + "npz"
	mm.save(pathPre + "/" + data.loc[i][1] + "/" + songName)