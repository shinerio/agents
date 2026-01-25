from veadk import Agent, Runner
from veadk.tools.builtin_tools.mcp_router import mcp_router
import asyncio

agent = Agent(
    # instruction 是 Agent 的 Prompt，这里只是一个示例，具体场景下需要根据实际情况调整
    instruction="你是一个智能助手，必须使用 mcp_router 工具来解决问题，并礼貌回复用户的问题。",
    tools=[mcp_router],
)

runner = Runner(agent=agent)
user_prompt = "你好，把大象装冰箱需要几步？"
session_id = "mcp_toolset_session_id_123"
response = asyncio.run(
    runner.run(messages=user_prompt, session_id=session_id)
)

print(response)