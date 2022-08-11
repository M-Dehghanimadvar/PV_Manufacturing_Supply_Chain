import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

dataBase = pd.ExcelFile("Dataset.xlsx")
suppliers = pd.read_excel(dataBase, sheet_name="Suppliers")
candidate_location = pd.read_excel(dataBase, sheet_name="Potential_Manufacturer")
local_market = pd.read_excel(dataBase, sheet_name="National_Market")
global_market = pd.read_excel(dataBase, sheet_name="International_Market")
international_transportation_in = pd.read_excel(dataBase, sheet_name="International_Transportation_In")
national_transportation_in = pd.read_excel(dataBase, sheet_name="National_Transportation_In")
national_transportation_out = pd.read_excel(dataBase, sheet_name="National_Transportation_Out")
import_transportation = pd.read_excel(dataBase, sheet_name="ImportModule")
policy = pd.read_excel(dataBase, sheet_name="Policy")
Transport_Fixed = pd.read_excel(dataBase, sheet_name="Logistic_Fixed_Cost")


def Suppliers_Set(info):
    return suppliers[info].unique().tolist()


def Manufacturer_Set(info):
    return candidate_location[info].unique().tolist()


def National_Market_Set(info):
    return local_market[info].unique().tolist()


def International_Market_Set(info):
    return global_market[info].unique().tolist()


def International_Transportation_In_Set(info):
    return international_transportation_in[info].unique().tolist()


International_In_Conversion_Dict = {"Cell": 1117200,
                                    "Module": 840,
                                    "Glass": 2916,
                                    "EVA": 64800,
                                    "Backsheet": 64800,
                                    "Aluminium": 24000,
                                    "JunctionBox": 36000,
                                    "TabbingsStringingRibbons": 25365,
                                    "SealantPottingTapeStickers": 25365}

National_In_Conversion_Dict = {"Cell": 0.0138,
                               "Module": 19,
                               "Glass": 9.0192,
                               "EVA": 0.2667,
                               "Backsheet": 0.2667,
                               "Aluminium": 1,
                               "JunctionBox": 0.37,
                               "TabbingsStringingRibbons": 1,
                               "SealantPottingTapeStickers": 1}


def Transport_Fixed_Cost():
    np.random.seed(12)
    total_cost=[]
    for index, row in Transport_Fixed.iterrows():
        if np.isnan(row["Cost"]):
            cost = round(np.random.uniform(row["Cost" + "RangeL"], row["Cost" + "RangeH"]), 4)
        else:
            cost = Transport_Fixed.at[index, "Cost"]
        total_cost.append(cost)
    return ((sum(total_cost)))


def Param_Suppliers(model, column_info, column_product, *Sets):
    np.random.seed(12)
    product_suppliers = suppliers[suppliers["Product"] == column_product].reset_index(drop=True)
    result = product_suppliers == np.inf
    for s in Sets:
        result = (product_suppliers == s) | result
    Match_sum = np.sum(result, axis=1) == len(Sets)
    if np.sum(Match_sum) == 1:
        Match_index = Match_sum.idxmax()
        if column_info == "Price":
            if np.isnan(product_suppliers.iloc[Match_index][column_info]):
                raw_price = round(np.random.uniform(product_suppliers.iloc[Match_index][column_info + "RangeL"],
                                                    product_suppliers.iloc[Match_index][column_info + "RangeH"]), 4)
            else:
                raw_price = product_suppliers.iloc[Match_index][column_info]
            if column_product in ["Cell", "Module"]:
                return raw_price
            else:
                return raw_price + (raw_price * (((candidate_location.iloc[1]["Capacity"] / 1000000000) **
                                                  (-0.18)) - 1))
        else:
            if np.isnan(product_suppliers.iloc[Match_index][column_info]):
                return round(np.random.uniform(product_suppliers.iloc[Match_index][column_info + "RangeL"],
                                               product_suppliers.iloc[Match_index][column_info + "RangeH"]), 4)
            return product_suppliers.iloc[Match_index][column_info]
    return 1000000000


def Compute_LabourCost(row):
    np.random.seed(12)
    if np.isnan(row["OperatorsWage"]):
        OperatorWage = round(np.random.uniform(row["OperatorsWage" + "RangeL"], row["OperatorsWage" + "RangeH"]), 4)
    else:
        OperatorWage = row["OperatorsWage"]
    if np.isnan(row["TechnicianWage"]):
        TechnicianWage = round(np.random.uniform(row["TechnicianWage" + "RangeL"], row["TechnicianWage" + "RangeH"]), 4)
    else:
        TechnicianWage = row["TechnicianWage"]
    if np.isnan(row["SupervisorsWage"]):
        SupervisorsWage = round(np.random.uniform(row["SupervisorsWage" + "RangeL"], row["SupervisorsWage" + "RangeH"]),
                                4)
    else:
        SupervisorsWage = row["SupervisorsWage"]
    Total_Cost = ((TechnicianWage * 307) + (OperatorWage * 167) + (SupervisorsWage * 23)) / 1000000000
    return (Total_Cost + (Total_Cost * (((candidate_location.iloc[1]["Capacity"] / 1000000000) **
                                         (-0.18)) - 1))) * 310


def Param_Potential_Manufacturer(model, info, *Sets):
    np.random.seed(12)
    result = candidate_location == np.inf
    for s in Sets:
        result = (s == candidate_location) | result  # Check which cells in candidate_location sheets
        # has the same name with recalled indices. (result is true or false)
    Match_sum = np.sum(result, axis=1) == len(Sets)  # Check which row is fully match with number of sets. If we
    # have 4 sets, then which row has 4 True columns
    if np.sum(Match_sum) == 1:  # if exists!
        Match_index = Match_sum.idxmax()  # find the row index, we use np.sum so return would be the row with one
        # True bool. If we have two row with True so the data is duplicated and should be omitted.
        if info == "Capacity":
            return candidate_location.iloc[Match_index][info] * 1.000005
        if info == "LabourCost":
            return Compute_LabourCost(candidate_location.iloc[Match_index])
        if info == "ElectricityCost":
            if np.isnan(candidate_location.iloc[Match_index][info]):
                ElectricityCost_R = round(np.random.uniform(candidate_location.iloc[Match_index][info + "RangeL"],
                                                            candidate_location.iloc[Match_index][info + "RangeH"]),
                                          4)
                ElectricityCost_W = ElectricityCost_R * 20 * (1 / 100)
                return ElectricityCost_W + (ElectricityCost_W *
                                            (((candidate_location.iloc[1]["Capacity"] / 1000000000) **
                                              (-0.18)) - 1))
            ElectricityCost = (candidate_location.iloc[Match_index][info]) * 20 * (1 / 100)
            return ElectricityCost + (ElectricityCost *
                                      (((candidate_location.iloc[1]["Capacity"] / 1000000000) **
                                        (-0.18)) - 1))
        if info == "Fixed_Cost":
            if np.isnan(candidate_location.iloc[Match_index][info]):
                return (round(np.random.uniform(candidate_location.iloc[Match_index][info + "RangeL"],
                                                candidate_location.iloc[Match_index][info + "RangeH"]), 4)) - \
                       (float(policy[policy["Policy"] == "Incentive_CapEx"]["Value"]) *
                        (candidate_location.iloc[1]["Capacity"]))
            return candidate_location.iloc[Match_index][info] - \
                   (float(policy[policy["Policy"] == "Incentive_CapEx"]["Value"]) *
                    (candidate_location.iloc[1]["Capacity"]))
        if np.isnan(candidate_location.iloc[Match_index][info]):
            return round(np.random.uniform(candidate_location.iloc[Match_index][info + "RangeL"],
                                           candidate_location.iloc[Match_index][info + "RangeH"]), 4)
        return candidate_location.iloc[Match_index][info]
    return 0


def Param_International_Transportation_In(model, column_info, column_product, *Sets):
    np.random.seed(12)
    if column_product is not None:
        product_suppliers = international_transportation_in[international_transportation_in["Product"] ==
                                                            column_product].reset_index(drop=True)
        result = product_suppliers == np.inf
        for s in Sets:
            result = (product_suppliers == s) | result
        Match_sum = np.sum(result, axis=1) == len(Sets)
        if np.sum(Match_sum) == 1:
            Match_index = Match_sum.idxmax()
            if column_info == "Price":
                if np.isnan(product_suppliers.iloc[Match_index][column_info]):
                    raw_price = \
                        round(np.random.uniform(product_suppliers.iloc[Match_index][column_info + "RangeL"],
                                                product_suppliers.iloc[Match_index][column_info + "RangeH"]), 4)
                    return (raw_price + Transport_Fixed_Cost()) / International_In_Conversion_Dict[column_product]
                return (product_suppliers.iloc[Match_index][column_info] + Transport_Fixed_Cost()) / International_In_Conversion_Dict[
                    column_product]
            else:
                if np.isnan(product_suppliers.iloc[Match_index][column_info]):
                    return round(np.random.uniform(product_suppliers.iloc[Match_index][column_info + "RangeL"],
                                                   product_suppliers.iloc[Match_index][column_info + "RangeH"]), 4)
                return product_suppliers.iloc[Match_index][column_info]
        return 1000000000
    if column_product is None:
        results = international_transportation_in == np.inf
        for s in Sets:
            results = (international_transportation_in == s) | results
        Match_sum = np.sum(results, axis=1) == len(Sets)
        if np.sum(Match_sum) >= 1:
            Match_index = Match_sum.idxmax()
            if np.isnan(international_transportation_in.iloc[Match_index][column_info]):
                return round(np.random.uniform(international_transportation_in.iloc[Match_index]
                                               [column_info + "RangeL"],
                                               international_transportation_in.iloc[Match_index]
                                               [column_info + "RangeH"]), 4)
            return international_transportation_in.iloc[Match_index][column_info]
        return 1000000000
    return 1000000000


def Param_National_Transportation_In(model, column_info, product_info, *Sets):
    np.random.seed(12)
    if product_info is not None:
        product_port = national_transportation_in[national_transportation_in["Product"] ==
                                                  product_info].reset_index(drop=True)
        results = product_port == np.inf
        for s in Sets:
            results = (product_port == s) | results
        Match_sum = np.sum(results, axis=1) == len(Sets)
        if np.sum(Match_sum) == 1:
            Match_index = Match_sum.idxmax()
            if column_info == "Price":
                if np.isnan(product_port.iloc[Match_index][column_info]):
                    raw_price = round(np.random.uniform(product_port.iloc[Match_index]
                                                        [column_info + "RangeL"],
                                                        product_port.iloc[Match_index]
                                                        [column_info + "RangeH"]), 4)
                    return raw_price * National_In_Conversion_Dict[product_info] * \
                           product_port.iloc[Match_index]["Distance"]
                return product_port.iloc[Match_index][column_info] * National_In_Conversion_Dict[product_info] * \
                       product_port.iloc[Match_index]["Distance"]
    if product_info is None:
        results = national_transportation_in == np.inf
        for s in Sets:
            results = (national_transportation_in == s) | results
        Match_sum = np.sum(results, axis=1) == len(Sets)
        if np.sum(Match_sum) >= 1:
            Match_index = Match_sum.idxmax()
            if np.isnan(national_transportation_in.iloc[Match_index][column_info]):
                return round(np.random.uniform(national_transportation_in.iloc[Match_index]
                                               [column_info + "RangeL"],
                                               national_transportation_in.iloc[Match_index]
                                               [column_info + "RangeH"]), 4)
            return national_transportation_in.iloc[Match_index][column_info]
        return 1000000000
    return 1000000000


def Param_National_Transportation_Out(model, info, *Sets):
    np.random.seed(12)
    results = national_transportation_out == np.inf
    for s in Sets:
        results = (national_transportation_out == s) | results
    Match_sum = np.sum(results, axis=1) == len(Sets)
    if np.sum(Match_sum) == 1:
        Match_index = Match_sum.idxmax()
        if info == "Price":
            if np.isnan(national_transportation_out.iloc[Match_index][info]):
                price = round(np.random.uniform(national_transportation_out.iloc[Match_index]
                                                [info + "RangeL"],
                                                national_transportation_out.iloc[Match_index]
                                                [info + "RangeH"]), 4)
            else:
                price = national_transportation_out.iloc[Match_index][info]
            if Sets in ["Ship"]:
                return (price * national_transportation_out.iloc[Match_index]["Distance"]) + 0.023712
            else:
                return price * national_transportation_out.iloc[Match_index]["Distance"]
        else:
            if np.isnan(national_transportation_out.iloc[Match_index][info]):
                return round(np.random.uniform(national_transportation_out.iloc[Match_index]
                                               [info + "RangeL"],
                                               national_transportation_out.iloc[Match_index]
                                               [info + "RangeH"]), 4)
            return national_transportation_out.iloc[Match_index][info]
    return 1000000000


def Param_National_Market_Demand(model, info, *Sets):
    np.random.seed(12)
    results = local_market == np.inf
    for s in Sets:
        results = (local_market == s) | results
    Match_sum = np.sum(results, axis=1) == len(Sets)
    if np.sum(Match_sum) == 1:
        Match_index = Match_sum.idxmax()
        if np.isnan(local_market.iloc[Match_index][info]):
            return round(np.random.uniform(local_market.iloc[Match_index]
                                           [info + "RangeL"],
                                           local_market.iloc[Match_index]
                                           [info + "RangeH"]), 4)
        return local_market.iloc[Match_index][info]
    return 0


def Param_International_Market_Demand(model, info, *Sets):
    np.random.seed(12)
    results = global_market == np.inf
    for s in Sets:
        results = (local_market == s) | results
    Match_sum = np.sum(results, axis=1) == len(Sets)
    if np.sum(Match_sum) == 1:
        Match_index = Match_sum.idxmax()
        if np.isnan(global_market.iloc[Match_index][info]):
            return round(np.random.uniform(global_market.iloc[Match_index]
                                           [info + "RangeL"],
                                           global_market.iloc[Match_index]
                                           [info + "RangeH"]), 4)
        return global_market.iloc[Match_index][info]
    return 1000000000


def Param_Transportation_Import(model, info, *Sets):
    results = import_transportation == np.inf
    for s in Sets:
        results = (s == import_transportation) | results
    Match_sum = np.sum(results, axis=1) == len(Sets)
    if np.sum(Match_sum) == 1:
        Match_index = Match_sum.idxmax()
        if np.isnan(import_transportation.iloc[Match_index][info]):
            raw_price = round(np.random.uniform(import_transportation.iloc[Match_index]
                                                [info + "RangeL"],
                                                import_transportation.iloc[Match_index]
                                                [info + "RangeH"]), 4)
        else:
            raw_price = import_transportation.iloc[Match_index][info]
        if info == "Price":
            if Sets in ["Ship"]:
                return (raw_price * import_transportation.iloc[Match_index]["Distance"]) + 0.023712
            else:
                return raw_price * import_transportation.iloc[Match_index]["Distance"]
        else:
            return raw_price
    return 1000000000


def Param_Incentives(model, info):
    return float(policy[policy["Policy"] == info]["Value"])


def Param_Location_number(model, info):
    return candidate_location[candidate_location["Number_of_Locations"] == info]["Value"]


