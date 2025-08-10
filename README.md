# 🚀 UV Copier Template

A modern [Copier](https://github.com/copier-org/copier) template for scaffolding Python packages and applications with best practices built-in.

## 🎁 Features

- 📦 **Modern Python packaging** using [UV](https://github.com/astral-sh/uv) for lightning-fast dependency management
- ⚡️ **Streamlined task execution** with [Task](https://taskfile.dev/)
- ✍️ **Code formatting and linting** with [Ruff](https://github.com/charliermarsh/ruff)
- 🔍 **Type checking** with [Mypy](https://github.com/python/mypy)
- 🛡️ **Quality gates** with [Pre-commit](https://pre-commit.com/) hooks
- 🏷️ **Automated versioning** following [Conventional Commits](https://www.conventionalcommits.org/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
- 📋 **Changelog generation** compatible with [Keep A Changelog](https://keepachangelog.com/)
- 🔄 **Continuous integration** with [GitHub Actions](https://docs.github.com/en/actions)
- 🏗️ **Template updates** with [Copier](https://github.com/copier-org/copier) for easy maintenance

## ✨ Quick Start

### Creating a New Python Project

1. **Install UV globally:**

   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Generate your project:**

   ```sh
   # Create in a new directory
   uvx copier copy https://github.com/gotofritz/copier-python-template my-project/ --trust

   # Or create in current directory
   mkdir my-project && cd my-project
   uvx copier copy https://github.com/gotofritz/copier-python-template . --trust
   ```

   > **Note:** The `--trust` flag is required as the template executes setup scripts.

3. **Configure your project** by answering the interactive prompts.

4. **Initialize Git and create remote repository:**

   ```sh
   cd my-project
   git init

   # Using GitHub CLI (recommended)
   gh repo create my-org/my-project --private --source=. --push

   # Or follow GitHub's instructions to push an existing repository
   ```

5. **Set up dependencies:**

   ```sh
   uv sync
   git add uv.lock && git commit -m "feat: add dependency lock file"
   ```

### Updating Your Project

Keep your project aligned with the latest template improvements:

```sh
uvx copier update
```

If conflicts arise, resolve them by inspecting the generated `.rej` files.

## 🖥️ CLI Application Support

When you enable CLI support during project creation, the template generates a ready-to-use command-line interface:

- **Automatic script installation** named after your project (kebab-case)
- **Sample commands** to get you started
- **Easy customization** via `pyproject.toml`

Example usage:

```sh
❯ my-project --help
Usage: my-project [OPTIONS] COMMAND [ARGS]...

  Main entry point for the CLI.

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  simple-command  This is a simple command.
  subcommand      This contains sub-subcommands
```

## 🔧 Development and Customization

### Testing Locally

To test modifications to this template:

```bash
copier copy ./copier-python-template --trust --vcs-ref=HEAD my-test-project
```

### Forking the Template

1. Fork this repository
2. Update all occurrences of `gotofritz` to your GitHub username
3. Customize the template to match your preferences
4. Use your forked version in the copy commands above

## 📚 What's Included

Your generated project comes with:

- **Modern Python packaging** with PEP 621 compliant `pyproject.toml`
- **Development tools** pre-configured and ready to use
- **GitHub Actions workflows** for testing and quality checks
- **Pre-commit hooks** to maintain code quality
- **Documentation structure** with README and changelog templates
- **Testing setup** with pytest and coverage reporting

---
