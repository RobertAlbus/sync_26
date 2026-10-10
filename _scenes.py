import importlib


def scene_names() -> str:
    return importlib.import_module("00_main").scene_names()
