from pyomo.environ import *
import numpy as np
from DataBase import *


def info():
    """
    Considering BoM separately may not be correct, because in this case,
    the economies of scale would not apply to BoM.
    """


model = ConcreteModel()

# Set
model.Supplier = Set(initialize=Suppliers_Set("Suppliers_Name"))
model.potential_manufacturer = Set(initialize=Manufacturer_Set("Location_Name"))
model.national_market = Set(initialize=National_Market_Set("National_Market_Name"))
model.international_market = Set(initialize=International_Market_Set("International_Market_Name"))
model.month = Set(initialize=Suppliers_Set("Month"))
model.transportation_type = Set(initialize=International_Transportation_In_Set("Type"))
model.port = Set(initialize=International_Transportation_In_Set("Location_Port_Name"))
model.product = Set(initialize=Suppliers_Set("Product"))

# Parameters
# Fixed Cost

model.fixed_cost_module_center = Param(model.potential_manufacturer,
                                       initialize=lambda model, potential_manufacturer:
                                       Param_Potential_Manufacturer(model, "Fixed_Cost", potential_manufacturer))

model.desirability_state = Param(model.potential_manufacturer,
                                 initialize=lambda model, potential_manufacturer:
                                 Param_Potential_Manufacturer(model, "Preference_Factor", potential_manufacturer))


Number_of_manufacturer = candidate_location.iloc[0]["Number_of_Locations"]

# Purchasing Costs

model.solar_module_purchasing_cost = Param(model.Supplier, model.month,
                                           initialize=lambda model, suppliers, month:
                                           Param_Suppliers(model, "Price", "Module", suppliers,
                                                                                 month))
model.solar_cell_purchasing_cost = Param(model.Supplier, model.month,
                                         initialize=lambda model, suppliers, month:
                                         Param_Suppliers(model, "Price", "Cell", suppliers, month))

model.solar_Al_purchasing_cost = Param(model.Supplier, model.month,
                                       initialize=lambda model, suppliers, month:
                                       Param_Suppliers(model, "Price", "Aluminium", suppliers, month))

model.solar_glass_purchasing_cost = Param(model.Supplier, model.month,
                                          initialize=lambda model, suppliers, month:
                                          Param_Suppliers(model, "Price", "Glass", suppliers, month))

model.solar_eva_purchasing_cost = Param(model.Supplier, model.month,
                                        initialize=lambda model, suppliers, month:
                                        Param_Suppliers(model, "Price", "EVA", suppliers, month))

model.solar_backsheet_purchasing_cost = Param(model.Supplier, model.month,
                                              initialize=lambda model, suppliers, month:
                                              Param_Suppliers(model, "Price", "Backsheet", suppliers, month))

model.solar_jBox_purchasing_cost = Param(model.Supplier, model.month,
                                         initialize=lambda model, suppliers, month:
                                         Param_Suppliers(model, "Price", "JunctionBox", suppliers, month))

model.solar_TabbingsStringingRibbons_purchasing_cost = Param(model.Supplier, model.month,
                                                             initialize=lambda model, suppliers, month:
                                                             Param_Suppliers(model, "Price",
                                                                             "TabbingsStringingRibbons", suppliers,
                                                                             month))

model.solar_SealantPottingTapeStickers_purchasing_cost = Param(model.Supplier, model.month,
                                                               initialize=lambda model, suppliers, month:
                                                               Param_Suppliers(model, "Price",
                                                                               "SealantPottingTapeStickers",
                                                                               suppliers, month))

# Production Cost
model.labour_cost = Param(model.potential_manufacturer,
                          initialize=lambda model, potential_manufacturer:
                          Param_Potential_Manufacturer(model, "LabourCost", potential_manufacturer))

model.electricity_cost = Param(model.potential_manufacturer,
                               initialize=lambda model, potential_manufacturer:
                               Param_Potential_Manufacturer(model, "ElectricityCost", potential_manufacturer))

# International Transportation Cost Input
# model.international_transportation_input_cost_cell = \
#     Param(model.Supplier, model.potential_manufacturer, model.transportation_type,
#           initialize=lambda model, suppliers, potential_manufacturer, type:
#           Param_International_Transportation_In(model, "Price", "Cell", suppliers, potential_manufacturer, type))

model.international_transportation_input_cost_cell = \
    Param(model.Supplier, model.port, model.transportation_type,
          initialize=lambda model, suppliers, port, type:
          Param_International_Transportation_In(model, "Price", "Cell", suppliers, port, type))

model.international_transportation_input_cost_eva = \
    Param(model.Supplier, model.port, model.transportation_type,
          initialize=lambda model, suppliers, port, type:
          Param_International_Transportation_In(model, "Price", "EVA", suppliers, port, type))


model.international_transportation_input_cost_backsheet = \
    Param(model.Supplier, model.port, model.transportation_type,
          initialize=lambda model, suppliers, port, type:
          Param_International_Transportation_In(model, "Price", "Backsheet", suppliers, port, type))

model.international_transportation_input_cost_glass = \
    Param(model.Supplier, model.port, model.transportation_type,
          initialize=lambda model, suppliers, port, type:
          Param_International_Transportation_In(model, "Price", "Glass", suppliers, port, type))

model.international_transportation_input_cost_Al = \
    Param(model.Supplier, model.port, model.transportation_type,
          initialize=lambda model, suppliers, port, type:
          Param_International_Transportation_In(model, "Price", "Aluminium", suppliers, port, type))

model.international_transportation_input_cost_jBox = \
    Param(model.Supplier, model.port, model.transportation_type,
          initialize=lambda model, suppliers, port, type:
          Param_International_Transportation_In(model, "Price", "JunctionBox", suppliers, port, type))

model.international_transportation_input_cost_TabbingsStringingRibbons = \
    Param(model.Supplier, model.port, model.transportation_type,
          initialize=lambda model, suppliers, port, type:
          Param_International_Transportation_In(model, "Price", "TabbingsStringingRibbons", suppliers, port,
                                                type))


model.international_transportation_input_cost_SealantPottingTapeStickers = \
    Param(model.Supplier, model.port, model.transportation_type,
          initialize=lambda model, suppliers, port, type:
          Param_International_Transportation_In(model, "Price", "SealantPottingTapeStickers", suppliers, port,
                                                type))

# National Transportation Cost Input

model.national_transportation_input_cost_cell = \
    Param(model.port, model.potential_manufacturer, model.transportation_type,
          initialize=lambda model, port, potential_manufacturer, type:
          Param_National_Transportation_In(model, "Price", "Cell", port, potential_manufacturer, type))

model.national_transportation_input_cost_Al = \
    Param(model.port, model.potential_manufacturer, model.transportation_type,
          initialize=lambda model, port, potential_manufacturer, type:
          Param_National_Transportation_In(model, "Price", "Aluminium", port, potential_manufacturer, type))

model.national_transportation_input_cost_eva = \
    Param(model.port, model.potential_manufacturer, model.transportation_type,
          initialize=lambda model, port, potential_manufacturer, type:
          Param_National_Transportation_In(model, "Price", "EVA", port, potential_manufacturer, type))

model.national_transportation_input_cost_backsheet = \
    Param(model.port, model.potential_manufacturer, model.transportation_type,
          initialize=lambda model, port, potential_manufacturer, type:
          Param_National_Transportation_In(model, "Price", "Backsheet", port, potential_manufacturer, type))

model.national_transportation_input_cost_glass = \
    Param(model.port, model.potential_manufacturer, model.transportation_type,
          initialize=lambda model, port, potential_manufacturer, type:
          Param_National_Transportation_In(model, "Price", "Glass", port, potential_manufacturer, type))

model.national_transportation_input_cost_jBox = \
    Param(model.port, model.potential_manufacturer, model.transportation_type,
          initialize=lambda model, port, potential_manufacturer, type:
          Param_National_Transportation_In(model, "Price", "JunctionBox", port, potential_manufacturer, type))

model.national_transportation_input_cost_TabbingsStringingRibbons = \
    Param(model.port, model.potential_manufacturer, model.transportation_type,
          initialize=lambda model, port, potential_manufacturer, type:
          Param_National_Transportation_In(model, "Price", "TabbingsStringingRibbons",
                                           port, potential_manufacturer, type))

model.national_transportation_input_cost_SealantPottingTapeStickers = \
    Param(model.port, model.potential_manufacturer, model.transportation_type,
          initialize=lambda model, port, potential_manufacturer, type:
          Param_National_Transportation_In(model, "Price", "SealantPottingTapeStickers",
                                           port, potential_manufacturer, type))

model.national_transportation_out_cost_solar_module = \
    Param(model.potential_manufacturer, model.national_market, model.transportation_type,
          initialize=lambda model, potential_manufacturer, national_market, transportation_type:
          Param_National_Transportation_Out(model, "Price", potential_manufacturer, national_market,
                                            transportation_type))


# Import Module

model.international_transportation_input_cost_module = \
    Param(model.Supplier, model.port, model.transportation_type,
          initialize=lambda model, suppliers, port, type:
          Param_International_Transportation_In(model, "Price", "Module", suppliers, port, type))
model.national_transportation_input_cost_module = \
    Param(model.port, model.national_market, model.transportation_type,
          initialize=lambda model, port, national_market, type:
          Param_Transportation_Import(model, "Price", port, national_market, type))


# Capacity

model.production_capacity = Param(model.potential_manufacturer,
                                  initialize=lambda model, potential_manufacturer:
                                  Param_Potential_Manufacturer(model, "Capacity", potential_manufacturer))

model.production_capacity.display()

# Demand

model.national_demand = Param(model.national_market, model.month,
                              initialize=lambda model, national_market, month:
                              Param_National_Market_Demand(model, "Demand", national_market, month))

model.international_demand = Param(model.international_market, model.month,
                                   initialize=lambda model, international_market, month:
                                   Param_International_Market_Demand(model, "Demand", international_market, month))


# Distance

model.suppliers_port_distance = Param(model.Supplier, model.port,
                                      initialize=lambda model, suppliers, port:
                                      Param_International_Transportation_In(model, "Distance", None, suppliers, port))

model.port_manufacturer_distance = Param(model.port, model.potential_manufacturer,
                                         initialize=lambda model, port, potential_manufacturer:
                                         Param_National_Transportation_In(model, "Distance", None, port,
                                                                          potential_manufacturer))

model.manufacturer_market_distance = Param(model.potential_manufacturer, model.national_market,
                                           model.transportation_type,
                                           initialize=lambda model, potential_manufacturer, national_market, type:
                                           Param_National_Transportation_Out(model, "Distance",
                                                                             potential_manufacturer, national_market,
                                                                             type))

model.distance_port_national_market = Param(model.port, model.national_market, model.transportation_type,
                                            initialize=lambda model, port, national_market, type:
                                            Param_Transportation_Import(model, "Distance", port, national_market, type))

# Policy

model.import_tariff_module = Param(initialize=lambda model: float(Param_Incentives(model, "Module_Import_Tariff")))
model.import_tariff_BoMs = Param(initialize=lambda model: float(Param_Incentives(model, "BoMs_Import_Tariff")))
model.tax = Param(initialize=lambda model: float(Param_Incentives(model, "Tax")))
model.GST = Param(initialize=lambda model: float(Param_Incentives(model, "GST")))
model.module_incentives = Param(initialize=lambda model: float(Param_Incentives(model, "Incentive_Module")))
model.CapEx_incentives = Param(initialize=lambda model: float(Param_Incentives(model, "Incentive_CapEx")))


# Variables

model.module_center = Var(model.potential_manufacturer, within=Binary)

model.purchasing_solar_module = Var(model.Supplier, model.month, within=NonNegativeIntegers)
model.purchasing_solar_cell = Var(model.Supplier, model.month, within=NonNegativeIntegers)
model.purchasing_solar_eva = Var(model.Supplier, model.month, within=NonNegativeIntegers)
model.purchasing_solar_backsheet = Var(model.Supplier, model.month, within=NonNegativeReals)
model.purchasing_solar_glass = Var(model.Supplier, model.month, within=NonNegativeReals)
model.purchasing_solar_Al = Var(model.Supplier, model.month,within=NonNegativeReals)
model.purchasing_solar_jBox = Var(model.Supplier, model.month,within=NonNegativeReals)
model.purchasing_solar_SealantPottingTapeStickers = Var(model.Supplier, model.month,within=NonNegativeReals )
model.purchasing_solar_TabbingsStringingRibbons = Var(model.Supplier, model.month, within=NonNegativeReals)

model.international_transportation_input_solar_module = Var(model.Supplier, model.port, model.transportation_type,
                                                            within=NonNegativeIntegers)

model.international_transportation_input_solar_cell = Var(model.Supplier, model.port, model.transportation_type,
                                                          within=NonNegativeIntegers)
model.international_transportation_input_solar_eva = Var(model.Supplier, model.port, model.transportation_type,
                                                         within=NonNegativeReals)
model.international_transportation_input_solar_backsheet = Var(model.Supplier, model.port, model.transportation_type,
                                                               within=NonNegativeReals)
model.international_transportation_input_solar_glass = Var(model.Supplier, model.port, model.transportation_type,
                                                           within=NonNegativeReals)
model.international_transportation_input_solar_Al = Var(model.Supplier, model.port, model.transportation_type,
                                                        within=NonNegativeReals)
model.international_transportation_input_solar_jBox = Var(model.Supplier, model.port, model.transportation_type,
                                                          within=NonNegativeReals)
model.international_transportation_input_solar_SealantPottingTapeStickers = \
    Var(model.Supplier, model.port, model.transportation_type, within=NonNegativeReals)
model.international_transportation_input_solar_TabbingsStringingRibbons = \
    Var(model.Supplier, model.port, model.transportation_type, within=NonNegativeReals)

model.national_transportation_input_solar_module = \
    Var(model.port, model.national_market, model.transportation_type, within=NonNegativeIntegers)
model.national_transportation_out_solar_module = \
    Var(model.potential_manufacturer, model.national_market, model.transportation_type, within=NonNegativeIntegers)
model.international_transportation_out_solar_module = \
    Var(model.potential_manufacturer, model.port, model.transportation_type, within=NonNegativeIntegers)
model.national_transportation_input_solar_cell = \
    Var(model.port, model.potential_manufacturer, model.transportation_type, within=NonNegativeIntegers)
model.national_transportation_input_solar_eva = \
    Var(model.port, model.potential_manufacturer, model.transportation_type, within=NonNegativeReals)
model.national_transportation_input_solar_backsheet = \
    Var(model.port, model.potential_manufacturer, model.transportation_type, within=NonNegativeReals)
model.national_transportation_input_solar_glass = \
    Var(model.port, model.potential_manufacturer, model.transportation_type, within=NonNegativeReals)
model.national_transportation_input_solar_Al = \
    Var(model.port, model.potential_manufacturer, model.transportation_type, within=NonNegativeReals)
model.national_transportation_input_solar_jBox = \
    Var(model.port, model.potential_manufacturer, model.transportation_type, within=NonNegativeReals)
model.national_transportation_input_solar_SealantPottingTapeStickers = \
    Var(model.port, model.potential_manufacturer, model.transportation_type, within=NonNegativeReals)
model.national_transportation_input_solar_TabbingsStringingRibbons = \
    Var(model.port, model.potential_manufacturer, model.transportation_type, within=NonNegativeReals)

model.solar_module_production = Var(model.potential_manufacturer, within=NonNegativeIntegers)

model.storing_solar_module = Var(model.potential_manufacturer, model.month, within=NonNegativeIntegers)


def Objective_Function(model):
    Fixed_Cost = sum(model.module_center[potential_manufacturer] *
                     model.fixed_cost_module_center[potential_manufacturer] * (1 + model.desirability_state[potential_manufacturer])
                     for potential_manufacturer in model.potential_manufacturer)


    Purchasing_solar_module = sum(model.purchasing_solar_module[suppliers, month] * (1 + model.import_tariff_module) *
                                  model.solar_module_purchasing_cost[suppliers, month]
                                  for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_cell = sum(model.purchasing_solar_cell[suppliers, month] * (1 + model.import_tariff_BoMs) *
                                model.solar_cell_purchasing_cost[suppliers, month]
                                for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_eva = sum(model.purchasing_solar_eva[suppliers, month] * (1 + model.import_tariff_BoMs) *
                               model.solar_eva_purchasing_cost[suppliers, month]
                               for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_backsheet = sum(model.purchasing_solar_backsheet[suppliers, month] *
                                     (1 + model.import_tariff_BoMs) *
                                     model.solar_backsheet_purchasing_cost[suppliers, month]
                                     for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_glass = sum(model.purchasing_solar_glass[suppliers, month] * (1 + model.import_tariff_BoMs) *
                                 model.solar_glass_purchasing_cost[suppliers, month]
                                 for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_Al = sum(model.purchasing_solar_Al[suppliers, month] * (1 + model.import_tariff_BoMs) *
                              model.solar_Al_purchasing_cost[suppliers, month]
                              for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_jBox = sum(model.purchasing_solar_jBox[suppliers, month] * (1 + model.import_tariff_BoMs) *
                                model.solar_jBox_purchasing_cost[suppliers, month]
                                for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_SealantPottingTapeStickers = sum(
        model.purchasing_solar_SealantPottingTapeStickers[suppliers, month] * (1 + model.import_tariff_BoMs) *
        model.solar_SealantPottingTapeStickers_purchasing_cost[suppliers, month]
        for suppliers in model.Supplier for month in model.month)
    Purchasing_solar_TabbingsStringingRibbons = sum(model.purchasing_solar_TabbingsStringingRibbons[suppliers, month] *
                                                    (1 + model.import_tariff_BoMs) *
                                                    model.solar_TabbingsStringingRibbons_purchasing_cost[
                                                        suppliers, month]
                                                    for suppliers in model.Supplier for month in model.month)

    Production_cost = sum((model.labour_cost[potential_manufacturer] + model.electricity_cost[potential_manufacturer]) *
                          model.solar_module_production[potential_manufacturer]
                          for potential_manufacturer in model.potential_manufacturer)

    International_Transportation_In_solar_module = \
        sum(model.international_transportation_input_solar_module[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_module[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_cell = \
        sum(model.international_transportation_input_solar_cell[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_cell[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_eva = \
        sum(model.international_transportation_input_solar_eva[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_eva[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_backsheet = \
        sum(model.international_transportation_input_solar_backsheet[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_backsheet[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_Al = \
        sum(model.international_transportation_input_solar_Al[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_Al[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_glass = \
        sum(model.international_transportation_input_solar_glass[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_glass[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_jBox = \
        sum(model.international_transportation_input_solar_jBox[suppliers, port, transportation_type] *
            model.international_transportation_input_cost_jBox[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_SealantPottingTapeStickers = \
        sum(model.international_transportation_input_solar_SealantPottingTapeStickers[
                suppliers, port, transportation_type] *
            model.international_transportation_input_cost_SealantPottingTapeStickers[
                suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)
    International_Transportation_In_solar_TabbingsStringingRibbons = \
        sum(model.international_transportation_input_solar_TabbingsStringingRibbons[
                suppliers, port, transportation_type] *
            model.international_transportation_input_cost_TabbingsStringingRibbons[suppliers, port, transportation_type]
            for suppliers in model.Supplier for port in model.port for transportation_type in
            model.transportation_type)

    National_Transportation_In_solar_module = \
        sum(model.national_transportation_input_solar_module[port, national_market, transportation_type] *
            model.national_transportation_input_cost_module[port, national_market, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for national_market in model.national_market)
    National_Transportation_In_solar_cell = \
        sum(model.national_transportation_input_solar_cell[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_cell[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_eva = \
        sum(model.national_transportation_input_solar_eva[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_eva[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_backsheet = \
        sum(model.national_transportation_input_solar_backsheet[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_backsheet[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_Al = \
        sum(model.national_transportation_input_solar_Al[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_Al[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_glass = \
        sum(model.national_transportation_input_solar_glass[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_glass[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_jBox = \
        sum(model.national_transportation_input_solar_jBox[port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_jBox[port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_SealantPottingTapeStickers = \
        sum(model.national_transportation_input_solar_SealantPottingTapeStickers
            [port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_SealantPottingTapeStickers
            [port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)
    National_Transportation_In_solar_TabbingsStringingRibbons = \
        sum(model.national_transportation_input_solar_TabbingsStringingRibbons
            [port, potential_manufacturer, transportation_type] *
            model.national_transportation_input_cost_TabbingsStringingRibbons
            [port, potential_manufacturer, transportation_type]
            for port in model.port for transportation_type in model.transportation_type
            for potential_manufacturer in model.potential_manufacturer)

    national_transportation_out_solar_module = \
        sum(model.national_transportation_out_solar_module[
                potential_manufacturer, national_market, transportation_type] *
            model.national_transportation_out_cost_solar_module
            [potential_manufacturer, national_market, transportation_type]
            for potential_manufacturer in model.potential_manufacturer for national_market in model.national_market
            for transportation_type in model.transportation_type)
    Purchasing_BoMs = Purchasing_solar_cell + Purchasing_solar_Al + Purchasing_solar_eva + Purchasing_solar_backsheet + \
                      Purchasing_solar_glass + Purchasing_solar_jBox + Purchasing_solar_SealantPottingTapeStickers + \
                      Purchasing_solar_TabbingsStringingRibbons
    International_Transportation_in_BoMs = International_Transportation_In_solar_cell + \
                                           International_Transportation_In_solar_Al + \
                                           International_Transportation_In_solar_eva + \
                                           International_Transportation_In_solar_backsheet + \
                                           International_Transportation_In_solar_jBox + \
                                           International_Transportation_In_solar_TabbingsStringingRibbons + \
                                           International_Transportation_In_solar_glass + \
                                           International_Transportation_In_solar_SealantPottingTapeStickers
    National_Transportation_in_BoMs = National_Transportation_In_solar_cell + \
                                      National_Transportation_In_solar_Al + \
                                      National_Transportation_In_solar_eva + \
                                      National_Transportation_In_solar_backsheet + \
                                      National_Transportation_In_solar_jBox + \
                                      National_Transportation_In_solar_TabbingsStringingRibbons + \
                                      National_Transportation_In_solar_glass + \
                                      National_Transportation_In_solar_SealantPottingTapeStickers
    Transportation_In = International_Transportation_in_BoMs + National_Transportation_in_BoMs
    R_and_D_SGA = ((national_transportation_out_solar_module * 0.25) - Purchasing_solar_cell) * 0.105
    Depreciation_cost = Fixed_Cost / 7
    maintenance = Fixed_Cost * 0.04
    import_module = Purchasing_solar_module + International_Transportation_In_solar_module + \
                    National_Transportation_In_solar_module
    return Fixed_Cost + Purchasing_BoMs + Transportation_In + R_and_D_SGA + Depreciation_cost + maintenance + \
           import_module + Production_cost



model.Objective_function = Objective(rule=Objective_Function, sense=minimize)

