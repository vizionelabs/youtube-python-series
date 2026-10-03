"""
VIZIONE LABS — PYTHON: BUILD REAL PROJECTS
Track A: Phase 2 (Lesson 15)
Production System: main.py

Title: Automated Local Environment & Runtime Compliance Auditor
Description: An enterprise-grade environment verification system designed to validate
             local IDE configurations, virtual environment isolation, python binary
             integrity, and system dependencies before executing critical enterprise pipelines.
"""

import os
import sys
import platform

from pathlib import Path


def verify_python_version(min_major: int = 3, min_minor: int = 10) -> dict:
    """
    Validates that the active Python interpreter meets minimum runtime requirements.
    """
    current_major = sys.version_info.major
    current_minor = sys.version_info.minor
    is_supported = (current_major > min_major) or (
        current_major == min_major and current_minor >= min_minor
    )

    return {
        "check": "Python Version Compliance",
        "status": "PASS" if is_supported else "FAIL",
        "details": f"Active Version: {current_major}.{current_minor}.{sys.version_info.micro} (Required >= {min_major}.{min_minor})",
    }


def verify_virtual_environment() -> dict:
    """
    Validates that the script is running inside an isolated virtual environment
    rather than global system Python.
    """
    virtual_env = os.environ.get("VIRTUAL_ENV")
    is_venv = sys.prefix != sys.base_prefix or virtual_env is not None

    if is_venv:
        venv_path = virtual_env if virtual_env else sys.prefix
        status = "PASS"
        details = f"Active Virtual Environment: {venv_path}"
    else:
        status = "FAIL"
        details = "WARNING: Execution detected on Global System Python! Isolated venv required."

    return {
        "check": "Virtual Environment Isolation",
        "status": status,
        "details": details,
    }


def verify_workspace_directory(required_subdirs: list[str] = None) -> dict:
    """
    Ensures the current working directory context matches expected enterprise workspace standards.
    """
    if required_subdirs is None:
        required_subdirs = ["practice"]

    cwd = Path.cwd()
    missing_dirs = [d for d in required_subdirs if not (cwd / d).exists()]

    if not missing_dirs:
        status = "PASS"
        details = f"Workspace root verified at: {cwd}"
    else:
        status = "WARN"
        details = f"Workspace verified at {cwd}, but missing expected directories: {missing_dirs}"

    return {
        "check": "Workspace Directory Structure",
        "status": status,
        "details": details,
    }


def verify_environment_variables(required_keys: list[str] = None) -> dict:
    """
    Checks for required environment configuration keys.
    """
    if required_keys is None:
        required_keys = ["PATH"]

    missing_keys = [key for key in required_keys if key not in os.environ]

    if not missing_keys:
        status = "PASS"
        details = (
            f"All required environment variables present: {required_keys}"
        )
    else:
        status = "FAIL"
        details = f"Missing environment variables: {missing_keys}"

    return {
        "check": "Environment Variables Validation",
        "status": status,
        "details": details,
    }


def run_environment_audit() -> None:
    """
    Executes all compliance checks and prints a structured enterprise status report.
    """
    print("=" * 80)
    print("VIZIONE LABS — ENTERPRISE ENVIRONMENT COMPLIANCE AUDITOR")
    print("=" * 80)
    print(
        f"Host System: {platform.system()} {platform.release()} ({platform.machine()})"
    )
    print(f"Active Interpreter Binary: {sys.executable}")
    print("-" * 80)

    audit_suite = [
        verify_python_version(),
        verify_virtual_environment(),
        verify_workspace_directory(),
        verify_environment_variables(),
    ]

    total_checks = len(audit_suite)
    passed_checks = 0

    for result in audit_suite:
        check_name = result["check"]
        status = result["status"]
        details = result["details"]

        badge = f"[{status}]"
        print(f"{badge:<8} | {check_name:<35} | {details}")

        if status == "PASS":
            passed_checks += 1

    print("-" * 80)
    print(f"AUDIT SUMMARY: {passed_checks}/{total_checks} Checks Passed.")

    if passed_checks == total_checks:
        print(
            "STATUS: [READY] Environment fully compliant for enterprise execution."
        )
    else:
        print(
            "STATUS: [ACTION REQUIRED] Please adjust PyCharm interpreter / venv configuration."
        )

    print("=" * 80)


if __name__ == "__main__":
    run_environment_audit()