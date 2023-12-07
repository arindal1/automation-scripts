import os


def get_subdirectories(path):
    """
    Return a list containing the absolute path of the direct subdirectories in the provided path.
    Doesn't walk the directory tree.
    :param path: the path to check
    :return: a list with the direct subdirectory names
    """
    return [os.path.join(path, subdirectory) for subdirectory in os.listdir(path)
            if os.path.isdir(os.path.join(path, subdirectory))]


def clean_empty_folders(path, remove_root=True, verbose=False):
    """
    Recursively remove empty folders and subdirectories.
    :param path: the initial (root) path
    :param remove_root: if True (default), also removes the root path if all subdirectories are empty
    :param verbose: if True, prints progress
    :return: True if 'path' was removed, false otherwise. Note that, if remove_root=False,
             this function will always return False
    """
    if not os.path.isdir(path):
        if verbose:
            print(path, "is not a directory. Abort.")
        return False

    subdirectories = get_subdirectories(path)
    for subdirectory in subdirectories:
        clean_empty_folders(subdirectory, remove_root=True, verbose=verbose)

    # After removing subdirectories, check if the folder is empty
    if not os.listdir(path) and remove_root:
        os.rmdir(path)
        if verbose:
            print(path, "removed")
        return True

    return False


if __name__ == '__main__':
    selected_path = input("Write the desired path: ")

    # Validate user input for removing the root folder
    while True:
        remove_root_input = input("Also remove the root folder (Y/N)? ").lower()
        if remove_root_input == "y":
            remove_root = True
            break
        elif remove_root_input == "n":
            remove_root = False
            break
        print(f"Invalid input '{remove_root_input}', please try again.")

    # Execute the clean_empty_folders function
    clean_empty_folders(selected_path, remove_root, verbose=True)
    print("Done!")
