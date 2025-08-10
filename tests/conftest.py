import random
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def root_path() -> str:
    return str(Path(__file__).parent.parent)


@pytest.fixture(scope="session")
def common_data() -> dict[str, str]:
    return {
        "project_name": "test-project",
        "package_name": "test_project",
        "project_description": "A test Python package",
        "project_url": "https://github.com/gotifritz/test-project",
        "author_name": "Gotofritz",
        "author_email": "gotofritz@users.noreply.github.com",
        "python_version": "3.13",
    }


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Randomise the order of tests to avoid flakiness."""
    random.shuffle(items)
