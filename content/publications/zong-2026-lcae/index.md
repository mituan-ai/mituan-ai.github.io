---
title: "LLM-Guided Contextual Action Evaluation for Operational Decisions in Industrial Processes"
authors:
  - youcheng-zong
  - Runda Jia
  - Dakuo He
date: "2026-08-25T07:16:59Z"
publishDate: "2026-08-25T07:16:59Z"
publication_types: ["preprint"]
publication: "arXiv preprint arXiv:2608.24156"
publication_short: "arXiv"
abstract: >-
  LLM-Guided Contextual Action Evaluation (LCAE) uses industrial documents to construct a semantic representation of actions for operational decisions. Before training, an LLM extracts a fixed basis describing which observations an action affects, the effect direction, and the response delay. Recent numerical action-response history adjusts relation strengths, and candidate actions are represented through a state-conditioned action-effect field. The critic evaluates this representation, while the actor uses the same relation gains to generate actions. Training and deployment require no online LLM or embedding-model calls. The approach investigates whether documented action relations, conditioned on recent process history, provide a more useful decision bias than raw action coordinates.
summary: "Document-derived action relations and recent process history support contextual action evaluation for industrial operational decisions."
tags:
  - Industrial Decision Support
  - Action Semantics
  - Reinforcement Learning
featured: true
links:
  - type: custom
    url: https://arxiv.org/abs/2608.24156
    label: arXiv
    icon: academicons/arxiv
image:
  filename: featured.webp
  caption: "LCAE overview: offline semantic construction, history-conditioned relation gains, and action-effect composition."
  focal_point: "Center"
  preview_only: false
projects: []
slides: ""
---
