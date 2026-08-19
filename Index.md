---
share: true
---

```dataview
LIST rows.file.link
FROM "Learn"
WHERE file.tags
FLATTEN file.tags as tag
GROUP BY tag
```