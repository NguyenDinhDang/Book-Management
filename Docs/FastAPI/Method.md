# Phương thức và đường dẫn của dự án 
Thông thường bạn sử dụng:
POST:   Để tạo dữ liệu.
GET:    để đọc dữ liệu.
PUT:    Cập nhật dữ liệu.
DELETE: xóa dữ liệu.

## Khởi động dự án:
App = FastAPI(title = "My project")

## Đường dẫn 
Url ("/user") == https://example/user
Url: ("/user/{user_id}) == https://example/user/1

## Phương thức 
Các phương thức này giao tiếp với nhau bằng http :

@app.get("/") báo cho swagger biết sẽ lấy và đọc dữ liệu 
@app.post("/") Báo cho swagger biết sẽ tạo 1 dữ liệu như user hay book 
@app.put("/") Báo cho swagger biết sẽ cập nhật user/sách 
@app.delete ("/") báo cho swagger biết sẽ xoá 1 dữ liệu nào đó như user hay book

