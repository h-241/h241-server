from pathlib import Path


path: Path
for path in Path(".").glob("**/*.sh"):
    data = path.read_bytes()
    lf_data = data.replace(b"\r\n", b"\n")
    path.write_bytes(lf_data)

import subprocess

# Ensure the backend directory exists before running the command
backend_path = Path("./backend")
if backend_path.exists():
    # Run poetry-plugin-export to generate requirements.txt from poetry.toml
    subprocess.run(["poetry", "plugin", "add", "poetry-plugin-export"], check=True)
    subprocess.run(["poetry", "export", "-f", "requirements.txt", "--output", "./backend/requirements.txt", "--without-hashes"], check=True)
else:
    print("Backend directory does not exist. Skipping requirements generation.")
