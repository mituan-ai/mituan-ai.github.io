---
title: "Intelligent Transformation and State Recognition for Blast-Furnace Iron Tapping"
date: "2022-12-01"
summary: "An end-to-end system for molten-iron level tracking, tapping-state recognition, industrial communication, and digital-twin visualization."
tags:
  - "Intelligent Metallurgy"
  - "State Recognition"
  - "Digital Twin"
tech_stack:
  - "Bi-GRU"
  - "Post-Processing Classifier"
  - "Industrial Communication"
  - "Web Platform"
status: "Completed"
featured: true
image:
  filename: featured.webp
  caption: "Anonymous blast-furnace iron-tapping system architecture."
  focal_point: "Center"
  preview_only: true
links:
  - type: custom
    url: "/publications/zong-2023-irontapping/"
    label: "IEEE Sensors Journal"
    icon: "hero/document-text"
  - type: custom
    url: "/publications/zong-2023-judgment/"
    label: "PNSMI paper"
    icon: "hero/document-text"
---

The system combines field instrumentation and communication with molten-iron level tracking, Bi-GRU state recognition, post-processing, and an operator interface. The industrial partner and furnace identifiers are omitted from the public version.

![Anonymous blast-furnace iron-tapping system architecture](system.svg)

## Technical focus

- continuous extraction of level-related process signals;
- temporal state recognition using a Bi-GRU composite model;
- post-processing rules for stable tapping-state decisions;
- integration of algorithm services with industrial data and visualization.

## Public outputs

The work led to two first-author journal articles and the first-inventor patent **CN116678473B**, which covers a method for judging the tapping state of a blast-furnace hot-metal ladle.
