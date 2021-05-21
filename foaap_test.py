import foaap


def test_operations_in_all():
    operations = [
        operation for operation in dir(foaap) if "_" not in operation
    ]
    missed_operations = [
        operation for operation in operations if operation not in foaap.__all__
    ]
    if missed_operations:
        raise AssertionError(f"Miss {missed_operations} in __all__")


def test_anyway():
    assert (
        foaap.anyway("LM", "Sam")
        == "Who the fuck are you anyway, LM, why are you stirring up so much trouble, and, who pays you? - Sam"
    )


def test_ashole():
    assert foaap.ashole("Sam") == "Fuck you, asshole. - Sam"


def test_awesome():
    assert foaap.awesome("Sam") == "This is Fucking Awesome. - Sam"


def test_bag():
    assert foaap.bag("Sam") == "Eat a bag of fucking dicks. - Sam"


def test_balmer():
    assert (
        foaap.balmer("John", "LM", "Sam")
        == "Fucking John is a fucking pussy. I'm going to fucking bury that guy, I have done it before, and I will do it again. I'm going to fucking kill LM. - Sam"
    )


def test_back():
    assert foaap.back("John", "Sam") == "John, back the fuck off. - Sam"


def test_bday():
    assert foaap.bday("John", "Sam") == "Happy Fucking Birthday, John. - Sam"


def test_because():
    assert foaap.because("Sam") == "Why? Because fuck you, that's why. - Sam"


def test_blackadder():
    assert (
        foaap.blackadder("John", "Sam")
        == "John, your head is as empty as a eunuch’s underpants. Fuck off! - Sam"
    )


def test_bm():
    assert foaap.bm("John", "Sam") == "Bravo mike, John. - Sam"


def test_bucket():
    assert foaap.bucket("Sam") == "Please choke on a bucket of cocks. - Sam"


def test_bus():
    assert (
        foaap.bus("John", "Sam")
        == "Christ on a bendy-bus, John, don't be such a fucking faff-arse. - Sam"
    )


def test_bye():
    assert foaap.bye("Sam") == "Fuckity bye! - Sam"


def test_caniuse():
    assert foaap.caniuse("FOAAS", "Sam") == "Can you use FOAAS? Fuck no! - Sam"


def test_chainsaw():
    assert (
        foaap.chainsaw("John", "Sam")
        == "Fuck me gently with a chainsaw, John. Do I look like Mother Teresa? - Sam"
    )


def test_cocksplat():
    assert (
        foaap.cocksplat("John", "Sam")
        == "Fuck off John, you worthless cocksplat - Sam"
    )


def test_cool():
    assert foaap.cool("Sam") == "Cool story, bro. - Sam"


def test_cup():
    assert (
        foaap.cup("Sam") == "How about a nice cup of shut the fuck up? - Sam"
    )


def test_dalton():
    assert (
        foaap.dalton("John", "Sam")
        == "John: A fucking problem solving super-hero. - Sam"
    )


def test_dense():
    assert foaap.dense("Sam") == "You disingenuous dense motherfucker! - Sam"


def test_deraadt():
    assert (
        foaap.deraadt("John", "Sam")
        == "John you are being the usual slimy hypocritical asshole... You may have had value ten years ago, but people will see that you don't anymore. - Sam"
    )


def test_diabetes():
    assert (
        foaap.diabetes("Sam")
        == "I'd love to stop and chat to you but I'd rather have type 2 diabetes. - Sam"
    )


def test_donut():
    assert (
        foaap.donut("John", "Sam")
        == "John, go and take a flying fuck at a rolling donut. - Sam"
    )


def test_dosomething():
    assert (
        foaap.dosomething("Write", "test", "Sam")
        == "Write the fucking test! - Sam"
    )


def test_dumbledore():
    assert (
        foaap.dumbledore("Sam")
        == "Happiness can be found, even in the darkest of times, if one only remembers to fuck off. - Sam"
    )


def test_equity():
    assert (
        foaap.equity("John", "Sam")
        == "Equity only? Long hours? Zero Pay? Well John, just sign me right the fuck up. - Sam"
    )


def test_even():
    assert foaap.even("Sam") == "I can't fuckin' even. - Sam"


def test_everyone():
    assert foaap.everyone("Sam") == "Everyone can go and fuck off. - Sam"


def test_everything():
    assert foaap.everything("Sam") == "Fuck everything. - Sam"


def test_family():
    assert (
        foaap.family("Sam")
        == "Fuck you, your whole family, your pets, and your feces. - Sam"
    )


def test_fascinating():
    assert (
        foaap.fascinating("Sam")
        == "Fascinating story, in what chapter do you shut the fuck up? - Sam"
    )


def test_fewer():
    assert (
        foaap.fewer("John", "Sam")
        == "Go fuck yourself John, you'll disappoint fewer people. - Sam"
    )


def test_field():
    assert (
        foaap.field("John", "Sam", "Lui")
        == "And John said unto Sam, 'Verily, cast thine eyes upon the field in which I grow my fucks', and Sam gave witness unto the field, and saw that it was barren. - Lui"
    )


def test_flying():
    assert foaap.flying("Sam") == "I don't give a flying fuck. - Sam"


def test_ftfy():
    assert foaap.ftfy("Sam") == "Fuck That, Fuck You - Sam"


def test_fts():
    assert foaap.fts("John", "Sam") == "Fuck that shit, John. - Sam"


def test_fyyff():
    assert foaap.fyyff("Sam") == "Fuck you, you fucking fuck. - Sam"


def test_gfy():
    assert foaap.gfy("John", "Sam") == "Golf foxtrot yankee, John. - Sam"


def test_give():
    assert foaap.give("Sam") == "I give zero fucks. - Sam"


def test_greed():
    assert (
        foaap.greed("cookie", "Sam")
        == "The point is, ladies and gentleman, that cookie -- for lack of a better word -- is good. cookie is right. cookie works. cookie clarifies, cuts through, and captures the essence of the evolutionary spirit. cookie, in all of its forms -- cookie for life, for money, for love, knowledge -- has marked the upward surge of mankind. - Sam"
    )


def test_holygrail():
    assert (
        foaap.holygrail("Sam")
        == "I don't want to talk to you, no more, you empty-headed animal, food trough wiper. I fart in your general direction. Your mother was a hamster and your father smelt of elderberries. Now go away or I shall taunt you a second time. - Sam"
    )


def test_horse():
    assert foaap.horse("Sam") == "Fuck you and the horse you rode in on. - Sam"


def test_idea():
    assert foaap.idea("Sam") == "That sounds like a fucking great idea! - Sam"


def test_immensity():
    assert (
        foaap.immensity("Sam")
        == "You can not imagine the immensity of the FUCK I do not give. - Sam"
    )


def test_ing():
    assert foaap.ing("John", "Sam") == "Fucking fuck off, John. - Sam"


def test_jinglebells():
    assert (
        foaap.jinglebells("Sam")
        == "Fuck you, fuck me, fuck your family. Fuck your father, fuck your mother, fuck you and me. - Sam"
    )


def test_keep():
    assert (
        foaap.keep("John", "Sam")
        == "John: Fuck off. And when you get there, fuck off from there too. Then fuck off some more. Keep fucking off until you get back here. Then fuck off again. - Sam"
    )


def test_keepcalm():
    assert (
        foaap.keepcalm("write tests", "Sam")
        == "Keep the fuck calm and write tests! - Sam"
    )


def test_king():
    assert (
        foaap.king("John", "Sam")
        == "Oh fuck off, just really fuck off you total dickface. Christ, John, you are fucking thick. - Sam"
    )


def test_legend():
    assert (
        foaap.legend("John", "Sam") == "John, you're a fucking legend. - Sam"
    )


def test_life():
    assert foaap.life("Sam") == "Fuck my life. - Sam"


def test_linus():
    assert (
        foaap.linus("John", "Sam")
        == "John, there aren't enough swear-words in the English language, so now I'll have to call you perkeleen vittupää just to express my disgust and frustration with this crap. - Sam"
    )


def test_logs():
    assert foaap.logs("Sam") == "Check your fucking logs! - Sam"


def test_look():
    assert (
        foaap.look("John", "Sam")
        == "John, do I look like I give a fuck? - Sam"
    )


def test_looking():
    assert foaap.looking("Sam") == "Looking for a fuck to give. - Sam"


def test_lowpoly():
    assert foaap.lowpoly("Sam") == "You low polygon motherfucker! - Sam"


def test_madison():
    assert (
        foaap.madison("John", "Sam")
        == "What you've just said is one of the most insanely idiotic things I have ever heard, John. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having listened to it. I award you no points :name, and may God have mercy on your soul. - Sam"
    )


def test_maybe():
    assert foaap.maybe("Sam") == "Maybe. Maybe not. Maybe fuck yourself. - Sam"


def test_me():
    assert foaap.me("Sam") == "Fuck me. - Sam"


def test_mornin():
    assert foaap.mornin("Sam") == "Happy fuckin' mornin'! - Sam"


def test_no():
    assert foaap.no("Sam") == "No fucks given. - Sam"


def test_nugget():
    assert (
        foaap.nugget("John", "Sam")
        == "Well John, aren't you a shining example of a rancid fuck-nugget. - Sam"
    )


def test_off():
    assert foaap.off("John", "Sam") == "Fuck off, John. - Sam"


def test_off_with():
    assert foaap.off_with("love", "Sam") == "Fuck off with love - Sam"


def test_outside():
    assert (
        foaap.outside("John", "Sam")
        == "John, why don't you go outside and play hide-and-go-fuck-yourself? - Sam"
    )


def test_particular():
    assert (
        foaap.particular("cookie", "Sam")
        == "Fuck this cookie in particular. - Sam"
    )


def test_pink():
    assert foaap.pink("Sam") == "Well, fuck me pink. - Sam"


def test_problem():
    assert (
        foaap.problem("John", "Sam")
        == "What the fuck is your problem John? - Sam"
    )


def test_programmer():
    assert (
        foaap.programmer("Sam") == "Fuck you, I'm a programmer, bitch! - Sam"
    )


def test_pulp():
    assert (
        foaap.pulp("English", "Sam")
        == "English, motherfucker, do you speak it? - Sam"
    )


def test_question():
    assert (
        foaap.question("Sam")
        == "To fuck off, or to fuck off (that is not a question) - Sam"
    )


def test_ratsarse():
    assert foaap.ratsarse("Sam") == "I don't give a rat's arse. - Sam"


def test_retard():
    assert foaap.retard("Sam") == "You Fucktard! - Sam"


def test_ridiculous():
    assert foaap.ridiculous("Sam") == "That's fucking ridiculous - Sam"


def test_rockstar():
    assert (
        foaap.rockstar("John", "Sam")
        == "John, you're a fucking Rock Star! - Sam"
    )


def test_rtfm():
    assert foaap.rtfm("Sam") == "Read the fucking manual! - Sam"


def test_sake():
    assert foaap.sake("Sam") == "For Fuck's sake! - Sam"


def test_shakespeare():
    assert (
        foaap.shakespeare("John", "Sam")
        == "John, Thou clay-brained guts, thou knotty-pated fool, thou whoreson obscene greasy tallow-catch! - Sam"
    )


def test_shit():
    assert foaap.shit("Sam") == "Fuck this shit! - Sam"


def test_shutup():
    assert foaap.shutup("John", "Sam") == "John, shut the fuck up. - Sam"


def test_single():
    assert foaap.single("Sam") == "Not a single fuck was given. - Sam"


def test_thanks():
    assert foaap.thanks("Sam") == "Fuck you very much. - Sam"


def test_that():
    assert foaap.that("Sam") == "Fuck that. - Sam"


def test_think():
    assert foaap.think("John", "Sam") == "John, you think I give a fuck? - Sam"


def test_thinking():
    assert (
        foaap.thinking("John", "Sam")
        == "John, what the fuck were you actually thinking? - Sam"
    )


def test_this():
    assert foaap.this("Sam") == "Fuck this. - Sam"


def test_thumbs():
    assert (
        foaap.thumbs("John", "Sam")
        == "Who has two thumbs and doesn't give a fuck? John. - Sam"
    )


def test_too():
    assert foaap.too("Sam") == "Thanks, fuck you too. - Sam"


def test_tucker():
    assert (
        foaap.tucker("Sam") == "Come the fuck in or fuck the fuck off. - Sam"
    )


def test_understand():
    assert (
        foaap.understand("John", "Sam")
        == "Listen here John! What part of 'Fuck Off' don't you understand? - Sam"
    )


def test_waste():
    assert (
        foaap.waste("John", "Sam")
        == "I don't waste my fucking time with your bullshit John! - Sam"
    )


def test_what():
    assert foaap.what("Sam") == "What the fuck‽ - Sam"


def test_xmas():
    assert foaap.xmas("John", "Sam") == "Merry Fucking Christmas, John. - Sam"


def test_yeah():
    assert foaap.yeah("Sam") == "Fuck YEAH! - Sam"


def test_yoda():
    assert foaap.yoda("John", "Sam") == "Fuck off, you must, John. - Sam"


def test_you():
    assert foaap.you("John", "Sam") == "Fuck you, John. - Sam"


def test_zayn():
    assert foaap.zayn("Sam") == "Ask me if I give a motherfuck ?!! - Sam"


def test_zero():
    assert (
        foaap.zero("Sam") == "Zero, that's the number of fucks I give. - Sam"
    )
