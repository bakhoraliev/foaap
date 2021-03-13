"""Faster version of FOAAS"""


def anyway(company: str, name: str) -> str:
    return f"Who the fuck are you anyway, {company}, why are you stirring up so much trouble, and, who pays you? - {name}"


def ashole(name: str) -> str:
    return f"Fuck you, asshole. - {name}"


def awesome(name: str) -> str:
    return f"This is Fucking Awesome. - {name}"


__all__ = ["anyway", "ashole", "awesome"]
__version__ = "2.2.0"
