"""Faster version of FOAAS"""


def anyway(company: str, from_name: str) -> str:
    return f"Who the fuck are you anyway, {company}, why are you stirring up so much trouble, and, who pays you? - {from_name}"


def ashole(from_name: str) -> str:
    return f"Fuck you, asshole. - {from_name}"


def awesome(from_name: str) -> str:
    return f"This is Fucking Awesome. - {from_name}"


def back(name: str, from_name: str) -> str:
    return f"{name}, back the fuck off. - {from_name}"


__all__ = ["anyway", "ashole", "awesome", "back"]
__version__ = "2.2.0"
