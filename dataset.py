""" train and test dataset

author baiyu
"""
import os
import pickle
import numpy
from torch.utils.data import Dataset

class CIFAR100Train(Dataset):
    """cifar100 train dataset, derived from
    torch.utils.data.DataSet
    """
    def __init__(self, path, transform=None):
        # if transform is given, we transform data using it
        with open(os.path.join(path, 'train'), 'rb') as cifar100:
            self.data = pickle.load(cifar100, encoding='bytes')
        self.transform = transform

    def __len__(self):
        return len(self.data['fine_labels'.encode()])

    def __getitem__(self, index):
        label = self.data['fine_labels'.encode()][index]
        r = self.data['data'.encode()][index, :1024].reshape(32, 32)
        g = self.data['data'.encode()][index, 1024:2048].reshape(32, 32)
        b = self.data['data'.encode()][index, 2048:].reshape(32, 32)
        image = numpy.dstack((r, g, b))

        if self.transform:
            image = self.transform(image)
        return label, image

class CIFAR100Test(Dataset):
    """cifar100 test dataset, derived from
    torch.utils.data.DataSet
    """
    def __init__(self, path, transform=None):
        with open(os.path.join(path, 'test'), 'rb') as cifar100:
            self.data = pickle.load(cifar100, encoding='bytes')
        self.transform = transform

    def __len__(self):
        return len(self.data['data'.encode()])

    def __getitem__(self, index):
        label = self.data['fine_labels'.encode()][index]
        r = self.data['data'.encode()][index, :1024].reshape(32, 32)
        g = self.data['data'.encode()][index, 1024:2048].reshape(32, 32)
        b = self.data['data'.encode()][index, 2048:].reshape(32, 32)
        image = numpy.dstack((r, g, b))

        if self.transform:
            image = self.transform(image)
        return label, image

# Adding CIFAR-10 support
class CIFAR10Train(Dataset):
    """cifar10 train dataset, derived from
    torch.utils.data.DataSet
    """
    def __init__(self, path, transform=None):
        with open(os.path.join(path, 'train'), 'rb') as cifar10:
            self.data = pickle.load(cifar10, encoding='bytes')
        self.transform = transform

    def __len__(self):
        return len(self.data['labels'.encode()])

    def __getitem__(self, index):
        label = self.data['labels'.encode()][index]
        r = self.data['data'.encode()][index, :1024].reshape(32, 32)
        g = self.data['data'.encode()][index, 1024:2048].reshape(32, 32)
        b = self.data['data'.encode()][index, 2048:].reshape(32, 32)
        image = numpy.dstack((r, g, b))

        if self.transform:
            image = self.transform(image)
        return label, image

class CIFAR10Test(Dataset):
    """cifar10 test dataset, derived from
    torch.utils.data.DataSet
    """
    def __init__(self, path, transform=None):
        with open(os.path.join(path, 'test'), 'rb') as cifar10:
            self.data = pickle.load(cifar10, encoding='bytes')
        self.transform = transform

    def __len__(self):
        return len(self.data['labels'.encode()])

    def __getitem__(self, index):
        label = self.data['labels'.encode()][index]
        r = self.data['data'.encode()][index, :1024].reshape(32, 32)
        g = self.data['data'.encode()][index, 1024:2048].reshape(32, 32)
        b = self.data['data'.encode()][index, 2048:].reshape(32, 32)
        image = numpy.dstack((r, g, b))

        if self.transform:
            image = self.transform(image)
        return label, image
