import re

with open('generate_stage1_proposal.py', 'r', encoding='utf-8') as f:
    text = f.read()

keywords = [
    'medical-grade', '99%', 'world\'s first', 'first ever', 'revolutionary', 'breakthrough',
    'production AI', 'deployed on nRF52840', 'clinically validated AI', 'hospital trial', 'patient trial'
]

print("=== BUZZWORD RED-TEAM AUDIT ===")
for kw in keywords:
    matches = re.findall(rf'.{{0,40}}{re.escape(kw)}.{{0,40}}', text, re.IGNORECASE)
    print(f'Keyword: "{kw}" -> Matches: {len(matches)}')
    for m in matches[:3]:
        print(f'   [SNIPPET] {m.strip()}')

# Check occurrences of clinical, patient, battery, cost, accuracy
core_terms = ['clinical', 'accuracy', 'battery', 'cost', 'AI', 'nRF52840', 'FHR']
print("\n=== CORE TERMS FREQUENCY & CONTEXT ===")
for term in core_terms:
    count = len(re.findall(rf'\b{re.escape(term)}\b', text, re.IGNORECASE))
    print(f'Term: "{term}" -> Occurrences: {count}')
