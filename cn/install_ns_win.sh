#!/usr/bin/env bash
set -e

# Enable 32-bit architecture & install minimal Wine
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install -y --no-install-recommends wine wine32

# Download 32-bit NAM executable
wget https://www.isi.edu/nsnam/dist/binary/nam-1.15-win32.exe -O nam.exe

echo "Setup complete. Launch whenever ready using: wine nam.exe out.nam"
