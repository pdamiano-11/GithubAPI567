import hw04a

def test_response():
    gitInfo = hw04a.getGitInfo('pdamiano-11')
    assert 'pdamiano567' in gitInfo
    assert gitInfo['SSW567'] != 3
    assert gitInfo['SSW567-HW01'] == 2