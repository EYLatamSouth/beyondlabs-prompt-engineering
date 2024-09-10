import unittest
from unittest.mock import mock_open, patch, MagicMock
import os
import yaml
from update_navigation import (
    load_metadata,
    get_topic_by_id,
    generate_navigation_section,
    update_markdown_file,
)

METADATA_FILE = "metadata.yaml"

mock_metadata = {
    "global_links": {
        "issues": "https://github.com/issues",
        "pull_requests": "https://github.com/pulls",
        "index": "https://github.com/index",
        "about": "https://github.com/about",
        "license": "https://github.com/license",
    },
    "topics": [
        {
            "id": "1",
            "title": "Introduction",
            "file": "introduction.md",
            "previous": None,
            "next": "2",
            "related": [],
        },
        {
            "id": "2",
            "title": "Basic Concepts",
            "file": "basic_concepts.md",
            "previous": "1",
            "next": None,
            "related": ["1"],
        },
    ],
}

class TestNavigationGenerator(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="yaml content")
    @patch("yaml.safe_load", return_value=mock_metadata)
    def test_load_metadata_success(self, mock_safe_load, mock_file):
        """Test loading YAML metadata successfully."""
        metadata = load_metadata(METADATA_FILE)
        mock_file.assert_called_with(METADATA_FILE, "r", encoding="utf-8")
        self.assertEqual(metadata, mock_metadata)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_metadata_file_not_found(self, mock_file):
        """Test loading YAML when file is not found."""
        with self.assertRaises(FileNotFoundError):
            load_metadata(METADATA_FILE)

if __name__ == "__main__":
    unittest.main()
    
# TODO: NEED TO ADD MORE TESTS. MINIMUM 80% COVERAGE