# horten_badetemp
Viser badetemperaturer i Horten og hvordan man bruker GitHub

# Preperation

```
pip install virtualenvwrapper-win
mkvirtualenv horten
```

# Installation

```
pip install -r requirements.txt
jupyter nbextension enable --py widgetsnbextension
jupyter nbextension enable --py --sys-prefix ipyleaflet
python -m ipykernel install --user --name=horten
```

# Resources

**Data Norge**
https://data.norge.no/

**ipyleaflet**
https://ipyleaflet.readthedocs.io/en/latest/index.html

**arrow**
https://arrow.readthedocs.io/en/stable/

**ipywidgets**
https://ipywidgets.readthedocs.io/en/latest/

# Run
```
voila index.ipynb
```

# Data structures

**1**

```
[
    {'location': 'Borrestranda',
    'coordinate': [59.3775, 10.4688],
    'temperature': 17.0,
    'updated': '2020-09-09T20:59:10.531Z'},
    {'location': 'Borrevannet',
    'coordinate': [59.4088, 10.4379],
    'temperature': 17.3,
    'updated': '2020-09-09T20:57:14.932Z'}
]
```

**2**

```
{'type': 'FeatureCollection',
 'features': [{'type': 'Feature',
   'properties': {'time': '2020-09-09T20:59:10.531Z',
    'last': '17.0',
    'device': 'Borrestranda'},
   'geometry': {'coordinates': [10.4688, 59.3775], 'type': 'Point'}},
  {'type': 'Feature',
   'properties': {'time': '2020-08-24T18:28:23.610Z',
    'last': '20.3',
    'device': 'Åsgårdstrand'},
   'geometry': {'coordinates': [10.4733, 59.3484], 'type': 'Point'}}]}
```