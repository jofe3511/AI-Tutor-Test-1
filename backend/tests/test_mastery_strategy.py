from backend.mastery.strategy import MasteryInputs, SimpleWeightedMasteryStrategy


def test_simple_weighted_mastery_strategy() -> None:
    strategy = SimpleWeightedMasteryStrategy()

    result = strategy.calculate(
        MasteryInputs(
            recent_practice=0.8,
            assessment_performance=0.6,
            prior_mastery=0.5,
        )
    )

    assert result == 0.66
