import os
from main import generate_resume

def test_generate_valid_free():
    res = generate_resume("Engineer role", "valid@test.com", "free")
    assert "pdf_path" in res and res["usage_info"]["tier"] == "free"

def test_limit_rejection():
    for _ in range(2):
        res = generate_resume("Engineer role", "limited@test.com", "free")
    assert res.get("error") == "limit reached"

def test_invalid_input():
    res = generate_resume("", "user@test.com", "free")
    assert res.get("error") == "Job description is required."
