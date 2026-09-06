# Giá trị được xác định trước
Nếu bạn có một thao tác đường dẫn nhận tham số đường dẫn , nhưng bạn muốn các giá trị tham số đường dẫn hợp lệ có thể được xác định trước, bạn có thể sử dụng cú pháp chuẩn của Python Enum.

## Tạo một Class Enum
Nhập Enum và tạo một lớp con kế thừa từ str và từ Enum.

Bằng cách kế thừa từ str tài liệu API, người ta sẽ biết được các giá trị phải thuộc loại nào string và sẽ có thể hiển thị chính xác.

Sau đó, hãy tạo các thuộc tính lớp với các giá trị cố định, đó sẽ là các giá trị hợp lệ khả dụng:

## cú pháp lấy giá trị của enum: your_enum_member.value 
""python ""
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
async def get_models(model_name: ModelLLM): // Khai báo tham số đường dẫn
    if model_name == ModelLLM.Fable_5: // làm việc với kiểu liệt kê 
        return {"Model": "Fable 5", "Description": "This is a model create by Anthropic"} 
    elif model_name == ModelLLM.Gemini_3_8:
        return {"Model": "Gemini 3.8", "Description": "This is a model create by Google"}
    elif model_name == ModelLLM.DeepSeek_4_Pro:
        return {"Model": "DeepSeek 4 Pro", "Description": "This is a model create by DeepSeek"}
"" python ""