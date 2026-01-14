from typing import Dict, List, Tuple

MAX_SCORE = 100

def analyze_seo(metrics: Dict) -> Tuple[int, List[str]]:
    score = MAX_SCORE
    issues: List[str] = []

    if not metrics.get("title"):
        score -= 15
        issues.append("Missing page title")

    if not metrics.get("meta_description"):
        score -= 15
        issues.append("Missing meta description")

    h1_count = metrics.get("h1_count", 0)
    if h1_count == 0:
        score -= 10
        issues.append("No H1 tag found")
    elif h1_count > 1:
        score -= 5
        issues.append("Multiple H1 tags detected")

    missing_alt = metrics.get("images_missing_alt", 0)
    if missing_alt > 0:
        penalty = min(20, missing_alt * 2)
        score -= penalty
        issues.append(f"{missing_alt} images missing alt attributes")

    return max(score, 0), issues
