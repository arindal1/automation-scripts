#include <iostream>
#include <fstream>
#include <opencv2/opencv.hpp>

void generate_ascii_art(cv::Mat& image, int width, bool color_invert) {
    const std::string ascii_chars = color_invert ? "@%#*+=-:. "[::-1] : "@%#*+=-:. "[::1];

    std::ofstream output_file("output.txt");
    if (!output_file.is_open()) {
        std::cerr << "Error opening output file." << std::endl;
        return;
    }

    for (int j = 0; j < image.rows; ++j) {
        for (int i = 0; i < image.cols; ++i) {
            cv::Mat pixel_block = image(cv::Rect(i, j, 1, 1));
            double intensity = cv::mean(pixel_block)[0];
            char ascii_char = ascii_chars[static_cast<int>((intensity * 9) / 255)];
            output_file << ascii_char;
            std::cout << ascii_char;
        }
        output_file << "\n";
        std::cout << std::endl;
    }

    output_file.close();
}

int main(int argc, char** argv) {
    if (argc < 4) {
        std::cerr << "Usage: " << argv[0] << " <input_image> <output_file> [-w <width>] [-c]" << std::endl;
        return 1;
    }

    std::string input_image_path = argv[1];
    std::string output_path = argv[2];
    int width = 75;
    bool color_invert = false;

    for (int i = 3; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "-w" && i + 1 < argc) {
            width = std::stoi(argv[i + 1]);
            ++i;
        } else if (arg == "-c") {
            color_invert = true;
        }
    }

    cv::Mat image = cv::imread(input_image_path, cv::IMREAD_GRAYSCALE);
    if (image.empty()) {
        std::cerr << "Error loading input image." << std::endl;
        return 1;
    }

    cv::resize(image, image, cv::Size(width, static_cast<int>(width * (static_cast<double>(image.rows) / image.cols))));
    
    generate_ascii_art(image, width, color_invert);

    return 0;
}
