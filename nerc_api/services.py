from transformers import pipeline
from typing import List, Dict
from functools import lru_cache

from nerc_api.settings import settings


class NERCService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NERCService, cls).__new__(cls)
            cls._instance._initialize_model()
        return cls._instance

    def _initialize_model(self):
        """
        Initialize the token classification pipeline.
        Uses lru_cache to memoize the pipeline creation.
        """
        self.classifier = self._load_ner_pipeline()

    @lru_cache(maxsize=1)
    def _load_ner_pipeline(self):
        """
        Load the NER model pipeline with caching.
        """
        return pipeline(
            "ner",
            model=settings.MODEL_NAME,
            stride=settings.STRIDE,
            aggregation_strategy=settings.AGGREGATION_STRATEGY,
        )

    def predict(self, text: str) -> List[Dict]:
        """
        Perform named entity recognition on the input text.

        :param text: Input text to process
        :return: List of recognized entities
        """
        return self.classifier(text)


# Create a singleton service instance
nerc_service = NERCService()