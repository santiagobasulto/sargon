import random

from sargon import build_generator, youtube, heroku, six_digit
from sargon import engines


def test_build_generator_standard():
    generator = build_generator(engines.YoutubeEngine(), engines.NumberEngine(4))

    random.seed(1)
    assert generator.generate() == "rK2ZWeqhF7C-7631"


def test_build_generator_classes():
    generator = build_generator(engines.YoutubeEngine, engines.NumberEngine)

    random.seed(1)
    assert generator.generate() == "rK2ZWeqhF7C-763170"


# Predefined generators
def test_youtube_generator():
    random.seed(30)
    assert youtube() == "LNb-P0nqdzy"

    random.seed(30)
    assert youtube(6) == "LNb-P0"


def test_heroku_generator():
    random.seed(2)
    assert heroku() == "brainy-ceramic-2524"

    random.seed(3)
    assert heroku(code_length=6) == "judicious-vinyl-359791"


def test_six_digit_generator():
    random.seed(1)
    assert six_digit() == "391417"
