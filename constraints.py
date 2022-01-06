#!/usr/bin/env python3

from sys import argv as sys_argv
from pathlib import Path
from typing import Dict, List, Union
from dataclasses import dataclass
from yaml import load as yaml_load, Loader as yaml_loader, dump as yaml_dump
from re import findall as re_findall, M as re_M


rootDir = Path(__file__).resolve().parent
boardInfoDir = rootDir / "board"


def generatePerBoardMarkdownFileWithFrontmatter(contentDir):
    boardFileDir = contentDir / "boards"
    boardFileDir.mkdir(exist_ok=True)

    # FIXME
    # Currently, files use key 'Documentation', which is polymorphic, but Hugo expects a list of strings.
    # When this function is converted to use dataclasses, that should be fixed (transformed).

    for item in boardInfoDir.glob("**/info.yml"):

        name = item.parent.name
        prefix = ""
        suffix = ""
        print("-", name)

        with (boardFileDir / f"{name}.md").open("w") as wfptr:
            wfptr.write("---\n")
            wfptr.write(item.read_text())
            wfptr.write(f"ref: https://github.com/hdl/constraints/tree/main/board/{prefix}{name}{suffix}\n")
            wfptr.write("---\n")

    for item in boardInfoDir.glob("**/info.md"):

        name = item.parent.name
        prefix = ""
        suffix = ""
        print("-", name)

        with item.open("r") as rfptr:
            with (boardFileDir / f"{name}.md").open("w") as wfptr:
                for line in [
                    "---",
                    f"ref: https://github.com/hdl/constraints/tree/main/board/{prefix}{name}{suffix}",
                ] + rfptr.read().splitlines()[1:]:
                    wfptr.writelines("{}\n".format(line))


@dataclass
class ProgItem:
    ID: str = None
    Description: str = None
    Tools: Union[str, List[str]] = None


@dataclass
class BoardInfo:
    Label: str
    Description: str = None
    PartNumber: str = None
    Device: str = None
    Package: str = None
    Documentation: Union[str, List[str]] = None
    Prog: Union[ProgItem, str, List[str]] = None
    Content: str = None


@dataclass
class LogicResources:
    LUT: int = None
    FF: int = None
    BRAM: int = None
    DSP: int = None
    IO: int = None


@dataclass
class DeviceInfo:
    Label: str
    Device: str
    Packages: List[str] = None
    Documentation: Union[str, List[Union[str, Dict[str, str]]]] = None
    Resources: LogicResources = None


def getBoardsInfo(verbose : bool = True):
    boards = {}

    for item in boardInfoDir.glob("**/info.yml"):
        if verbose:
            print(" >", item.parent.name)
        with item.open() as fptr:
            boards[item.parent.name] = BoardInfo(**yaml_load(fptr, yaml_loader))

    for item in boardInfoDir.glob("**/info.md"):
        if verbose:
            print(" >", item.parent.name)
        with item.open() as fptr:
            # TODO:
            # Currently, we are extracting the frontmatter with a regular expression, and ignoring the markdown body.
            # We should keep the markdown content as well.
            # - https://python-markdown.github.io/extensions/
            # - https://pypi.org/project/python-frontmatter/
            frontmatter = re_findall(r"^---$\r?\n((?:.*?\r?\n)*)^---$", fptr.read(), re_M)[0]
            boards[item.parent.name] = BoardInfo(**yaml_load(frontmatter, yaml_loader))

    return boards


if __name__ == "__main__":
    generatePerBoardMarkdownFileWithFrontmatter(Path(sys_argv[1]))
