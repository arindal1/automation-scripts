import os
import streamlit as st

def generate_boilerplate(project_name, language, project_type):
    base_path = os.path.join(os.getcwd(), project_name)

    # Create project directory
    os.makedirs(base_path, exist_ok=True)
    st.success(f"Created project directory: {project_name}")

    # Determine project structure based on project type
    if project_type.lower() == "web":
        web_project_structure(base_path, language)
    elif project_type.lower() == "desktop":
        desktop_project_structure(base_path, language)
    elif project_type.lower() == "console":
        console_project_structure(base_path, language)
    else:
        st.warning("Invalid project type. Supported types: web, desktop, console")

def web_project_structure(base_path, language):
    # Create web project structure
    web_path = os.path.join(base_path, "web")
    os.makedirs(web_path)
    st.success("Created web project structure.")

    # Add placeholder files for web project
    index_html = os.path.join(web_path, "index.html")
    with open(index_html, "w") as file:
        file.write("<!DOCTYPE html>\n<html>\n<head>\n\t<title>Welcome to My Web Project</title>\n</head>\n<body>\n\t<h1>Hello, World!</h1>\n</body>\n</html>")
    st.success("Added placeholder files for a web project.")

def desktop_project_structure(base_path, language):
    # Create desktop project structure
    desktop_path = os.path.join(base_path, "desktop")
    os.makedirs(desktop_path)
    st.success("Created desktop project structure.")

    # Add placeholder files for desktop project
    main_file = os.path.join(desktop_path, f"main.{language}")
    with open(main_file, "w") as file:
        file.write(f"// Welcome to My {language.capitalize()} Desktop Project\n\nint main() {{\n\t// Your code here\n\treturn 0;\n}}")
    st.success(f"Added placeholder files for a {language} desktop project.")

def console_project_structure(base_path, language):
    # Create console project structure
    console_path = os.path.join(base_path, "console")
    os.makedirs(console_path)
    st.success("Created console project structure.")

    # Add placeholder files for console project
    main_file = os.path.join(console_path, f"main.{language}")
    with open(main_file, "w") as file:
        file.write(f"// Welcome to My {language.capitalize()} Console Project\n\n#include <iostream>\n\nint main() {{\n\tstd::cout << \"Hello, World!\" << std::endl;\n\treturn 0;\n}}")
    st.success(f"Added placeholder files for a {language} console project.")

def main():
    st.title("Boilerplate Code Generator")

    # Get user input
    project_name = st.text_input("Enter project name:")
    language = st.text_input("Enter programming language (e.g., python, cpp, java):")
    project_type = st.selectbox("Select project type:", ["web", "desktop", "console"])

    # Generate boilerplate code
    if st.button("Generate Boilerplate Code"):
        generate_boilerplate(project_name, language, project_type)

if __name__ == "__main__":
    main()
