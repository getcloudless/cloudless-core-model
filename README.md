# The Cloudless Model

This is an abstract model of the resources that a cloud provider can provide.

While there is a lot of variance in terms of the features that different cloud
providers support, this is meant to focus in on the features that are actually
core to most use cases, and simplify a complex ecosystem.

Each resource type can be translated into real resources by a driver.  The
description of how that resource should be created should be included with the
resource.

Note that these files use relative file references.
https://medium.com/grammofy/handling-complex-json-schemas-in-python-9eacc04a60cf
describes how to support that using the python package jsonref.  See validate.py
for an example.
