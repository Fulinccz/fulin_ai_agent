# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AgentRequest(BaseModel):
    query: str

@app.post("/api/agent")
async def agent_query(request: AgentRequest):
    # 简单的AI Agent逻辑
    response = f"Agent received: {request.query}"
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)