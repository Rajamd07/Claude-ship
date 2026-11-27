"""Legacy helpers. Frozen: do not change (enforced by Claude Approvals)."""


def slugify(text):
    return "-".join(text.lower().split())
