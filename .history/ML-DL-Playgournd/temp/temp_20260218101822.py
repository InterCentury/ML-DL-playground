import os

# Root directory name
ROOT_DIR = "AI-Mate-Project"

# Folder structure definition
structure = {
    "00_Admin": [
        "Dev-Log"
    ],
    "01_Software": [
        "Ollama",
        "llama.cpp",
        "Blender",
        "UnrealEngine",
        "Tools"
    ],
    "02_AI_Core": {
        "Models": [
            "Mistral-7B-Q4",
            "Experimental"
        ],
        "Ollama-Configs": [
            "Modelfiles",
            "Emotion-Prompts"
        ],
        "Emotion-System": [
            "State-Logic",
            "Drift-Logic",
            "Memory-Manager"
        ],
        "API-Bridge": [
            "Unreal-HTTP-Test",
            "Local-Test-Scripts"
        ],
        "TTS-System": [
            "Voice-Profiles",
            "Emotion-Voice-Mapping",
            "Audio-Tests"
        ]
    },
    "03_Unreal_Project": {
        "Content": {
            "Blueprints": [
                "EmotionController",
                "AI_Interface",
                "AnimationController",
                "UI"
            ],
            "Characters": [
                "Meshes",
                "Materials",
                "Animations"
            ],
            "AI": [
                "PromptTemplates",
                "ResponseHandlers"
            ],
            "Levels": []
        },
        "Config": [],
        "Saved": []
    },
    "04_Blender": [
        "CharacterModels",
        "Rigs",
        "Facial-Setup",
        "Animation-Exports",
        "Export-Presets"
    ],
    "05_Testing": {
        "Performance-Tests": [
            "VRAM-Logs",
            "FPS-Tests"
        ],
        "Emotion-Behavior-Tests": [],
        "TTS-Tests": [],
        "Latency-Measurements": []
    },
    "06_Builds": [
        "Dev-Builds",
        "Experimental-Builds",
        "Stable-Releases"
    ],
    "07_Backups": [
        "Weekly",
        "Milestones"
    ]
}


def create_structure(base_path, tree):
    if isinstance(tree, dict):
        for folder, subfolders in tree.items():
            folder_path = os.path.join(base_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            create_structure(folder_path, subfolders)
    elif isinstance(tree, list):
        for folder in tree:
            folder_path = os.path.join(base_path, folder)
            os.makedirs(folder_path, exist_ok=True)


def create_admin_files():
    admin_path = os.path.join(ROOT_DIR, "00_Admin")

    files = [
        "Roadmap.md",
        "Vision-Document.md",
        "Hardware-Notes.md",
        "VRAM-Budget.md"
    ]

    for file in files:
        file_path = os.path.join(admin_path, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# {file.replace('.md', '')}\n\n")


if __name__ == "__main__":
    os.makedirs(ROOT_DIR, exist_ok=True)
    create_structure(ROOT_DIR, structure)
    create_admin_files()
    print("✅ AI-Mate-Project folder structure created successfully!")
