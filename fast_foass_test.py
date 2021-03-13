import fast_foaas


def test_anyway():
    assert (
        fast_foaas.anyway("LM", "Sam")
        == "Who the fuck are you anyway, LM, why are you stirring up so much trouble, and, who pays you? - Sam"
    )


def test_ashole():
    assert fast_foaas.ashole("Sam") == "Fuck you, asshole. - Sam"
