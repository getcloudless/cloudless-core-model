from jsonschema import validate
import json


with open("models/virtual-machine.json") as vm_model_raw:
    vm_model = json.loads(vm_model_raw.read())

validate(instance={"version" : "1.0.0", "name" : "foo",
                   "region": "bar", "availability_zone": "baz"}, schema=vm_model)

with open("models/private-network.json") as private_network_model_raw:
    private_network_model = json.loads(private_network_model_raw.read())

validate(instance={"version" : "1.0.0", "name" : "foo",
                   "region": "bar", "availability_zone": "baz"}, schema=private_network_model)
