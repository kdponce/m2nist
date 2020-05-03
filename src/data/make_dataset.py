import zipfile
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = 'farhanhubble/multimnistm2nist'
DIR_PATH = SCRIPT_DIR + (2 * (os.sep + os.pardir)) + '/data/raw'

# Checks if API token has been setup.
try:
    from kaggle.api.kaggle_api_extended import KaggleApi
except OSError as e:
    sys.exit(e)

api = KaggleApi()
api.authenticate()

# Download M2NIST dataset
if not os.path.exists(os.path.join(DIR_PATH, 'multimnistm2nist.zip')):
    print('Downloading M2NIST dataset...', end=' ')
    api.dataset_download_files('farhanhubble/multimnistm2nist', path=DIR_PATH)
    print('Done.')
else:
    print('Dataset already downloaded.')

# Checks if extracted files already exist. Ignore existing files.
dataset = zipfile.ZipFile(os.path.join(DIR_PATH, 'multimnistm2nist.zip'), 'r')
files = dataset.namelist()
for f in files:
    if not os.path.exists(os.path.join(DIR_PATH, f)):
        print('Extracting {}...'.format(f), end=' ')
        dataset.extract(f, path=DIR_PATH)
        print('Done.')
    else:
        print('{} already exists.'.format(f))

for f in files:
    path = os.path.join(DIR_PATH, f)
    os.chmod(path, 0o444)
    print('Converted {} to read-only.'.format(f))
