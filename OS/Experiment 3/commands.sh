#!/bin/bash

echo "================= (a) OS Version, Release, and Kernel Info ================="
echo "-> /etc/os-release:"
cat /etc/os-release

echo -e "\n-> Kernel Info (uname -a):"
uname -a

echo -e "\n-> Hostname Info:"
hostnamectl

echo -e "\n================= (b) Top 10 Processes (Descending by CPU) ================="
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 11

echo -e "\n================= (c) Process with Highest Memory Usage ================="
ps aux --sort=-%mem | head -n 11

echo -e "\n================= (d) Current User and Logname ================="
echo "Logged in user (whoami): $(whoami)"
echo "Login name (logname): $(logname)"

echo -e "\n================= (e) System Info & Environment ================="
echo "Current Shell: $SHELL"
echo "Home Directory: $HOME"
echo "Operating System Type: $(uname)"
echo "PATH Setting: $PATH"
echo "Current Working Directory: $(pwd)"
