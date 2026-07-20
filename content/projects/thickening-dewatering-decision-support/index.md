---
title: "Digital-Twin and LLM Decision Support for Thickening–Dewatering"
date: "2026-03-01"
summary: "An operational workflow linking field measurements, condition recognition, a process digital twin, and controlled LLM tools."
tags:
  - "Industrial AI"
  - "Decision Support"
  - "Digital Twin"
tech_stack:
  - "RAG"
  - "Text2SQL"
  - "Tool Calling"
  - "Process Monitoring"
status: "Completed"
featured: true
links:
  - type: custom
    url: "/publications/zong-2026-roam/"
    label: "Related paper"
    icon: "hero/document-text"
---

This project developed an operational decision-support workflow for a thickening–dewatering line. It joins field measurements, condition recognition, a process digital twin, and an LLM layer with retrieval, Text2SQL, and controlled tool use. The public description omits the industrial partner, site, and operating values.

![Anonymous thickening–dewatering system architecture](system.svg)

## System scope

- process-data access and online condition recognition;
- a digital representation of the thickening–dewatering equipment;
- retrieval over technical documents and structured production data;
- tool-mediated analysis with the operator retained in the decision loop.

## Research connection

The project supplied an application setting for work on specialist-model adaptation under operating shifts. The associated preprint presents the method and evaluation protocol without exposing production identifiers.
