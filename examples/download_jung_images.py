# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:50:50 2015

@author: igordsm
"""

import urllib.request
import tarfile

import os

def check_downloaded():
    return os.path.isdir('images') and os.path.exists('images/jung-1a.png')

def download_images():
    if check_downloaded(): return
    
    with urllib.request.urlopen(
        "http://vision.ime.usp.br/projects/trios/datasets/dataset-character.tar.gz"
        ) as images:

        
        with tarfile.open(fileobj=images, mode="r|gz") as tgz:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tgz, path="jung-images")

if __name__ == "__main__":
    download_images()
        