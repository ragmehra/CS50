from twttr import shorten 

def test_shorten():
    assert shorten("twitter") == 'twttr'
    assert shorten("goobie") == "gb"
    assert shorten("twItter") == "twttr"
    assert shorten("123,a") == "123,"
