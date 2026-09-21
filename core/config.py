from pathlib import Path
import yaml
import pytest

from core.browser import BrowserDriver
from pages import Pages

CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"

with CONFIG_PATH.open() as file:
    settings = yaml.safe_load(file)

BASE_URL = settings["application"]["base_url"]