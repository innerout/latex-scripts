#!/bin/python
import glob
import os
from os import path

reformat_function = '(defun format-whole-buffer()\n\
  (interactive)\n\
  (find-file "filepath")\n\
  (mark-whole-buffer)\n\
  (fill-paragraph)\n\
  (save-buffer)\n\n\
'

final_reformat_function = '  (find-file "filepath")\n\
  (mark-whole-buffer)\n\
  (fill-paragraph)\n\
  (save-buffer)\n\
  (kill-emacs))\n\
'

reformat_all_files_with_emacs = ""
count = len(glob.glob("*.tex"))
i = 0
for file_path in glob.glob("*.tex"):
    temp_reformat_function = reformat_function
    temp_reformat_function = temp_reformat_function.replace("filepath", file_path)

    i += 1
    if count != i:
        reformat_all_files_with_emacs += temp_reformat_function
    else:
        reformat_all_files_with_emacs += final_reformat_function.replace(
            "filepath", file_path
        )

print(reformat_all_files_with_emacs)
print(count)

with open("reformat.el", "w") as opened_file:
    opened_file.write(reformat_all_files_with_emacs)
