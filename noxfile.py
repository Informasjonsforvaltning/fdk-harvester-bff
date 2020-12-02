"""Nox sessions."""
import tempfile

import nox
from nox.sessions import Session
import nox_poetry

package = "fdk_harvester_bff"
locations = "src", "tests", "noxfile.py"
nox.options.stop_on_first_error = True
nox.options.sessions = "lint", "mypy", "pytype", "contract_tests"


@nox.session(python="3.8")
def tests(session: Session) -> None:
    """Run the test suite."""
    args = session.posargs or ["--cov"]
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(
        session, "coverage[toml]", "pytest", "pytest-cov",
    )
    session.run(
        "pytest", "-m unit", "-rA", *args, env={"ALTINN_URI": "altinn-uri"},
    )
    session.run("pytest", "-m unit", "-rA", *args)


@nox.session(python="3.8")
def contract_tests(session: Session) -> None:
    """Run the contract_test suite."""
    args = session.posargs
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(session, "pytest", "pytest-docker")
    session.run("pytest", "-m contract", *args)


@nox.session(python="3.8")
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    nox_poetry.install(session, "black")
    session.run("black", *args)


@nox.session(python="3.8")
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    nox_poetry.install(
        session,
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


@nox.session(python="3.8")
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
        nox_poetry.install(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python="3.8")
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    nox_poetry.install(session, "mypy")
    session.run("mypy", *args)


@nox.session(python="3.8")
def pytype(session: Session) -> None:
    """Run the static type checker using pytype."""
    args = session.posargs or ["--disable=import-error", *locations]
    nox_poetry.install(session, "pytype")
    session.run("pytype", *args)


@nox.session(python="3.8")
def xdoctest(session: Session) -> None:
    """Run examples with xdoctest."""
    args = session.posargs or ["all"]
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(session, "xdoctest")
    session.run("python", "-m", "xdoctest", package, *args)


@nox.session(python="3.8")
def docs(session: Session) -> None:
    """Build the documentation."""
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(session, "sphinx", "sphinx_autodoc_typehints")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(python="3.8")
def coverage(session: Session) -> None:
    """Upload coverage data."""
    nox_poetry.install(session, "coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)
