from sys import argv as sys_argv
from pathlib import Path


rootDir = Path(__file__).resolve().parent
boardInfoDir = rootDir / "board"


def generatePerBoardMarkdownFileWithFrontmatter(contentDir):
    boardFileDir = contentDir / "boards"
    boardFileDir.mkdir(exist_ok=True)

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


if __name__ == "__main__":
    generatePerBoardMarkdownFileWithFrontmatter(Path(sys_argv[1]))
