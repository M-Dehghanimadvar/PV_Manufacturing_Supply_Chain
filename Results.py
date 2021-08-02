from Sets_Parameters import *
from Solve import *

National_Demand = value(sum(model.national_demand[national_market, month] for national_market in
                            model.national_market for month in model.month))

CapEx = value(sum(model.module_center[potential_manufacturer] *
                  model.fixed_cost_module_center[potential_manufacturer]
                  for potential_manufacturer in model.potential_manufacturer)) / National_Demand

Purchasing_solar_module = value(sum(model.purchasing_solar_module[Supplier, month] *
                                    model.solar_module_purchasing_cost[Supplier, month]
                                    for Supplier in model.Supplier for month in model.month)) / National_Demand
Purchasing_solar_cell = value(sum(model.purchasing_solar_cell[Supplier, month] *
                                  model.solar_cell_purchasing_cost[Supplier, month]
                                  for Supplier in model.Supplier for month in model.month)) / National_Demand
Purchasing_solar_eva = value(sum(model.purchasing_solar_eva[Supplier, month] *
                                 model.solar_eva_purchasing_cost[Supplier, month]
                                 for Supplier in model.Supplier for month in model.month)) / National_Demand
Purchasing_solar_backsheet = value(sum(model.purchasing_solar_backsheet[Supplier, month] *
                                       model.solar_backsheet_purchasing_cost[Supplier, month]
                                       for Supplier in model.Supplier for month in model.month)) / National_Demand
Purchasing_solar_glass = value(sum(model.purchasing_solar_glass[Supplier, month] *
                                   model.solar_glass_purchasing_cost[Supplier, month]
                                   for Supplier in model.Supplier for month in model.month)) / National_Demand
Purchasing_solar_Al = value(sum(model.purchasing_solar_Al[Supplier, month] *
                                model.solar_Al_purchasing_cost[Supplier, month]
                                for Supplier in model.Supplier for month in model.month)) / National_Demand
Purchasing_solar_jBox = value(sum(model.purchasing_solar_jBox[Supplier, month] *
                                  model.solar_jBox_purchasing_cost[Supplier, month]
                                  for Supplier in model.Supplier for month in model.month)) / National_Demand
Purchasing_solar_SealantPottingTapeStickers = value(sum(
    model.purchasing_solar_SealantPottingTapeStickers[Supplier, month] *
    model.solar_SealantPottingTapeStickers_purchasing_cost[Supplier, month]
    for Supplier in model.Supplier for month in model.month)) / National_Demand
Purchasing_solar_TabbingsStringingRibbons = \
    value(sum(model.purchasing_solar_TabbingsStringingRibbons[Supplier, month] *
              model.solar_TabbingsStringingRibbons_purchasing_cost[Supplier, month]
              for Supplier in model.Supplier for month in model.month)) / National_Demand
Production_cost = \
    ((value(sum((model.labour_cost[potential_manufacturer] + model.electricity_cost[potential_manufacturer]) *
               model.solar_module_production[potential_manufacturer]
               for potential_manufacturer in model.potential_manufacturer)))) / National_Demand

International_Transportation_In_solar_module = (value(
    sum(model.international_transportation_input_solar_module[Supplier, port, transportation_type] *
        model.international_transportation_input_cost_module[Supplier, port, transportation_type]
        for Supplier in model.Supplier for port in model.port for transportation_type in
        model.transportation_type))+175.8) / National_Demand
International_Transportation_In_solar_cell = \
    (value(sum(model.international_transportation_input_solar_cell[Supplier, port, transportation_type] *
               model.international_transportation_input_cost_cell[Supplier, port, transportation_type]
               for Supplier in model.Supplier for port in model.port for transportation_type in
               model.transportation_type))+175.8) / National_Demand
International_Transportation_In_solar_eva = \
    (value(sum(model.international_transportation_input_solar_eva[Supplier, port, transportation_type] *
               model.international_transportation_input_cost_eva[Supplier, port, transportation_type]
               for Supplier in model.Supplier for port in model.port for transportation_type in
               model.transportation_type))+175.8) / National_Demand
International_Transportation_In_solar_backsheet = \
    (value(sum(model.international_transportation_input_solar_backsheet[Supplier, port, transportation_type] *
               model.international_transportation_input_cost_backsheet[Supplier, port, transportation_type]
               for Supplier in model.Supplier for port in model.port for transportation_type in
               model.transportation_type))+175.8) / National_Demand
International_Transportation_In_solar_Al = \
    (value(sum(model.international_transportation_input_solar_Al[Supplier, port, transportation_type] *
               model.international_transportation_input_cost_Al[Supplier, port, transportation_type]
               for Supplier in model.Supplier for port in model.port for transportation_type in
               model.transportation_type))+175.8) / National_Demand

International_Transportation_In_solar_glass = \
    (value(sum(model.international_transportation_input_solar_glass[Supplier, port, transportation_type] *
               model.international_transportation_input_cost_glass[Supplier, port, transportation_type]
               for Supplier in model.Supplier for port in model.port for transportation_type in
               model.transportation_type))+175.8) / National_Demand
International_Transportation_In_solar_jBox = \
    (value(sum(model.international_transportation_input_solar_jBox[Supplier, port, transportation_type] *
               model.international_transportation_input_cost_jBox[Supplier, port, transportation_type]
               for Supplier in model.Supplier for port in model.port for transportation_type in
               model.transportation_type))+175.8) / National_Demand
International_Transportation_In_solar_SealantPottingTapeStickers = \
    (value(sum(model.international_transportation_input_solar_SealantPottingTapeStickers[
                  Supplier, port, transportation_type] *
               model.international_transportation_input_cost_SealantPottingTapeStickers[
                  Supplier, port, transportation_type]
               for Supplier in model.Supplier for port in model.port for transportation_type in
               model.transportation_type))+175.8) / National_Demand
International_Transportation_In_solar_TabbingsStringingRibbons = \
    (value(sum(model.international_transportation_input_solar_TabbingsStringingRibbons[
                  Supplier, port, transportation_type] *
               model.international_transportation_input_cost_TabbingsStringingRibbons[
                  Supplier, port, transportation_type]
               for Supplier in model.Supplier for port in model.port for transportation_type in
               model.transportation_type))+175.8) / National_Demand

national_transportation_input_solar_module = \
    value(sum(model.national_transportation_input_solar_module[port, national_market, transportation_type] *
              model.national_transportation_input_cost_module[port, national_market, transportation_type]
              for port in model.port for transportation_type in model.transportation_type
              for national_market in model.national_market)) / National_Demand
National_Transportation_In_solar_cell = \
    value(sum(model.national_transportation_input_solar_cell[port, potential_manufacturer, transportation_type] *
              model.national_transportation_input_cost_cell[port, potential_manufacturer, transportation_type]
              for port in model.port for transportation_type in model.transportation_type
              for potential_manufacturer in model.potential_manufacturer)) / National_Demand
National_Transportation_In_solar_eva = \
    value(sum(model.national_transportation_input_solar_eva[port, potential_manufacturer, transportation_type] *
              model.national_transportation_input_cost_eva[port, potential_manufacturer, transportation_type]
              for port in model.port for transportation_type in model.transportation_type
              for potential_manufacturer in model.potential_manufacturer)) / National_Demand
National_Transportation_In_solar_backsheet = \
    value(sum(model.national_transportation_input_solar_backsheet[port, potential_manufacturer, transportation_type] *
              model.national_transportation_input_cost_backsheet[port, potential_manufacturer, transportation_type]
              for port in model.port for transportation_type in model.transportation_type
              for potential_manufacturer in model.potential_manufacturer)) / National_Demand
National_Transportation_In_solar_Al = \
    value(sum(model.national_transportation_input_solar_Al[port, potential_manufacturer, transportation_type] *
              model.national_transportation_input_cost_Al[port, potential_manufacturer, transportation_type]
              for port in model.port for transportation_type in model.transportation_type
              for potential_manufacturer in model.potential_manufacturer)) / National_Demand
National_Transportation_In_solar_glass = \
    value(sum(model.national_transportation_input_solar_glass[port, potential_manufacturer, transportation_type] *
              model.national_transportation_input_cost_glass[port, potential_manufacturer, transportation_type]
              for port in model.port for transportation_type in model.transportation_type
              for potential_manufacturer in model.potential_manufacturer)) / National_Demand
National_Transportation_In_solar_jBox = \
    value(sum(model.national_transportation_input_solar_jBox[port, potential_manufacturer, transportation_type] *
              model.national_transportation_input_cost_jBox[port, potential_manufacturer, transportation_type]
              for port in model.port for transportation_type in model.transportation_type
              for potential_manufacturer in model.potential_manufacturer)) / National_Demand
National_Transportation_In_solar_SealantPottingTapeStickers = \
    value(sum(model.national_transportation_input_solar_SealantPottingTapeStickers
              [port, potential_manufacturer, transportation_type] *
              model.national_transportation_input_cost_SealantPottingTapeStickers
              [port, potential_manufacturer, transportation_type]
              for port in model.port for transportation_type in model.transportation_type
              for potential_manufacturer in model.potential_manufacturer)) / National_Demand
National_Transportation_In_solar_TabbingsStringingRibbons = \
    value(sum(model.national_transportation_input_solar_TabbingsStringingRibbons
              [port, potential_manufacturer, transportation_type] *
              model.national_transportation_input_cost_TabbingsStringingRibbons
              [port, potential_manufacturer, transportation_type]
              for port in model.port for transportation_type in model.transportation_type
              for potential_manufacturer in model.potential_manufacturer)) / National_Demand

national_transportation_out_solar_module = \
    (value(sum(model.national_transportation_out_solar_module[
                   potential_manufacturer, national_market, transportation_type] *
               model.national_transportation_out_cost_solar_module
               [potential_manufacturer, national_market, transportation_type]
               for potential_manufacturer in model.potential_manufacturer for national_market in model.national_market
               for transportation_type in model.transportation_type))) / National_Demand

Produced_Module = \
    (value((sum(
        model.national_transportation_out_solar_module[potential_manufacturer, national_market, transportation_type]
        for potential_manufacturer in model.potential_manufacturer for national_market in model.national_market
        for transportation_type in model.transportation_type))))*310 / National_Demand


def variables():
    for v in model.component_objects(Var, active=True):
        varobject = getattr(model, str(v))
        for index in varobject:
            if varobject[index].value is None:
                continue
            elif varobject[index].value > 0.000000001:
                print("%s: %.3f" % (varobject[index].getname(), varobject[index].value))
