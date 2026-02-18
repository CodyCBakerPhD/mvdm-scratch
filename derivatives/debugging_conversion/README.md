# Debugging

All code used for NWB conversion can be found on the https://github.com/con/vandermeerlab-to-bids repository.

The initial version was built off of a single example (one of the M541 sessions) and a number of issues occurred when expanding to all sessions.



`M489-2024-08-07`:
- See [Issues #53](https://github.com/con/vandermeerlab-to-bids/issues/53)
- A new chemical type was detected.
- In addition, a new experimenter name was discovered and their full name had to be looked up and added.

`M509-2024-09-13`:
- Had no subject sex specified.
- A fallback value of "U" was built into the converter.

`M540-2024-08-16`:
- Had no `channel_ids` in the `mua_units_imec0.mat` file.
- The SpikeGLX gate is `g1` without an accompanying `g0`.

`M540-2024-08-20`:
- `ExpKeys.sex="2024-08-19"`, not the expected letter code. This was likely a typo. I built in a specific session override rather than modifying source files.

`M588-2025-06-24`:
- The lines around `_best_SWR_channel` had no space after the equals; not required by any syntax, but was consistent elsewhere and used in the JSON parsing rules.
- Required debug to JSON converter.

`M588-2025-06-24`:
- Observed another new experimenter, `"Mimi"`. Mapped to `"Janssen, Miriam"` based on publication record.
- `ExpKeys.sex="Male"`. Added to mapping.
- It was then noticed that the rest of the data was empty and that this particular session wasn't actually in the used sessions list. Session was then discarded.

`M610-2025-06-16`:
- `ExpKeys.sex="Female"`. Added to mapping.

I also added the mean waveform data stream to the processed conversion.
