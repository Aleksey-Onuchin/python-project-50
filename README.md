#### Hexlet tests and linter status:
[![Actions Status](https://github.com/Aleksey-Onuchin/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Aleksey-Onuchin/python-project-50/actions)

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
json and yaml files flat
[![asciicast](https://asciinema.org/a/H4zK8X23eMUptb6xlDZKhsE3b.svg)](https://asciinema.org/a/H4zK8X23eMUptb6xlDZKhsE3b)

json and yaml files recursion -f stylish
[![asciicast](https://asciinema.org/a/tpq8GHxYq3AAagyEZ6ZTO7xvD.svg)](https://asciinema.org/a/tpq8GHxYq3AAagyEZ6ZTO7xvD)

json and yaml files recursion -f plain
[![asciicast](https://asciinema.org/a/oSSfngNn0vU5CTihUN9TJ77DA.svg)](https://asciinema.org/a/oSSfngNn0vU5CTihUN9TJ77DA)

json and yaml files recursion -f json_formatter
[![asciicast](https://asciinema.org/a/ELOzIVcfWgnv9bCs2SO8nl9oy.svg)](https://asciinema.org/a/ELOzIVcfWgnv9bCs2SO8nl9oy)

https://github.com/Aleksey-Onuchin/python-project-50/actions/workflows/code-check.yml/badge.svg