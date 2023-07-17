import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)
data["company"]["employee"]["birth_date"] = "1990-01-01"
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)
