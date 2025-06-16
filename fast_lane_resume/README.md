# Fast-Lane Resume Builder Module (Free Tier)

## Function

```python
generate_resume(job_description: str, email: str, tier: str, uploaded_resume: Optional[str] = None) -> dict
```

## Outputs

Returns a dict with:
- `pdf_path`: Path to generated PDF resume
- `resume_text`: Text summary of resume
- `usage_info`: Tier, resumes remaining

## Requirements

- One resume per day for Free
- Ten for Premium
- Unlimited for Elite
- Email required
