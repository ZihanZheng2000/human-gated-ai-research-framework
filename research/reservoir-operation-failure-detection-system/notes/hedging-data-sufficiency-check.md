# Hedging Data Sufficiency Check

- Project: reservoir-operation-failure-detection-system
- Stage: Planning
- Planning unit: hedging data feasibility
- Status: preliminary source-screening check, not Modeling-acquired data
- Date: 2026-07-03

## User Correction

The hedging question should be framed as **loss reduction**, not "can the event
be avoided." The key data question is whether public data are sufficient to
estimate how much hedging, demand reduction, or operation changes could reduce
storage loss, shortage cost, low-storage duration, or low-storage intensity.

## Minimum Data Needed For A Hedging Model

The hedging literature review in
`hedging-literature-demand-loss-review.md` makes demand and shortage/loss
non-optional. Storage, inflow, outflow, precipitation, and evaporation are enough
for hydrologic diagnosis, but not enough for a meaningful hedging optimization
claim unless a demand target and shortage/loss representation are available or
explicitly approved as scenario assumptions.

| Data need | Why it matters | Hords Creek preliminary status |
|---|---|---|
| storage or elevation time series | state variable `S_t` and threshold metrics | available from TWDB CSV and USACE/USGS elevation |
| inflow | separates climate/runoff deficit from operation | available in USACE CWMS catalog for HORT2 daily flow-in |
| total outflow/release | identifies water leaving reservoir | available in USACE CWMS catalog for HORT2 daily flow-out |
| outflow components | separates gated, pump, spillway, and possible supply withdrawals | USACE has gated total and spillway daily series; pump series exists in catalog but returned no values in the 2011-09-30 to 2012-02-17 event check |
| precipitation | climate forcing and drought diagnosis | available in USACE daily precipitation series; USGS precipitation starts too late for 2011 |
| evaporation | loss term in water balance | available in USACE project evaporation series |
| demand / target supply | structural requirement for shortage definition and hedging objective | not yet found as event-period daily/monthly data; Coleman 2019 plan gives modern baseline information, but not 2011-2012 historical demand |
| mandatory vs discretionary release rule | prevents treating required release as hedgeable | not yet encoded; must be extracted from water-control / drought-contingency documents |
| drought restriction stages and dates | defines allowed demand reductions and feasible hedging policies | documents exist, but exact event-period dates need acquisition/extraction |
| shortage/loss penalty | objective function for optimization; determines whether hedging is justified over standard operation | not directly observed; Coleman 2019 drought plan/rates can support a policy/proxy scenario, but not a historical economic-loss claim without more records |

## Source Checks Performed

These checks only establish that the source routes look feasible. They are not
the formal Modeling data acquisition.

| Source | Preliminary finding |
|---|---|
| TWDB Hords Creek CSV | Has `date`, `water_level`, `surface_area`, `reservoir_storage`, `conservation_storage`, `percent_full`, `conservation_capacity`, and `dead_pool_capacity`. Event window 2011-09-30 to 2012-02-17 has 141 daily storage rows. |
| USGS monitoring location `08141000` | Daily lake elevation is available for 2011-2012; USGS precipitation at this site begins too late for the 2011 event. |
| USACE CWMS catalog for `HORT2*` | Daily series exist for flow-in, flow-out, gated total outflow, spillway outflow, elevation, project evaporation, and precipitation, with long historical coverage. |
| USACE event-window quick check | For 2011-09-30 to 2012-02-17, preliminary daily values were returned for inflow, total outflow, gated outflow, spillway outflow, evaporation, precipitation, and elevation. Pump outflow returned no values for this event check. |

## Preliminary Event-Window Signals

Planning-only quick check for 2011-09-30 to 2012-02-17:

| Variable | Preliminary result |
|---|---|
| TWDB storage | 141 rows; storage ranged about 1,911 to 2,228 acre-feet |
| USACE inflow | 141 daily values; average about 3.23 cfs; rough event-window volume about 902 acre-feet |
| USACE total outflow | 141 daily values; constant about 1.06 cfs; rough event-window volume about 296 acre-feet |
| USACE gated total outflow | same as total outflow in this quick check |
| USACE spillway outflow | 141 daily values; zero during event window |
| USACE pump outflow | no event-window values returned in this quick check |
| USACE project evaporation | 141 daily values; units returned as inches |
| USACE precipitation | 141 daily values; precipitation occurred on 19 days in quick check |

## Feasibility Judgment

Hords Creek appears **sufficient for a storage and hydrologic diagnosis demo**:

- Detect low storage using storage/elevation.
- Diagnose drought, inflow, outflow, precipitation, and evaporation context.
- Estimate changes in storage trajectory, low-storage duration, and low-storage
  intensity under clearly labeled water-balance scenarios.

Hords Creek is **only sufficient for a meaningful hedging / loss-reduction
optimization demo** if the Demand-Loss Gate passes:

- demand or target supply is available for the event period, or the user
  approves a modern-policy or synthetic demand scenario;
- shortage/loss is available as an official economic value, policy proxy, or
  explicitly synthetic convex penalty;
- mandatory and controllable releases/withdrawals are separated before
  optimization.

Hords Creek is **not yet sufficient for a strong real-operation optimal hedging
claim** unless Modeling can acquire or defensibly reconstruct:

- daily demand or target supply;
- daily supply withdrawals / pumpage or municipal delivery;
- which releases are mandatory versus discretionary;
- drought-stage trigger dates and actual restriction implementation dates;
- an approved shortage/loss penalty function;
- forecast information available to operators at the time, if testing realistic
  forecast-based hedging rather than perfect-hindsight diagnostics.

## Recommended Modeling Gate

Before building the hedging model, add a **Demand-Loss Gate**:

> Are demand, shortage/loss, and controllability data sufficient for (A) a
> historical hedging counterfactual, (B) a modern-policy scenario on historical
> hydrology, or (C) only a toy workflow/data-sufficiency demo?

Default recommendation for this project: do **not** run hedging optimization as
a substantive finding until demand and shortage/loss are found or explicitly
approved as scenario assumptions. If they cannot be found for Hords Creek, the
workflow can still report that the case fails the Demand-Loss Gate, or the
project should switch to a reservoir with better demand/loss data.
