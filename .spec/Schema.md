# Data Models & Schemas (Schema.md)
## Project: MOM

### 1. Core State Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MOMState",
  "type": "object",
  "required": ["sessionId", "timestamp", "status"],
  "properties": {
    "sessionId": { "type": "string" },
    "timestamp": { "type": "integer" },
    "status": { "type": "string", "enum": ["IDLE", "RUNNING", "VERIFIED", "FAILED"] }
  }
}
```
