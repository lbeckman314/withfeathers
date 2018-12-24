Output a randomly chosen poem by emily dickinson. Poems were retrieved from [Project Gutenberg](https://www.gutenberg.org/ebooks/12242). Optionally download and parse the poems straight from the source!

To print a poem, add the `--print` flag to `main.py`!
```shell
$ python3 withfeathers/withfeathers.py --print --decorate --time

XXXVII.

VOID.

Great streets of silence led away
To neighborhoods of pause;
Here was no notice, no dissent,
No universe, no laws.

By clocks 't was morning, and for night
The bells at distance called;
But epoch had no basis here,
For period exhaled.

~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~

time elapsed: 39.45207595825195 ms

```

A really good **R implementation** (and inspiration for this program) is this one! -> [Display a random Emily Dickinson poem (Gutenberg edition)](https://r.amherst.edu/apps/nhorton/Dickinson1/)

<br />
<hr />

# Installation

## 0. Prerequisites

[`python 3`](https://www.python.org/) :: for running the script.

[`git`](https://git-scm.com/) :: for a quick git clone.

If you are running Windows, the above utilities will be packaged in any of the following: [babun](https://babun.github.io/), [cmder](http://cmder.net/), or [Linux Subsystem for Windows](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Take your pick! : )

The above utilities should be installed (or readily available) if you are running a Unix derivative (such as Linux, macOS, or any of the BSD's).

## 1. Quickstart

```shell
# clone the git repo
git clone https://github.com/lbeckman314/withFeathers

# enter directory
cd withFeathers

# setup dependencies
python3 -m venv virtual
source virtual/bin/activate
pip install flask

# test flask server (for development, don't use for production)
cd withfeathers
FLASK_APP=server.py flask run

# run the script
python3 withfeathers.py --print --time
```

<br />

# Uninstallation

<h2 class="code">0. Delete the directory.</h2>

```shell
rm -rfI withFeathers
```

<br />
<hr />

# Documentation

Poems will be downloaded into a file (e.g. `pg12242.txt`) in `main.py`'s working directory. The file will then be parsed into individual poem files into a directory (e.g. `emilyPoems`), from which random poems will be selected.

`python main.py --help` will print all options accepted by `main.py`.

```shell
$ python withfeathers/main.py --help
usage: main.py [-h] [-c] [-d] [-f FILENAME] [-o OUTPUTDIR] [-p] [-r] [-t]
               [-u URL] [-v]

Print some poems!

optional arguments:
  -h, --help            show this help message and exit
  -c, --clean           remove files/dirs after run (default: False)
  -d, --decorate        decorate the output (default: False)
  -f FILENAME, --filename FILENAME
                        specify filename of source file (default: pg12242.txt)
  -o OUTPUTDIR, --outputDir OUTPUTDIR
                        specify directory path of poem files (default:
                        emilyPoems)
  -p, --print           print poems to stdout (default: False)
  -r, --randomoff       toggle picking random poem (default: False)
  -t, --time            print time elapsed to stdout (default: False)
  -u URL, --url URL     specify source url
  -v, --version         show program's version number and exit
```
