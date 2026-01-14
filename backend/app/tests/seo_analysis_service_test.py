from app.services.seo_analysis_service import analyze_seo

def test_perfect_seo_score():
    metrics = {
        "title": "Test Page",
        "meta_description": "A description",
        "h1_count": 1,
        "images_missing_alt": 0,
    }

    score, issues = analyze_seo(metrics)

    assert score == 100
    assert issues == []


def test_missing_meta_and_title():
    metrics = {
        "title": None,
        "meta_description": None,
        "h1_count": 1,
        "images_missing_alt": 0,
    }

    score, issues = analyze_seo(metrics)

    assert score < 100
    assert 100 - score == 30
    assert "Missing page title" in issues
    assert "Missing meta description" in issues
