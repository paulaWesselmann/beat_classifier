from heapq import nlargest
from collections import defaultdict
import logging

# using pretrained spacy word embeddings
import spacy
nlp = spacy.load('en_core_web_lg')

logger = logging.getLogger(__name__)


class BeatClassification():

    def __init__(self):
        self.beat_dict =

    def get_beat_similarities(self, keywords):
        '''Return similarity scores for all beats.'''

        similarity = {}
        keywords_token = nlp(keywords)
        for beat, beat_value in beats_dict.items():
            beat_token = nlp(beat_value)
            similarity[beat] = keywords_token.similarity(beat_token)
        return similarity
