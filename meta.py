from pathlib import Path


def main():
    """Main entry point of the script."""
    
    directories: dict[Path, str] = {}
    
    for file in Path.cwd().iterdir():
        if not file.is_dir():
            continue
        
        directory = file
        
        if (readme := directory / "README.md").exists():
            with open(readme, 'r') as f:
                content = f.read()
            directories[directory] = content
            
    for directory, content in directories.items():
        print(f"-> {directory.stem}: {content}")
        print("----")

if __name__ == "__main__":
    main()
