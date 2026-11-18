---
bump: patch
title: Point updates and publishing at the custom fork
---
## vi
### Cải thiện
- **Toàn bộ cơ chế cập nhật và phát hành trỏ về repo riêng `ncthanh3290-del/Javis_OS_custom`.**
  Kiểm tra bản mới, image Docker trên GHCR, link docs trong dashboard, URL tải bản cài desktop,
  nhãn image trong compose, CODEOWNERS: cùng một repo thay vì repo gốc `blogminhquy/javis-os`.
  Bấm "Cập nhật" trong app giờ kiểm và kéo từ image của repo riêng; muốn nhận tính năng từ bản
  gốc thì `git fetch upstream` + cherry-pick thủ công.
- **Bỏ các file dữ liệu chạy khỏi git** (`.gitignore` + untrack): sqlite3 trạng thái, cache,
  checkpoint, export não, PID, share link. Cú `git add -A` sau này không còn dính dữ liệu chạy.

## en
### Improved
- **The whole update and release machinery points at the custom fork
  `ncthanh3290-del/Javis_OS_custom`.** New-version checks, the GHCR Docker image, doc links in
  the dashboard, desktop installer download URLs, compose image labels, CODEOWNERS: one repo
  instead of the original `blogminhquy/javis-os`. The in-app "Update" button now checks and
  pulls this fork's image; picking up features from upstream is `git fetch upstream` plus a
  manual cherry-pick.
- **Runtime data files are out of git** (`.gitignore` + untrack): state sqlite3 databases,
  caches, checkpoints, brain exports, PID and share-link files. A later `git add -A` no longer
  commits runtime data.
