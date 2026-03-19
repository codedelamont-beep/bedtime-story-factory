# 🔄 Workflow Diagram — Full Pipeline

## Overview

```mermaid
graph TD
    START["🌙 /story-pipeline 'theme'"] --> S1

    subgraph WF1["Workflow 1: Discovery"]
        S1["/story-research"] --> S2["/story-concept"]
        S2 --> S3["/originality-check"]
    end

    subgraph WF15["Workflow 1.5: Bridge"]
        S3 --> S35["/story-bridge"]
        S35 -->|"GO ✅"| WF2
        S35 -->|"MODIFY ⚠️"| S35FIX["Apply suggestions"]
        S35FIX --> S35
        S35 -->|"SKIP ❌"| SKIP["Remove from batch"]
    end

    subgraph WF2["Workflow 2: Production"]
        S4["/story-writing<br/>→ _v0_draft.md"]
    end

    subgraph WF3["Workflow 3: Quality"]
        S5["/story-review<br/>→ _v1_reviewed.md"]
        S5 -->|"Score < 8"| S5FIX["Implement fixes"]
        S5FIX --> S5
        S5 -->|"Score ≥ 8 ✅"| S6
        S6["/story-improvement-loop<br/>→ _v2_improved.md"]
        S6 -->|"Score < 9"| S6FIX["Polish fixes"]
        S6FIX --> S6
        S6 -->|"Score ≥ 9 ✅"| WF4
    end

    subgraph WF4["Workflow 4: Output"]
        S7["/story-illustrate<br/>→ Midjourney prompts"]
        S7 --> S8["/story-export<br/>→ EPUB + KDP"]
    end

    WF2 --> WF3
    WF4 --> DONE["📚 Production Report"]

    style START fill:#1a237e,stroke:#333,color:#fff
    style DONE fill:#1b5e20,stroke:#333,color:#fff
    style SKIP fill:#b71c1c,stroke:#333,color:#fff
```

## Decision Points

```mermaid
graph LR
    subgraph "Decision Gates"
        G1["Gate 1<br/>AUTO_PROCEED?"]
        G2["Gate 2<br/>Bridge Score"]
        G3["Gate 3<br/>Review Score"]
        G4["Gate 4<br/>Human Checkpoint"]
        G5["Gate 5<br/>Improve Score"]
    end

    G1 -->|"true"| AUTO["Skip all checkpoints"]
    G1 -->|"false"| MANUAL["Pause for approval"]
    
    G2 -->|"≥ 7"| GO["GO → Write"]
    G2 -->|"5-6"| MOD["MODIFY → Fix → Re-check"]
    G2 -->|"< 5"| SKIP2["SKIP → Remove"]
    
    G3 -->|"≥ 8 READY"| APPROVE["Approved"]
    G3 -->|"6-7 ALMOST"| FIX["Fix → Re-review"]
    G3 -->|"< 6 NEEDS WORK"| REWRITE["Major rewrite"]
    
    G4 -->|"go"| ALL["All fixes"]
    G4 -->|"skip N"| PARTIAL["Skip fix N"]
    G4 -->|"stop"| PAUSE["Save state"]
    G4 -->|"custom: ..."| CUSTOM["Custom instructions"]
    
    G5 -->|"≥ 9 PUBLISH"| DONE2["Done → Illustrate"]
    G5 -->|"< 9 ALMOST"| POLISH["Polish → Re-check"]
```

## Version Flow

```mermaid
graph LR
    V0["v0_draft.md<br/>/story-writing"] 
    V1["v1_reviewed.md<br/>/story-review"]
    V2["v2_improved.md<br/>/story-improvement-loop"]
    V3["v3_final.md<br/>Approved for export"]
    
    V0 -->|"Review R1-R3"| V1
    V1 -->|"Improve R1-R2"| V2
    V2 -->|"Score ≥ 9"| V3
    
    V0 -.->|"preserved"| V0
    V1 -.->|"preserved"| V1
    V2 -.->|"preserved"| V2

    style V0 fill:#fff3e0,stroke:#e65100
    style V1 fill:#e3f2fd,stroke:#1565c0
    style V2 fill:#e8f5e9,stroke:#2e7d32
    style V3 fill:#f3e5f5,stroke:#6a1b9a
```

## State Files

```mermaid
graph TD
    PS["PIPELINE_STATE.json<br/>Current stage + story index"]
    RS["REVIEW_STATE.json<br/>Current round + score"]
    IS["IMPROVEMENT_STATE.json<br/>Current round + score"]
    NL["NOTIFICATION_LOG.md<br/>All sent notifications"]
    PE["PIPELINE_ERRORS.md<br/>Skipped stories + errors"]
    ST["SCORE_TRACKER.md<br/>All scores across rounds"]
    
    PS --> RS
    PS --> IS
    PS --> NL
    PS --> PE
    RS --> ST
    IS --> ST
```

## Timing (10 story batch)

```
22:00 ─── START ────────────────────────────────────────────
22:05 ─── Research + Concepts (Workflow 1) ─────────────────
22:10 ─── Originality Check ────────────────────────────────
22:15 ─── Bridge Validation (Workflow 1.5) ─────────────────
      │
22:15 ─── Writing Story 1 ─────────────┐
22:20 ─── Writing Story 2              │
22:25 ─── Writing Story 3              │ Workflow 2
22:30 ─── ...                          │ (batch)
23:00 ─── Writing Story 10 ────────────┘
      │
23:00 ─── Review Story 1 (R1→R2→R3) ──┐
23:10 ─── Review Story 2               │
23:20 ─── ...                          │ Workflow 3a
01:00 ─── Review Story 10 ─────────────┘
      │
01:00 ─── Improve Story 1 (R1→R2) ────┐
01:05 ─── Improve Story 2             │ Workflow 3b
01:10 ─── ...                          │ (skip if ≥9)
01:50 ─── Improve Story 7 ─────────────┘
      │
01:50 ─── Illustrate (batch) ──────────  Workflow 4
02:20 ─── Export (batch) ──────────────
02:25 ─── COMPLETE ─────────────────────────────────────────
```
