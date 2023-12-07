#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

void clean_empty_folders(const fs::path& path, bool removeRoot, bool verbose) {
    if (!fs::is_directory(path)) {
        if (verbose) {
            std::cout << path << " is not a directory. Abort." << std::endl;
        }
        return;
    }

    for (const auto& entry : fs::directory_iterator(path)) {
        if (fs::is_directory(entry)) {
            clean_empty_folders(entry.path(), true, verbose);
        }
    }

    // After removing subdirectories, check if the folder is empty
    if (fs::is_empty(path) && removeRoot) {
        fs::remove(path);
        if (verbose) {
            std::cout << path << " removed" << std::endl;
        }
    }
}

int main() {
    std::string selectedPath;
    std::cout << "Write the desired path: ";
    std::getline(std::cin, selectedPath);

    bool removeRoot;
    while (true) {
        char removeRootInput;
        std::cout << "Also remove the root folder (Y/N)? ";
        std::cin >> removeRootInput;

        if (removeRootInput == 'y' || removeRootInput == 'Y') {
            removeRoot = true;
            break;
        } else if (removeRootInput == 'n' || removeRootInput == 'N') {
            removeRoot = false;
            break;
        }

        std::cout << "Invalid input '" << removeRootInput << "', please try again." << std::endl;
    }

    // Execute the clean_empty_folders function
    clean_empty_folders(selectedPath, removeRoot, true);
    std::cout << "Done!" << std::endl;

    return 0;
}
