---
title: ""
summary: ""
date: "2026-05-04"
type: "landing"
sections:
  - block: "resume-biography-3"
    content:
      username: "youcheng-zong"
      text: |
        My recent work includes LLM-driven human-AI collaborative decision
        support for metallurgical processes, adaptive temperature trend
        prediction in ladle preheating, random-forest-based pressure prediction
        for manufacturing, blast furnace iron-tapping state recognition, and
        data-driven analysis of continuous casting and metallurgical processes.
      headings:
        about: "About"
        education: "Education"
        interests: "Research Interests"
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: "md"
      avatar:
        size: "large"
        shape: "circle"
    ce: "section-a8a3a0ad"
    id: "biography"
    As: "section-7668f1bc"
  - block: "markdown"
    content:
      title: "Research"
      subtitle: ""
      text: |-
        I work on data-driven and LLM-assisted intelligence for complex
        industrial processes, with a particular focus on metallurgy, process
        decision support, adaptive prediction, and industrial time-series
        modeling.
    design:
      columns: "1"
    ce: "section-7fbe6595"
    id: "research"
    As: "section-f89358aa"
  - block: "collection"
    content:
      title: "Featured Publications"
      filters:
        folders:
          - "publications"
        featured_only: true
    design:
      view: "article-grid"
      columns: 3
    ce: "section-papers"
    id: "papers"
    As: "section-5847d5ef"
  - block: "collection"
    content:
      title: "Publications"
      text: ""
      filters:
        folders:
          - "publications"
        exclude_featured: false
        featured_only: true
      count: 5
      sort_by: "Date"
      archive:
        enable: true
      order: "desc"
    design:
      view: "citation"
      fill_image: true
    ce: "section-2dca0dee"
    id: "publications"
    As: "section-1a3c413c"
---
