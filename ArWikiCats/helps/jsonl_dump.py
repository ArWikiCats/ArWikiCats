#!/usr/bin/python3
"""
!
"""

import functools
import inspect
import json
from pathlib import Path

import jsonlines

SAVE_ENABLE = True
SAVE_ENABLE = False


def save(path: Path | str, data: dict | list) -> str:
    """Append data to the specified JSONL file, creating it if needed."""
    path = Path(path)
    if isinstance(data, dict):
        data = [data]
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with jsonlines.open(path, mode="w") as writer:
            writer.write({})
    with jsonlines.open(path, mode="a") as writer:
        writer.write(data)


already_saved = {}


def dump_data(enable: bool = False, input_keys: list = None, compare_with_output: str = ""):
    """
    Decorator to save function inputs and output into a JSONL file.

    If input_keys is empty or None, all inputs (args + kwargs) are saved.
    Only saves unique data entries (no duplicates).
    """

    def decorator(func: callable) -> callable:
        """Wrap a function so its inputs and outputs are written to JSONL."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Execute the wrapped function and persist call details when enabled."""
            # Execute the wrapped function
            output = func(*args, **kwargs)

            if not SAVE_ENABLE and not enable:
                return output

            if not output:
                return output

            if isinstance(output, (list, tuple)) and not any(output):
                return output

            path = Path(__file__).parent / f"{func.__name__}.jsonl"

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

            if compare_with_output and data.get(compare_with_output) == output:
                return output

            # Create a unique key for this data entry to prevent duplicates
            # Use frozenset for hashable representation of the data
            try:
                data_key = (func.__name__, json.dumps(data, sort_keys=True))
            except TypeError:
                # If data is not serializable, use string representation
                data_key = (func.__name__, str(data))

            # Check if this exact data has already been saved
            if data_key in already_saved:
                return output

            # Mark as saved
            already_saved[data_key] = True

            # Write the JSON line using jsonlines
            with jsonlines.open(path, mode="a") as writer:
                writer.write(data)

            return output

        return wrapper

    return decorator
