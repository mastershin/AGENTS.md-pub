# Rust

Put lints in `Cargo.toml` / `clippy.toml`, not only in chat. Add those files if missing, then use them.

- **Toolchain:** latest **stable** via `rustup`, or the org-pinned stable. Do not use nightly in production without an explicit waiver.
- **Tools:** `cargo`, `clippy`, `fmt`, `test`; `cargo deny check` (advisories, licenses, bans); `cargo careful test` for unsafe, parsers, and FFI.
- **Types:** newtypes over primitives; enums for state machines; `thiserror` in libs; `anyhow` in bins; `tracing` for logs.
- **Clippy (library code):** deny `unwrap_used`, `panic`, `todo`, `unimplemented`, `dbg_macro`, `allow_attributes`, `await_holding_lock`, `mem_forget`, `exit`. `expect` MAY be used with a message in bins and tests.
- **`print_stdout` / `print_stderr` MUST NOT be denied on CLI crates.**
- Profile before micro-optimizing. Write clear, allocation-honest code first.
- **Do not** `unsafe` without a safety comment next to the block and tests that exercise it.
