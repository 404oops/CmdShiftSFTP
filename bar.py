
from tqdm import tqdm
import sys
def viewBar(a,b):
    # original version
    res = a/int(b)*100
    sys.stdout.write('\rComplete precent: %.2f %%' % (res))
    sys.stdout.flush()

def tqdmWrapViewBar(*args, **kwargs):
    pbar = tqdm(*args, **kwargs)  # make a progressbar
    last = [0]  # last known iteration, start at 0
    def viewBar2(a, b):
        pbar.total = int(b)
        pbar.update(int(a - last[0]))  # update pbar with increment
        last[0] = a  # update last known iteration
    return viewBar2, pbar  # return callback, tqdmInstance

cbk, pbar = tqdmWrapViewBar(ascii=True, unit='b', unit_scale=True)