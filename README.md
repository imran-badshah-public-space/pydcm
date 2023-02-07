# DCM with python

## Install
```
python3 -m pip install --user virtualenv
python3 -m venv <venv_name>
<venv_name>/bin/activate
pip3 install -r requirements.txt
```

## DCM to IMG
```shell
python3 dcm2img.py -i input/Lung_Cancer__M_1970-01-01_Lung_Cancer_Default/1.3.12.2.1107.5.8.3.807665.857777.55565748.2013031511383306/1.3.12.2.1107.5.1.4.60171.30000013031907425126200000204 -o output
```

## Extract meta-data and specific tags from DCM
```shell
python3 extract_data.py -i input/Lung_Cancer__M_1970-01-01_Lung_Cancer_Default/1.3.12.2.1107.5.8.3.807665.857777.55565748.2013031511383306/1.3.12.2.1107.5.1.4.60171.30000013031907425126200000204
```

For specific tags
```shell
python3 extract_data.py -i input/Lung_Cancer__M_1970-01-01_Lung_Cancer_Default/1.3.12.2.1107.5.8.3.807665.857777.55565748.2013031511383306/1.3.12.2.1107.5.1.4.60171.30000013031907425126200000204 -u
```

