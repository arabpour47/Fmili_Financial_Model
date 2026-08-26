# Integrated 3-Statement Financial Model: National Iranian Copper Industries Co. (Fmili)

## Overview
This repository contains a fully integrated 3-statement financial model for National Iranian Copper Industries Co. (Ticker: FMILI), historically based on the official audited financial statements published on the Codal system. The model forecasts the company's financial performance for the next 5 years (1403-1407) based on macroeconomic drivers, industry-specific metrics, and corporate taxation frameworks in Iran.

## Methodology & Architecture
The model adheres to best practices in financial modeling and corporate finance valuation, strictly separating inputs, calculations, and outputs.

### Historical Data Aggregation
* **Source:** Audited annual reports (Codal.ir).
* **Period:** 1398 - 1402.
* **Adjustments:** Normalized for non-recurring items to reflect core operating performance.

### Forecasting Drivers (Assumptions)
The 5-year forecast relies on a dynamic assumptions schedule, incorporating:
* **Macroeconomic Variables:** Estimated inflation rates and Nima Exchange Rate adjustments.
* **Revenue Build-up:** Driven by LME Copper price projections and volumetric sales growth.
* **Cost Structure:** COGS broken down into raw materials, direct labor, and manufacturing overhead, grown proportionally.
* **Taxation:** Statutory corporate income tax rates applied to EBT, adjusted for non-deductible expenses and statutory reserves as per Iranian tax legislation.

### Schedules Developed
1. **Working Capital Schedule:** Linking Days Sales Outstanding (DSO), Days Inventory Outstanding (DIO), and Days Payable Outstanding (DPO) to forecast current assets and liabilities.
2. **Depreciation & CAPEX Schedule:** PPE roll-forward using straight-line/declining balance methods aligned with the company's historical accounting policies.
3. **Debt Schedule:** Debt roll-forward capturing interest expenses and principal repayments.

## Output & Verification
* The Income Statement, Balance Sheet, and Cash Flow Statement are dynamically linked.
* The Balance Sheet balances perfectly across all projected years without manual hardcoding (using a Cash/Revolver plug).
* A built-in circular reference circuit breaker is implemented to handle interest income/expense calculations on average cash/debt balances.

## Usage
Download the `Fmili_Financial_Model.xlsx` file. All input drivers (blue font) in the `Assumptions` tab can be modified to run various scenario analyses (Base, Bull, Bear cases).
