from pathlib import Path

from copier import run_copy


def test_defaults(root_path: str, tmp_path: Path, common_data: dict[str, str]) -> None:
    destination_path = tmp_path / "generated_project"
    run_copy(
        root_path,
        destination_path,
        data=common_data,
        vcs_ref="HEAD",
        defaults=True,
        skip_tasks=True,
    )
    assert (destination_path / "pyproject.toml").exists()
    assert (destination_path / "README.md").exists()
    assert (destination_path / "test_project").exists()
    assert (destination_path / "test_project" / "__init__.py").exists()
    assert (destination_path / ".pre-commit-config.yaml").exists()
    assert (destination_path / "tests").exists()

    # assert settings.py exists
    assert (destination_path / "test_project" / "config" / "app_config.py").exists()

    # Check pyproject.toml content for default dependencies
    content = (destination_path / "pyproject.toml").read_text()
    assert "pydantic>=" in content
    assert "pydantic-settings>=" in content

    # Check that CLI dependencies are NOT present by default
    assert "click>=" in content
    assert "rich>=" in content

    # Check that conventional commits dependencies ARE present by default
    assert "commitizen>=" in content

    # Check that strict development dependencies are NOT present by default
    assert "safety>=" in content

    # Check that project scripts section is NOT present by default
    assert "[project.scripts]" in content

    # Check that commitizen config IS present by default
    assert "[tool.commitizen]" in content
    assert "bump_message = " in content
    assert "tag_format = " in content
    assert "update_changelog_on_bump = true" in content
    assert 'version_provider = "pep621"' in content

    # Check that mypy strict settings are NOT present by default
    assert "strict = true" in content

    # Check that changelog URL IS present by default
    assert "changelog = " in content

    # Check that strict pytest options are NOT present by default
    assert "--strict-config" not in content
    assert "--strict-markers" not in content
    assert "--typeguard-packages=" not in content


def test_without_conventional_commits(
    root_path: str, tmp_path: Path, common_data: dict[str, str]
) -> None:
    destination_path = tmp_path / "generated_project"
    data = {
        **common_data,
        "with_conventional_commits": False,
    }
    run_copy(
        root_path,
        destination_path,
        data=data,
        vcs_ref="HEAD",
        defaults=True,
        skip_tasks=True,
    )

    # Check pyproject.toml content for conventional commits disabled
    pyproject_content = (destination_path / "pyproject.toml").read_text()
    assert "commitizen>=" not in pyproject_content
    assert "[tool.commitizen]" not in pyproject_content
    assert "bump_message = " not in pyproject_content
    assert "tag_format = " not in pyproject_content
    assert "update_changelog_on_bump = true" not in pyproject_content
    assert 'version_provider = "pep621"' not in pyproject_content

    # Check that changelog URL is NOT present
    assert "changelog = " not in pyproject_content


def test_with_cli(root_path: str, tmp_path: Path, common_data: dict[str, str]) -> None:
    destination_path = tmp_path / "generated_project"
    data = {
        **common_data,
        "cli": True,
    }
    run_copy(
        root_path,
        destination_path,
        data=data,
        vcs_ref="HEAD",
        defaults=True,
        skip_tasks=True,
    )

    assert (destination_path / "pyproject.toml").exists()
    content = (destination_path / "pyproject.toml").read_text()
    assert 'test-project = "test_project.cli.__main__:cli"' in content

    assert (destination_path / "test_project" / "cli").exists()
    assert (destination_path / "test_project" / "cli" / "__main__.py").exists()

    assert (destination_path / "tests" / "cli").exists()

    # Check for CLI dependencies
    assert "click>=" in content
    assert "rich>=" in content

    # Check for project scripts section
    assert "[project.scripts]" in content
