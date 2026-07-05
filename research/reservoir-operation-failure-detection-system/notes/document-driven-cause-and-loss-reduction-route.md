# Document-Driven Cause and Loss-Reduction Route

- Project: reservoir-operation-failure-detection-system
- Stage: Planning
- Planning unit: Modeling-route correction
- Status: added after user correction on 2026-07-03

## User Correction

The Modeling stage must not only detect low storage and build a model. It must
first analyze **why** the low-storage situation happened using documents, then
use time-series data to test the documented mechanisms and evaluate whether
approved hedging or conservation actions could reduce shortage/storage losses.

## Preliminary Document Evidence To Use In Modeling

These are source directions, not yet Modeling-acquired data.

| Evidence type | Source | Modeling implication |
|---|---|---|
| reservoir purpose and setting | TWDB Hords Creek page, `https://www.twdb.texas.gov/surfacewater/rivers/reservoirs/hords_creek/index.asp`; USACE Hords Creek page, `https://www.swf-wc.usace.army.mil/hords/` | Hords Creek is a small water-supply, flood-control, and recreation project; diagnosis must consider water-supply role, not only hydrologic anomaly. |
| 2011 drought and heat context | NWS San Angelo "Heat and Drought of 2011", `https://www.weather.gov/sjt/climate-heatdrought2011`; Texas State Climatologist / Climatexas 2011 drought materials, `https://climatexas.tamu.edu/files/2011-drought`; NOAA climate material, `https://www.climate.gov/news-features/videos/record-breaking-texas-drought` | Candidate drivers include extremely low precipitation, extreme heat, drought persistence, soil moisture depletion, and reduced runoff. |
| reservoir impact evidence | TWDB December 2011 reservoir storage report, `https://www.twdb.texas.gov/publications/reports/waterconditions/twc_pdf_archives/2011/twcDec2011.pdf` | Confirms Hords Creek was among reservoirs at or below 10% full / effectively empty in late 2011. |
| drought-response rules | City of Coleman drought contingency plan/code, `https://ecode360.com/40535082`; Region F drought-response appendix, `https://www.twdb.texas.gov/waterplanning/rwp/plans/2021/2021_RWP_Chp_7/RegionF_2021RWP_Ch7_AppG.pdf` | Candidate human-action variables include drought stage triggers, demand-reduction targets, curtailment, public restrictions, and reservoir-operation modifications. |
| conservation and infrastructure context | City of Coleman 2019 Water Conservation Plan, `https://www.cityofcolemantx.us/water/pdf/2019%20Water%20Conservation%20Plan.pdf` | Long-term mitigation variables include water-loss reduction, meter replacement, supply-line maintenance, reuse, and conservation education. |
| drought contingency planning context | USACE Hords Creek water-control/drought-contingency materials, `https://water.usace.army.mil/cda/documents/wc/3335/HORDS%20CREEK%20DAM%20AND%20LAKE%20.pdf` | Modeling should distinguish uncontrollable climate forcing from operational response rules and supply curtailment. |

## Cause Analysis Before Time-Series Modeling

Modeling should begin with a document-coded causal hypothesis table:

| Candidate cause or contributor | Document support needed | Time-series proxy to test |
|---|---|---|
| precipitation deficit / low runoff | NWS, State Climatologist, NOAA, drought reports | precipitation anomaly, inflow proxy, streamflow if available |
| extreme heat / evaporation pressure | NWS, Climatexas, USACE water-control materials | temperature anomaly, evaporation, storage loss rate |
| persistent regional drought / dry soils | NWS, Drought Monitor, TWDB, State Climatologist | drought category, antecedent precipitation index, lagged storage |
| water demand / municipal withdrawals | Coleman drought plan, conservation plan, water-use records if available | daily/monthly demand, release/withdrawal, demand-stage indicators |
| curtailment or operation constraints | Coleman plan, USACE materials | release rules, curtailment dates, operational stage flags |
| infrastructure loss / conservation inefficiency | Coleman conservation plan | water-loss rate, unaccounted-for water, conservation target scenarios |

No contributor should be reported as "the cause" unless both documents and data
support it. Otherwise use "documented likely contributor" or "data-consistent
contributor."

## Loss-Reduction / Mitigation Modeling

The question should be framed as:

> Given the documented drought context and approved response options, how much
> shortage/storage loss could hedging, conservation, or operation changes reduce?

Proposed scenario tests:

1. **Earlier demand-reduction trigger**: apply Stage I/II/III demand reductions
   earlier than documented trigger dates or threshold crossings.
2. **Demand reduction magnitude**: simulate 10%, 20%, and 30% reductions aligned
   with drought-plan style targets.
3. **Reduced loss / conservation improvement**: test whether lower system losses
   or conservation improvements materially change storage trajectory.
4. **Hydrologic-normal counterfactual**: replace 2011 drought forcing with a
   normal-year or percentile-normal inflow/precipitation profile to estimate how
   much of the event was climate-driven. This is an attribution scenario, not an
   operator-controlled action.
5. **No-action baseline**: compare all scenarios to the observed storage path.

## Hedging / Operation Optimization Formulation

The user's key modeling insight is that the loss-reduction question is an
operation optimization problem. The model should identify which water releases
or withdrawals were mandatory and which water could plausibly have been stored
or reallocated through hedging, demand reduction, conservation, or delayed
allocation.

Decision variables:

- `q_t`: water supplied/released at time `t`.
- `h_t`: hedging factor, where `h_t = q_t / demand_t` and `0 <= h_t <= 1`.
- `shortage_t = demand_t - q_t`.
- `saved_storage_t`: water that would have left storage under observed
  operation but remains stored under a hedging policy.

Reservoir balance skeleton:

```text
S_{t+1} = S_t + inflow_t - evaporation_t - mandatory_release_t
          - q_t - spill_t + adjustment_t
```

The optimization problem can be framed as:

```text
minimize over q_t or h_t:
    current shortage penalty
  + severe future shortage penalty
  + low-storage threshold violation penalty
  + terminal-storage penalty
  + rule-change / reliability penalty

subject to:
    storage capacity limits
    dead-pool or minimum storage limits
    mandatory environmental / downstream / legal releases
    drought-stage rules or approved modified rules
    maximum feasible demand reduction
    no use of future information unless a forecast policy is explicitly tested
```

This turns "how much loss can hedging reduce?" into a measurable optimization
question: under approved constraints and available foresight assumptions, what
hedging policy best reduces current shortage, future severe shortage, and
low-storage intensity?

## Water Classification For Hedging

Before optimization, Modeling must classify outflows:

| Water category | Can it be stored by better operation? | Modeling treatment |
|---|---|---|
| mandatory legal/downstream/environmental release | usually no | constraint, not a decision variable |
| municipal or supply withdrawal | partly, if drought restrictions or alternative supply are allowed | decision variable or demand-reduction scenario |
| discretionary release / nonessential use | potentially yes | hedgeable water if documents support it |
| system loss / leakage | potentially reducible but not by reservoir operation alone | conservation/infrastructure scenario |
| evaporation | no direct storage by release policy | climate/loss term; may be reduced only by structural or long-term measures |
| spill because storage exceeds capacity | generally no during low-storage drought | excluded unless flood/storage conflict exists |

For the Hords Creek demo, if release/withdrawal data are incomplete, the first
optimization should be a transparent simplified hedging scenario using observed
storage residuals and documented demand-reduction targets. Strong claims about
operator-controlled loss-reduction claims require actual
release/withdrawal/demand data.

Loss-reduction outcomes:

| Outcome | Meaning |
|---|---|
| threshold violation eliminated | counterfactual storage never crosses the approved low-storage threshold, reported as a special high-end mitigation result rather than the main goal |
| delayed threshold crossing | crossing occurs later than observed |
| shortened low-storage duration | event duration is shorter than observed |
| reduced intensity | cumulative low-storage intensity is lower |
| reduced shortage cost | objective-function shortage penalty is lower |
| no material reduction | tested actions do not materially reduce the approved loss metrics |

## Human Gates To Add In Modeling

| Modeling unit | Human gate question |
|---|---|
| document evidence gate | Are the documents sufficient to define candidate causes and possible response actions? |
| causal hypothesis gate | Are these candidate causes and data proxies acceptable before modeling? |
| release classification gate | Which outflows are mandatory, controllable, hedgeable, or unknown? |
| optimization formulation gate | Are the objective function, constraints, hedging assumptions, and foresight assumptions acceptable? |
| scenario design gate | Are the loss-reduction/mitigation scenarios realistic and evidence-bound? |
| scenario result gate | Do the scenario results justify the reported reduction in duration, intensity, shortage cost, or storage loss? |

## Key Claim Boundary

The workflow can test whether selected actions might have reduced the modeled
storage/shortage losses. It cannot prove that operators "failed" or that a
stronger threshold-elimination result would certainly have occurred unless
official documents, data, and scenario results all support that stronger claim.
