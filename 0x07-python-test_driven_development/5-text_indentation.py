#!/usr/bin/python3
"""Doc"""
def text_indentation(text):
  """Indents text based on punctuation and newlines."""

  if not isinstance(text, str):
    raise TypeError("text must be a string")

  new_text = ""
  leading_space = True
  ender = ""

  for i in range(len(text)):
    if (i == len(text) - 1 and
        (text[i] not in '.?:')):
      ender = '\n'

    if text[i] == '\n':
      new_text += text[i]
      leading_space = True
      continue

    if text[i] == ' ':
      if i == len(text) - 1:
        break
      elif text[i + 1] == '\n':
        i += 1
        continue
      elif leading_space:
        continue

    leading_space = False

    if text[i] in '.?:':
      new_text += text[i] + "\n\n"
    else:
      new_text += text[i]

  print(new_text.rstrip(), end=ender)  # Remove trailing newline

