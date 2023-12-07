#!/bin/bash

get_subdirectories() {
    # Return a list containing the absolute path of the direct subdirectories in the provided path.
    # Doesn't walk the directory tree.
    # $1: the path to check
    find "$1" -mindepth 1 -maxdepth 1 -type d
}

clean_empty_folders() {
    # Recursively remove empty folders and subdirectories.
    # $1: the initial (root) path
    # $2: if true, also removes the root path if all subdirectories are empty
    # $3: if true, prints progress

    local path=$1
    local remove_root=$2
    local verbose=$3

    if [ ! -d "$path" ]; then
        if [ "$verbose" = true ]; then
            echo "$path is not a directory. Abort."
        fi
        return 1
    fi

    subdirectories=($(get_subdirectories "$path"))

    for subdirectory in "${subdirectories[@]}"; do
        clean_empty_folders "$subdirectory" true "$verbose"
    done

    # After removing subdirectories, check if the folder is empty
    if [ -z "$(ls -A "$path")" ] && [ "$remove_root" = true ]; then
        rm -r "$path"
        if [ "$verbose" = true ]; then
            echo "$path removed"
        fi
        return 0
    fi

    return 1
}

# Main script

read -p "Write the desired path: " selected_path

remove_root=""
while [ -z "$remove_root" ]; do
    read -p "Also remove the root folder (Y/N)? " remove_root_input
    case "$remove_root_input" in
    [yY])
        remove_root=true
        break
        ;;
    [nN])
        remove_root=false
        break
        ;;
    *)
        echo "Invalid input '$remove_root_input', please try again."
        ;;
    esac
done

# Execute the clean_empty_folders function
clean_empty_folders "$selected_path" "$remove_root" true
echo "Done!"
