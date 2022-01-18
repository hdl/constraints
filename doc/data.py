from sys import path as sys_path
from os.path import abspath
from pathlib import Path

from constraints import getBoardsInfo, getConstraintFiles, ProgItem

# From submoduled openFPGALoader
from boards import ReadDataFromYAML

ROOT = Path(__file__).resolve().parent
boardDataDir = ROOT / "Data/Boards"


def generateBoardPages():

    boardsInfo = getBoardsInfo()
    sortedBoardNames = sorted(boardsInfo, key=str.casefold)
    boardConstraints = getConstraintFiles(sortedBoardNames)

    OFLData = ReadDataFromYAML()

    for name in sortedBoardNames:
        content = boardsInfo[name]
        with (boardDataDir / f"{name}.inc").open("w", encoding="utf-8") as wfptr:
            wfptr.write(f"\n\n.. _Boards:{name}:\n\n")
            wfptr.write(f"{content.Label}\n{'='*len(content.Label)}\n\n")

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

            for OFLBoard in OFLData:
                OFLConstraints = OFLBoard.Constraints
                if OFLConstraints is not None:
                    if isinstance(OFLConstraints, str):
                        OFLConstraints = [OFLConstraints]
                    if name in OFLConstraints:
                        prefix = ''
                        if content.Prog is None:
                            wfptr.write("* **Programming**:\n\n")
                        elif isinstance(content.Prog, ProgItem) and prog.Tools is not None:
                            prefix = '  '
                        wfptr.write(f"{prefix}  * openFPGALoader [:ref:`{OFLBoard.ID} <openfpgaloader:compatibility:boards>`]\n\n")
                        wfptr.write(f"{prefix}    * Memory: {OFLBoard.Memory}\n\n")
                        wfptr.write(f"{prefix}    * Flash: {OFLBoard.Flash}\n\n")
                        break

            constraints = boardConstraints[name]
            if constraints is None:
                wfptr.write(f"* **Constraints**: :ghsrc:`board/{name} ✗ <board/{name}>`\n\n")
            else:
                wfptr.write(f"* **Constraints**: :ghsrc:`board/{name}`\n\n")
                if len(constraints.LPF) != 0:
                    wfptr.write(f"  * **LPF**:\n\n")
                    for item in constraints.LPF:
                        wfptr.write(f"    * :ghsrc:`{item.replace('.',' » ')} <board/{name}/{item}.lpf>`\n\n")
                if len(constraints.PCF) != 0:
                    wfptr.write(f"  * **PCF**:\n\n")
                    for item in constraints.PCF:
                        wfptr.write(f"    * :ghsrc:`{item.replace('.',' » ')} <board/{name}/{item}.pcf>`\n\n")
                if len(constraints.SDC) != 0:
                    wfptr.write(f"  * **SDC**:\n\n")
                    for item in constraints.SDC:
                        wfptr.write(f"    * :ghsrc:`{item.replace('.',' » ')} <board/{name}/{item}.sdc>`\n\n")
                if len(constraints.UCF) != 0:
                    wfptr.write(f"  * **UCF**:\n\n")
                    for item in constraints.UCF:
                        wfptr.write(f"    * :ghsrc:`{item.replace('.',' » ')} <board/{name}/{item}.ucf>`\n\n")
                if len(constraints.XDC) != 0:
                    wfptr.write(f"  * **XDC**:\n\n")
                    for item in constraints.XDC:
                        wfptr.write(f"    * :ghsrc:`{item.replace('.',' » ')} <board/{name}/{item}.xdc>`\n\n")

            if content.Content is not None:
                wfptr.write(f"* {content.Content}\n")

            wfptr.write("\n")

    with (boardDataDir / "boards.inc").open("w", encoding="utf-8") as wfptr:
        for name in sortedBoardNames:
            wfptr.write(f".. include:: {name}.inc\n\n")
