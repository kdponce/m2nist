"""Generate dataset.

Download M2NIST Dataset from Kaggle and perform processing as needed.
"""
import zipfile
import sys
import os
import numpy as np

# Check if API token has been setup.
try:
    from kaggle.api.kaggle_api_extended import KaggleApi
except OSError as e:
    sys.exit(e)

DATASET_URL = 'farhanhubble/multimnistm2nist'
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = SCRIPT_PATH + 2 * (os.sep + os.pardir) + '/data'
RAW_DATA_PATH = os.path.join(DATA_PATH, 'raw')
PROCESSED_DATA_PATH = os.path.join(DATA_PATH, 'processed')

api = KaggleApi()
api.authenticate()

# Download M2NIST dataset
if not os.path.exists(os.path.join(RAW_DATA_PATH, 'multimnistm2nist.zip')):
    print('Downloading M2NIST dataset...', end='')
    api.dataset_download_files(DATASET_URL, path=RAW_DATA_PATH)
    print('Done.')
else:
    print('Dataset already downloaded.')

# Check if extracted files already exist. Ignore existing files.
dataset = zipfile.ZipFile(os.path.join(RAW_DATA_PATH, 'multimnistm2nist.zip'), 'r')
files = dataset.namelist()
for f in files:
    if not os.path.exists(os.path.join(RAW_DATA_PATH, f)):
        print('Extracting {}...'.format(f), end='')
        dataset.extract(f, path=RAW_DATA_PATH)
        print('Done.')
    else:
        print('{} already exists.'.format(f))

for f in files:
    path = os.path.join(RAW_DATA_PATH, f)
    print('Converting {} to read-only...'.format(f), end='')
    os.chmod(path, 0o444)
    print('Done.')

# Load dataset
print('Processing datasets...', end='')
data = np.load(os.path.join(RAW_DATA_PATH, 'combined.npy')).astype('float16')
labels = np.load(os.path.join(RAW_DATA_PATH, 'segmented.npy')).astype('uint8')

# Rescale input from [0,255] to [0,1] and reshape to (N,H,W,C)
data /= 255.0
data = np.expand_dims(data, -1)

# Split data to train, val, test
x_train = data[:3000]
y_train = labels[:3000]

x_val = data[3000:4000]
y_val = labels[3000:4000]

x_test = data[4000:]
y_test = labels[4000:]

print('Done.')

# Save to data/processed
print('Saving processed datasets...', end='')
np.save(os.path.join(PROCESSED_DATA_PATH, 'x_train'), x_train)
np.save(os.path.join(PROCESSED_DATA_PATH, 'x_val'), x_val)
np.save(os.path.join(PROCESSED_DATA_PATH, 'x_test'), x_test)

np.save(os.path.join(PROCESSED_DATA_PATH, 'y_train'), y_train)
np.save(os.path.join(PROCESSED_DATA_PATH, 'y_val'), y_val)
np.save(os.path.join(PROCESSED_DATA_PATH, 'y_test'), y_test)
print('Done.')
