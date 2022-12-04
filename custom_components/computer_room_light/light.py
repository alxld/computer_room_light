"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = ComputerRoomLight()
    add_entities([ent])


class ComputerRoomLight(NewLight):
    """Computer Room Light."""

    def __init__(self) -> None:
        """Initialize Computer Room Light."""
        super(ComputerRoomLight, self).__init__(
            "Computer Room", domain=DOMAIN, debug=True, debug_rl=False
        )

        self.entities["light.computer_room_group"] = None
        self.other_light_trackers["light.mudroom_low_group"] = 0
        self.other_light_trackers["light.living_room_lamps_group"] = 0
        self.track_other_light_off_events = True
