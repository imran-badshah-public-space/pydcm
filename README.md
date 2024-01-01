# DCM with python

## Description

Functionalities related to DICOM manipulation and reading utilizing the [`pydicom`](https://pydicom.github.io/) library:

1. DICOM to JPEG Conversion
1. Extraction of DICOM Data into Tabular Format

## Tech Stack

### Languages
- Python

### Frameworks and Libraries
- pydicom
- opencv-python

### Algorithms and Techniques
- DICOM
- Normailzation

### Categories
- Biomedical
- Imaging
- Scripting
- Console

### Platforms
- Linux
- MacOS

## Install
```
python3 -m pip install --user virtualenv
python3 -m venv <venv_name>
. <venv_name>/bin/activate
pip3 install -r requirements.txt
```

## Usage

### DCM to IMG

Converts DICOM to a JPEG image.

```shell
python3 dcm2img.py -i input/Lung_Cancer__M_1970-01-01_Lung_Cancer_Default/1.3.12.2.1107.5.8.3.807665.857777.55565748.2013031511383306/1.3.12.2.1107.5.1.4.60171.30000013031907425126200000204 -o output
```

### Extract meta-data and specific tags from DCM

Extracts meta-data from DICOM and lists this (even as a table with the `-g` flag):

| study-uuid  |   occurances  |   file_path |
|    :---:    |     :---:     |     :---:   |
|     ---     |      ---      |      ---    |


```shell
python3 extract_data.py -i input/Lung_Cancer__M_1970-01-01_Lung_Cancer_Default/1.3.12.2.1107.5.8.3.807665.857777.55565748.2013031511383306/1.3.12.2.1107.5.1.4.60171.30000013031907425126200000204
```

For specific tags
```shell
python3 extract_data.py -i input/Lung_Cancer__M_1970-01-01_Lung_Cancer_Default/1.3.12.2.1107.5.8.3.807665.857777.55565748.2013031511383306/1.3.12.2.1107.5.1.4.60171.30000013031907425126200000204 -u
```

