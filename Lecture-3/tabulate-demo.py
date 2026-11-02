# pip install tabulate 
from tabulate import tabulate 

todos = [
    {
        "id":1,
        "title":"Do Homework",
        "description":"Complete Python lecture-3 homework",
        "status": "pending",
    },
    {
        "id":2,
        "title":"Do Math Homework",
        "description": "Solve Algebra questions",
        "status":"completed"
    }
]

table = tabulate(todos,headers="keys",tablefmt="grid")
print(table)