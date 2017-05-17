from parsers.twitch_parser import TwitchParser

class ParserFactory:
    def build(self, type, bsoup, senturls, substr, t):
        temp = type.lower().replace(" ", "")
        temp = temp.replace("_", "")
        if temp == "twitchparser":
            return TwitchParser(bsoup, senturls, substr, t)
        else:
            assert 0, "invalid parser type"
