from typing import Dict, Any, List
from refiner.models.refined import Base
from refiner.transformer.base_transformer import DataTransformer
from refiner.models.refined import MindCheckRefined
from refiner.models.unrefined import MindCheck
from datetime import datetime


class MindCheckTransformer(DataTransformer):
    """
    Transformer for mind check data.
    """

    def transform(self, data: Dict[str, Any]) -> List[Base]:
        """
        Transform raw mind check data into SQLAlchemy model instances.

        Args:
            data: Dictionary containing mind check data

        Returns:
            List of SQLAlchemy model instances
        """
        # Validate data with Pydantic
        unrefined_mind = MindCheck.model_validate(data)

        # Create mind check instance
        mind_check = MindCheckRefined(
            # PANAS ratings
            interested=unrefined_mind.panas.interested,
            distressed=unrefined_mind.panas.distressed,
            excited=unrefined_mind.panas.excited,
            upset=unrefined_mind.panas.upset,
            strong=unrefined_mind.panas.strong,
            guilty=unrefined_mind.panas.guilty,
            scared=unrefined_mind.panas.scared,
            hostile=unrefined_mind.panas.hostile,
            enthusiastic=unrefined_mind.panas.enthusiastic,
            proud=unrefined_mind.panas.proud,
            irritable=unrefined_mind.panas.irritable,
            alert=unrefined_mind.panas.alert,
            ashamed=unrefined_mind.panas.ashamed,
            inspired=unrefined_mind.panas.inspired,
            nervous=unrefined_mind.panas.nervous,
            determined=unrefined_mind.panas.determined,
            attentive=unrefined_mind.panas.attentive,
            jittery=unrefined_mind.panas.jittery,
            active=unrefined_mind.panas.active,
            afraid=unrefined_mind.panas.afraid,
            # Free text responses
            best_thing=unrefined_mind.bestThing,
            worst_thing=unrefined_mind.worstThing,
            # Demographic information
            location=unrefined_mind.location.value,
            race_ethnicity=unrefined_mind.raceEthnicity.value,
            gender_identity=unrefined_mind.genderIdentity.value,
            # Metadata
            created_at=datetime.utcnow(),
        )

        return [mind_check]
