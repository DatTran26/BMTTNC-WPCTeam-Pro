# Formatting Audit

## Scope

Checked documentation and Postman files for broken character formatting and
mojibake markers.

Files reviewed:

- `readme.md`
- `lab_02/ex01_API/postman/postman-usage-guide.md`
- `lab_03/postman/postman-usage-guide.md`
- `lab_03/postman/*.postman_collection.json`

## Findings

- `readme.md` is stored as UTF-8. Vietnamese text may display incorrectly in
  a PowerShell session that is not configured for UTF-8, but Python UTF-8
  inspection did not find broken mojibake content in the file.
- `lab_02/ex01_API/postman/postman-usage-guide.md` uses ASCII-only Vietnamese
  without accents, so it is stable across terminals.
- `lab_03/postman/postman-usage-guide.md` also uses ASCII-only Vietnamese
  without accents.
- The latest Lab 03 Postman collection is now separated as:

```text
lab_03/postman/api-cipher-rsa-ecc.postman_collection.json
```

## Recommendations

- Keep English supplemental docs in `docs-en/`.
- Keep generated key folders ignored by Git.
- Prefer UTF-8 without BOM for Markdown and JSON files.
- In PowerShell, use UTF-8 output settings when viewing Vietnamese text.
