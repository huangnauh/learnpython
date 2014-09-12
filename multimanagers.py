#!/usr/bin/env python
# coding: utf-8

from multiprocessing.managers import BaseManager
manager = BaseManager(address=('',5000),authkey='abc')
server = manager.get_server()
server.serve_forever()
