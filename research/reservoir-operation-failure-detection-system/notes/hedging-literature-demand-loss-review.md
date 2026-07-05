# Hedging Literature Demand-Loss Review

- Project: reservoir-operation-failure-detection-system
- Stage: Planning
- Planning unit: hedging literature and data requirements
- Status: targeted literature note, not a full systematic review
- Date: 2026-07-03

## User Requirement

The user identified demand and shortage-loss estimation as the core feasibility
issue. If the project cannot represent (1) how much water is demanded and (2)
how much loss follows from shortage, the hedging/operation-optimization part is
not meaningful enough for this research.

Planning response: add a **Demand-Loss Gate** before Modeling can build any
hedging model or make any loss-reduction claim.

## Search Strategy

Searches were run on 2026-07-03 using terms such as:

- `reservoir hedging rule demand shortage loss function optimization`
- `water supply operations drought continuous hedging rule`
- `Draper Lund optimal hedging carryover storage value`
- `You Cai 2008 hedging rule reservoir operations demand`
- `optimal hedging rules water supply reservoir forecast uncertainty CVaR`
- `urban water scarcity economic loss functions`

Included sources were peer-reviewed reservoir hedging papers or closely related
shortage-loss/economic-loss papers that explicitly discuss demand, delivery,
shortage, benefit, loss, rationing, carryover storage, or risk.

## Sources Read

| Source | Type | Why it matters for this project |
|---|---|---|
| Shih and ReVelle (1994), *Water-Supply Operations during Drought: Continuous Hedging Rule* | peer-reviewed article; RFF/ASCE metadata checked | Seminal continuous hedging paper; frames drought operation as water-supply demand management. |
| Shih and ReVelle (1995), *Water supply operations during drought: A discrete hedging rule* | peer-reviewed article; ScienceDirect abstract checked | Uses a mixed-integer model for a single water-supply reservoir and determines rationing trigger volumes. |
| Draper and Lund (2004), *Optimal Hedging and Carryover Storage Value* | peer-reviewed article; UC Davis PDF checked | Shows hedging depends on the balance between beneficial release and carryover storage value. |
| You and Cai (2008a), *Hedging rule for reservoir operations: 1. A theoretical analysis* | peer-reviewed article; Illinois/Wiley metadata checked | Explicitly links hedging range to water demand, uncertain inflow, evaporation loss, and utility functions. |
| You and Cai (2008b), *Hedging rule for reservoir operations: 2. A numerical model* | peer-reviewed article; Illinois/Wiley metadata checked | Embeds hedging derivation in simulation with nonlinear utility, inflow distribution, price elasticity, and discount rate. |
| Tu, Hsu, Tsai, and Yeh (2008), *Optimization of hedging rules for reservoir operations* | peer-reviewed article; LSU/ASCE metadata checked | Defines shortage as failure to satisfy target delivery/planned demand; hedging balances current shortage and future storage. |
| Xu et al. (2017), *Optimal Hedging Rules for Water Supply Reservoir Operations under Forecast Uncertainty and Conditional Value-at-Risk Criterion* | peer-reviewed open-access article | Uses benefit/loss and CVaR to ration delivery under forecast uncertainty; directly relevant to risk-averse loss reduction. |
| Shiau (2023), *Risk-aversion optimal hedging scenarios during droughts* | peer-reviewed open-access article | Uses water shortage probability and optimization to create real-time hedging scenarios. |
| Jenkins, Lund, and Howitt (2003), *Using Economic Loss Functions to Value Urban Water Scarcity in California* | peer-reviewed article; publisher/metadata checked | Not a hedging-rule paper, but directly relevant to estimating shortage-loss functions for municipal demand. |

## Literature Conclusions

### 1. Demand is structural, not optional

The hedging literature treats reservoir operation as a release/delivery decision
relative to target demand. Shortage exists only after a demand or planned
delivery target is defined. Without `D_t`, the model can still describe storage
decline, but it cannot answer the user's real question: how much demand was not
served and how much loss followed.

Minimum demand representations, strongest to weakest:

| Tier | Demand representation | Claim allowed |
|---|---|---|
| A | Event-period withdrawals, deliveries, pumpage, billing, or source-by-user demand | Historical hedging/loss-reduction counterfactual. |
| B | Official baseline demand and drought-stage reduction targets from plans or ordinances | Policy-scenario hedging on historical hydrology, not proof of actual 2011 operation. |
| C | Synthetic or literature-assumed demand curve | Toy workflow demo only; not a substantive reservoir finding. |

### 2. Shortage loss determines whether hedging is justified

Hedging is not automatically better than standard operating policy. The result
depends on the loss or benefit function. If shortage loss is linear, standard
operation can be optimal in some formulations. Hedging becomes meaningful when
the system prefers several smaller shortages over one severe shortage, which is
usually represented by nonlinear/convex shortage loss, utility functions,
carryover storage value, CVaR, reliability/vulnerability metrics, or explicit
rationing penalties.

Minimum loss representations, strongest to weakest:

| Tier | Shortage-loss representation | Claim allowed |
|---|---|---|
| A | Official shortage cost, willingness-to-pay, sectoral economic loss, or published customer shortage cost | Economic loss-reduction estimate. |
| B | Official drought-stage reductions, surcharges, fines, tiered rates, or allocation penalties | Policy/proxy loss-reduction estimate. |
| C | Predeclared convex penalty with sensitivity analysis | Illustrative optimization behavior only. |

### 3. Hedging is an optimization/control problem

For this project, hedging should be framed as a controlled allocation problem:

```text
state:      storage/elevation S_t
drivers:    inflow I_t, precipitation P_t, evaporation E_t, forecast/uncertainty
decision:   delivery/release q_t, demand reduction/rationing r_t, carryover storage
constraint: water balance, capacity, minimum/mandatory releases, demand bounds
shortage:   max(0, D_t - q_t)
objective:  minimize shortage loss + low-storage/carryover-storage risk
```

This means automatic model building is downstream. First the workflow must
define demand, controllable water, constraints, and shortage/loss.

### 4. Document analysis must precede time-series modeling

The documents should identify which low-storage drivers are plausible and which
actions are controllable:

- climate/runoff deficit;
- evaporation;
- mandatory release;
- municipal/wholesale/irrigation/manufacturing demand;
- leakage or distribution loss;
- drought-stage restrictions;
- controllable supply release or demand reduction.

The time-series model should then test these document-supported mechanisms
rather than inventing explanations after seeing correlations.

## Hords Creek Implication

Current Hords Creek public data appear adequate for storage, inflow, outflow,
precipitation, evaporation, and event detection. That is enough for a
hydrologic-storage diagnosis and for demonstrating that the workflow can detect
missing information.

It is **not yet enough for a meaningful hedging optimization claim** unless
Modeling can acquire or approve a demand and shortage-loss representation.

Available Coleman public documents provide useful but limited inputs:

- The 2019 Coleman Water Conservation Plan reports that Coleman obtains water
  from Lake Coleman, Hords Creek Lake, and Lake Scarborough, and reports recent
  average use, average daily use, service population, water loss, and rates.
- The Coleman Drought Contingency Plan defines pro rata allocation, monthly
  baselines, excess-use surcharges, and fines.
- These documents are from 2019, after the 2011-09-30 to 2012-02-17 event.
  They can support a **modern-policy scenario on historical hydrology**, but
  not a historical claim about what Coleman actually did in 2011-2012 unless
  event-period records are found.

## Demand-Loss Gate

Before Modeling may build the hedging model, the researcher must present a
Demand-Loss Gate to the user:

| Gate question | Pass condition | If not passed |
|---|---|---|
| Demand | Event-period or policy-scenario demand is available and its claim level is explicit. | Search more official records or switch reservoir. |
| Shortage/loss | Official, proxy, or explicitly synthetic loss function is available and approved. | Do not run hedging optimization as a substantive finding. |
| Controllability | Releases/withdrawals are classified as mandatory, controllable, hedgeable, reducible loss, or unknown. | Restrict output to diagnosis/data-gap report. |
| Claim level | User approves historical counterfactual, policy scenario, or toy demo claim. | Backtrack to Planning or change case reservoir. |

Recommended default route for Hords Creek:

1. Search for 2011-2012 Coleman/Hords Creek demand, pumpage, withdrawal,
   drought-stage, meeting-minute, and water-shortage records.
2. If found, build a historical hedging/loss-reduction formulation.
3. If not found but 2019 plan/ordinance inputs are accepted, build a
   modern-policy scenario on the 2011-2012 hydrology.
4. If neither route is acceptable, switch to another reservoir or make the demo
   a workflow/data-sufficiency finding rather than a hedging-optimization study.

## Sources

- RFF page for Shih and ReVelle (1994): https://www.rff.org/publications/journal-articles/water-supply-operations-during-drought-a-continuous-hedging-rule/
- ScienceDirect page for Shih and ReVelle (1995): https://www.sciencedirect.com/science/article/abs/pii/0377221793E0237R
- UC Davis PDF for Draper and Lund (2004): https://wla.engineering.ucdavis.edu/papers/DraperLund1.pdf
- Illinois Experts page for You and Cai (2008a): https://experts.illinois.edu/en/publications/hedging-rule-for-reservoir-operations-1-a-theoretical-analysis/
- Illinois Experts page for You and Cai (2008b): https://experts.illinois.edu/en/publications/hedging-rule-for-reservoir-operations-2-a-numerical-model/
- LSU repository page for Tu et al. (2008): https://repository.lsu.edu/civil_engineering_pubs/1170/
- MDPI page for Xu et al. (2017): https://www.mdpi.com/2073-4441/9/8/568
- Springer page for Shiau (2023): https://link.springer.com/article/10.1007/s13201-022-01817-x
- Wiley page for Jenkins et al. (2003): https://awwa.onlinelibrary.wiley.com/doi/abs/10.1002/j.1551-8833.2003.tb10292.x
- City of Coleman Water Conservation Plan (2019): https://www.cityofcolemantx.us/water/pdf/2019%20Water%20Conservation%20Plan.pdf
- City of Coleman Drought Contingency Plan code: https://ecode360.com/40535082
