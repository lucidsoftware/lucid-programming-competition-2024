#!/usr/bin/env python3

import os
import shutil
import pathlib
import zipfile


SCRIPT_PATH = pathlib.Path(__file__).resolve().parent


def iter_problem_folders():
    for problem in (SCRIPT_PATH / "problems").iterdir():
        if problem.is_dir():
            yield problem


def create_test_case_zip(problem: pathlib.Path):
        with zipfile.ZipFile(SCRIPT_PATH / "zips" / (str(problem.name) + ".zip"), mode='w', compression=zipfile.ZIP_STORED) as zip:

            input_files = sorted((problem / "tests").glob("*.in"), key=lambda k: int(str(k.name).replace(".in", "")))
            output_files = sorted((problem / "tests").glob("*.out"), key=lambda k: int(str(k.name).replace(".out", "")))
            assert len(input_files) == len(output_files)

            for num, infile in enumerate(input_files):
                print(infile)
                zip.write(infile, arcname=pathlib.Path("input/input{:02d}.txt".format(num)))
            
            for num, outfile in enumerate(output_files):
                print(outfile)
                zip.write(outfile, arcname=pathlib.Path("output/output{:02d}.txt".format(num)))


def main():
    shutil.rmtree(SCRIPT_PATH / "zips", ignore_errors=True)
    os.mkdir(SCRIPT_PATH / "zips")
    for problem in iter_problem_folders():
        create_test_case_zip(problem)      


if __name__ == "__main__":
    main()