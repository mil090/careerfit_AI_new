"""Diagnostic script for pip/pandas install failure (session 11d116)."""
import json
import os
import sys
import time
import urllib.request

LOG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "..",
    "debug-11d116.log",
)
LOG_PATH = os.path.normpath(LOG_PATH)


def log(hypothesis_id: str, message: str, data: dict) -> None:
    # #region agent log
    payload = {
        "sessionId": "11d116",
        "runId": "post-fix",
        "hypothesisId": hypothesis_id,
        "location": "scripts/debug_pip_env.py",
        "message": message,
        "data": data,
        "timestamp": int(time.time() * 1000),
    }
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    # #endregion


def main() -> None:
    cwd = os.getcwd()
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    path_has_nonascii = any(ord(c) > 127 for c in cwd)

    log("A", "python_version", {"version": sys.version, "major_minor": py_ver})
    log("B", "path_encoding", {"cwd": cwd, "path_has_nonascii": path_has_nonascii})

    wheel_tags = []
    for ver in ("2.2.3", "2.3.3", "3.0.3"):
        url = f"https://pypi.org/pypi/pandas/{ver}/json"
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                meta = json.loads(resp.read().decode())
            cp314_wheels = [
                f["filename"]
                for f in meta.get("urls", [])
                if f.get("packagetype") == "bdist_wheel" and "cp314" in f.get("filename", "")
            ]
            any_wheels = [
                f["filename"]
                for f in meta.get("urls", [])
                if f.get("packagetype") == "bdist_wheel"
            ]
            wheel_tags.append(
                {
                    "pandas_version": ver,
                    "cp314_wheel_count": len(cp314_wheels),
                    "cp314_wheels": cp314_wheels[:3],
                    "total_wheel_count": len(any_wheels),
                }
            )
        except Exception as exc:  # noqa: BLE001
            wheel_tags.append({"pandas_version": ver, "error": str(exc)})

    log("A", "pypi_wheel_availability", {"versions": wheel_tags})

    import subprocess

    proc = subprocess.run(
        [sys.executable, "-m", "pip", "install", "pandas==2.2.3", "--dry-run"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    uses_sdist = "pandas-2.2.3.tar.gz" in proc.stdout or "pandas-2.2.3.tar.gz" in proc.stderr
    has_unicode_error = "UnicodeDecodeError" in proc.stderr
    log(
        "C",
        "pip_dry_run_pandas_2_2_3",
        {
            "returncode": proc.returncode,
            "uses_sdist_not_wheel": uses_sdist,
            "has_unicode_error": has_unicode_error,
            "stderr_tail": proc.stderr[-800:] if proc.stderr else "",
        },
    )

    import importlib.util

    packages = {}
    for name in ("fastapi", "pandas", "chromadb", "pydantic"):
        spec = importlib.util.find_spec(name)
        packages[name] = spec is not None

    log(
        "FIX",
        "post_fix_import_check",
        {
            "python": sys.version,
            "packages_importable": packages,
            "install_ok": all(packages.values()),
        },
    )

    print(f"Diagnostics written to {LOG_PATH}")


if __name__ == "__main__":
    main()
