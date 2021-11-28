import json
import requests
import argparse

MANIFEST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

# Get program arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "--release",
    help="latest release version of minecraft",
    action="store_true",
    default=True,
)
parser.add_argument(
    "--snapshot",
    help="latest snapshot version of minecraft, overrides --release if both "
    "are provided",
    action="store_true",
    default=False,
)
parser.add_argument(
    "version",
    help="desired version number, latest if not provided",
    type=str,
    default="latest",
    nargs="?",
)
args = parser.parse_args()

target = "snapshot" if args.snapshot else "release"
desired_version = args.version

# Get the latest release manifest from Mojang
manifest = json.loads(requests.get(MANIFEST_URL).content)

# Parse the version number, respecting user input if any
version = None
if desired_version == "latest":
    version = manifest["latest"][target]
else:
    version = desired_version

# Find the desired version number from the release manifest
version_blob = None
try:
    version_blob = next(blob for blob in manifest["versions"] if blob["id"] == version)
except StopIteration:
    print(f"Could not find download for version {version}")
    exit(1)

print(f"Found blob for {target} version {version}")

# Download the server.jar
download_url = json.loads(requests.get(version_blob["url"]).content)["downloads"][
    "server"
]["url"]

print(f"Downloading server.jar for {version}...")

file_data = requests.get(download_url)

# Replace the user's server.jar
print("Replacing ./server.jar")

with open("server.jar", "wb") as file_object:
    file_object.write(file_data.content)

print("Done!")
