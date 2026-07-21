# OSH Park 6-mil DRC verification method (Task 8)

Artifact: `xiao-task8-6mil-drc.json` (kicad-cli 10.0.4, `pcb drc --severity-error`).
Result: 0 violations, 0 unconnected, 0 schematic parity issues.

Board under test: byte-identical copy of `Custom PCB esp32c6/esp32c6_daikin.kicad_pcb`
at commit `eda8131` (verified via `git show`). Only the rule files were patched, on
copies outside the repo:

- `.kicad_dru`: every clearance-class constraint minimum set to 0.1524 mm
  (OSH Park 6-mil): `clearance` (track spacing 0.127, track-to-pad 0.2,
  pad/via-to-pad/via 0.127), `hole_clearance` (0.254 NPTH / 0.33 PTH),
  `edge_clearance` (0.3), `hole_to_hole` (0.5 / 0.254).
- `.kicad_pro`: both netclass `clearance` values set to 0.1524 mm (netclass
  clearance can mask DRU rules, so both must be patched).

The committed board keeps the original JLCPCB-conservative rules (0.2 mm
track-to-pad etc.) and passes them natively (`xiao-task8-drc.json`). This
artifact proves the same board also passes at OSH Park's 6-mil
(0.1524 mm) capability floor.

Note: an earlier check patched only the DRU clearance floor and under-tested
(missed track-to-pad/hole/edge rules and netclass masking); this method
supersedes it.
