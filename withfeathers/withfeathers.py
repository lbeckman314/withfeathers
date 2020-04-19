from subprocess import run
from subprocess import PIPE
from subprocess import Popen
from pathlib import Path
from random import shuffle
import argparse
import time
import os
import urllib.request


def getArgs():
    parser = argparse.ArgumentParser(description='Print some poems!')

    parser.add_argument('-c', '--clean', dest='clean',
                        action='store_true', default=False,
                        help='remove files/dirs after run (default: False)')

    parser.add_argument('-d', '--decorate', dest='decorate',
                        action='store_true', default=False,
                        help='decorate the output (default: False)')

    parser.add_argument('-f', '--filename', dest='filename', action='store',
                        help='specify filename of source file (default: emilyPoems.txt)')

    parser.add_argument('-o', '--outputDir', dest='outputDir', action='store',
                        help='specify directory path of poem files (default: emilyPoems)')

    parser.add_argument('-p', '--print', dest='stdout', action='store_true',
                        default=False,
                        help='print poems to stdout (default: False)')

    parser.add_argument('-r', '--randomoff', dest='randomoff',
                        action='store_true', default=False,
                        help='toggle picking random poem (default: False)')

    parser.add_argument('-t', '--time', dest='time', action='store_true',
                        default=False,
                        help='print time elapsed to stdout (default: False)')

    parser.add_argument('-u', '--url', dest='url', action='store',
                        help='specify source url')

    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 0.1.0')

    # https://stackoverflow.com/questions/12818146/python-argparse-ignore-unrecognised-arguments
    args, unknown = parser.parse_known_args()
    return args


def download(url):
    with urllib.request.urlopen(url) as response, open("emilyPoems.txt", 'wb') as outFile:
        data = response.read()
        outFile.write(data)


def parse(filename, outputDir):
    f = open(filename, 'r')

    lines = f.readlines()
    poemNum = 0
    for i in range(0, len(lines)-1):
        w = open('%s/%s.txt' % (outputDir, poemNum), 'w')

        counter = 0
        nl = lines[i+counter]
        emptyLine = 0
        strings = ("I.\n", "V.\n", "X.\n", "L.\n")
        willWrite = []

        # https://stackoverflow.com/questions/8583615/how-to-check-if-a-line-has-one-of-the-strings-in-a-list
        if any(s in lines[i] for s in strings):

            # write the roman numeral
            willWrite += lines[i]

            # while there are not two blank lines
            while emptyLine < 2:
                counter += 1
                nl = lines[i+counter]
                willWrite += nl

                if nl in ('\n', '\r\n'):
                    emptyLine += 1

                else:
                    emptyLine = 0

            # https://stackoverflow.com/questions/1877999/delete-final-line-in-file-with-python
            # remove last two blank lines
            willWrite = willWrite[:-2]

            # write to the files
            for line in willWrite:
                w.write(line)

            poemNum += 1

    return poemNum


def clean(filename, dirpath):
    run('rm -fI "%s"*' % filename, shell=False)
    run('rm -rfI "%s"*' % dirpath, shell=False)


def display(path, isRandom):
    group = []
    output = ""

    # get list of files in poem directory
    poemFiles = Popen(('ls', path), shell=False, stdout=PIPE, close_fds=True)
    dirList = poemFiles.communicate()[0].decode('utf-8')

    # add all poems in directory to list
    for newFile in dirList.splitlines():
        group.append(newFile)

    if (isRandom):
        group = randomize(group)

    pathFull = path + "/" + group[0]
    poemFile = open(pathFull, 'r')
    for line in poemFile:
        output += line

    return output


def randomize(group):
    shuffle(group)
    return group


def main():
    start = time.time()

    PATH = os.path.dirname(os.path.abspath(__file__))

    args = getArgs()

    if (args.url):
        myUrl = args.url
    else:
        myUrl = "http://www.gutenberg.org/cache/epub/12242/pg12242.txt"

    if (args.filename):
        myFile = args.filename
    else:
        myFile = PATH + "/" + "emilyPoems.txt"

    if (args.outputDir):
        poemDir = args.outputDir
    else:
        poemDir = "emilyPoems"

    if (args.randomoff):
        isRandom = False
    else:
        isRandom = True

    # if poem text file is not found, retrieve it from web source
    myObj = Path("%s" % myFile)
    if not myObj.is_file():
        download(myUrl)

    # if the poem directory does not exist, create it with parsed poems.
    myObj = Path("%s" % poemDir)
    if not myObj.is_dir():
        os.mkdir(poemDir)

    if len(os.listdir(poemDir)) == 0:
        parse(myFile, poemDir)

    # remove all poem files
    if (args.clean):
        clean(myFile, poemDir)

    # output the poems
    poem = display(poemDir, isRandom)

    # calculate and output program run time in milliseconds
    finish = time.time()
    difference = 1000*(finish - start)
    elapsed = "time elapsed: "
    elapsed += str(difference)
    elapsed += " ms"

    decorator = "~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~"

    output = ""
    output += poem

    if (args.decorate):
        output += "\n"
        output += decorator
        output += "\n"

    if (args.time):
        output += "\n"
        output += elapsed
        output += "\n"

    if (args.stdout):
        print(output)

    return output


main()

