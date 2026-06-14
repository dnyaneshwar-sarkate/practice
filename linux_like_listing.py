## Python programme to list down all the directory content Ex. Linux command: ls -lrth

# import subprocess

# result = subprocess.run(
#     "dir",
#     shell=True,
#     capture_output=True,
#     text=True
# )

# print(result.stdout)

from pathlib import Path

for file in Path(".").iterdir():
    print(file)