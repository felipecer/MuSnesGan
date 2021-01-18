# Musegan-Videogame

## Description

This is a replica of MuseGAN, a Deep Learning model to generate multitrack music. We trained this model using video game music and using Pytorch.
Follow this [link](https://github.com/salu133445/musegan) to the original content. 

You can find more video game music at https://www.vgmusic.com/

Brief description files and folders.

* td-dataset: dataset in midi format.
* td-dataset-preprocesado: dataset in npz format. It contains a subset of td-dataset according to the criteria described in MuSnesGan.ipynb

## Train this model
If you wish to train this model, run the code on MuSnesGan.ipynb feeding with the td-dataset provided or your own generated dataset.

## Generate your own dataset

### Download more tracks.

If you want to download aditional tracks feel free to use our webscrapping script (it only works for [VGMusic](https://www.vgmusic.com/) webpage).

### Prepare new training data
  -Use generar_info_csv.py to generate a csv containing information about the midi files, such as time_signature necessary for the GAN training (it needs 4/4 time_signature data)
  -Drop items on the generated csv that don't meet the criteria for the data preprocessing and save the dropped csv with the filtered songs data.
  -Run preprocess.py to generate the dataset (it needs the csv mentioned before to make the preprocess and generate the new files)
