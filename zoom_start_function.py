import subprocess

# Define the command to execute
command = ["pip", "playwright", "install-deps"]

# Execute the command
try:
    subprocess.run(command, check=True)
    print("Playwright dependencies installed successfully.")
except subprocess.CalledProcessError as e:
    print("Error: Playwright dependencies installation failed.")
    print(e)
