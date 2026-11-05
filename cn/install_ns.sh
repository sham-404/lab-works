#!/usr/bin/env bash
set -e

echo "[+] Creating workspace in /tmp/ns_nam_setup..."
mkdir -p /tmp/ns_nam_setup
cd /tmp/ns_nam_setup

echo "[+] Installing core X11 and Tcl/Tk runtime dependencies..."
sudo apt-get update
sudo apt-get install -y libx11-6 libx11-dev libxmu6 libxext6 libxft2 libstdc++6 wget

echo "[+] Downloading Ubuntu 20.04 (Focal) release packages..."
wget -q --show-progress http://archive.ubuntu.com/ubuntu/pool/universe/n/nam/nam_1.15-5_amd64.deb
wget -q --show-progress http://archive.ubuntu.com/ubuntu/pool/universe/n/n/ns2/ns2_2.35+dfsg-3build1_amd64.deb

echo "[+] Unpacking legacy binaries..."
sudo dpkg -i nam_1.15-5_amd64.deb ns2_2.35+dfsg-3build1_amd64.deb || true

echo "[+] Resolving missing shared libraries..."
sudo apt-get install -f -y

echo "[+] Pinning 'ns2' and 'nam' in APT to prevent system upgrades..."
sudo apt-mark hold ns2 nam

echo "[+] Verification of held packages:"
dpkg --get-selections | grep -E "ns2|nam"

echo "[+] Cleaning up temporary download files..."
cd ~
rm -rf /tmp/ns_nam_setup

echo "[+] Setup complete! Test execution with: nam out.nam"
