#include <iostream>
#include <SDL2/SDL.h>
#include <thread>
#include <chrono>

// ======== Controls ========
const SDL_Keycode start_or_pause_key = SDLK_F1;
const SDL_Keycode exit_key = SDLK_ESCAPE;
const int default_delay = 1000;  // milliseconds

// ==== Global variables ====
bool pause = true;
bool running = true;
int delay = default_delay;

// Function for auto-clicking
void click_periodically() {
    while (running) {
        if (!pause) {
            // Simulate mouse click here
            std::cout << "Clicking..." << std::endl;
            std::this_thread::sleep_for(std::chrono::milliseconds(delay));
        }
    }
}

// SDL event handler
void handle_events(SDL_Event& event) {
    if (event.type == SDL_KEYDOWN) {
        if (event.key.keysym.sym == start_or_pause_key) {
            pause = !pause;
            std::cout << (pause ? "< Pause >" : "< Start >") << std::endl;
            if (!pause) {
                std::thread(click_periodically).detach();
            }
        } else if (event.key.keysym.sym == exit_key) {
            running = false;
            std::cout << "< Exit >" << std::endl;
        }
    }
}

int main() {
    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL initialization failed: " << SDL_GetError() << std::endl;
        return 1;
    }

    // Create window
    SDL_Window* window = SDL_CreateWindow("Auto Clicker", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, 0);
    if (!window) {
        std::cerr << "Window creation failed: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    // Create renderer
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        std::cerr << "Renderer creation failed: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    SDL_Event event;

    while (running) {
        // Handle events
        while (SDL_PollEvent(&event)) {
            handle_events(event);
        }

        // Simulate main loop
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }

    // Cleanup
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
