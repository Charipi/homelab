from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.messages import SystemMessage, HumanMessage, ToolMessage, AIMessage
from calls import execute_remote_python
from dotenv import dotenv_values
config = dotenv_values(".env")

def off():
	"""Turn off the LED strip. Returns the success value."""
	return execute_remote_python(script_path=f'{config["LIGHT_SERVER_REPO_PATH"]}/LightServer/solid.py', args=["0", "0", "0"])

@tool
def set_color(red: int, green: int, blue: int) -> str:
	"""Set the LED strip to be a solid rgb color with values between 0 and 255. Returns the success value."""
	return execute_remote_python(script_path=f'{config["LIGHT_SERVER_REPO_PATH"]}/LightServer/solid.py', args=[str(red), str(green), str(blue)])

@tool
def set_color_loop(primary_hue: int, secondary_hue: int) -> str:
	"""Set the LED strip to cycle the primary and secondary hues in a loop.
	All hue values are between 0 and 360. Returns the success value."""
	return execute_remote_python(script_path=f'{config["LIGHT_SERVER_REPO_PATH"]}/LightServer/generic.py', args=["loop", str(primary_hue), str(secondary_hue)])

@tool
def set_color_breathe(primary_hue: int, secondary_hue: int) -> str:
	"""Set the LED strip to create a breathing effect with the primary and secondary hues.
	All hue values are between 0 and 360. Returns the success value."""
	return execute_remote_python(script_path=f'{config["LIGHT_SERVER_REPO_PATH"]}/LightServer/generic.py', args=["breathe", str(primary_hue), str(secondary_hue)])

llm = ChatGoogleGenerativeAI(
	model="gemini-2.5-flash", 
	# model="gemini-2.5-flash-lite", # kinda sucks, but could be a backup
	temperature=0, 
	api_key=config["VOICE_CLIENT_GEMINI_API_KEY"])

agent = create_agent(llm, [set_color, set_color_loop, set_color_breathe])

def run(command):
	print("Running command:", command)
	try:
		result = agent.invoke({"messages": [
			SystemMessage("You are a helpful assistant. When given instructions, use your best intuition to call the appropriate tool with good parameters to complete the task immediately without clarification."),
			HumanMessage(command)
		]})
	except Exception as e:
		print("Error during agent execution:", e)
		return
	messages = result["messages"]

	# # could use this for function return values
	# tool_output = next(
	#     m for m in messages if isinstance(m, ToolMessage)
	# )
	# print(tool_output.content)

	try:
		ai_message = next(
			m for m in reversed(messages)
			if isinstance(m, AIMessage) and m.content
		)
		print(ai_message.content)
	except StopIteration:
		print("Done")