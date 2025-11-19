#!/usr/bin/python3
"""
!
"""
import functools
import jsonlines
from pathlib import Path
import inspect

SAVE_ENABLE = True
SAVE_ENABLE = False


def save(path, data) -> str:
    path = Path(path)
    # ---
    if isinstance(data, dict):
        data = [data]
    # ---
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with jsonlines.open(path, mode='w') as writer:
            writer.write({})
    # ---
    with jsonlines.open(path, mode='a') as writer:
        writer.write(data)


def save_data(filename: str="", input_keys: list = None):
    """
    Decorator to save function inputs and output into a JSONL file.

    If input_keys is empty or None, all inputs (args + kwargs) are saved.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Execute the wrapped function
            output = func(*args, **kwargs)

            if not SAVE_ENABLE:
                return output

            if not output:
                return output

            if isinstance(output, (list, tuple)) and not any(output):
                return output

            path = Path(__file__).parent / f"{func.__name__}.jsonl"
            # path = Path(filename)

            # if not path.exists(): path.touch()

            bound_args = inspect.signature(func).bind(*args, **kwargs)
            bound_args.apply_defaults()
            all_arguments = bound_args.arguments
            data = {}
            # Case 1: Save all inputs
            if not input_keys:
                data.update(all_arguments)
            # Case 2: Save only the selected keys
            else:
                for key in input_keys:
                    if key in all_arguments:
                        data[key] = all_arguments[key]

            # Add function output
            data["output"] = output

            # Write the JSON line using jsonlines
            with jsonlines.open(path, mode="a") as writer:
                writer.write(data)

            return output

        return wrapper

    return decorator
