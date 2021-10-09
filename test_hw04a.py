import hw04a
import mock
from pytest_mock import mocker
import pytest

def test_response(mocker):
    mocker.patch('hw04a.getGitInfo', return_value = 18)
    
    gitInfo = hw04a.getGitInfo('pdamiano-11')
    expect = 18
    assert gitInfo == expect
    assert gitInfo != 15

    mocker.patch('hw04a.getGitInfo', return_value = True)
    
    gitInfo = hw04a.getGitInfo('pdamiano-11')
    expect = True
    assert gitInfo == expect
    assert gitInfo != False