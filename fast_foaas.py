"""Faster version of FOAAS"""


def anyway(company: str, from_name: str) -> str:
    return f"Who the fuck are you anyway, {company}, why are you stirring up so much trouble, and, who pays you? - {from_name}"


def ashole(from_name: str) -> str:
    return f"Fuck you, asshole. - {from_name}"


def awesome(from_name: str) -> str:
    return f"This is Fucking Awesome. - {from_name}"


def bag(from_name: str) -> str:
    return f"Eat a bag of fucking dicks. - {from_name}"


def balmer(name: str, company, from_name: str):
    return f"Fucking {name} is a fucking pussy. I'm going to fucking bury that guy, I have done it before, and I will do it again. I'm going to fucking kill {company}. - {from_name}"


def back(name: str, from_name: str) -> str:
    return f"{name}, back the fuck off. - {from_name}"


def bday(name: str, from_name: str) -> str:
    return f"Happy Fucking Birthday, {name}. - {from_name}"


__all__ = ["anyway", "ashole", "awesome", "bag", "balmer", "back", "bday"]
__version__ = "2.2.0"
