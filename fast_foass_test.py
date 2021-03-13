import fast_foaas


def test_operations_in_all():
    assert len([x for x in dir(fast_foaas) if "_" not in x]) == len(
        fast_foaas.__all__
    )


def test_anyway():
    assert (
        fast_foaas.anyway("LM", "Sam")
        == "Who the fuck are you anyway, LM, why are you stirring up so much trouble, and, who pays you? - Sam"
    )


def test_ashole():
    assert fast_foaas.ashole("Sam") == "Fuck you, asshole. - Sam"


def test_awesome():
    assert fast_foaas.awesome("Sam") == "This is Fucking Awesome. - Sam"


def test_bag():
    assert fast_foaas.bag("Sam") == "Eat a bag of fucking dicks. - Sam"


def test_balmer():
    assert (
        fast_foaas.balmer("John", "LM", "Sam")
        == "Fucking John is a fucking pussy. I'm going to fucking bury that guy, I have done it before, and I will do it again. I'm going to fucking kill LM. - Sam"
    )


def test_back():
    assert fast_foaas.back("John", "Sam") == "John, back the fuck off. - Sam"
