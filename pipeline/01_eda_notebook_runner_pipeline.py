"""
EDA Notebook Runner Pipeline.
Executes a sequence of Jupyter notebooks for exploratory data analysis (EDA)
in a predefined order. Each notebook is executed in-place, enabling a
step-by-step data analysis workflow.
"""
import os
EDA_NOTEBOOK_PATH = "notebooks/01_eda"
eda_steps = [
    "01_data_overview.ipynb",
    "02_univariate_analysis.ipynb",
    "03_time_series_analysis.ipynb",
    "04_correlation_analysis.ipynb",
    "05_return_and_risk_analysis.ipynb",
    "06_visualization_generation_and_saving.ipynb",
    "07_visualization_preview.ipynb",
    "08_summary.ipynb",
    "09_summary_pdf_generation_and_saving.ipynb",
    "10_overall_data_merging_and_saving.ipynb"
]
def run_notebook(notebook_path):
    """
    Execute a single Jupyter notebook.
    Runs the notebook in-place using nbconvert and returns execution status.
    Args:
        notebook_path (str): Path to the notebook file.
    Returns:
        bool: True if execution succeeds, False otherwise.
    """
    print(f"\n Running: {notebook_path}")
    exit_code = os.system(
        f"jupyter nbconvert --to notebook --execute --inplace {notebook_path}"
    )
    if exit_code != 0:
        print(f"Error running {notebook_path}")
        return False
    print(f"Completed: {notebook_path}")
    return True
def run_eda_pipeline():
    """
    Execute the complete EDA pipeline.
    Iterates through all defined EDA notebooks and executes them sequentially.
    Stops execution if any notebook fails.
    Returns:
        None
    """
    print("\n==============================")
    print("STARTING EDA PIPELINE")
    print("==============================\n")
    for step in eda_steps:
        notebook_full_path = os.path.join(EDA_NOTEBOOK_PATH, step)
        if not os.path.exists(notebook_full_path):
            print(f"Skipping (not found): {step}")
            continue
        success = run_notebook(notebook_full_path)
        if not success:
            print("\n Pipeline stopped due to error.")
            break
    print("\n==============================")
    print("EDA PIPELINE FINISHED")
    print("==============================\n")
if __name__ == "__main__":
    run_eda_pipeline()