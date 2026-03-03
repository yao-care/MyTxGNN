/*
 * MyTxGNN Drug Repurposing CQL Library
 *
 * This Clinical Quality Language (CQL) library provides logic for
 * identifying drug repurposing opportunities based on TxGNN predictions.
 *
 * Version: 1.0.0
 * Author: MyTxGNN Team
 * Last Updated: 2026-03-03
 */

library DrugRepurposingLibrary version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1' called FHIRHelpers

// Value Sets
valueset "TxGNN Predicted Drugs": 'http://mytxgnn.yao.care/ValueSet/txgnn-predicted-drugs'
valueset "Active Medication Status": 'http://terminology.hl7.org/ValueSet/medicationrequest-status'

// Code Systems
codesystem "DrugBank": 'http://drugbank.ca'
codesystem "SNOMED-CT": 'http://snomed.info/sct'

// Parameters
parameter "MinimumPredictionScore" Decimal default 0.7
parameter "EvaluationPeriod" Interval<DateTime> default Interval[@2026-01-01, @2026-12-31]

// Context
context Patient

// Definitions

/*
 * Active Medications
 * Retrieves all active medication requests for the patient
 */
define "Active Medications":
  [MedicationRequest] MR
    where MR.status in {'active', 'completed'}
    and MR.intent = 'order'

/*
 * Medications with DrugBank ID
 * Filters medications that have a DrugBank identifier
 */
define "Medications with DrugBank ID":
  "Active Medications" MR
    where exists(
      MR.medication.coding C
        where C.system = 'http://drugbank.ca'
    )

/*
 * TxGNN Predicted Medications
 * Identifies medications that have TxGNN repurposing predictions
 */
define "TxGNN Predicted Medications":
  "Medications with DrugBank ID" MR
    where MR.medication.coding.code in "TxGNN Predicted Drugs"

/*
 * Patient Conditions
 * Retrieves active conditions for the patient
 */
define "Patient Conditions":
  [Condition] C
    where C.clinicalStatus ~ 'active'

/*
 * Potential Repurposing Opportunities
 * Identifies potential drug repurposing opportunities based on
 * patient's current medications and conditions
 */
define "Potential Repurposing Opportunities":
  "TxGNN Predicted Medications" MR
    where exists(
      "Patient Conditions" C
        where HasRepurposingPrediction(MR.medication, C.code)
    )

/*
 * Helper function to check if a drug has a repurposing prediction
 * for a given condition
 */
define function HasRepurposingPrediction(medication CodeableConcept, condition CodeableConcept):
  // This would be implemented with actual TxGNN prediction lookup
  // For now, returns true if medication has DrugBank ID
  exists(
    medication.coding C
      where C.system = 'http://drugbank.ca'
  )

/*
 * High Confidence Predictions
 * Filters for predictions with score >= MinimumPredictionScore
 */
define "High Confidence Predictions":
  "Potential Repurposing Opportunities" MR
    // Additional filtering based on prediction score would go here
    return MR

/*
 * Clinical Trial Candidates
 * Identifies patients who might be candidates for clinical trials
 * based on their medications and conditions
 */
define "Clinical Trial Candidates":
  exists("High Confidence Predictions")
    and exists("Patient Conditions")

/*
 * Drug Interaction Alert Flag
 * Checks if any active medications have known interactions
 */
define "Has Potential Drug Interactions":
  Count("Active Medications") > 1

/*
 * Summary Report
 * Provides a summary of repurposing opportunities
 */
define "Repurposing Summary":
  Tuple {
    patientId: Patient.id,
    activeMedicationCount: Count("Active Medications"),
    predictedMedicationCount: Count("TxGNN Predicted Medications"),
    opportunityCount: Count("Potential Repurposing Opportunities"),
    hasTrialCandidacy: "Clinical Trial Candidates",
    hasDrugInteractionRisk: "Has Potential Drug Interactions"
  }
