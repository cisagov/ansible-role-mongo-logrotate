"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["logrotate"])
def test_apt_packages(host, pkg):
    """Test that the apt packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize(
    "file",
    [
        {
            "contents": "^/var/log/mongodb",
            "mode": "0o644",
            "path": "/etc/logrotate.d/mongo",
        }
    ],
)
def test_files(host, file):
    """Test that appropriate files exist."""
    assert host.file(file["path"]).exists
    assert host.file(file["path"]).is_file
    assert oct(host.file(file["path"]).mode) == file["mode"]
    assert host.file(file["path"]).contains(file["contents"])
