# Used by:
# Ships from group: Logistics (3 of 5)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Transfer Array",
                                  "power", ship.getModifiedItemAttr("powerTransferPowerNeedBonus"))