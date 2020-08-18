""" remove duplicate images from a given folder """
import collections
import os
import shutil
import sys
import re

from pathlib import Path

TEMP_FOLDER = Path.cwd() / "temp"
DUP_IMG_REGEX = re.compile(r"^.* \([0-9]*\)")
IS_KEEPING = False


def handle_args():
    if len(sys.argv) < 2:
        print("USAGE: main.py [-k] <absolute/path/to/file>")
        exit(1)
    elif "-k" in sys.argv:
        global IS_KEEPING
        IS_KEEPING = True
    elif len(sys.argv) > 3:
        print("USAGE: main.py [-k] <absolute/path/to/file>")
        exit(1)
    #end if/elif

    library = Path(sys.argv[-1])
    if not os.path.exists(library):
        print("ERROR: %s is not a valid path!" % sys.argv[-1])
        exit(1)
    #end if

    return library
#end handle_args


def remove_duplicates(library, dups):
    print("\nRemoving duplicates...")
    for d in dups:
        d_original = re.sub(r" \([0-9]*\)", "", d)
        file = dups.get(d)
        if d_original in library.keys():
            # move file to TEMP_FOLDER
            print("\tOriginal found for", d)
            file.replace(TEMP_FOLDER / file.name)
        else:
            # rename file
            print("\tNo original found for", d)
            print("\tNew filename is:", d_original)
            print("\tNew filepath is:", file.root / file.parent / d_original, "\n")
            file.rename(file.with_name(d_original))

            # update library to contain reference to the renamed file
            new_file = Path(file.root / file.parent / d_original)
            library.update({new_file.name: new_file})
        # end if/else
    # end for
    print("Done.")
#end remove_duplicates


def get_lib_dups(library_dir):
    library = {}
    dups = {}
    files = library_dir.glob("**/*")
    for _ in files:
        library.update({_.name: _})
        if re.match(DUP_IMG_REGEX, _.name):
            dups.update({_.name: _})
        # end if
    # end for
    print("Library size:", len(library))
    print("Duplicates found:", len(dups))

    return library, dups
#end get_lib_dups


def main():
    library_dir = handle_args()
    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)

    print("File data for %s:" % library_dir.name)
    print(collections.Counter(p.suffix for p in library_dir.iterdir()))
    print()
    lib, dups = get_lib_dups(library_dir)
    remove_duplicates(lib, dups)
    if not IS_KEEPING:
        shutil.rmtree(TEMP_FOLDER)
#end main


if __name__ == '__main__':
    main()
