import os

import gsd.hoomd


def extract(
    path_input: str, path_output: str, output_file: str, num_frame: int = -1
) -> None:
    """Extraction one frame from gsd file trajectory

    Args:
        path_input (str): name of input path
        path_output (str): name of output path
        output_file (str): name of output gsd file
        num_frame (int, optional): Number of frame. Defaults to -1.

    Raises:
        ValueError: Length of trajectory > num_frame
        ValueError: Path {path_input} does not exist!
        ValueError: Path {path_output} does not exist!
        ValueError: Invalid format of input file!
        ValueError: Names of input and output files are the same!
    """
    traj = gsd.hoomd.open(path_input)

    if len(traj) < num_frame:
        raise ValueError("Length of trajectory > num_frame")
    if not os.path.exists(path_input):
        raise ValueError(f"Path {path_input} does not exist!")
    if not os.path.exists(path_output):
        raise ValueError(f"Path {path_output} does not exist!")
    if path_input.split(".")[-1] != "gsd":
        raise ValueError("Invalid format of input file!")

    output = os.path.join(path_output, output_file)
    if output == path_input:
        raise ValueError("Names of input and output files are the same!")

    with gsd.hoomd.open(name=output, mode="w") as f:
        f.append(traj[num_frame])


if __name__ == "__main__":
    extract(
        "/home/imc24/hoomd_run/data/cycle_test/N=100_g=0_n=0/output.gsd",
        ".",
        "test.gsd",
    )
