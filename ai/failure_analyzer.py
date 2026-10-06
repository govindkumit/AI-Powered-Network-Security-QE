"""Provider-neutral AI failure-analysis adapter.

Replace analyze() with an Ollama/local-LLM call when desired.
No cloud API key is required for the demo repository.
"""

def analyze(failure: str) -> dict:
    text = failure.lower()
    if '500' in text or 'internal server error' in text:
        category = 'Application defect'
        priority = 'High'
    elif 'timeout' in text:
        category = 'Reliability / dependency issue'
        priority = 'High'
    else:
        category = 'Test or functional failure'
        priority = 'Medium'
    return {
        'category': category,
        'priority': priority,
        'recommended_action': 'Review logs, reproduce independently, and add a regression test.'
    }
