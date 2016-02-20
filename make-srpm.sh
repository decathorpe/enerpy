#!/usr/bin/bash

VERSION=0.3.2

mkdir -p $HOME/rpmbuild/SOURCES
mkdir -p $HOME/rpmbuild/SPECS

git archive --format=tar.gz --prefix=enerpy-$VERSION/ HEAD > $HOME/rpmbuild/SOURCES/enerpy-$VERSION.tar.gz

cp ./enerpy.spec $HOME/rpmbuild/SPECS/

cd $HOME/rpmbuild/SPECS/
rpmbuild -bs enerpy.spec

cd $HOME/rpmbuild/SRPMS/
mv *.rpm $HOME/

cd $HOME
rm -r rpmbuild
