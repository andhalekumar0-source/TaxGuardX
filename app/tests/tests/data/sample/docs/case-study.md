# TaxGuardX Case Study

## 1. Introduction

TaxGuardX is a defensive cybersecurity case-study project designed to demonstrate explainable risk analysis for fictional tax-related transactions.

The project focuses on input validation, rule-based anomaly detection, risk scoring, and security-oriented testing.

## 2. Problem Statement

Large-scale transaction systems may need mechanisms to identify unusual transaction patterns.

TaxGuardX demonstrates how predefined security signals can be evaluated and converted into an explainable risk score.

## 3. Project Objectives

The main objectives are:

- Validate transaction input
- Detect predefined suspicious patterns
- Calculate an explainable risk score
- Classify transaction risk
- Provide API-based analysis
- Demonstrate automated testing
- Document security considerations

## 4. Detection Signals

TaxGuardX currently evaluates:

1. Large transaction amount
2. Country mismatch
3. Multiple failed attempts
4. Duplicate transaction
5. High transaction velocity

## 5. Risk Scoring

Each detected signal contributes a predefined number of points.

```text
Large Amount       = 30
Country Mismatch   = 25
Failed Attempts    = 20
Duplicate          = 25
High Velocity      = 20
