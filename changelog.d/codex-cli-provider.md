---
bump: minor
title: New Codex CLI card: run the official Codex through your own endpoint and key
---
## vi
### Thêm mới
- **Thẻ "Codex CLI" mới ở trang Models.** Nhập tên, Base URL và API key của một cổng tự khai
  (9router chạy trên máy, LiteLLM, proxy xoay key...) là Codex bản chính thức chạy qua cổng đó,
  giống phương thức của thẻ OpenAI Compatible nhưng giữ nguyên toàn bộ năng lực CLI: shell, tool
  của Codex, MCP của Javis, không cần đăng nhập ChatGPT. Javis tự đọc danh sách model của cổng,
  kiểm tra kết nối trước khi lưu, và tự hạ về thẻ khác khi thẻ này không chạy được.

## en
### Added
- **A new "Codex CLI" card on the Models page.** Enter a name, a Base URL and an API key of any
  OpenAI-format gateway (a local 9router, LiteLLM, a key-rotating proxy...) and the official
  Codex CLI runs through it, the same method as the OpenAI Compatible card while keeping the full
  CLI power: native shell, Codex's own tools, the Javis hub, no ChatGPT sign-in needed. Javis
  reads the gateway's model list, checks the connection before saving, and falls back to the next
  card when this one cannot run.
