import os
import torch
import torch.utils.data
from torch.nn import DataParallel
from torch.optim import lr_scheduler
import torch.optim as optim
import time
import numpy as np
import torchvision.transforms as transforms
import argparse
from margin.ArcMarginProduct import ArcMarginProduct
from margin.MultiMarginProduct import MultiMarginProduct
from margin.CosineMarginProduct import CosineMarginProduct
from margin.InnerProduct import InnerProduct

def train(args):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PyTorch for recognition')
    parser.add_argument('--train_root', type=str, default='/media/ramdisk/msra_align_112', help='train image root')
    parser.add_argument('--train_file_list', type=str, default='/media/ramdisk/msra_align_train.list', help='train list')
    parser.add_argument('--lfw_test_root', type=str, default='/media/sda/lfw/lfw_align_112', help='lfw image root')
    args = parser.parse_args()
    train(args)# working on