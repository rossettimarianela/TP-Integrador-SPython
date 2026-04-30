from pathlib import Path
from os.path import dirname


r = dirname(__file__)
IADIZA_DIR = r / Path('../raw_datasets')/ "Colección Ornitológica del IADIZA-CCT CONICET Mendoza IADIZA-COI"

INATURALIST_DIR = r / Path('../raw_datasets')/ "inaturalist-filtered"
#print(INATURALIST_DIR)

XENO_CANTO_DIR = r / Path('../raw_datasets')/ "xeno-canto-bird-sounds-filtered"
#print(XENO_CANTO_DIR)

PROCESSED_DIR = r / Path('../processed_datasets')