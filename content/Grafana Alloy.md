---
title: Grafana Alloy
date: 2026-04-15
tags:
  - monitoring
  - tooling
share: true
---

### HTTP static endpoint discovery

You can define static [http](https://grafana.com/docs/alloy/latest/reference/components/discovery/discovery.http/) endpoint for discovery of targets. 

```
        discovery.http "va" {
          url = "https://nexus3.indexexchange.com/repository/blackbox_targets/VA_targets_icmp.json"
        }
```

## Sources
- 
## Related
- [](%5D)
