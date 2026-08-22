---
trigger: glob
description: Rust stable toolchain, Clippy policy, and cargo deny
globs:
  - "**/*.rs"
  - "**/Cargo.toml"
  - "**/Cargo.lock"
  - "**/clippy.toml"
  - "**/rust-toolchain.toml"
  - "**/deny.toml"
---

@../../rules/rust.md
