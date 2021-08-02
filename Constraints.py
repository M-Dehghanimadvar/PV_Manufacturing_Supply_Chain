from Sets_Parameters import *
# from Sensitivity import *

def Get_Previous_Month(month):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if month == "Jan":
        return None
    return months[months.index(month) - 1]


def International_Transport_In_Module(model, Supplier):
    """The amount of purchased Module should be equal to amount Module transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_module[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_module[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


model.International_Transport_In_Module_con = Constraint(model.Supplier, rule=International_Transport_In_Module)


def National_Transport_In_Module(model, port):
    """The amount of Module transport from potential_manufacturer to the market should be equal to the amount of Module received at the
    potential_manufacturer """
    return sum(model.international_transportation_input_solar_module[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_module[port, national_market, transportation_type]
               for national_market in model.national_market for transportation_type in
               model.transportation_type)


model.National_Transport_In_Module_con = Constraint(model.port, rule=National_Transport_In_Module)


def International_Transport_In_cell(model, Supplier):
    """The amount of purchased cell should be equal to amount cell transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_cell[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_cell[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


model.International_Transport_In_cell_con = Constraint(model.Supplier, rule=International_Transport_In_cell)


def National_Transport_In_cell(model, port):
    """The amount of cell transport from potential_manufacturer to the manufacturer should be equal to the amount of cell received at the
     potential_manufacturer"""
    return sum(model.international_transportation_input_solar_cell[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_cell[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


model.National_Transport_In_cell_con = Constraint(model.port, rule=National_Transport_In_cell)


def International_Transport_In_eva(model, Supplier):
    """The amount of purchased eva should be equal to amount eva transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_eva[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_eva[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


model.International_Transport_In_eva_con = Constraint(model.Supplier, rule=International_Transport_In_eva)


def National_Transport_In_eva(model, port):
    """The amount of eva transport from potential_manufacturer to the manufacturer should be equal to the amount of eva received at the
     potential_manufacturer"""
    return sum(model.international_transportation_input_solar_eva[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_eva[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


model.National_Transport_In_eva_con = Constraint(model.port, rule=National_Transport_In_eva)


def International_Transport_In_Al(model, Supplier):
    """The amount of purchased Al should be equal to amount Al transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_Al[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_Al[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


model.International_Transport_In_Al_con = Constraint(model.Supplier, rule=International_Transport_In_Al)


def National_Transport_In_Al(model, port):
    """The amount of Al transport from potential_manufacturer to the manufacturer should be equal to the amount of Al received at the
     potential_manufacturer"""
    return sum(model.international_transportation_input_solar_Al[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_Al[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


model.National_Transport_In_Al_con = Constraint(model.port, rule=National_Transport_In_Al)


def International_Transport_In_glass(model, Supplier):
    """The amount of purchased glass should be equal to amount glass transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_glass[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_glass[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


model.International_Transport_In_glass_con = Constraint(model.Supplier, rule=International_Transport_In_glass)


def National_Transport_In_glass(model, port):
    """The amount of glass transport from potential_manufacturer to the manufacturer should be equal to the amount of glass received at
    the potential_manufacturer"""
    return sum(model.international_transportation_input_solar_glass[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_glass[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


model.National_Transport_In_glass_con = Constraint(model.port, rule=National_Transport_In_glass)


def International_Transport_In_backsheet(model, Supplier):
    """The amount of purchased backsheet should be equal to amount backsheet transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_backsheet[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_backsheet[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


model.International_Transport_In_backsheet_con = Constraint(model.Supplier, rule=International_Transport_In_backsheet)


def National_Transport_In_backsheet(model, port):
    """The amount of backsheet transport from potential_manufacturer to the manufacturer should be equal to the amount of backsheet
    received at the potential_manufacturer"""
    return sum(model.international_transportation_input_solar_backsheet[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_backsheet[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


model.National_Transport_In_backsheet_con = Constraint(model.port, rule=National_Transport_In_backsheet)


def International_Transport_In_jBox(model, Supplier):
    """The amount of purchased jBox should be equal to amount jBox transport to the potential_manufacturer"""
    return sum(model.purchasing_solar_jBox[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_jBox[Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


model.International_Transport_In_jBox_con = Constraint(model.Supplier, rule=International_Transport_In_jBox)


def National_Transport_In_jBox(model, port):
    """The amount of jBox transport from potential_manufacturer to the manufacturer should be equal to the amount of jBox
    received at the potential_manufacturer"""
    return sum(model.international_transportation_input_solar_jBox[Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_jBox[port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


model.National_Transport_In_jBox_con = Constraint(model.port, rule=National_Transport_In_jBox)


def International_Transport_In_SealantPottingTapeStickers(model, Supplier):
    """The amount of purchased SealantPottingTapeStickers should be equal to amount SealantPottingTapeStickers
    transport to the potential_manufacturer """
    return sum(model.purchasing_solar_SealantPottingTapeStickers[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_SealantPottingTapeStickers
               [Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


model.International_Transport_In_SealantPottingTapeStickers_con = \
    Constraint(model.Supplier, rule=International_Transport_In_SealantPottingTapeStickers)


def National_Transport_In_SealantPottingTapeStickers(model, port):
    """The amount of SealantPottingTapeStickers transport from potential_manufacturer to the manufacturer should be equal to the amount
    of SealantPottingTapeStickers received at the potential_manufacturer"""
    return sum \
               (model.international_transportation_input_solar_SealantPottingTapeStickers[
                    Supplier, port, transportation_type]
                for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_SealantPottingTapeStickers
               [port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


model.National_Transport_In_SealantPottingTapeStickers_con = \
    Constraint(model.port, rule=National_Transport_In_SealantPottingTapeStickers)


def International_Transport_In_TabbingsStringingRibbons(model, Supplier):
    """The amount of purchased TabbingsStringingRibbons should be equal to amount TabbingsStringingRibbons transport
    to the potential_manufacturer """
    return sum(model.purchasing_solar_TabbingsStringingRibbons[Supplier, month] for month in model.month) >= \
           sum(model.international_transportation_input_solar_TabbingsStringingRibbons
               [Supplier, port, transportation_type]
               for port in model.port for transportation_type in model.transportation_type)


model.International_Transport_In_TabbingsStringingRibbons_con = \
    Constraint(model.Supplier, rule=International_Transport_In_TabbingsStringingRibbons)


def National_Transport_In_TabbingsStringingRibbons(model, port):
    """The amount of TabbingsStringingRibbons transport from potential_manufacturer to the manufacturer should be equal to the amount of
    TabbingsStringingRibbons received at the potential_manufacturer"""
    return sum(model.international_transportation_input_solar_TabbingsStringingRibbons[
                   Supplier, port, transportation_type]
               for Supplier in model.Supplier for transportation_type in model.transportation_type) >= \
           sum(model.national_transportation_input_solar_TabbingsStringingRibbons
               [port, potential_manufacturer, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for transportation_type in
               model.transportation_type)


model.National_Transport_In_TabbingsStringingRibbons_con = \
    Constraint(model.port, rule=National_Transport_In_TabbingsStringingRibbons)


def Production_Capacity(model, potential_manufacturer):
    """This function still need more work. Wondering how to connect the potential_manufacturer to the final market"""
    return ((model.solar_module_production[potential_manufacturer]) * 310) <= \
           ((model.production_capacity[potential_manufacturer]) * model.module_center[potential_manufacturer])


model.Production_Capacity_con = Constraint(model.potential_manufacturer, rule=Production_Capacity)


def Production_binary(model):
    """Potential manufacturer candidate selection"""
    return sum(model.module_center[potential_manufacturer] for
               potential_manufacturer in model.potential_manufacturer) <= Number_of_manufacturer


model.Production_binary_con = Constraint(rule=Production_binary)


def Production_Out(model, potential_manufacturer):
    """The produced module should transport to national market or either international market"""
    return (model.solar_module_production[potential_manufacturer]) >= \
           (sum(model.national_transportation_out_solar_module[
                    potential_manufacturer, national_market, transportation_type]
                for national_market in model.national_market for transportation_type in model.transportation_type) +
            sum(model.international_transportation_out_solar_module[potential_manufacturer, port, transportation_type]
                for port in model.port for transportation_type in model.transportation_type))


model.Production_Out_con = Constraint(model.potential_manufacturer, rule=Production_Out)


def Module_Production_Cell(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_cell[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) / 60)


model.Module_Production_Cell = Constraint(model.potential_manufacturer, rule=Module_Production_Cell)


def Module_Production_Al(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_Al[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) / 2.303)


model.Module_Production_Al = Constraint(model.potential_manufacturer, rule=Module_Production_Al)


def Module_Production_eva(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_eva[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) / (2 * 1.6368))


model.Module_Production_eva = Constraint(model.potential_manufacturer, rule=Module_Production_eva)


def Module_Production_glass(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_glass[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) / (1.6368))


model.Module_Production_glass = Constraint(model.potential_manufacturer, rule=Module_Production_glass)


def Module_Production_backsheet(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_backsheet[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) / (1.6368))


model.Module_Production_backsheet = Constraint(model.potential_manufacturer, rule=Module_Production_backsheet)


def Module_Production_jBox(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_jBox[port, potential_manufacturer, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)))


model.Module_Production_jBox = Constraint(model.potential_manufacturer, rule=Module_Production_jBox)


def Module_Production_SealantPottingTapeStickers(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_SealantPottingTapeStickers[port, potential_manufacturer,
                                                                                      transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)))


model.Module_Production_SealantPottingTapeStickers = Constraint(model.potential_manufacturer,
                                                                rule=Module_Production_SealantPottingTapeStickers)


def Module_Production_TabbingsStringingRibbons(model, potential_manufacturer):
    return (model.solar_module_production[potential_manufacturer]) == \
           ((sum(model.national_transportation_input_solar_TabbingsStringingRibbons[port, potential_manufacturer,
                                                                                    transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)))


model.Module_Production_TabbingsStringingRibbons = Constraint(model.potential_manufacturer,
                                                              rule=Module_Production_TabbingsStringingRibbons)


def Inventory(model, potential_manufacturer):
    return (sum(model.storing_solar_module[potential_manufacturer, month] for month in model.month)) == \
           sum(model.storing_solar_module[potential_manufacturer, Get_Previous_Month(month)] for month in model.month +
               ((sum(
                   model.national_transportation_input_solar_cell[port, potential_manufacturer, transportation_type]
                   for port in model.port for transportation_type in model.transportation_type))) + ((sum(
               model.national_transportation_input_solar_eva[
                   port, potential_manufacturer, transportation_type]
               for port in model.port for transportation_type in
               model.transportation_type))) + ((sum(
               model.national_transportation_input_solar_Al[
                   port, potential_manufacturer, transportation_type]
               for port in model.port for transportation_type in model.transportation_type))) + (
                   (sum(
                       model.national_transportation_input_solar_glass[
                           port, potential_manufacturer, transportation_type]
                       for port in model.port for transportation_type in
                       model.transportation_type))) + ((sum(
               model.national_transportation_input_solar_backsheet[
                   port, potential_manufacturer, transportation_type]
               for port in model.port for transportation_type in model.transportation_type))) + (
                   (sum(model.national_transportation_input_solar_jBox[
                            port, potential_manufacturer, transportation_type]
                        for port in model.potential_manufacturer for transportation_type in model.transportation_type))) + ((sum(
               model.national_transportation_input_solar_SealantPottingTapeStickers[
                   port, potential_manufacturer, transportation_type]
               for port in model.port for transportation_type in model.transportation_type))) + ((sum(
               model.national_transportation_input_solar_TabbingsStringingRibbons[
                   port, potential_manufacturer, transportation_type]
               for port in model.port for transportation_type in model.transportation_type))) -
               (model.solar_module_production[potential_manufacturer]))


# model.Inventory_con = Constraint(model.potential_manufacturerl_manufacturer, rule=Inventory)


def Local_Demand_by_Production(model, national_market):
    """The amount of produced module should be equal to national demand. Since the demand unit is W, the module should
    multiply by 310. Each module output is considered to be 310W"""
    return \
        ((sum(model.national_transportation_out_solar_module
              [potential_manufacturer, national_market, transportation_type] for potential_manufacturer in
              model.potential_manufacturer for transportation_type in model.transportation_type)) * 310) >= \
        sum(model.national_demand[national_market, month] for month in model.month)


def Local_Demand_by_Import(model, national_market):
    """The amount of imported module should be equal to national demand. Since the demand unit is W, the module should
    multiply by 310. Each module output is considered to be 310W"""
    return ((sum(model.national_transportation_input_solar_module[port, national_market, transportation_type]
                 for port in model.port for transportation_type in model.transportation_type)) * 310) >= \
           sum(model.national_demand[national_market, month] for month in model.month)


def Demand_Constraint(mode):
    if mode == "Local":
        model.Local_Demand_by_Production_con = Constraint(model.national_market, rule=Local_Demand_by_Production)
        return
    if mode == "Global":
        model.Local_Demand_by_Import_con = Constraint(model.national_market, rule=Local_Demand_by_Import)
        return
    return print("Error")


Demand_Constraint("Local")


def No():
    def International_Demand(model, international_market):
        """The amount of exported module should be equal to international demand. Since the demand unit is W, the module
#     should multiply by 310. Each module output is considered to be 310W"""
        return ((sum(
            model.international_transportation_out_solar_module[potential_manufacturer, port, transportation_type]
            for potential_manufacturer in model.potential_manufacturer for port in model.port for
            transportation_type in model.transportation_type)) * 310) == \
               sum(model.international_demand[international_market, month] for month in model.month)

    model.International_Demand_con = Constraint(model.international_market, rule=International_Demand)
