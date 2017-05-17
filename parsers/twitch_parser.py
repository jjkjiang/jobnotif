from parsers.base_parser import BaseParser

#twitch parser, which looks at names stored in h5, compares and then finds the link in the parent


class TwitchParser(BaseParser):
    def parse(self):
        msg = ""

        for i in self.bsoup.find_all("h5"):
            if self.substr.lower() in i.string.lower():
                jobname = i.string
                p = i.find_parent("a")
                if self.t:
                    print(p)
                joblink = p.get('href')

                if joblink not in self.senturls:
                    self.senturls.add(joblink)
                    if self.t:
                        print("adding " + jobname)

                    msg += jobname + '\n' + joblink + '\n'

        if self.t:
            print("msg: " + msg)

        return msg
