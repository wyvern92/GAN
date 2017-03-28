import logging
import os
import sys


class AverageMeter(object):
  """
  Computes and stores the average and current value
  """
  def __init__(self):
    self.val = 0
    self.avg = 0
    self.sum = 0
    self.count = 0

  def update(self, val, n=1):
    self.val = val
    self.sum += val*n
    self.count += n
    self.avg = self.sum/self.count


class Statistics(object):
  def __init__(self, names):
    self.meters = {}
    for name in names:
      self.meters.update({name: AverageMeter()})

  def update(self, n, **kwargs):
    info = ''
    for key in kwargs:
      self.meters[key].update(kwargs[key], n)
      info += '{key}={loss.val:.4f}, avg {key}={loss.avg:.4f}, '.format(key=key, loss=self.meters[key])
    return info[:-2]


def get_logger(path):
  logger = logging.getLogger()
  logger.setLevel(logging.INFO)
  formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%Y-%m-%d,%H:%M:%S')

  fh = logging.FileHandler(os.path.join(path, 'debug.log'))
  fh.setLevel(logging.INFO)
  fh.setFormatter(formatter)
  logger.addHandler(fh)

  ch = logging.StreamHandler(sys.stdout)
  ch.setLevel(logging.INFO)
  ch.setFormatter(formatter)
  logger.addHandler(ch)

  return logger