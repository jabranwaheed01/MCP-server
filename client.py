# import asyncio

# from mcp import ClientSession,  StdioServerParameters
# from mcp.client.stdio import stdio_client

# server_params = StdioServerParameters(
#     command= "python",
#     args= ["server.py"],
# )

# async def main():
#     async with stdio_client(server_params) as (read,write):
#         async with ClientSession (read,write) as session:
#             await session.initialize()

# #---------------  Available_Tools.  -------------------

#             tools = await session.list_tools()

#             print("Available Tools: ")
#             for tool in tools.tools:
#                 print (tool.name)

# #---------------  Add_Function.  -------------------

#                 a = int(input("Enter 1st Number: "))
#                 b = int(input("Enter 2nd Number: "))
#                 result = await session.call_tool(
#                     "add",
#                     arguments= {"a": a , "b" : b}
#                 )   


# #---------------  Resources.  -------------------
                
#             resources = await session.list_resources()
#             print("Available Resources.")
#             for resource in resources.resources:
#                 print(resource.uri)
# #---------------  Print_Resources -------------------
#                 resource_result = await session.read_resource(
#                     "config://app"
#                     )
#                 print("Resource Data")
#                 print(resource_result.contents[0].text)
# #---------------  User_query.  -------------------
#                 query = input("Enter your Question.")

 

# #---------------  Print_Add_Function_Result.   -------------------
#             print("Result= " ,result.structured_content["result"])  

# #---------------  Available_Prompts_Result.  -------------------

#             prompts = await session.list_prompts()
#             print("Available Prompts.")
#             for prompt in prompts.prompts:
#                 print(prompt.name)

# #---------------  Prompts_Result -------------------
#             prompt_result = await session.get_prompt(
#                 "explain_query",
#                 arguments={"query": query}
            
#             ) 
#             print("\nPrompt Data")
#             print(prompt_result)  

                

# asyncio.run(main())              
            




import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="python",
    args=["server.py"],
)


async def main():

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            # ---------------- Available Tools ----------------

            tools = await session.list_tools()

            print("\nAvailable Tools:")
            for tool in tools.tools:
                print(tool.name)

            # ---------------- Add Function ----------------

            a = int(input("\nEnter 1st Number: "))
            b = int(input("Enter 2nd Number: "))

            result = await session.call_tool(
                "add",
                arguments={"a": a, "b": b}
            )

            print("\nResult =", result.structured_content["result"])

            # ---------------- Available Resources ----------------

            resources = await session.list_resources()

            print("\nAvailable Resources:")
            for resource in resources.resources:
                print(resource.uri)

            # ---------------- Read Resource ----------------

            resource_result = await session.read_resource(
                "config://app"
            )

            print("\nResource Data:")
            print(resource_result.contents[0].text)

            # ---------------- User Query ----------------

            query = input("\nEnter your question: ")

            # ---------------- Available Prompts ----------------

            prompts = await session.list_prompts()

            print("\nAvailable Prompts:")
            for prompt in prompts.prompts:
                print(prompt.name)

            # ---------------- Get Prompt ----------------

            prompt_result = await session.get_prompt(
                "explain_query",
                arguments={"query": query}
            )

            print("\nPrompt Data:")
            print(prompt_result.messages[0].content.text)


asyncio.run(main())

