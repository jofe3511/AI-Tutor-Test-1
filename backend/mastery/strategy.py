from dataclasses import dataclass


@dataclass(frozen=True)
class MasteryInputs:
    recent_practice: float
    assessment_performance: float
    prior_mastery: float


class SimpleWeightedMasteryStrategy:
    """Interpretable MVP mastery strategy.

    This class exists behind a small interface-shaped API so it can later be
    replaced with Bayesian Knowledge Tracing, IRT, or another model.
    """

    def calculate(self, inputs: MasteryInputs) -> float:
        score = (
            0.4 * inputs.recent_practice
            + 0.4 * inputs.assessment_performance
            + 0.2 * inputs.prior_mastery
        )
        return round(max(0.0, min(1.0, score)), 3)
