# word_finder
[![DOI](https://zenodo.org/badge/613132267.svg)](https://zenodo.org/badge/latestdoi/613132267)
---

#### Description
This is a proof-of-concept substring finder which, by default, finds occurrences of the words 'mouse' and 'mice' within a user-defined input string. Aside from this input, the user can also specify the usage of custom strings and find conditions (as a substring or singular word) within the console interface.

#### Installation and Usage
The base version of "Word Finder" does not require any additional libraries outside of what's included with Python 3.10. However, I recommend using Conda to separate your environments.

Execute the following command to install all necessary libraries via Conda (assuming you name the enviroment `word_finder_env`):
```lang=python
conda create --name word_finder_env --file requirements.txt
```

Afterwards, activate your environment:
```lang=python
conda activate word_finder_env
```

You can now use the substring finder with
```lang=python
python3 main.py
```

Alternatively, if you're looking to execute unit tests:
```lang=python
pytest
```

#### Demo
Default ('mouse' is singular and 'mice' is a substring):
[![asciicast](https://asciinema.org/a/X7kPSjEknNcBYEmaye9sEMG0A.svg)](https://asciinema.org/a/X7kPSjEknNcBYEmaye9sEMG0A)

Custom: ('piggy' is singular and 'wolf' is a substring)
[![asciicast](https://asciinema.org/a/lQ0FjTYfREywLieFNMfpSqbZN.svg)](https://asciinema.org/a/lQ0FjTYfREywLieFNMfpSqbZN)
