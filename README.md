# Trust-Aware Fusion of Heterogeneous Security Evidence for IoT Intrusion Detection under Simulated Evidence Manipulation

This repository accompanies the manuscript:

**Trust-Aware Fusion of Heterogeneous Security Evidence for IoT Intrusion Detection under Simulated Evidence Manipulation**

It contains the executable research notebooks, a machine-readable snapshot of the centralized research configuration, and the publication figures and corrected stress-test summary table supplied with the Round 2 manuscript package.

## Repository contents

```text
.
├── README.md
├── LICENSE_STATUS.txt
├── requirements.txt
├── configs/
│   └── experiment_config.json
├── notebooks/
│   ├── trust_aware_fusion_pipeline.ipynb
│   └── fusion_robustness_evaluation.ipynb
├── demo/
│   └── verify_paper_assets.py
├── docs/
│   └── REPRODUCIBILITY.md
└── results/
    └── paper_assets/
        ├── figures/
        └── tables/
            └── corrected_stress_breakdown.csv
```

## Main executable notebook

`notebooks/trust_aware_fusion_pipeline.ipynb` is the integrated executable research workflow supplied for the revised manuscript. It includes data acquisition/provenance and validation, leakage-aware preprocessing, detector experiments, evidence generation, trust-aware fusion variants, reviewer-requested analyses, and the corrected held-out-test and counterfactual evaluation protocol.

`notebooks/fusion_robustness_evaluation.ipynb` is retained as a separate supplementary notebook for the dedicated robustness experiments. It is not a replacement for the integrated main notebook.

Earlier development snapshots are intentionally not included as release notebooks. The integrated pipeline is the primary implementation; the supplementary notebook contains additional robustness experiments.

## Dataset

The experiments use the publicly available **CICIoT2023** dataset.

- Official dataset page: https://www.unb.ca/cic/datasets/iotdataset-2023.html
- Dataset paper DOI: https://doi.org/10.3390/s23135941

The dataset itself is **not redistributed** in this repository. Obtain it from the official source and follow its terms of use. Review the dataset path and configuration before running the notebook.

## Reproducing the corrected evaluation

The manuscript reports a final held-out test partition of 4,000 observations and a corrected counterfactual stress evaluation of 720,000 scenarios:

- 4,000 held-out observations
- 3 targeted evidence sources
- 4 evidence-manipulation mechanisms
- 5 intensity levels
- 3 trust variants (Fixed, Adaptive, Robust)

The integrated notebook's corrected evaluation section implements this protocol, restores the same pre-observation reliability state for counterfactual scenarios, and checks state isolation and order invariance. On successful execution, it writes detailed corrected evaluation outputs beneath `results/corrected_evaluation/` and creates `corrected_evaluation_results.zip`.

The manuscript also distinguishes an earlier 600,000-row validation-stage diagnostic from the corrected 720,000-scenario held-out-test protocol. These are different analyses and must not be conflated. The earlier diagnostic is not represented here as the final corrected stress-test result.

## Configuration and environment

`configs/experiment_config.json` is a machine-readable snapshot of the research configuration. The integrated notebook contains the executable `CONFIG` definition and remains authoritative if later reviewer-specific notebook cells override or refine a setting. The JSON file is provided for inspection and configuration documentation; it is not automatically loaded by the notebook.

The notebook records its runtime and package versions and sets a reproducibility seed. Core dependencies are listed in `requirements.txt`. PyTorch, Transformers, Accelerate, and OpenAI are optional paths and should only be installed when needed by the selected execution path.

The notebook was developed for a Kaggle-style notebook runtime and may require adaptation of dataset paths, available compute resources, and package versions elsewhere. A GPU is useful for the neural detector path, but the notebook also detects available hardware.

## Quick start

1. Clone or download this repository.
2. Obtain CICIoT2023 from the official dataset source.
3. Open `notebooks/trust_aware_fusion_pipeline.ipynb` in Kaggle or a compatible Jupyter environment.
4. Review and update the notebook's `CONFIG` dataset path for your environment. Consult `configs/experiment_config.json` as the accompanying configuration snapshot.
5. Install the dependencies from `requirements.txt` (or use the notebook's dependency check for missing core packages).
6. Execute the notebook from top to bottom.
7. Inspect the generated `results/` artifacts and the final reviewer requirement gate.

For an integrity check of the included publication summary table and figure files, run:

```bash
python demo/verify_paper_assets.py
```

## Scope and interpretation

The robustness experiments evaluate the **post-detection evidence-fusion layer** by simulating corruption of `SecurityEvidence` objects. They do not establish end-to-end adversarial robustness against real network traffic, feature manipulation, data poisoning, detector-level attacks, or attacks on the underlying network stack.

The taxonomy-based semantic channel depends on the Random Forest canonical-category prediction; evidence channels should therefore not be interpreted as statistically independent.

## Results included in this repository

`results/paper_assets/` contains the figures distributed with the corrected Round 2 manuscript package and the corrected stress-test breakdown table. The full scenario-level corrected evaluation result archive is generated by executing the integrated notebook. It was not included in the supplied repository-assembly files, so this archive is not fabricated or replaced with older diagnostic outputs.

## Code Availability

The complete research implementation is publicly available through GitHub and has been archived on Zenodo as a permanent versioned release.

- **GitHub Repository:** https://github.com/aeyouseff/TrustAwareEvidenceFusion
- **Version:** v1.0.0
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.24100757

The release includes the integrated executable research pipeline, supplementary fusion robustness evaluation notebook, experiment configuration files, demonstration scripts, publication figures, evaluation summaries, and reproducibility documentation.

The CICIoT2023 dataset is not redistributed in this repository and must be obtained directly from its official source.

The archived Zenodo release provides a permanent reference to the research software version associated with this manuscript.
