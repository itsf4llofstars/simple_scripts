"""main_functions.py"""
import os
import shutil
import sys


def check_directory(path: str) -> bool:
    """Check if path exists as a directory

    Expands and joins path to /home/$USER/ and
    checks if the expanded and joined path exists,

    Returns:
        True (bool): If directory exists
        False (bool): if directory does not exist
    """
    return os.path.isdir(os.path.expanduser(os.path.join("~", path)))


def remove_tree(path: str) -> None:
    """Remove the directory at path"""
    shutil.rmtree(os.path.expanduser(os.path.join("~", path)))


def create_directory(path: str) -> None:
    """Create a directory at path"""
    if not os.path.isdir(os.path.expanduser(os.path.join("~", path))):
        os.makedirs(os.path.expanduser(os.path.join("~", path)))


def copy_a_file(source: str, destination: str, filename: str) -> None:
    """Copy a single file from source to destination"""
    shutil.copy(
        os.path.expanduser(os.path.join("~", "source", filename)),
        os.path.expanduser(os.path.join("~", "destination", filename[1:])),
    )


def copy_files(dest_dir: str, files) -> None:
    """Copy the list of files form source to dest"""
    for name in files:
        if os.path.isfile(os.path.expanduser(os.path.join("~", name))):
            shutil.copy(
                os.path.expanduser(os.path.join("~", name)),
                os.path.expanduser(
                    os.path.join("~", dest_dir, name[1:] + ".bak")
                ),
            )


def make_tar(base, filename, ext, root):
    """Create an archive in base, named filename witht he extension
    ext from the root path
    """
    shutil.make_archive(
        os.path.expanduser(os.path.join("~", base, filename)),
        ext,
        os.path.expanduser(os.path.join("~", root)),
    )


def main(args):
    directory = "temp_dir"
    base_dir = "archives"
    tar_name = "py_dotfiles"
    tar_ext = "tar"

    file_names = [
        ".vimrc",
        ".bashrc",
        ".bash_aliases",
        ".nanorc",
        ".gitconfig",
        ".tmux.conf",
    ]

    if check_directory(directory):
        remove_tree(directory)

    create_directory(directory)

    if check_directory(directory):
        copy_files("temp_dir", file_names)
        make_tar(base_dir, tar_name, tar_ext, directory)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
