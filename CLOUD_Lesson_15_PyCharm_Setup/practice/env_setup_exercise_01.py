"""
VIZIONE LABS — PYTHON: BUILD REAL PROJECTS
Track A: Phase 2 (Lesson 15)
Exercise File: practice/env_setup_exercise_01.py

Title: Environment Setup, PyCharm Configuration, Local Execution Context
Description: A fundamental practice script to inspect and verify the active
             Python interpreter, virtual environment boundaries, executable paths,
             and system environment variables.
"""

import sys
import os
from pathlib import Path


def inspect_execution_environment() -> None:
    """
    Inspects and displays key parameters of the active Python interpreter,
    system paths, and virtual environment bindings.
    """
    print("=" * 70)
    print("VIZIONE LABS — LOCAL ENVIRONMENT & INTERPRETER DIAGNOSTIC")
    print("=" * 70)

    # 1. Active Python Executable Binary Path
    python_executable = sys.executable
    print(f"[1] Active Python Binary Path:\n    -> {python_executable}\n")

    # 2. Python Version Details
    version_info = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"[2] Active Python Runtime Version:\n    -> Python {version_info}\n")

    # 3. Virtual Environment Detection
    # VIRTUAL_ENV is automatically set by venv / PyCharm run configurations
    virtual_env_path = os.environ.get("VIRTUAL_ENV")
    is_in_venv = sys.prefix != sys.base_prefix or virtual_env_path is not None

    print("[3] Virtual Environment Status:")
    if is_in_venv:
        active_env = virtual_env_path if virtual_env_path else sys.prefix
        print("    -> STATUS: Isolated Virtual Environment Detected (Active)")
        print(f"    -> VENV ROOT: {active_env}\n")
    else:
        print("    -> STATUS: WARNING! Running on Global System Python Interpreter\n")

    # 4. Current Working Directory (CWD) Execution Context
    cwd = Path.cwd()
    print(f"[4] Current Working Directory Context:\n    -> {cwd}\n")

    # 5. Core Environment Variable Check
    print("[5] Execution Context Variables:")
    user_name = os.environ.get("USERNAME", os.environ.get("USER", "Unknown"))
    os_name = os.name
    print(f"    -> OS Platform: {os_name}")
    print(f"    -> Current OS User: {user_name}")
    print("=" * 70)


if __name__ == "__main__":
    inspect_execution_environment()