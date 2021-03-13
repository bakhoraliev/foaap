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


def because(from_name: str) -> str:
    return f"Why? Because fuck you, that's why. - {from_name}"


def blackadder(name: str, from_name: str) -> str:
    return f"{name}, your head is as empty as a eunuch’s underpants. Fuck off! - {from_name}"


def bm(name: str, from_name: str) -> str:
    return f"Bravo mike, {name}. - {from_name}"


def bucket(from_name: str) -> str:
    return f"Please choke on a bucket of cocks. - {from_name}"


def bus(name: str, from_name: str) -> str:
    return f"Christ on a bendy-bus, {name}, don't be such a fucking faff-arse. - {from_name}"


def bye(from_name: str) -> str:
    return f"Fuckity bye! - {from_name}"


def caniuse(tool: str, from_name: str) -> str:
    return f"Can you use {tool}? Fuck no! - {from_name}"


def chainsaw(name: str, from_name: str) -> str:
    return f"Fuck me gently with a chainsaw, {name}. Do I look like Mother Teresa? - {from_name}"


def cocksplat(name: str, from_name: str) -> str:
    return f"Fuck off {name}, you worthless cocksplat - {from_name}"


def cool(from_name: str) -> str:
    return f"Cool story, bro. - {from_name}"


def cup(from_name: str) -> str:
    return f"How about a nice cup of shut the fuck up? - {from_name}"


__all__ = [
    "anyway",
    "ashole",
    "awesome",
    "bag",
    "balmer",
    "back",
    "bday",
    "because",
    "blackadder",
    "bm",
    "bucket",
    "bus",
    "bye",
    "caniuse",
    "chainsaw",
    "cocksplat",
    "cool",
    "cup",
]
__version__ = "2.2.0"
