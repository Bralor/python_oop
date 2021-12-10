import pytest
from typing import List

from notes import KindleReader


class TestKindleReader:
    """Test the list of methods that should get the .txt file with notes."""

    def setup(self):
        """Set up the test fixtures."""
        path: str = "dope"
        filename: str = "file"
        self.test_reader = KindleReader(path, filename)


    def test_create_valid_absolute_path(self):
        """Test the method 'create_absolute_path' with valid parameters"""
        assert str(self.test_reader.create_absolute_path()) == "dope/file"


    def test_create_invalid_absolute_path(self):
        """Test the method 'create_absolute_path' with invalid parameters"""
        assert str(self.test_reader.create_absolute_path()) != "dope/foo/file"


    def test_existing_path(self):
        """
        Test the method 'is_path_valid'. Method returns True if the path
        is correct.
        """
        assert self.test_reader.is_path_valid(
            "/home/matous/projects/python_oop/README.md"
        )


    def test_not_existing_path(self):
        """
        Test the method 'is_path_valid'. Method returns True if the path
        is correct.
        """
        assert not self.test_reader.is_path_valid(
            "dope/path/to/file"
        )


    def test_read_notes_invalid(self):
        """
        Test the method 'read_notes'. This method should return

        :name: read_notes
        :return: List[str]
        """
        with pytest.raises(Exception):
            isinstance(
                self.test_reader.read_notes("/home/fake/file.txt"),
                list
            )

