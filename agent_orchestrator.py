import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

reseach_question = "Do adhd medications increase the risk of cardivascular events significantly"
study_type = "systematic review"
# the paramenters argument of the function is defined as a a json schema object
def read_file(file_name):
    return open(file_name).read()
# ideas_tools =
my_messages = [
    {
        "role": "system",
        "content": "You an honest and helpful assistant  that only outups your respose in strict JSON without any trailing or leading character. Use the functions to provide answers:",
    },
    {"role": "system", "content": "You are an expert understanding and evaluating research papers"},
    {
        "role": "user",
        "content": f"provide in json format for for the following research question {reseach_question} and for this type of studies {study_type}",
    },
]

my_tools2 = [
    {
        "type": "function",
        "function": {
            "name": "get_paper_evaluation",
            "description": f"evaluate the next research paper  {company_description} in relation to the study",
            "parameters": {
                "type": "object",
                "properties": {
                    "paper_evaluation_list": {
                        "type": "array",
                        "description": "evaluate the paper.",
                        "items": {"type": "string"},
                        "prefixItems": [
                            {"type": "string"},
                            {"type": "string"},
                            {"type": "string"},
                        ],
                    }
                },
                "required": ["paper_evaluation_list"],
            },
        },
    },
]
my_tool_choice = {"type": "function", "function": {"name": "get_paper_evaluation"}}

completion = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},  # always used in
    temperature=0.2,
    messages=my_messages,
    tools=my_tools2,
    tool_choice=my_tool_choice,
    max_tokens=3000,
)
response = completion.choices[0].message.content

tool_calls_response = completion.choices[0].message.tool_calls
function_args = json.loads(tool_calls_response[0].function.arguments)
print(function_args)
print("finale")

