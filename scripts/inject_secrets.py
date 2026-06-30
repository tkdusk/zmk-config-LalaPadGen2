#!/usr/bin/env python3
"""Inject secrets from environment variables into keymap."""

import os
import re
import sys

def inject_secrets():
    """Replace secret placeholders in keymap with actual values."""
    keymap_path = "config/lalapadgen2.keymap"

    # Read keymap
    with open(keymap_path, "r") as f:
        content = f.read()

    # Get ENTER_PASS_BINDINGS from environment
    enter_pass = os.environ.get("ENTER_PASS_BINDINGS", "")

    if not enter_pass:
        print("Warning: ENTER_PASS_BINDINGS not set, using placeholder")
        return

    # Replace placeholder with actual bindings
    # Pattern: bindings = <&none>; // ENTER_PASS_PH
    pattern = r"bindings = <&none>; // ENTER_PASS_PH"
    replacement = f"bindings = <{enter_pass}>;"

    if pattern not in content:
        print("Error: Could not find ENTER_PASS_PH placeholder in keymap")
        sys.exit(1)

    content = content.replace(pattern, replacement)

    # Write back
    with open(keymap_path, "w") as f:
        f.write(content)

    print(f"Injected ENTER_PASS_BINDINGS successfully")

if __name__ == "__main__":
    inject_secrets()
