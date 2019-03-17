"""
Simple validator library.
"""
import os
import json
import jsonref
from jsonschema import validate, Draft4Validator, RefResolver


def validate_with_refs(schema_path, data):
    base_path = os.path.abspath(os.path.dirname(schema_path))
    base_uri = 'file://{}/'.format(base_path)
    with open(schema_path) as subnet_model_raw:
        subnet_model = jsonref.loads(subnet_model_raw.read(), base_uri=base_uri, jsonschema=True)
    validate(instance=data, schema=subnet_model)

validate_with_refs(data={"version" : "1.0.0", "name" : "foo",
                         "region": "bar", "availability_zone": "baz"},
                   schema_path="models/virtual-machine.json")

validate_with_refs(data={"version" : "1.0.0", "name" : "foo",
                         "region": "bar", "availability_zone": "baz"},
                   schema_path="models/private-network.json")

validate_with_refs(data={"version" : "1.0.0", "name" : "foo",
                         "network": {"version": "0.0.0", "name": "bar"}},
                   schema_path="models/subnet.json")
