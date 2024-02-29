# tests/conftest.py
def pytest_addoption(parser):
    parser.addoption("--custom-option", action="store_true", help="Enable custom test behavior")
    