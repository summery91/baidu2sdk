#coding=utf-8
import base64
import gzip
from io import StringIO
'''
    preview unzip & base64
'''
class PreviewUtil():
    @classmethod
    def decode(cls,msg):
        cstr = StringIO(base64.b64decode(msg))
        ziper = gzip.GzipFile(fileobj=cstr)
        data = ziper.read()
        return data



