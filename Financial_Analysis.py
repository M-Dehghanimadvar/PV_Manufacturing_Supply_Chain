from Results import *
from numpy_financial import irr

BoM_Materials = [Purchasing_solar_cell, Purchasing_solar_glass, Purchasing_solar_Al, Purchasing_solar_eva,
                 Purchasing_solar_backsheet, Purchasing_solar_jBox,
                 Purchasing_solar_TabbingsStringingRibbons, Purchasing_solar_SealantPottingTapeStickers]

Purchasing_BoMs = sum(BoM_Materials)

International_Transportation = [International_Transportation_In_solar_cell,
                                International_Transportation_In_solar_glass,
                                International_Transportation_In_solar_Al,
                                International_Transportation_In_solar_eva,
                                International_Transportation_In_solar_backsheet,
                                International_Transportation_In_solar_jBox,
                                International_Transportation_In_solar_TabbingsStringingRibbons,
                                International_Transportation_In_solar_SealantPottingTapeStickers]

International_Transportation_in_BoMs = sum(International_Transportation)

National_Transportation = [National_Transportation_In_solar_cell,
                           National_Transportation_In_solar_glass,
                           National_Transportation_In_solar_Al,
                           National_Transportation_In_solar_eva,
                           National_Transportation_In_solar_backsheet,
                           National_Transportation_In_solar_jBox,
                           National_Transportation_In_solar_TabbingsStringingRibbons,
                           National_Transportation_In_solar_SealantPottingTapeStickers]

National_Transportation_in_BoMs = sum(National_Transportation)

Transportation_In = International_Transportation_in_BoMs + National_Transportation_in_BoMs

Trade_Cost_BoM = Purchasing_BoMs * (value(model.import_tariff_BoMs))

Depreciation_cost = CapEx / 7

maintenance = CapEx * 0.04

Trade_Cost_Module = Purchasing_solar_module * (value(model.import_tariff_module))

import_module = (Purchasing_solar_module * (1 + value(model.GST))) + International_Transportation_In_solar_module + \
                national_transportation_input_solar_module + Trade_Cost_Module

Working_Capital = Production_cost * 0.25

Initial_Investment = Working_Capital + CapEx

variable_cost = (Transportation_In + Production_cost +
                 Purchasing_BoMs + national_transportation_out_solar_module + Trade_Cost_BoM) \
                - value(model.module_incentives)

for Selling_price in np.arange(0.20, 0.40, 0.00005):
    R_and_D_SGA = (Selling_price - Purchasing_solar_cell) * 0.105
    Final_cost = variable_cost + R_and_D_SGA + Depreciation_cost + maintenance
    Income = (Selling_price - Final_cost)
    Profit_margin = (Income / Selling_price) * 100
    Tax = 0.3 * Income
    Cash_flow = variable_cost + R_and_D_SGA + maintenance + Tax
    IRR = irr([-(CapEx + Working_Capital),
               (Selling_price - Cash_flow), (Selling_price - Cash_flow),
               (Selling_price - Cash_flow),
               (Selling_price - Cash_flow), (Selling_price - Cash_flow),
               (Selling_price - Cash_flow),
               (Selling_price - (Cash_flow - Working_Capital))])
    if 0.138 <= IRR <= 0.145:
        break
    else:
        continue

        
