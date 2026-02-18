# Running original analysis

This refers to the scripts in the private repo: https://github.com/vandermeerlab/odor-pixels

One big issues with ALL the notebooks here is the use of `*` imports from local submodule `minimoh_utils`. This makes it difficult to tell what functions are being used and which specific file they are defined in.

`create_fig3_ensemble_decoding.ipynb`:
- Off the bat, adjusting the `dir_path` in the `big_df` creation cell did not lead to successful population of the data frame.
  - This is determined to be because the `summarize_standard_decoding` function is looking for files of the form `block1_standard_decoding{primary_suffix}.pkl` inside each session path (seemingly at the same level as raw/preprocessed).
  - 
