import inspect

from . import engines

__version__ = "0.1.0"


class Generator:
    def __init__(self, *engines, separator):
        self.engines = engines
        self.separator = separator

    def generate(self):
        parts = [engine.generate() for engine in self.engines]
        return self.separator.join(parts)


def build_generator(*engines, separator="-"):
    engines = [engine() if inspect.isclass(engine) else engine for engine in engines]
    return Generator(*engines, separator=separator)


def youtube(length=11, avoid_confusing_chars=False, blacklist_symbols=None):
    generator = Generator(
        engines.YoutubeEngine(
            length=length, avoid_confusing_chars=False, blacklist_symbols=None
        ),
        separator="",
    )
    return generator.generate()


def heroku(code_length=4):
    generator = Generator(
        engines.AdjectiveWordEngine(),
        engines.NounWordEngine(),
        engines.NumberEngine(length=code_length, zero_start=False),
        separator="-",
    )
    return generator.generate()


def six_digit():
    generator = Generator(
        engines.NumberEngine(length=6, zero_start=False), separator=""
    )
    return generator.generate()
