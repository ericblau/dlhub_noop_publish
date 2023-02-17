from dlhub_sdk import DLHubClient
from dlhub_sdk.models.servables.python import PythonStaticMethodModel
from dlhub_sdk.utils.schemas import validate_against_dlhub_schema
from noop import run_noop


model = PythonStaticMethodModel.from_function_pointer(run_noop)

model.set_title("DLHub No-op Publication Test client-side")
# TODO: change this each time
model.set_name("noop_v25")

model.set_inputs("boolean", "Any boolean value")
model.set_outputs("string", "'Hello world!'")
# TODO: change path
#model.add_file("/Users/aristanascourtas/Documents/Work/noop.py")
model.add_file("/Users/blau/Garden/ContainerService/test_publish/noop.py")

res = validate_against_dlhub_schema(model.to_dict(), 'servable')
print(res)
client = DLHubClient()
taskid = client.publish_servable(model)
print(taskid)

# TODO: get full ID from website or SDK -- needs your username
# res = client.run("aristana_uchicago/noop_v21", True, debug=True)
# print(res)



