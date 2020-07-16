from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant("6be359cc-8c9e-42d3-84ba-a10909a8e163-bluemix", "2bc41d8b84103d06ac9700ade4ed6a865a9264560ff846cf9e3e62c7121a6449", url="https://6be359cc-8c9e-42d3-84ba-a10909a8e163-bluemix:2bc41d8b84103d06ac9700ade4ed6a865a9264560ff846cf9e3e62c7121a6449@6be359cc-8c9e-42d3-84ba-a10909a8e163-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()

database_name = "sample"
my_database = client.create_database(database_name)

if my_database.exists():
   print(f"'{database_name}' successfully created.")

record={"Device":"Laptop","Name":"Dell"}

new_document = my_database.create_document(record)

if new_document.exists():
     print(f"Document successfully created.")

result_collection = Result(my_database.all_docs,include_docs=True)

print(f"Retrieved minimal document:\n{result_collection[0]}\n")



