from enum import Enum
from fastapi import FastAPI

app = FastAPI(title="Antigravity")

class ModelLLM (str ,Enum):
    Fable_5 = "fable-5"
    Gemini_3_8 = "gemini-3.8"
    DeepSeek_4_Pro = "deepseek_4_pro"

@app.get("/")
async def root():
    return {"message": "Welcome to Antigravity API"}

@app.get("/models")
async def get_models(model_name: ModelLLM):
    if model_name == ModelLLM.Fable_5:
        return {"Model": "Fable 5", "Description": "This is a model create by Anthropic"}
    elif model_name == ModelLLM.Gemini_3_8:
        return {"Model": "Gemini 3.8", "Description": "This is a model create by Google"}
    elif model_name == ModelLLM.DeepSeek_4_Pro:
        return {"Model": "DeepSeek 4 Pro", "Description": "This is a model create by DeepSeek"}
