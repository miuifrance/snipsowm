OpenWeatherMap skill for Snips

Installation
The skill is on PyPI, so you can just install it with pip:

$ pip install snipsowm
Locale
To have the skills properly working, you need to generate locales for your languages. So far the supported locales are:

us en_US
fr fr_FR
You can generate them with sudo raspi-config. Going in the Localisation Options submenu, then in the Change Locale submenu, and selecting the locales you want to support. For instance, select en_US UTF-8 if you want support for English.

Usage
Snips Skills Server
