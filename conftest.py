from datetime import datetime


def pytest_configure(config):
    config._metadata = {
        "Project": "Autonomize AI QA Assignment",
        "Environment": "QA",
        "Execution Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def pytest_addoption(parser):
    # handle cli options if needed
    pass


def pytest_sessionstart(session):
    # setup resources if needed
    print("\nStarting test session...")


def pytest_sessionfinish(session):
    # collect results and generate report
    # notify slack if needed
    # teardown resources if needed
    print("\nTest session finished.")
