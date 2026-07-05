# Candidate Reservoir and Source Scan

- Date: 2026-07-03
- Stage: Planning
- Planning unit: candidate reservoir and public data/source strategy
- Status: discussion artifact, not approved plan

## Source Strategy

Use ResOpsUS as the standardized public dataset candidate, then validate and
document the selected reservoir using official operator or agency sources.

Why this matters:

- ResOpsUS gives daily reservoir operations data in consistent units and format.
- Official sources provide authoritative provenance, current data, and event
  documents needed to explain why an operation failed or entered a stress state.
- Candidate links do not count as usable data until Modeling downloads or
  queries records and verifies variables for the selected reservoir/event.

## Verified Public Dataset Candidate

| Source | What it provides | Planning implication |
|---|---|---|
| USGS Water Mission Area catalog: ResOpsUS | Daily storage, inflow, outflow, evaporation, and elevation variables where available; CONUS coverage; static public access through Zenodo | Strong public dataset candidate, but source is academic/curated rather than live operator data |
| Zenodo record: ResOpsUS Version 2 | Downloadable public zip; notes identify "ResOpsUS 2.csv" as most recent version; CC-BY 4.0 license | Modeling should avoid downloading the full zip unless needed; first check whether the selected reservoir can be extracted efficiently |
| Scientific Data descriptor | Peer-reviewed dataset description; 679 major reservoirs; daily resolution; data assembled from agencies/operators | Good citation source and methodology documentation |
| USGS low-storage anomaly data release | Storage percentiles, low-storage anomaly events, annual stats, and trends for selected ResOpsUS reservoirs | Useful if selected route is drought/low-storage failure |

## First Candidate Pass: Well-Documented But Too Complex

| Candidate | Failure or stress type | Public time-series evidence | Event/document evidence | Modeling simplicity | Notes |
|---|---|---|---|---|---|
| Lake Mendocino / Coyote Valley Dam, California | drought water-supply reliability plus flood-operation tradeoff | ResOpsUS candidate; CDEC COY station; USACE Coyote Valley monthly/daily operation reports | Sonoma Water FIRO pages document reduced reliability, outdated water-control rules, and FIRO improvements for drought/flood resilience | medium | Good documentation but more complex than desired because FIRO involves forecasts, water-control rules, and coordinated operations. |
| Lake Oroville, California | 2017 spillway/flood emergency | ResOpsUS candidate; CDEC ORO station has storage, inflow, outflow, river release, rain | DWR has detailed incident timeline and forensic-team pages | medium | Strong documented failure, but event mixes hydrology, infrastructure, emergency operations, and dam safety. Good backup for severe incident route. |
| Lake Mead / Hoover Dam, Nevada-Arizona | prolonged drought and shortage operation | USBR RISE has daily elevation, storage, release items; Lower Colorado River Operations page has historical/projection links | USBR shortage-condition news releases and 24-Month Studies document shortage triggers and operations | medium | Excellent drought route but multi-reservoir/legal allocation context may make "reason why fail" less simple. |
| Folsom Lake, California | flood-operation constraints, drought releases, and historical spillway gate failure | USBR RISE daily time series; USACE Folsom water data; Reclamation Central Valley Operations reports | USBR Folsom FAQ explains release decisions, flood operations, drought releases, and operating constraints | medium | Good official data. The 1995 gate failure is a clearer infrastructure failure but cause diagnosis may need maintenance/engineering data not in time series. |

## Second Candidate Pass: Smaller, Simpler Reservoirs

This pass uses the USGS low-storage anomaly data release built on ResOpsUS.
Planning-screening files were downloaded to
`../artifacts/data/candidate-source-scan/`:

- `reservoir_metadata.csv`
- `reservoir_1981_2020_weibull_jd_drought_properties.csv`
- `reservoir_1981_2020_operating_curve_drought_properties.csv`
- `reservoir_1981_2020_weibull_jd_trends.csv`

These are candidate-screening artifacts only. They do not count as acquired
Modeling data until the chosen reservoir is formally acquired and checked.

| Candidate | Why simpler | USGS/ResOpsUS signal from candidate files | Official source support | Decision |
|---|---|---|---|---|
| Hords Creek Lake / Hords Creek Dam, Texas | Very small single reservoir; TWDB describes it as one of the smallest Corps projects in Texas; purposes are flood control, water supply, and recreation | ResOpsUS/USGS Dam_ID 1249; main use marked recreation; capacity 60.8 MCM; longest 10th-percentile low-storage anomaly is 897 days from 1983-12-21 to 1986-06-04; also events in 2011-2012 | TWDB Water Data for Texas gives current and historical storage plus CSV downloads; TWDB project page gives purpose, capacity, conservation pool, flood pool, drainage area; USACE water data gives current elevation/inflow/outflow | recommended |
| Clark Canyon Reservoir, Montana | Single Reclamation irrigation reservoir with long daily official records | Dam_ID 362; main use irrigation; capacity 217.8 MCM; one 10th-percentile low-storage anomaly from 2001-08-22 to 2005-08-21 | USBR RISE provides daily storage, inflow, release, elevation; Reclamation testimony documents drought management concerns for Clark Canyon users | backup |
| Gillham Lake, Arkansas | Small USACE reservoir, local rather than basin-scale; clear public data and project page | Dam_ID 1122; main use flood control; highly variable storage; longest 10th-percentile low-storage anomaly is 139 days in 2012 | USACE Little Rock District page describes authorized purposes and links water levels; USACE water data page exposes elevation, inflow, outflow, and storage | backup |
| Pactola Reservoir, South Dakota | Single water-supply reservoir with explicit public threshold rules | Dam_ID 882; main use water supply; capacity 173.8 MCM; 734-day and 727-day 10th-percentile low-storage anomalies | USACE/USBR data exist; Rapid City documents water restrictions tied to reservoir level and inflow thresholds | backup, more policy than Hords Creek |
| Lake Abilene, Texas | Ultra-simple storage-only drought case | Not found in the USGS low-storage candidate metadata under this name | TWDB Water Data for Texas shows very low storage and TPWD documents that the reservoir went dry in 2014 | optional if we accept non-ResOpsUS and storage-only modeling |

## Recommended First Route

Recommended candidate for the first prototype: **Hords Creek Lake / Hords Creek Dam, Texas**.

Reason:

- It is much less complex than Lake Mead, Oroville, Folsom, or Mendocino.
- It is a small single reservoir rather than a large multi-reservoir system.
- The first failure/stress concept can be low-storage drought stress, using an
  official USGS anomaly label rather than an ambiguous catastrophic failure
  diagnosis.
- ResOpsUS/USGS candidate files already identify low-storage anomaly windows.
- TWDB and USACE give official reservoir context and public time-series access.
- The first model can be simple: detect low-storage anomaly, explain with
  storage trajectory, inflow/outflow/release where available, and contextual
  drought/precipitation variables.

Recommended initial failure-mode framing:

> Detect and diagnose low-storage operation stress for a small public reservoir,
> using daily storage as the primary signal and inflow/outflow or climate context
> as explanatory drivers.

## Alternative Route If User Wants a More Dramatic Failure Case

Choose **Lake Oroville 2017** if the goal is a clear emergency/failure incident.
The model would focus on event-window anomaly detection around February 2017 and
diagnosis would remain limited to documented hydrologic, structural, operational,
and management contributing factors. This route is higher risk because time
series alone cannot fully diagnose spillway structural failure.

## Decision Needed

Choose the first reservoir/failure route for the Planning package:

1. Hords Creek Lake low-storage/drought stress - recommended for first prototype.
2. Clark Canyon Reservoir drought allocation stress - good official inflow/storage/release data, still modestly more complex.
3. Gillham Lake low-storage anomaly - simple USACE setting, good backup.
4. Pactola Reservoir water-restriction trigger - clear threshold rules, but more policy/municipal context.
5. Lake Abilene severe low-storage case - ultra-simple storage-only case, likely outside ResOpsUS.

## Sources Checked

- USGS ResOpsUS catalog: https://water.usgs.gov/catalog/datasets/f1bb6ddc-faa4-4e3b-883d-de3ac02c116c/
- Zenodo ResOpsUS: https://zenodo.org/records/6612040
- ResOpsUS Scientific Data article: https://www.nature.com/articles/s41597-022-01134-7
- USGS low-storage anomaly data release: https://www.usgs.gov/data/metrics-characterizing-periods-anomalously-low-water-storage-selected-reservoirs-conterminous
- Sonoma Water FIRO: https://www.sonomawater.org/firo
- Sonoma Water current water supply levels: https://www.sonomawater.org/current-water-supply-levels
- CDEC Lake Mendocino/COY: https://cdec.water.ca.gov/river/res_COY.html
- USACE Coyote Valley Dam report: https://www.spk-wc.usace.army.mil/fcgi-bin/monthly.py?report=coy
- DWR Oroville incident background: https://water.ca.gov/Programs/State-Water-Project/SWP-Facilities/Oroville/Oroville-Spillways/Background
- DWR Oroville forensic team: https://water.ca.gov/Programs/State-Water-Project/SWP-Facilities/Oroville/Oroville-Spillways/Forensic-Team
- CDEC Oroville/ORO: https://cdec.water.ca.gov/dynamicapp/QueryF?s=ORO
- USBR Lower Colorado River Operations: https://www.usbr.gov/lc/riverops.html
- USBR RISE Lake Mead daily elevation item: https://data.usbr.gov/catalog/4370/item/6123
- USBR Folsom RISE release item: https://data.usbr.gov/catalog/2304/item/10780
- USBR Folsom FAQ: https://www.usbr.gov/mp/docs/folsom-dam-and-reservoir-faq-draft.pdf
- USGS low-storage anomaly data release: https://data.usgs.gov/datacatalog/data/USGS%3A6425e918d34e370832ff618e
- TWDB Hords Creek Lake page: https://www.twdb.texas.gov/surfacewater/rivers/reservoirs/hords_creek/index.asp
- Water Data for Texas Hords Creek Lake: https://waterdatafortexas.org/reservoirs/individual/hords-creek
- USACE Hords Creek water-control manual candidate: https://water.usace.army.mil/cda/documents/wc/3335/HORDS%20CREEK%20DAM%20AND%20LAKE%20.pdf
- USBR Clark Canyon daily release item: https://data.usbr.gov/catalog/2264/item/242
- Reclamation drought testimony mentioning Clark Canyon drought tier: https://www.usbr.gov/newsroom/congressional-testimony/4241
- USACE Gillham Lake official page: https://www.swl.usace.army.mil/Missions/Recreation/Lakes/Gillham-Lake/Dam-and-Lake-Information/
- Rapid City Pactola restriction notice: https://www.rcgov.org/rapid-city-news-room/pactola-water-levels-lack-of-snowpack-lead-rapid-city-to-enact-water-restrictions-april-1-15260.html
- TWDB Lake Abilene Water Data for Texas page: https://waterdatafortexas.org/reservoirs/individual/abilene
