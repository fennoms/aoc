if ! echo $SHELL | grep -q "zsh"; then
    echo "This script is only supported by zsh."
    echo "To make it work, manually add the contents of aoc.sh to your shell's configuration file."
    exit 1
fi

echo "source $(realpath ./aoc.sh)" >> ~/.zshrc
echo "Setup complete. Restart your shell in order to use the commands. Also ensure you have set the AOC_SESSION environment variable
and make sure that AOC_DIR is also set to the directory where this repository is located."
