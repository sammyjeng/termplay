#!/bin/bash

# set -x
if [ "$1" = "" ]; then echo "./mplaylist.sh ~/Music or a main directory containing your music files"; fi
declare -a FLIST
FLIST=( 'mkv' 'mp4' 'webm' 'm4a' 'mp3' 'wav' 'mpa' 'wma' '3gp' 'flv' 'mov' )
for i in "${FLIST[@]}"
do
    find $1 -type f -name *.$i | tee -a tmp.pl

done

sort -u tmp.pl >> list.pl ; rm tmp.pl

