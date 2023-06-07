import esphome.codegen as cg
from esphome.const import CONF_ID
import esphome.config_validation as cv

from esphome.components import cover
from .. import (
    ratgdo_ns,
    RATGDO,
    register_ratgdo_child,
    RATGDO_CLIENT_SCHMEA
)

DEPENDENCIES = ["ratgdo"]

RATGDOCover = ratgdo_ns.class_(
    "RATGDOCover", cover.Cover, cg.Component
)


CONFIG_SCHEMA = cover.COVER_SCHEMA.extend({cv.GenerateID(): cv.declare_id(RATGDOCover)}).extend(RATGDO_CLIENT_SCHMEA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cover.register_cover(var, config)
    await cg.register_component(var, config)
    await register_ratgdo_child(var, config)