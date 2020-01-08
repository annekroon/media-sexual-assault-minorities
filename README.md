# media-sexual-assault-minorities
Automated content analysis of media coverage of sexual abuse

---
This repo contains the following elements:

-  Model training
    - train embedding models over two time periods
-  Get associations
-  Get results + visuals

---

## Attention for sexual assault and minorities in Dutch news: `/media_attention/`

`/media_attention/get_timeline_data_from_inca`: this file will retrieve relevant frequenties from Dutch newspapers.
Search terms included.

`/media_attention/plot_media_attention`: this file will use the output of `/media_attention/get_timeline_data_from_inca` to create graphs.


## Model training:

## Get associations from embedding models:

`/associations/sexualviolence.py`

python3 sexualviolence.py --attribute neg --target dutch
python3 sexualviolence.py --attribute neg --target ref
python3 sexualviolence.py --attribute neg --target ingroup
python3 sexualviolence.py --attribute neg --target arab

python3 sexualviolence.py --attribute pos --target dutch
python3 sexualviolence.py --attribute pos --target ref
python3 sexualviolence.py --attribute pos --target ingroup
python3 sexualviolence.py --attribute pos --target arab
