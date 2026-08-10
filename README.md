# OpsRCA AI

OpsRCA AI is an AI-assisted root cause analysis tool designed to help operations leaders turn incident information into a structured, actionable RCA.

## What It Does

The user provides:
- Incident description
- Relevant metrics or observations
- Known contributing factors
- Immediate actions taken

OpsRCA AI analyzes the information and generates a structured RCA that includes:
- Incident summary
- Known facts
- Potential contributing factors
- 5 Whys analysis
- Root cause assessment
- Corrective actions
- Preventive actions
- Missing information and follow-up questions
- Executive summary

The tool distinguishes known facts from hypotheses and avoids presenting unsupported assumptions as confirmed root causes.

## Technology

- Python
- Streamlit
- OpenAI API
- OpenAI Responses API
- Prompt engineering
- GitHub
- Streamlit Community Cloud

## How It Works

1. The user enters operational incident information.
2. The application structures the information into an RCA prompt.
3. The prompt is submitted to an AI model through the OpenAI API.
4. The model performs evidence-based RCA reasoning.
5. The structured analysis is displayed in the Streamlit interface.

## Demo

Live application:

https://ops-rca-ai.streamlit.app

A synthetic incident scenario is included in `sample_incident.md` for demonstration and testing.

## Safety and Data Handling

This public demonstration is intended for synthetic scenarios only.

Do not enter confidential, proprietary, personally identifiable, or sensitive operational information.

The application is an analytical support tool. AI-generated findings should be validated by a qualified human before operational decisions are made.

## Purpose

OpsRCA AI demonstrates how generative AI can support operational problem solving by accelerating initial incident analysis while maintaining human review and accountability.
