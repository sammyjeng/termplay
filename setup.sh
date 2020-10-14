#!/usr/bin/env bash
PM=$1 #package-manager like apt, pacman
which mpv 1>/dev/null ; if [[ $? = 1 ]]; then sudo $PM install mpv; else echo "Mpv is installed." ; fi
