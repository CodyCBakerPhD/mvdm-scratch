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
- The SpikeGLX gate is `g1` without an accompanying `g0`, resulting in the following error when running the raw data conversion:

<details>

```bash
  File "/usr/local/bin/vandermeerlab2bids", line 7, in <module>
    sys.exit(_vandermeerlab_to_bids_cli())
             ~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/local/lib/python3.13/site-packages/click/core.py", line 1485, in __call__
    return self.main(*args, **kwargs)
           ~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/site-packages/click/core.py", line 1406, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.13/site-packages/click/core.py", line 1873, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/usr/local/lib/python3.13/site-packages/click/core.py", line 1873, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/usr/local/lib/python3.13/site-packages/click/core.py", line 1269, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/site-packages/click/core.py", line 824, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.13/site-packages/vandermeerlab_to_bids/_command_line_interface/_cli.py", line 81, in _vandermeerlab_to_bids_convert_nwb_cli
    odor_sequence_to_nwb(
    ~~~~~~~~~~~~~~~~~~~~^
        data_directory=datapath,
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ...<4 lines>...
        raw_or_processed=stream,
        ^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/usr/local/lib/python3.13/site-packages/pydantic/_internal/_validate_call.py", line 39, in wrapper_function
    return wrapper(*args, **kwargs)
  File "/usr/local/lib/python3.13/site-packages/pydantic/_internal/_validate_call.py", line 136, in __call__
    res = self.__pydantic_validator__.validate_python(pydantic_core.ArgsKwargs(args, kwargs))
  File "/usr/local/lib/python3.13/site-packages/vandermeerlab_to_bids/manish_2025/_odor_sequence_to_nwb.py", line 67, in odor_sequence_to_nwb
    spikeglx_converter = neuroconv.converters.SpikeGLXConverterPipe(folder_path=raw_data_directory)
  File "/usr/local/lib/python3.13/site-packages/pydantic/_internal/_validate_call.py", line 39, in wrapper_function
    return wrapper(*args, **kwargs)
  File "/usr/local/lib/python3.13/site-packages/pydantic/_internal/_validate_call.py", line 136, in __call__
    res = self.__pydantic_validator__.validate_python(pydantic_core.ArgsKwargs(args, kwargs))
pydantic_core._pydantic_core.ValidationError: 1 validation error for SpikeGLXConverterPipe.__init__
folder_path
  Path does not point to a directory [type=path_not_directory, input_value=PosixPath('input/M540/rawdata/M540-2024-08-16_g0'), input_type=PosixPath]
```

</details>

  - this was resolved by manually renaming the file using `g0` (the SpikeGLX metadata retains the previous name).

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
