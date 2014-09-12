#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
import ConfigParser
config = ConfigParser.ConfigParser()
def test1():
    config.add_section('Section1')
    config.set('Section1','age','15')
    config.set('Section1','male','true')
    config.set('Section1','score','97.5')
    config.set('Section1', 'baz', 'fun')
    config.set('Section1', 'bar', 'Python')
    config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

    with open('hello.ini', 'wb+') as configfile:
        config.write(configfile)
        
        
config.read('hello.ini')
score = config.getfloat('Section1','score')
age = config.getfloat('Section1','age')
male = config.getboolean('Section1', 'male')
print male,type(male)
print score+age
foo = config.get("Section1",'foo',0,{'bar':100,'baz':'hello'})
print foo,type(foo)