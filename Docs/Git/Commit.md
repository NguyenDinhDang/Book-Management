# Cách viết commit chuẩn
Format phổ biến nhất: Conventional Commits
<type>(<scope>): <mô tả ngắn>

<mô tả chi tiết (optional)>

<footer (optional, VD: breaking change, closes #issue)>

## Type thường dùng:

Type	           Ý nghĩa
feat	           thêm tính năng mới
fix	               sửa bug
docs	           chỉ sửa docs (README, comment)
refactor	       sửa code nhưng không đổi hành vi
style	           format, dấu cách, không ảnh hưởng logic
test	           thêm/sửa test
chore	           việc lặt vặt (update dependency, config)
perf	           cải thiện performance

## Ví dụ thực tế cho dự án của bạn:

* feat(api): add POST /books endpoint for creating new book

* fix(db): correct date format in ngay_doc_xong column

* docs(readme): update tech stack section to separate learning goals

* refactor(service): move book creation logic from router to service layer

* chore(docker): add postgres service to docker-compose

## Nguyên tắc viết message tốt
* Dòng đầu ≤ 50 ký tự, viết ở thì mệnh lệnh: "add" không phải "added" hay "adds" (tưởng tượng câu "This commit will... add X")
* Một commit = một thay đổi logic — đừng gộp "fix bug + thêm feature + sửa README" vào 1 commit
* Dòng đầu không chấm câu cuối
* Nếu cần giải thích tại sao (không phải cái gì), viết ở phần mô tả chi tiết bên dưới, cách dòng đầu 1 dòng trống
## Sai lầm thường gặp cần tránh
* "update", "fix bug", "asdf" — không nói được gì
* Commit quá to gộp nhiều ngày làm việc — khó review, khó revert
* Commit code chưa chạy được (nên: mỗi commit ít nhất phải build/chạy được)