import os
import subprocess
import sys

def main():
    # Check if WiX Toolset is installed and available in PATH
    try:
        subprocess.run(["candle.exe", "-help"], check=True, stdout=subprocess.PIPE)
    except FileNotFoundError:
        print("WiX Toolset not found. Please ensure it is installed and added to your system's PATH.")
        sys.exit(1)

    # Compile WiX XML into WiX object file
    result = subprocess.run(["candle.exe", "template.wxs"], stdout=subprocess.PIPE)
    if result.returncode != 0:
        print("Error compiling WiX XML:")
        print(result.stdout.decode("utf-8"))
        sys.exit(1)

    # Link WiX object file into MSI package
    result = subprocess.run(["light.exe", "template.wixobj", "-ext", "WixUIExtension", "-o", "output.msi"], stdout=subprocess.PIPE)
    if result.returncode != 0:
        print("Error linking WiX object file:")
        print(result.stdout.decode("utf-8"))
        sys.exit(1)

    print("MSI package created successfully: output.msi")

if __name__ == "__main__":
    main()
