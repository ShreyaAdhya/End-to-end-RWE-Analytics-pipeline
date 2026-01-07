# End-to-End Real-World Evidence (RWE) Analytics Pipeline using Healthcare data

## Overview
This project demonstrates an **end-to-end Real-World Evidence (RWE) analytics workflow** using healthcare data. The objective is to replicate how RWE analysts generate clinical and population-level insights from real-world data to support pharmaceutical research, clinical decision-making, and healthcare analytics.

The pipeline covers **data ingestion, cohort definition, epidemiological analysis, patient outcomes, predictive modeling, and interactive visualization**, following industry-standard RWE practices.

---

## Objectives
- Perform **retrospective observational analysis** using healthcare data  
- Estimate **disease prevalence and risk patterns** across patient subgroups  
- Analyze **patient outcomes and healthcare utilization**  
- Build **predictive and stratification models** to assess disease risk  
- Deliver insights via **reproducible code and interactive dashboards**

---

## Data Description
The project uses a **synthetic healthcare dataset** structured to resemble real-world data sources such as EHRs and claims.

### Key Domains
- Patient demographics (age, sex)
- Diagnoses (disease labels)
- Clinical risk factors (BMI, blood pressure, cholesterol, heart rate)
- Healthcare utilization proxies

> Note: Synthetic data is used to ensure privacy while preserving realistic analytical workflows.

---

## Study Design
- **Study Type:** Retrospective observational study  
- **Population:** Adult patients across multiple diagnosis classes  
- **Index Date:** First recorded observation in the dataset  
- **Outcomes of Interest:**  
  - Disease prevalence by age group  
  - Risk factor distributions  
  - Time-to-event (simulated) outcomes  
  - Disease prediction and risk stratification  

---

## Analytical Pipeline

### 1. Data Preparation & Quality Checks
- Loaded and validated structured healthcare data
- Assessed missingness and variable distributions
- Standardized features for downstream analysis

---

### 2. Epidemiology Analysis
- Estimated **disease prevalence across age strata**
- Compared prevalence patterns across diagnosis classes
- Generated population-level summaries to support descriptive epidemiology

---

### 3. Outcomes & Time-to-Event Analysis
- Constructed **time-to-event variables** (simulated follow-up)
- Applied **Kaplan–Meier survival analysis** to compare patient trajectories
- Demonstrated outcome analysis commonly used in RWE studies

---

### 4. Risk Factor & Predictive Modeling
- Built **logistic regression models** to assess associations between clinical risk factors and disease occurrence
- Developed **decision tree models** for interpretable patient risk stratification
- Evaluated model performance using standard classification metrics

---

### 5. Patient Subgroup Discovery
- Applied **unsupervised clustering (KMeans)** to identify patient subgroups based on clinical profiles
- Characterized clusters to understand heterogeneity in patient populations

---

### 6. Interactive Visualization
- Delivered insights through a **Streamlit-based dashboard**
- Enabled cohort filtering, summary statistics, and exploratory analysis
- Demonstrated product-oriented RWE delivery for clinical and internal stakeholders

---

## Key Insights (Illustrative)
- Disease prevalence increases with age across multiple diagnosis categories
- Certain clinical risk factors show stronger associations with disease presence
- Distinct patient subgroups emerge based on combined risk profiles
- Predictive models provide interpretable risk stratification signals

---

## Limitations
- Synthetic dataset limits external validity
- Simplified outcome definitions
- Time-to-event analysis uses simulated follow-up durations

---

## Relevance to Real-World Evidence (RWE)
This project mirrors real-world RWE workflows used in:
- Pharmaceutical research
- Healthcare analytics
- Clinical insights generation
- Observational study design
- Evidence synthesis for decision-making

The pipeline demonstrates **end-to-end ownership of RWE analytics**, from raw healthcare data to actionable insights and visualization.

---

## Future Extensions
- Integration of claims or longitudinal EHR data
- Validation against published epidemiological studies
- Advanced survival and causal inference methods

---

## How to Run
```bash
python analysis/epidemiology.py
python analysis/outcomes.py
python analysis/modeling.py
streamlit run app/dashboard.py
