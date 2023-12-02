use image::{DynamicImage, GenericImageView};
use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn generate_ascii_art(image: &DynamicImage, width: u32, color_invert: bool) -> String {
    let ascii_chars = if color_invert {
        "@%#*+=-:. ".chars().rev().collect::<String>()
    } else {
        "@%#*+=-:. ".to_string()
    };

    let mut ascii_art = String::new();

    for y in 0..image.height() {
        for x in 0..image.width() {
            let pixel = image.get_pixel(x, y);
            let intensity = (pixel[0] as f64 * 0.299
                + pixel[1] as f64 * 0.587
                + pixel[2] as f64 * 0.114)
                / 255.0;

            let ascii_char = ascii_chars
                .chars()
                .nth((intensity * 9.0) as usize / 255)
                .unwrap();
            ascii_art.push(ascii_char);
            print!("{}", ascii_char);
        }
        ascii_art.push('\n');
        println!();
    }

    ascii_art
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 4 {
        eprintln!("Usage: {} <input_image> <output_file> [-w <width>] [-c]", args[0]);
        std::process::exit(1);
    }

    let input_image_path = &args[1];
    let output_path = &args[2];
    let mut width: u32 = 75;
    let mut color_invert = false;

    for i in 3..args.len() {
        match args[i].as_str() {
            "-w" if i + 1 < args.len() => {
                width = args[i + 1].parse().unwrap_or(75);
            }
            "-c" => color_invert = true,
            _ => {}
        }
    }

    let image = image::open(input_image_path).expect("Error loading input image.");
    let resized_image = image.resize_exact(width, (width as f64 * (image.height() as f64 / image.width() as f64)) as u32, image::imageops::FilterType::Triangle);
    
    let ascii_art = generate_ascii_art(&resized_image, width, color_invert);

    File::create(output_path)
        .and_then(|mut file| file.write_all(ascii_art.as_bytes()))
        .expect("Error writing to output file.");
}
