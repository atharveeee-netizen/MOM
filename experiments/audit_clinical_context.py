import re

with open('generate_stage1_proposal.py', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'([^.\n]*?clinical[^.\n]*)', text, re.IGNORECASE)
print("=== CLINICAL CONTEXT INSPECTION ===")
for i, m in enumerate(matches):
    print(f"{i+1}: {m.group(0).strip()}")
