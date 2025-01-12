import nox


@nox.session(python=["3.12"])
def tests(session):
    args = session.posargs or ["--cov"]
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("poetry", "run", "pytest", *args, external=True)


locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.12"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)
