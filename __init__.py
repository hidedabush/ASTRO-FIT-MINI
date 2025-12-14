"""
Create all necessary __init__.py files for Python packages
Run this script once to create the package structure
"""

from pathlib import Path

#define all directories that need __init__.py
package_dirs = [
    "config",
    "src",
    "src/sensors",
    "src/exercises",
    "src/evaluation",
    "src/ml",
    "src/database",
    "src/ui",
    "src/core",
    "tests",
]

project_root = Path(__file__).parent
for package_dir in package_dirs:
    init_file = project_root / package_dir / "__init__.py"
    init_file.parent.mkdir(parents=True, exist_ok=True)
    
    if not init_file.exists():
        # Create with docstring
        module_name = package_dir.replace("/", ".").replace("src.", "")
        init_file.write_text(f'"""{module_name} module for ASTRO-FIT MINI"""\n')
        print(f"Created: {init_file}")
    else:
        print(f"Exists: {init_file}")

print("\n✅ All __init__.py files created!")