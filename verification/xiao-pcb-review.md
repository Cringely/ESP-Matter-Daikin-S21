# Task 9: Delegated PCB DFM review — xiao-carrier

Reviewer: pcb-dfm-reviewer agent (trusted tier, kicad-cli 10.0.4 + pcbnew geometry
extraction). Board at commit `cab059d`. Gate state reviewed: DRC 0 errors /
0 unconnected / 315 warnings; schematic parity 13 informational items.

## Verdict

READY-WITH-FIXES. Board fabricates and functions as reviewed; two required
cleanups applied before gerber export (see dispositions).

## Findings and dispositions

| # | Finding | Severity/conf | Disposition |
|---|---------|---------------|-------------|
| F1 | 124 vias on 39 unique locations: 17 GND stitch points carry 6 co-located vias each (85 redundant drill hits, all 199 holes_co_located warnings) | medium/high | FIX before gerbers: dedupe to one via per location |
| F2 | Dangling 4.87mm 0.3mm stub on /5V_BUCK F.Cu (183.432,100.262)-(179.989,103.705), unterminated | medium/high | FIX before gerbers: delete stub |
| F3 | SW node U1.2-L1.1 = 5.58mm (TPS562246 wants short); EMC margin concern near 2.4GHz radio; no measurement data | medium/medium | ACCEPTED for rev 1 (watch item). Respin note: pull L1 against U1 SW pin. Carried to Task 10 verification doc |
| F4 | Silk crowding: refdes R11/R10/D5/J2/F1 over neighbor pads; no polarity band or pin-1 marker obscured | low/high | Optional cosmetic nudge; fab clips silk off copper automatically |
| F5 | U2 refdes below DRU text minimums; outline arc clipped at antenna overhang (expected) | low/high | Accepted, cosmetic |
| F6 | U2.12 pad vs 3V3 via drill-to-drill < 0.254mm, same net | low/high | Accepted, electrically harmless |
| F7 | Parity: "no pad for pin 15-24" on U2 (unlanded XIAO symbol pins; all needed rails on pads 7/8/12/13/14) | low/high | Accepted, known-benign since Task 7 |
| F8 | Parity: 3 blank Description/Datasheet fields on PCB | low/high | Accepted, metadata |
| F9 | 25 lib_footprint_issues: fp-lib-table config gaps; footprints embedded | low/high | Accepted, no fab impact |
| F10 | GND pours solid-connect (no thermal relief): good for reflow/thermal, harder hand-rework | low/high | Conscious choice, accepted |
| F11 | No mounting holes; J2 + enclosure fixation | low/high | Design choice, flagged for mechanical |
| F12 | Confirm board-setup copper-to-edge >= 0.25mm before export | low/low | Verified at fix time |

## Requirement verifications (all confirmed)

- Antenna keep-out: zero copper inside H-polygon both layers (point-in-polygon
  test). Extent ~6.48mm from module tip vs ~5mm ceramic antenna region:
  conservative. No official Seeed keep-out dimension exists (3rd search
  confirms); extent adequacy medium confidence by construction.
- D5 SMF15A: pad1 cathode = V_in, pad2 anode = GND. Correct unidirectional
  TVS orientation, 15V standoff over 12V rail.
- D6 Schottky: anode = /5V_BUCK, cathode = /VBUS; blocks USB backfeed;
  D6.1 -> C20.1 -> U2.14 path intact.
- Trace widths: min 0.2mm, power 0.3mm; ample for 0.5A/5V and fused 12V input
  (IPC-2152 margins large).
- Annular rings 0.15mm, drills >= 0.3mm via / 0.889mm PTH: above OSH Park and
  JLCPCB floors. XIAO mounts on interior dual PTH+SMD pads, no edge-plating risk.
- Pour/return: GND both layers (632/688 mm^2), 17 stitch points, adequate for
  2.4GHz return path.
- 12V creepage: non-issue, no mains.

Evidence artifacts: session scratchpad (drc-native.json, parity.json,
keepout.py, analyze.py, trace.py, u2pads.py, zones2.py, layer SVGs).
