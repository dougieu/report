import subprocess
import sys
import os

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    # List of required packages
    packages = [
        "selenium",
        "webdriver_manager",
        "tkinter",
    ]

    print("Installing required packages...")
    for package in packages:
        try:
            install(package)
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")

    # Install ChromeDriver
    print("Installing ChromeDriver...")
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        ChromeDriverManager().install()
        print("ChromeDriver installed successfully")
    except Exception as e:
        print(f"Failed to install ChromeDriver: {e}")

    print("Setup complete. You can now run your main script.")

if __name__ == "__main__":
    main()
