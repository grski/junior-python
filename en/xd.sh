#!/usr/bin/env bash

pandoc -o dist/python.pdf --highlight-style pygments \
  --table-of-contents \
  -V mainfont="Roboto" \
  -V geometry:margin=2cm \
  -V papersize:b5 \
  chapters/chapter-03* \
  chapters/chapter-04* \
  chapters/chapter-05*
