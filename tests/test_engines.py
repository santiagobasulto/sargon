import random
from sargon.engines import (
    YoutubeEngine,
    NumberEngine,
    ColorWordEngine,
    NounWordEngine,
    VerbWordEngine,
    AdjectiveWordEngine,
    CityWordEngine,
)


def test_youtube_simple():
    engine = YoutubeEngine()

    random.seed(30)
    assert engine.generate() == "LNb-P0nqdzy"


def test_youtube_custom_length():
    engine = YoutubeEngine(length=6)

    random.seed(30)
    assert engine.generate() == "LNb-P0"


def test_youtube_confusing_chars():
    engine = YoutubeEngine()

    random.seed(33)
    assert engine.generate() == "vOo01rEPIHl"

    engine = YoutubeEngine(avoid_confusing_chars=True)

    random.seed(33)
    assert engine.generate() == "QmUr7uHVNMn"


def test_youtube_blacklist():
    engine = YoutubeEngine()

    random.seed(42)
    assert engine.generate() == "obVrp_i9gR4"

    engine = YoutubeEngine(blacklist_symbols="-_")

    random.seed(33)
    assert engine.generate() == "KkOo01rEPIH"


def test_number_engine():
    engine = NumberEngine()

    random.seed(1)
    assert engine.generate() == "291417"

    engine = NumberEngine(4)
    random.seed(50)
    assert engine.generate() == "7453"

    engine = NumberEngine(4)
    random.seed(2)
    assert engine.generate() == "0115"

    engine = NumberEngine(4, zero_start=False)
    random.seed(2)
    assert engine.generate() == "1115"


# Colors
def test_colors():
    engine = ColorWordEngine()

    random.seed(33)
    assert engine.generate() == "ultraviolet"

    random.seed(50)
    assert engine.generate() == "sepia"


def test_nouns():
    engine = NounWordEngine()

    random.seed(1)
    assert engine.generate() == "cucumber"

    random.seed(50)
    assert engine.generate() == "sweatshirt"


def test_verbs():
    engine = VerbWordEngine()

    random.seed(1)
    assert engine.generate() == "deliver"

    random.seed(50)
    assert engine.generate() == "spell"


def test_adjectives():
    engine = AdjectiveWordEngine()

    random.seed(3)
    assert engine.generate() == "judicious"

    random.seed(50)
    assert engine.generate() == "utopian"


def test_cities():
    engine = CityWordEngine()

    random.seed(628064)
    assert engine.generate() == "manhattan"

    engine = CityWordEngine(country="United States")
    random.seed(4630)
    assert engine.generate() == "pensacola"
