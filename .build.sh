#!/bin/bash

project=withfeathers
pkgs=/var/www/pkgs/$project
production=/var/www/$project

cd $production
#git pull origin master

echo "move compressed files and sha/gpg signatures to packages directory"
git archive --format=tar -o $project.tar.gz HEAD
git archive --format=zip -o $project.zip HEAD

sha256sum *.tar.gz *.zip > sha256sums.txt
gpg --pinentry-mode loopback --passphrase $gpgpass --batch --yes --detach-sign -a sha256sums.txt

mv $project.tar.gz $project.zip sha256sums.txt* $pkgs
