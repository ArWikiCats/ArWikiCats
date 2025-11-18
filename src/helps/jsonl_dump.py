#!/usr/bin/python3
"""
!
"""
import functools
import jsonlines
from pathlib import Path


def save(path, data) -> str:
    path = Path(path)
    # ---
    if isinstance(data, dict):
        data = [data]
    # ---
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with jsonlines.open(path, mode='w') as writer:
            writer.write_all({})
    # ---
    with jsonlines.open(path, mode='a') as writer:
        writer.write_all(data)


def save_data(filename: str, input_keys: list = None):
    """
    Decorator to save function inputs and output into a JSONL file.

    If input_keys is empty or None, all inputs (args + kwargs) are saved.
    """
    # path = Path(__file__).parent / filename
    path = Path(filename)

    if not path.exists():
        path.touch()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Execute the wrapped function
            output = func(*args, **kwargs)

            arg_names = func.__code__.co_varnames
            data = {}

            # Case 1: Save all inputs
            if not input_keys:
                # Save positional args by name
                for name, value in zip(arg_names, args):
                    data[name] = value

                # Save keyword args
                for key, value in kwargs.items():
                    data[key] = value

            # Case 2: Save only the selected keys
            else:
                for key in input_keys:
                    # Check kwargs first
                    if key in kwargs:
                        data[key] = kwargs[key]
                        continue

                    # Then check positional args
                    if key in arg_names:
                        index = arg_names.index(key)
                        if index < len(args):
                            data[key] = args[index]

            # Add function output
            data["output"] = output

            # Write the JSON line using jsonlines
            with jsonlines.open(path, mode="a") as writer:
                writer.write(data)

            return output

        return wrapper

    return decorator
