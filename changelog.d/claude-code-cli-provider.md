---
bump: minor
title: New Claude Code CLI card: run the official claude through your own endpoint and key
---
## vi
### Thêm mới
- **Thẻ "Claude Code CLI" mới ở trang Models.** Nhập tên, Base URL và API key của một tổng đài
  nói chuẩn API của Anthropic (9router chạy trên máy...) là binary `claude` bản chính thức chạy
  qua đó, giống phương thức của thẻ Codex CLI. Giữ nguyên toàn bộ năng lực CLI: shell, tool của
  Claude Code, MCP của Javis, nối tiếp phiên đã lưu; đăng nhập Claude ở ~/.claude không bị đụng
  tới. Javis tự đọc danh sách model của tổng đài, kiểm tra kết nối trước khi lưu, và tự hạ về
  thẻ khác khi thẻ này không chạy được.

## en
### Added
- **A new "Claude Code CLI" card on the Models page.** Enter a name, a Base URL and an API key of
  any Anthropic-format gateway (a local 9router...) and the official `claude` binary runs through
  it, the same method as the Codex CLI card. Full CLI power: native shell, Claude Code's own
  tools, the Javis hub, saved sessions resume; your Claude sign-in at ~/.claude is untouched.
  Javis reads the gateway's model list, checks the connection before saving, and falls back to
  the next card when this one cannot run.
