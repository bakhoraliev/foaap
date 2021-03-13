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
