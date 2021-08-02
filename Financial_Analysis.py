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

Selling_price = 0.308
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

# print((Production_cost)*1600000000)
#
# print(Selling_price*1600000000)
# print(Initial_Investment*1600000000)
# print(CapEx*1600000000)
# print(Working_Capital*1600000000)
# print(Depreciation_cost*1600000000)
# print(Purchasing_BoMs*1600000000)
# print((national_transportation_out_solar_module+ National_Transportation_in_BoMs)*1600000000)
# print(International_Transportation_in_BoMs*1600000000)
# print(R_and_D_SGA*1600000000)
# print(Trade_Cost_BoM*1600000000)
# print((Transportation_In+national_transportation_out_solar_module)*1600000000)
print(Income*1600000000)
# print(Profit_margin)
# print(Purchasing_solar_glass*1600000000)
# print((International_Transportation_In_solar_glass+National_Transportation_In_solar_glass)*1600000000)
# print(maintenance*1600000000)
# print(Depreciation_cost)

# print(maintenance)
# print(R_and_D_SGA)
# print(Trade_Cost_BoM)
# print(Tax)
print(IRR*100)
# print(Trade_Cost_BoM)

# print(International_Transportation_in_BoMs)
# print(Production_cost)
# print(National_Transportation_in_BoMs+national_transportation_input_solar_module)
# print(Final_cost)

# print(Production_cost)
# print((national_transportation_out_solar_module + National_Transportation_in_BoMs+International_Transportation_in_BoMs))
# print(International_Transportation_In_solar_module + national_transportation_input_solar_module)
