from __future__ import annotations

import importlib.util
import inspect
import sys
from pathlib import Path

from manim import Scene

_HERE = Path(__file__).resolve().parent


def _scene_files() -> list[Path]:
    return sorted(
        path
        for path in _HERE.glob("[0-9][0-9]_*.py")
        if path.name != Path(__file__).name
    )


def _import_scene_classes() -> list[type[Scene]]:
    classes: list[type[Scene]] = []
    for path in _scene_files():
        module_name = f"{__name__}.{path.stem}"
        spec = importlib.util.spec_from_file_location(module_name, path)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        for name, obj in vars(module).items():
            if (
                inspect.isclass(obj)
                and issubclass(obj, Scene)
                and obj is not Scene
                and obj.__module__ == module_name
            ):
                globals()[name] = obj
                if obj not in classes:
                    classes.append(obj)
    return classes


_SCENES = _import_scene_classes()


def scene_names() -> str:
    return " ".join(scene.__name__ for scene in _SCENES)
