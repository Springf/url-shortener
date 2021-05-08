from validator import regex_validator

def test_url_correct():
    assert regex_validator.validate('http://www.yahoo.com')
    assert regex_validator.validate('https://www.yahoo.com')
    assert regex_validator.validate('www.yahoo.com')
    assert regex_validator.validate('yahoo.com')
    assert regex_validator.validate('https://www.abc.com/foo/?bar=baz&inga=42&quux')
    assert regex_validator.validate('http://abc.com:8080')
    assert regex_validator.validate('http://a.b-c.de')
    assert regex_validator.validate('http://a.b_c.de')
    assert regex_validator.validate('https://github.com/Springf%3Ftab%3Drepositories')
    assert regex_validator.validate('https://www.youtube.com/watch?v=c4cUpAPvdVI')
    assert regex_validator.validate('https://forums.hardwarezone.com.sg/threads/gpgt-moi-humble-lunch.6511096/')
    assert regex_validator.validate('https://forums.sabc.sg/education-personal-growth/#')
    assert regex_validator.validate('www.microsoft.com/en-sg/microsoft-365/business/microsoft-365-plan-chooser')
    assert regex_validator.validate('https://t.co/DhQ1VfmTNR?amp=1')
    assert regex_validator.validate('https://sg.yahoo.com/news/sph-ceo-ng-yat-chung-question-editorial-integrity-122702142.html')
    assert regex_validator.validate('https://sg.finance.yahoo.com/quote/TSLA/key-statistics?p=TSLA')
    assert regex_validator.validate('https://login.yahoo.com/?activity=uh-signin&.intl=sg&.lang=en-SG&.src=finance&.done=https%3A%2F%2Fsg.finance.yahoo.com%2Fquote%2FTSLA%2Fkey-statistics%3Fp%3DTSLA&pspid=1187335917')

def test_url_wrong():
    assert regex_validator.validate('1234567') == False
    assert regex_validator.validate('abcdefg') == False
    assert regex_validator.validate('http://#') == False
    assert regex_validator.validate('http://3628126748') == False
    assert regex_validator.validate('hddp://3628126748') == False
    assert regex_validator.validate('tcp://yahoo.com') == False
    assert regex_validator.validate('ftp://google.com') == False
    assert regex_validator.validate('') == False
    assert regex_validator.validate('     ') == False