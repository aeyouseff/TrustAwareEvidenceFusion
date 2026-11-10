# Reproducibility notes

## Primary source of implementation

Use `notebooks/trust_aware_fusion_pipeline.ipynb` as the integrated executable research workflow. The notebook is preserved with its code and recorded cell outputs from the supplied Round 2 repository package. It includes the central `CONFIG` definition and later reviewer-specific evaluation refinements.

`configs/experiment_config.json` is a machine-readable snapshot of the centralized `CONFIG` object. It is provided for inspection and documentation; the notebook does not automatically load this JSON file. If later reviewer-specific notebook cells override or refine a parameter, the executable notebook section is authoritative for that analysis.

## Dataset handling

CICIoT2023 is external and is not included. Download it from the official CIC dataset page: https://www.unb.ca/cic/datasets/iotdataset-2023.html. Configure the dataset path in the notebook's `CONFIG` for the runtime being used. Do not commit the raw dataset, credentials, private keys, or data that the authors are not authorized to redistribute.

## Corrected evaluation outputs

The integrated notebook's corrected evaluation section creates the final held-out-test and counterfactual artifacts under `results/corrected_evaluation/`. Its final execution step packages these as `corrected_evaluation_results.zip`.

Expected protocol checks described by the manuscript/notebook:
- 4,000 held-out observations.
- 720,000 counterfactual scenario rows.
- 3 targeted evidence sources.
- 4 manipulation mechanisms.
- 5 intensity levels.
- 3 trust variants.
- 0 counterfactual state-isolation failures.
- 0 order-dependent counterfactual decisions.

These are protocol expectations to be verified by executing the notebook; this documentation does not substitute for a fresh run or claim that a fresh run was performed when assembling this archive.

## Earlier diagnostic vs. corrected protocol

The manuscript retains an earlier 600,000-row validation-stage diagnostic as historical context. It is distinct from the corrected 720,000-scenario held-out-test evaluation. Do not report the earlier diagnostic as the final corrected protocol.

## Runtime caveats

The main notebook was prepared in a Kaggle-style environment. Paths, available RAM/GPU, package compatibility, and dataset file discovery may need adjustment on other platforms. Record the actual environment used for any reproduction attempt.

## Manuscript code-availability alignment

The supplied Round 2 manuscript currently says that the notebook is available from the corresponding author upon reasonable request. Keep that statement until the repository has actually been made public. After publication, replace it with the real GitHub URL and, if archived, the real Zenodo DOI. Do not insert a placeholder URL or claim public availability before release.
