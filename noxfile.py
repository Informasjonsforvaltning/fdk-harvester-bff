"""Nox sessions."""

import tempfile

import nox
from nox.sessions import Session
import nox_poetry

nox.options.envdir = ".cache"
nox.options.reuse_existing_virtualenvs = True
package = "fdk_harvester_bff"
locations = "src", "tests", "noxfile.py"
nox.options.stop_on_first_error = True
nox.options.sessions = "lint", "mypy", "contract_tests"


@nox_poetry.session(python="3.9")
def contract_tests(session: Session) -> None:
    """Run the contract_test suite."""
    args = session.posargs
    session.install(".", "pytest", "pytest-docker")
    session.run("pytest", "-m contract", *args)


@nox_poetry.session(python="3.9")
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox_poetry.session(python="3.9")
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
        "darglint",
        "flake8-assertive",
    )
    session.run("flake8", *args)


@nox_poetry.session(python="3.9")
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run(
            "safety", "check", f"--file={requirements.name}", "--output", "text"
        )


@nox_poetry.session(python="3.9")
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)


@nox_poetry.session(python="3.9")
def xdoctest(session: Session) -> None:
    """Run examples with xdoctest."""
    args = session.posargs or ["all"]
    session.install(".", "xdoctest")
    session.run("python", "-m", "xdoctest", package, *args)


@nox_poetry.session(python="3.9")
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install(".", "sphinx", "sphinx_autodoc_typehints")
    session.run("sphinx-build", "docs", "docs/_build")


@nox_poetry.session(python="3.9")
def coverage(session: Session) -> None:
    """Upload coverage data."""
    session.install("coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)
