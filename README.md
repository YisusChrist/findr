<p align="center">
    <a href="https://github.com/YisusChrist/findr/issues">
        <img src="https://img.shields.io/github/issues/YisusChrist/findr?color=171b20&label=Issues%20%20&logo=gnubash&labelColor=e05f65&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/findr/forks">
        <img src="https://img.shields.io/github/forks/YisusChrist/findr?color=171b20&label=Forks%20%20&logo=git&labelColor=f1cf8a&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/findr/stargazers">
        <img src="https://img.shields.io/github/stars/YisusChrist/findr?color=171b20&label=Stargazers&logo=octicon-star&labelColor=70a5eb">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/findr/actions">
        <img alt="Tests Passing" src="https://github.com/YisusChrist/findr/actions/workflows/github-code-scanning/codeql/badge.svg">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/findr/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/YisusChrist/findr?color=0088ff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://opensource.org/license/gpl-2-0/">
        <img alt="License" src="https://img.shields.io/github/license/YisusChrist/findr?color=0088ff">
    </a>
</p>

<br>

<p align="center">
    <a href="https://github.com/YisusChrist/findr/issues/new?assignees=YisusChrist&labels=bug&projects=&template=bug_report.yml">Report Bug</a>
    ·
    <a href="https://github.com/YisusChrist/findr/issues/new?assignees=YisusChrist&labels=feature&projects=&template=feature_request.yml">Request Feature</a>
    ·
    <a href="https://github.com/YisusChrist/findr/issues/new?assignees=YisusChrist&labels=question&projects=&template=question.yml">Ask Question</a>
    ·
    <a href="https://github.com/YisusChrist/findr/security/policy#reporting-a-vulnerability">Report security bug</a>
</p>

<br>

![Alt](https://repobeats.axiom.co/api/embed/ba8cf53161aa08def0a1fd65f22338397227dca5.svg "Repobeats analytics image")

<br>

<details>
<summary>Table of Contents</summary>

- [Requirements](#requirements)
- [Installation](#installation)
  - [From PyPI](#from-pypi)
  - [Manual installation](#manual-installation)
  - [Uninstall](#uninstall)
- [Usage](#usage)
- [Contributors](#contributors)
  - [How do I contribute to findr?](#how-do-i-contribute-to-findr)
- [License](#license)
- [Credits](#credits)

</details>

# Requirements

Here's a breakdown of the packages needed and their versions:

- [rich](https://pypi.org/project/rich) (version 13.7.0)

> [!NOTE]
> The software has been developed and tested using Python `3.12.1`. The minimum required version to run the software is Python 3.6. Although the software may work with previous versions, it is not guaranteed.

# Installation

## From PyPI

`findr` can be installed easily as a PyPI package. Just run the following command:

```bash
pip3 install pyfindr
```

> [!IMPORTANT]
> For best practices and to avoid potential conflicts with your global Python environment, it is strongly recommended to install this program within a virtual environment. Avoid using the --user option for global installations. We highly recommend using [pipx](https://pypi.org/project/pipx) for a safe and isolated installation experience. Therefore, the appropriate command to install `findr` would be:
>
> ```bash
> pipx install pyfindr
> ```

The program can now be ran from a terminal with the `findr` command.

## Manual installation

If you prefer to install the program manually, follow these steps:

> [!WARNING]
> This will install the version from the latest commit, not the latest release.

1. Download the latest version of [findr](https://github.com/YisusChrist/findr) from this repository:

   ```bash
   git clone https://github.com/YisusChrist/findr
   cd findr
   ```

2. Install the package:

   ```bash
   poetry install
   ```

3. Run the program:

   ```bash
   poetry run findr
   ```

## Uninstall

If you installed it from PyPI, you can use the following command:

```bash
pipx uninstall pyfindr
```

# Usage

<h4 align="center">Search for a match in file contents.</h4>
<p align="center">
  <img width="600" src="https://i.imgur.com/bku2Ad0.png">
</p>

<br>

<h4 align="center">Search for a match in filenames.</h4>
<p align="center">
  <img width="600" src="https://i.imgur.com/vgWI2QP.png">
</p>

<br>

```sh
usage: findr key
             [--path PATH]
             [--mode {contents,filenames}]
             [--max-depth MAX_DEPTH]
             [--skip-dotfiles]
             [-h] [-v] [-d] [-V]

Recursively search files

Main Options:
  key                   The string to search for.
  --path PATH           the path to search under (default: D:\Documents\development\findr)
  --mode {contents,filenames}
                        The search mode. Default is 'contents'.
  --max-depth MAX_DEPTH
                        maximum depth for recursive search
  --skip-dotfiles       skip dotfiles

Miscellaneous Options:
  -h, --help            Show this help message and exit.
  -v, --verbose         Show log messages on screen. Default is False.
  -d, --debug           Activate debug logs. Default is False.
  -V, --version         Show version number and exit.
```

# Contributors

<a href="https://github.com/YisusChrist/findr/graphs/contributors"><img src="https://contrib.rocks/image?repo=YisusChrist/findr" /></a>

## How do I contribute to findr?

Before you participate in our delightful community, please read the [code of conduct](https://github.com/YisusChrist/.github/blob/main/CODE_OF_CONDUCT.md).

I'm far from being an expert and suspect there are many ways to improve – if you have ideas on how to make the configuration easier to maintain (and faster), don't hesitate to fork and send pull requests!

We also need people to test out pull requests. So take a look through [the open issues](https://github.com/YisusChrist/findr/issues) and help where you can.

See [Contributing Guidelines](https://github.com/YisusChrist/.github/blob/main/CONTRIBUTING.md) for more details.

# License

`findr` is released under the [GPL-2.0 license](https://opensource.org/licenses/GPL-2.0).

# Credits

> [!NOTE]
> Credits to [Julynx](https://github.com/Julynx) for creating the original [project](https://github.com/Julynx/findr). I only make improvements in his code based on my preferences to customize it. All the ideas and the base of the script are his.
