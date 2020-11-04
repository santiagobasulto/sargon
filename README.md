# Sargon: Random Code Generator

`sargon` is a simple Python package (no external dependencies) to generate random (mnemonic) codes simulating Youtube or Heroku style. It's extensible to define your own rules too.

### Basic usage

#### Heroku

`heroku(code_length=4)`

Heroku codes have the form `ADJECTIVE-NOUN-CODE`:

Example:

```python
>>> from sargon import heroku
>>> heroku()
"valuable-period-6016"

>>> heroku(6)
"sweet-hat-673004"
```

#### YouTube

`youtube(length=11, avoid_confusing_chars=False, blacklist_symbols=None)`

Example:

```python
>>> from sargon import youtube
>>> youtube()
"dQw4w9WgXcQ"

>>> youtube(6)
"LNb-P0"

>>> youtube(6, blacklist_symbols='-')
"LNbP0X"
```

#### 6 Digit Generator

`six_digit()`

```python
>>> from sargon import six_digit
>>> six_digit()
"770584"
```

### Defining your own generators

Checkout `engines.py` for the list of available engines and the parameters they receive. Here's an example:

```python
>>> from sargon import engines, build_generator
>>> generator = build_generator(
    engines.CityWordEngine(country='United States'),
    engines.NumberEngine(4))
>>> generator.generate()
"bellview-5269"


>>> generator = build_generator(
    engines.AdjectiveWordEngine(),
    engines.CityWordEngine(country='United States'),
    engines.NumberEngine(4))
>>> generator.generate()
"electric-knoxville-6594"
```

### Why `sargon`?

I wanted to call the package [Hammurabi](https://en.wikipedia.org/wiki/Hammurabi), as the babylonian king that issued the [Code of Hammurabi](https://en.wikipedia.org/wiki/Code_of_Hammurabi), but there's another package named `hammurabi`, so I went with another great ruler that I like to read about: [Sargon the great](https://en.wikipedia.org/wiki/Sargon_of_Akkad) the emperor of the Akkadian empire, what is thought today to be the first empire in history.
