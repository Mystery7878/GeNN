import os
import sys

def load_module():
    arch = os.uname().machine.lower()

    try:
        if 'aarch64' in arch:
            import gen64 as mod
            print("Loaded 64-bit module")

        elif 'armv7' in arch or 'armv8l' in arch or ('arm' in arch and '64' not in arch):
            import gen32 as mod
            print("Loaded 32-bit module")

        else:
            print("Unsupported Device:", arch)
            sys.exit()

        return mod

    except ImportError as e:
        print("Module load failed:", e)
        sys.exit()


mymodule = load_module()