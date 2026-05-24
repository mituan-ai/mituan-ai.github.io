---
title: ""
summary: ""
date: "2026-05-04"
type: "landing"
sections:
  - block: "resume-biography-3"
    content:
      username: "youcheng-zong"
      text: |-
        I am a PhD student in Control Science and Engineering at Northeastern
        University, China. My research focuses on AI and large-model applications in complex industrial scenarios, with interests in industrial process modeling, multimodal perception, analysis, and decision support. I am strong at abstracting tasks from real problems, connecting data with models, and turning research results into verifiable, deployable systems.
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
        My research develops large-model systems for complex industrial and
        clinical settings where decisions must be grounded in process data,
        domain knowledge, and deployable software.

        - **Industrial LLM agents and decision support.** RAG, tool calling,
          Text2SQL, and human-in-the-loop workflows for production-facing
          reasoning and operational decisions.
        - **Semantic time-series modeling.** Methods that connect sensor
          sequences, task descriptions, and process semantics for adaptive
          prediction under changing operating conditions.
        - **Application-grounded AI.** Metallurgical process intelligence
          remains the main application base, with selected work extending
          multimodal perception and reasoning to oral mucosal medical analysis.
    design:
      columns: "1"
    ce: "section-7fbe6595"
    id: "research"
    As: "section-f89358aa"
  - block: "resume-experience"
    content:
      username: "youcheng-zong"
    design:
      date_format: "Jan 2006"
      is_education_first: true
    ce: "section-experience"
    id: "experience"
    As: "section-experience"
  - block: "collection"
    content:
      title: "Publications"
      text: ""
      filters:
        folders:
          - "publications"
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
  - block: "collection"
    content:
      title: "Research Highlights"
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
---
