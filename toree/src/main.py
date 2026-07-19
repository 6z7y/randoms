import sys

from arg_handle import arg_handle
from data import Context
import layout
import utils

ctx = Context(1, 0, 0) # layout default 1
args = sys.argv

if (len(args) < 2):
    print(f"{utils.RED}usage: {utils.RESET}'{utils.GREEN}{args[0]} .{utils.RESET}'")
    exit(0)
else:
    args = arg_handle(args, ctx)


if ctx.layout == 1:
    layout.lay_1(args[1])

if ctx.layout == 2:
    layout.lay_2(args[1])

if ctx.layout == 3:
    layout.lay_3(args[1])
