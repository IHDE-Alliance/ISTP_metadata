def preserve_underscores(text: str) -> str:
    """Safely converts spaces to underscores while leaving existing underscores alone."""
    # Convert text to standard string, make lowercase, replace spaces
    slug = str(text).lower().replace(" ", "_")
    # Clean out bad characters but leave alphanumeric, hyphens, and underscores
    return "".join(c for c in slug if c.isalnum() or c in ("_", "-"))