#!/usr/bin/env python3
"""
Navigation Generator for Prompt Engineering Repository

This script reads a YAML metadata file and generates navigation sections
for Markdown files in a Prompt Engineering repository.
"""

import os
import yaml
from typing import Dict, List

def load_metadata(file_path: str) -> Dict:
    """Load metadata from a YAML file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: Metadata file '{file_path}' not found.")
        raise
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        raise

def get_topic_by_id(topics: List[Dict], topic_id: str) -> Dict:
    """Get a topic dictionary by its ID."""
    return next((t for t in topics if t["id"] == topic_id), None)

def generate_navigation_section(topic: Dict, metadata: Dict, global_links: Dict) -> str:
    """Generate a navigation section for a given topic."""
    nav_section = "\n## Navegação\n\n"

    if topic["previous"]:
        prev_topic = get_topic_by_id(metadata["topics"], topic["previous"])
        if prev_topic:
            nav_section += (
                f"- [Anterior: {prev_topic['title']}]({prev_topic['file']})\n"
            )

    if topic["next"]:
        next_topic = get_topic_by_id(metadata["topics"], topic["next"])
        if next_topic:
            nav_section += f"- [Próximo: {next_topic['title']}]({next_topic['file']})\n"

    nav_section += "\n## Tópicos Relacionados\n\n"
    for related_id in topic["related"]:
        related_topic = get_topic_by_id(metadata["topics"], related_id)
        if related_topic:
            nav_section += f"- [{related_topic['title']}]({related_topic['file']})\n"

    nav_section += f"""
## Contribuição

Encontrou um erro ou tem uma sugestão? Por favor, abra uma [issue]({global_links['issues']}) ou envie um [pull request]({global_links['pull_requests']}).

---

<div align="center">
  <a href="{global_links['index']}">Voltar ao Índice</a> | 
  <a href="{global_links['about']}">Sobre este Projeto</a> | 
  <a href="{global_links['license']}">Licença</a>
</div>
"""
    return nav_section

def update_markdown_file(file_path: str, navigation_section: str) -> None:
    """Update a Markdown file with the new navigation section."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        """ Find the existing navigation section or the end of the content """
        nav_start = content.find("\n## Navegação")
        if nav_start == -1:
            """ If no navigation section exists, add it at the end """
            updated_content = content + "\n" + navigation_section
        else:
            """ If a navigation section exists, replace it """
            nav_end = content.find("\n## Contribuição", nav_start)
            if nav_end == -1:
                nav_end = len(content)
            updated_content = (
                content[:nav_start] + navigation_section + content[nav_end:]
            )

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(updated_content)

        print(f"Updated navigation for {file_path}")
    except FileNotFoundError:
        print(f"Warning: File '{file_path}' not found. Skipping this file.")
    except IOError as e:
        print(f"Error updating file '{file_path}': {e}")

def main():
    """Main function to orchestrate the navigation generation process."""
    try:
        metadata = load_metadata("metadata.yaml")
        global_links = metadata["global_links"]

        for topic in metadata["topics"]:
            file_path = os.path.join("learning", "fundamentals", topic["file"])
            navigation_section = generate_navigation_section(
                topic, metadata, global_links
            )
            update_markdown_file(file_path, navigation_section)

        print("Navigation update completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

# TODO: FIX THIS SCRIPT; IT IS NOT CREATING THE RELATED FIELDS CORRECTLY.
