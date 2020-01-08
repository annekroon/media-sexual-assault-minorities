# media-and-sexual-abuse
Automated content analysis of media coverage of sexual abuse

---
This repo contains the following elements:

-  Model training
    - train embedding models over two time periods
-  Get associations
-  Get results + visuals

We extend our dataset with the newspaper dataset reported here: https://journals.sagepub.com/doi/10.1177/0002716215569441

---

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
