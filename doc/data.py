from pathlib import Path

from constraints import getBoardsInfo, ProgItem


boardDataDir = Path(__file__).resolve().parent / "Data/Boards"


def generateBoardPages():

    boardsInfo = getBoardsInfo()
    sortedBoardNames = sorted(boardsInfo, key=str.casefold)

    for name in sortedBoardNames:
        content = boardsInfo[name]
        with (boardDataDir / f"{name}.inc").open("w") as wfptr:
            wfptr.write("\n\n")

            wfptr.write(f"`hdl/constraints: board/{name} <https://github.com/hdl/constraints/tree/main/board/{name}>`__\n\n")

            if content.Description is not None:
                wfptr.write(f"*{content.Description}*\n\n")

            if content.PartNumber is not None:
                wfptr.write(f"* **Part Number**: {content.PartNumber}\n\n")

            if content.Device is not None:
                wfptr.write(f"* **Device**: {content.Device}\n\n")

            if content.Package is not None:
                wfptr.write(f"* **Package**: {content.Package}\n\n")

            if content.Documentation is not None:
                wfptr.write("* **Documentation**:\n\n")
                if isinstance(content.Documentation, str):
                    wfptr.write(f"  * {content.Documentation}\n")
                else:
                    if isinstance(content.Documentation, list):
                        for item in content.Documentation:
                            wfptr.write(f"  * {item}\n\n")
                    else:
                        for key, val in content.Documentation.items():
                            wfptr.write(f"  * `{key} <{val}>`__\n\n")

            if content.Prog is not None:
                wfptr.write("* **Programming**:\n\n")
                if isinstance(content.Prog, ProgItem):
                    prog = content.Prog
                    if prog.ID is not None:
                        wfptr.write(f"  * **ID**: {prog.ID}\n\n")
                    if prog.Description is not None:
                        wfptr.write(f"  * **Description**: {prog.Description}\n\n")
                    if prog.Tools is not None:
                        wfptr.write(f"  * **Tools**:\n\n")
                        items = [prog.Tools] if isinstance(prog.Tools, str) else prog.Tools
                        for item in items:
                            wfptr.write(f"    * {item}\n\n")
                else:
                    items = [content.Prog] if isinstance(content.Prog, str) else content.Prog
                    for item in items:
                        wfptr.write(f"  * {item}\n\n")

            if content.Content is not None:
                wfptr.write(f"* {content.Content}\n")

            wfptr.write("\n")

    with (boardDataDir / "boards.inc").open("w") as wfptr:
        for name in sortedBoardNames:
            content = boardsInfo[name]
            wfptr.write(f"{content.Label}\n{'='*len(content.Label)}\n\n")
            wfptr.write(f".. include:: {name}.inc\n\n")
