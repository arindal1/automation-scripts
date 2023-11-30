import streamlit as st
import textwrap

def get_default_code(language):
    default_codes = {
        "java": textwrap.dedent("""
            public class Main {
                public static void main(String[] args) {
                    // Your Java code here
                }
            }
        """),
        "cpp": textwrap.dedent("""
            #include <iostream>
            
            int main() {
                // Your C++ code here
                return 0;
            }
        """),
        "cs": textwrap.dedent("""
            using System;

            class Program {
                static void Main() {
                    // Your C# code here
                }
            }
        """),
        "python": textwrap.dedent("""
            # Your Python code here
        """),
        "ruby": textwrap.dedent("""
            # Your Ruby code here
        """),
        "rust": textwrap.dedent("""
            fn main() {
                // Your Rust code here
            }
        """),
        "c": textwrap.dedent("""
            #include <stdio.h>

            int main() {
                // Your C code here
                return 0;
            }
        """),
        "html": textwrap.dedent("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Your HTML Page</title>
            </head>
            <body>
                <!-- Your HTML content here -->
            </body>
            </html>
        """),
        "css": textwrap.dedent("""
            /* Your CSS styles here */
        """),
        "js": textwrap.dedent("""
            // Your JavaScript code here
        """),
        "go": textwrap.dedent("""
            package main

            import "fmt"

            func main() {
                // Your Go code here
            }
        """),
        "php": textwrap.dedent("""
            <?php
            // Your PHP code here
            ?>
        """),
        "r": textwrap.dedent("""
            # Your R code here
        """),
        "react": textwrap.dedent("""
            import React from 'react';

            function App() {
                // Your React code here
                return (
                    <div>
                        {/* Your React components here */}
                    </div>
                );
            }

            export default App;
        """),
        "node": textwrap.dedent("""
            // Your Node.js code here
        """),
        "flutter": textwrap.dedent("""
            import 'package:flutter/material.dart';

            void main() {
              runApp(MyApp());
            }

            class MyApp extends StatelessWidget {
              @override
              Widget build(BuildContext context) {
                // Your Flutter code here
                return MaterialApp(
                  home: Scaffold(
                    appBar: AppBar(
                      title: Text('Your Flutter App'),
                    ),
                    body: Center(
                      child: Text('Hello, World!'),
                    ),
                  ),
                );
              }
            }
        """),
        "kotlin": textwrap.dedent("""
            fun main() {
                // Your Kotlin code here
            }
        """),
        "typescript": textwrap.dedent("""
            // Your TypeScript code here
        """),
        "swift": textwrap.dedent("""
            import Foundation

            // Your Swift code here
        """),
        "dart": textwrap.dedent("""
            // Your Dart code here
        """),
        "scala": textwrap.dedent("""
            object Main extends App {
                // Your Scala code here
            }
        """),
        "racket": textwrap.dedent("""
            ; Your Racket code here
        """),
        "erlang": textwrap.dedent("""
            % Your Erlang code here
        """),
        "elixir": textwrap.dedent("""
            # Your Elixir code here
        """),
        "sql": textwrap.dedent("""
            -- Your SQL code here
        """),
        "mongodb": textwrap.dedent("""
            // Your MongoDB code here
        """),
    }

    return default_codes.get(language.lower(), "Language not supported.")

def main():
    st.title("Code Template Generator")

    # Get user input for the programming language
    language = st.text_input("Enter the programming language:")

    # Get and display the default code template
    default_code = get_default_code(language)
    st.markdown("### Default Code Template:")
    st.code(default_code, language="java")  # Adjust the language for syntax highlighting

if __name__ == "__main__":
    main()
