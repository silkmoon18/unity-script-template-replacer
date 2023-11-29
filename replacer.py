import os
import platform
import shutil


SOURCE_TEMPLATES = "source-templates"

PATHS = {
    "Windows": {
        "EDITOR": "E:/Unity",
        "TEMPLATES": "Editor\Data\Resources\ScriptTemplates",
    },
    "Darwin": {
        "EDITOR": "/Applications/Unity/Hub/Editor",
        "TEMPLATES": "Unity.app/Contents/Resources/ScriptTemplates",
    },
}


def replace(source_folder: str, target_folder: str):
    print()
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}\n")
        stop()

    # Check if the target folder exists
    if not os.path.exists(target_folder):
        print(f"Target folder does not exist: {target_folder}\n")
        stop()

    # Loop through files in the source folder
    print("--------------------")
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        target_file = os.path.join(target_folder, filename)

        # Check if the corresponding file exists in the target folder
        if os.path.exists(target_file):
            # Replace the file in the target folder
            shutil.copy(source_file, target_file)
            print(f"Replaced: {filename}")
        else:
            print(f"File not found in target folder: {filename}")
    print("--------------------")
    print("\nReplacement completed.\n")


def stop():
    input()
    exit()


if __name__ == "__main__":
    # Get the directory of the current script
    script_directory = os.path.dirname(__file__)

    # Specify the relative path to the source folder
    source_folder = os.path.join(script_directory, SOURCE_TEMPLATES)

    # Specify the paths by platform
    system_platform = platform.system()
    path = PATHS.get(system_platform)
    if not path:
        print(f"\nUnsupported operating system: {system_platform}\n")
        stop()

    editor_path = path["EDITOR"]
    templates_path = path["TEMPLATES"]

    # Read Editor version
    print("\nEnter the version of the Unity Editor: ")
    editor_version = input().strip()
    target_folder = os.path.join(editor_path, f"{editor_version}/{templates_path}")

    # Replace
    replace(source_folder, target_folder)
    stop()
