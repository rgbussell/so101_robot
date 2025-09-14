#!/bin/sh
set -e

if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed"
fi

echo >> /Users/rgbussell/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/rgbussell/.zprofile