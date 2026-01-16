#!/usr/bin/env bash

AUTHOR="Olaf Górski"
TITLE="Programming with Górski - Junior Python Developer"
FILENAME="${AUTHOR} - ${TITLE}"

pandoc -o "dist/${FILENAME}.epub" --highlight-style pygments \
  --css build_settings/epub.css --table-of-contents \
  --epub-embed-font=build_settings/fonts/Roboto-*.ttf \
  title.txt \
  preface.md \
  pirates.md \
  about.md \
  chapters/chapter*

pandoc -o "dist/${FILENAME}.pdf" --highlight-style pygments \
  --table-of-contents \
  -V mainfont="Roboto" \
  -V papersize:b5 \
  title.txt \
  preface.md \
  pirates.md \
  about.md \
  chapters/chapter*
