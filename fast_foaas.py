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


def dalton(name: str, from_name: str) -> str:
    return f"{name}: A fucking problem solving super-hero. - {from_name}"


def dense(from_name: str) -> str:
    return f"You disingenuous dense motherfucker! - {from_name}"


def deraadt(name: str, from_name: str) -> str:
    return f"{name} you are being the usual slimy hypocritical asshole... You may have had value ten years ago, but people will see that you don't anymore. - {from_name}"


def diabetes(from_name: str) -> str:
    return f"I'd love to stop and chat to you but I'd rather have type 2 diabetes. - {from_name}"


def donut(name: str, from_name: str) -> str:
    return (
        f"{name}, go and take a flying fuck at a rolling donut. - {from_name}"
    )


def dosomething(do: str, something: str, from_name: str) -> str:
    return f"{do} the fucking {something}! - {from_name}"


def dumbledore(from_name: str) -> str:
    return f"Happiness can be found, even in the darkest of times, if one only remembers to fuck off. - {from_name}"


def equity(name: str, from_name: str) -> str:
    return f"Equity only? Long hours? Zero Pay? Well {name}, just sign me right the fuck up. - {from_name}"


def even(from_name: str) -> str:
    return f"I can't fuckin' even. - {from_name}"


def everyone(from_name: str) -> str:
    return f"Everyone can go and fuck off. - {from_name}"


def everything(from_name: str) -> str:
    return f"Fuck everything. - {from_name}"


def family(from_name: str) -> str:
    return f"Fuck you, your whole family, your pets, and your feces. - {from_name}"


def fascinating(from_name: str) -> str:
    return f"Fascinating story, in what chapter do you shut the fuck up? - {from_name}"


def fewer(name: str, from_name: str) -> str:
    return f"Go fuck yourself {name}, you'll disappoint fewer people. - {from_name}"


def field(name: str, from_name: str, reference: str) -> str:
    return f"And {name} said unto {from_name}, 'Verily, cast thine eyes upon the field in which I grow my fucks', and {from_name} gave witness unto the field, and saw that it was barren. - {reference}"


def flying(from_name: str) -> str:
    return f"I don't give a flying fuck. - {from_name}"


def ftfy(from_name: str) -> str:
    return f"Fuck That, Fuck You - {from_name}"


def fts(name: str, from_name: str) -> str:
    return f"Fuck that shit, {name}. - {from_name}"


def fyyff(from_name: str) -> str:
    return f"Fuck you, you fucking fuck. - {from_name}"


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
    "dalton",
    "dense",
    "deraadt",
    "diabetes",
    "donut",
    "dosomething",
    "dumbledore",
    "equity",
    "even",
    "everyone",
    "everything",
    "family",
    "fascinating",
    "fewer",
    "field",
    "flying",
    "ftfy",
    "fts",
    "fyyff",
]
__version__ = "2.2.0"
