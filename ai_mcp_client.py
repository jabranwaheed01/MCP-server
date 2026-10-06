import asyncio

from mcp import ClientSession , StdioServerParameters
from mcp.client.stdio import stdio_client

from groq import Groq
from dotenv  import load_dotenv

import json

load_dotenv()
client = Groq()

server_params= StdioServerParameters(
    command= "python",
    args=["server.py"],
)

async def main():
    async with stdio_client (server_params) as (read , write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("\nMCP Tools.")
            for tool in tools.tools:
                groq_tools = {
                    "type" : "function",
                    "function" : {
                        "name" : tool.name,
                        "description" : tool.description,
                        "parameters" : tool.input_schema
                    }
                }
                print(groq_tools)


                a = int(input("Enter 1st number."))
                b = int(input("Enter 2nd number."))
                responce = client.chat.completions.create(
                    model = "openai/gpt-oss-20b",
                    messages = [
                        {
                        "role" :"user",
                        "content" : f"what is {a} + {b}"
                        }
                        ],
                        tools = [groq_tools]
                )
                print(responce.choices[0].message.tool_calls)


                tool_call = responce.choices[0].message.tool_calls[0]
                arguments = json.loads(tool_call.function.arguments)
                print (arguments)
                result = await session.call_tool(
                    tool_call.function.name,
                    arguments= arguments
                )
                print(result.structured_content)


asyncio.run(main())

               