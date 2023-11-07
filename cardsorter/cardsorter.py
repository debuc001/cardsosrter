import pandas as pd
import requests
import json
import numpy as np

from dataframe_functions import *
from image_manipulation import *

deckstats_card_dataframe = pd.DataFrame( columns = ['QUANTITY','CARDNAME_EN'])
scryfall_base_api_url = "https://api.scryfall.com/"
scryfall_cardname_object = "cards/named?exact=!"
image_input = "../tests/testcard.jpg"

#Create dataframe 
deckstats_card_dataframe = get_deckstats_card_dataframe(deckstats_card_dataframe)
deckstats_card_dataframe = preprocessing_dataframe(deckstats_card_dataframe)

#print(deckstats_card_dataframe)

crop_image(image_input)
get_image_size(image_input)