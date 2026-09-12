# ALC ICP Definition — Locked 2026-09-08

## Ideal Customer Profile (ICP)

**Business:** ALC Consulting

### Primary ICP: Military-to-Civilian Transition

**Who:**
- Separating or recently separated military officers (O3–O6) and senior NCOs (E7–E9)
- 1–3 years from transition or within 2 years post-separation
- Target sectors: defense contracting, government consulting, corporate leadership

**Pain Points:**
- Translating military experience to civilian resume/interview language
- Navigating federal hiring processes (USAJobs, clearance leverage)
- No civilian professional network
- Benefits navigation (GI Bill, VA, TSP rollover)

**Decision Criteria:**
- Trust: referred by peer or former colleague
- Credibility: consultant has military background
- ROI: clear path to role + compensation outcome

### Secondary ICP: Small Business / Consulting Firms
- 5–50 person firms needing AI workflow automation
- Decision maker is owner or COO
- Pain: manual processes eating billable hours

## Prospect Schema Fields
- `name`, `rank_or_title`, `branch`, `mos_or_afe`, `separation_date`
- `target_sector`, `clearance_level`, `location`, `linkedin_url`
- `source`, `icp_score`, `last_contact`, `stage`

## ML_FEATURES Spec
*(Placeholder — to be defined with Wolverine in Phase 2)*
- Features: days_to_separation, clearance_level_numeric, sector_match_score, network_gap_score
- Target: icp_score (0–100)
