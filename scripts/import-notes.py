"""Copy the current vault trees into generated Quartz content."""
from pathlib import Path
import shutil
import sys
import tempfile

project = Path(__file__).resolve().parent.parent
source = Path(sys.argv[1]).expanduser().resolve()
if not (source / "network-pentesting").is_dir():
    raise SystemExit("Source must be the Cyber vault, containing network-pentesting/")
content = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path(tempfile.gettempdir()) / "cyber-wiki-content"
if content == source or source in content.parents:
    raise SystemExit("Build content must be outside the source vault")
content.mkdir(parents=True, exist_ok=True)
shutil.copy2(project / "content/index.md", content / "index.md")
# Remove the former cookbook path from reused local build directories.
legacy = content / "xlaesch-Cookbook"
if legacy.exists():
    shutil.rmtree(legacy)
# Only these generated paths are replaced; the site's landing page stays intact.
folders = ("network-pentesting", "windows-fundamentals", "pwn", "azure", "ai", "sec+", "other", "Labs")
for folder in folders:
    destination = content / folder
    if destination.exists():
        shutil.rmtree(destination)
    if (source / folder).is_dir():
        shutil.copytree(source / folder, destination,
                        ignore=shutil.ignore_patterns(".git", ".obsidian", "AGENTS.md", "SUMMARY.md", "REORG_SOURCE_MAP.md"))
for name in ("pentesting-process.md",):
    destination = content / name
    destination.unlink(missing_ok=True)
    if (source / name).is_file():
        shutil.copy2(source / name, destination)
print(f"Imported {sum(1 for p in content.rglob('*.md'))} Markdown pages from {source}")
