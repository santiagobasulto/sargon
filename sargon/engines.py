import string
import random
from . import data


class YoutubeEngine:
    DEFAULT_CHARS = string.ascii_letters + string.digits + "-_"
    CONFUSING_CHARS = "iIlL0Oo"

    def __init__(self, length=11, avoid_confusing_chars=False, blacklist_symbols=None):
        blacklist = blacklist_symbols or []
        if avoid_confusing_chars:
            blacklist = set(blacklist + list(self.CONFUSING_CHARS))

        replacement_table = {ord(c): None for c in blacklist}

        self.chars = self.DEFAULT_CHARS.translate(replacement_table)
        self.length = length

    def generate(self):
        return "".join(random.sample(self.chars, self.length))


class WordEngine:
    DATA_VAR_NAME = None

    def generate(self):
        if not self.DATA_VAR_NAME:
            raise NotImplementedError()
        return random.choice(getattr(data, self.DATA_VAR_NAME))


class ColorWordEngine(WordEngine):
    DATA_VAR_NAME = "COLORS"


class NounWordEngine(WordEngine):
    DATA_VAR_NAME = "NOUNS"


class VerbWordEngine(WordEngine):
    DATA_VAR_NAME = "VERBS"


class AdjectiveWordEngine(WordEngine):
    DATA_VAR_NAME = "ADJECTIVES"


class CityWordEngine(WordEngine):
    DATA_VAR_NAME = "CITIES"

    def __init__(self, country=None):
        self.country = country

    def available_countries(self):
        return list(data.CITIES.keys())

    def generate(self):
        country = self.country or random.choice(self.available_countries())
        cities = data.CITIES[country]
        return random.choice(cities).lower().replace(" ", "-")


class NumberEngine:
    _NUMBER_LIST = list(range(10))
    _NUMBER_LIST_NON_ZERO = list(range(1, 10))

    def __init__(self, length=6, zero_start=True):
        self.length = length
        self.zero_start = zero_start

    def generate(self):
        base_start = ""
        length = self.length
        if not self.zero_start:
            base_start = str(random.choice(self._NUMBER_LIST_NON_ZERO))
            length -= 1
        return base_start + "".join(
            [str(random.choice(self._NUMBER_LIST)) for _ in range(length)]
        )
