#### Hexlet tests and linter status:
[![Actions Status](https://github.com/Aleksey-Onuchin/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Aleksey-Onuchin/python-project-50/actions)

[![Actions Status](https://github.com/Aleksey-Onuchin/python-project-50/actions/workflows/code-check.yml/badge.svg)](https://github.com/Aleksey-Onuchin/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/885fa6645ccad79efdbb/maintainability)](https://codeclimate.com/github/Aleksey-Onuchin/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/885fa6645ccad79efdbb/test_coverage)](https://codeclimate.com/github/Aleksey-Onuchin/python-project-50/test_coverage)

#### Version: python 3.10.6; poetry 1.5.1

#### Description:
Difference Calculator. Calculates difference between two .json or .yaml files and returns it in the selected format.\
3 Formatters available:
* Stylish formatter - tree structure with the indents, marked by +/-.
* Plain formatter - list of changed lines, marked by statuses (added/removed/updated).
* Json formatter - returns the .json file, containing the difference.

Stylish formatter is the default one.

**How to install:** run 'make package-install'\
**How to run:** run 'gendiff [-f formatter_name-optional] [.way/to/file1] [.way/to/file2]'


#### Work examples:
json and yaml flat files, default formatter
[![asciicast](https://asciinema.org/a/GMJftkXTYFoXPOY0yJvwncoqh.svg)](https://asciinema.org/a/GMJftkXTYFoXPOY0yJvwncoqh)

json and yaml recursion files, stylish formatter
[![asciicast](https://asciinema.org/a/3pUH9lKH52M7TkJ0XctnreL50.svg)](https://asciinema.org/a/3pUH9lKH52M7TkJ0XctnreL50)

json and yaml recursion files, plain formatter
[![asciicast](https://asciinema.org/a/kYHscWZMYUD5QFtEIJCcbCEnn.svg)](https://asciinema.org/a/kYHscWZMYUD5QFtEIJCcbCEnn)

json and yaml recursion files, json formatter
[![asciicast](https://asciinema.org/a/sllzmcwOm24HzuuYmPb89p4au.svg)](https://asciinema.org/a/sllzmcwOm24HzuuYmPb89p4au)

https://github.com/Aleksey-Onuchin/python-project-50/actions/workflows/code-check.yml/badge.svg