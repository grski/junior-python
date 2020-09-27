#!/usr/bin/env bash

pandoc -o dist/python.epub --highlight-style pygments \
  --css build_settings/epub.css --table-of-contents \
  --epub-embed-font=build_settings/fonts/Roboto-*.ttf \
  title.txt \
  preface.md \
  pirates.md \
  about.md \
  chapters/chapter*

pandoc -o dist/python.pdf --highlight-style pygments \
  --table-of-contents \
  -V mainfont="Roboto" \
  -V papersize:b5 \
  title.txt \
  preface.md \
  pirates.md \
  about.md \
  chapters/chapter*
