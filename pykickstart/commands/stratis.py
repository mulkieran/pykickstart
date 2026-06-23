from pykickstart.version import F45
from pykickstart.base import KickstartCommand
from pykickstart.options import KSOptionParser


class F45_Stratis(KickstartCommand):
    removedKeywords = KickstartCommand.removedKeywords
    removedAttrs = KickstartCommand.removedAttrs

    def __init__(self, writePriority=100, *args, **kwargs):
        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
        self.op = self._getParser()
        self.stratis = kwargs.get("stratis", False)

    def __str__(self):
        retval = KickstartCommand.__str__(self)

        if self.stratis:
            retval += "stratis\n"

        return retval

    def _getParser(self):
        op = KSOptionParser(prog="stratis", description="""
                            Configure a Stratis-based installation.
                            """, version=F45)
        return op

    def parse(self, args):
        self.op.parse_args(args=args, lineno=self.lineno)
        self.stratis = True
        return self
