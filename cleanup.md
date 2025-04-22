# Code Cleanup Plan for src_helix Scripts

This document outlines the remaining steps to clean up the Python and shell scripts in the `src_helix` directory, focusing on removing duplication, standardizing logging, and improving readability, based on the principles in `../my-globals/README-prompts.md`.

**Overall Goals:**

1.  Eliminate duplicated `get_api_token` and `create_template` functions by using the shared `src_helix.api_utils` module.
2.  Remove duplicated `VERKADA_API_BASE_URL` and `TOKEN_ENDPOINT` constants by importing them from `src_helix.api_utils`.
3.  Standardize logging configuration across all Python scripts using explicit handlers.
4.  Remove unused imports.
5.  Address any other identified code duplication or minor issues.

---

**Next Steps:**

All planned cleanup tasks are complete.
