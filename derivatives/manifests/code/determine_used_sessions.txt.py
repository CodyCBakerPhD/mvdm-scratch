import pathlib

def _run():
    """Initially run in iPython kernel."""
    present_processed_dir = pathlib.Path(r"E:\mvdm\all_processed")
    text_files = list(present_processed_dir.glob("*.txt"))

    all_text_content = [[val.removeprefix(" ") for val in path.read_text().splitlines()] for path in text_files]
    unique_text_content = [set(path_list) - {""} for path_list in all_text_content]
    flat_unique = {content for all_content in unique_text_content for content in all_content}

    all_diffs = [content - unique_text_content[0] for content in unique_text_content]
    # all_diffs

    standard_diffs = [content - unique_text_content[6] for content in unique_text_content]
    # standard_diffs

    all_and_repeat = unique_text_content[0].union(unique_text_content[5])

    all_and_repeat == flat_unique
    # Out[49]: True

    unique_sessions = {pathlib.Path(path).name for path in flat_unique}

    unique_subjects = sorted(list({pathlib.Path(path).parent.name for path in flat_unique}))


    # Determine any extra paths downloaded by accident (manifest was acquired after download completed)
    present_processed_sessions_paths = [
        path
        for path1 in present_processed_dir.iterdir()
        if path1.is_dir()
        for path2 in path1.iterdir()
        for path in path2.iterdir()
    ]
    present_processed_sessions_sessions = [
        path.name
        for path1 in present_processed_dir.iterdir()
        if path1.is_dir()
        for path2 in path1.iterdir()
        for path in path2.iterdir()
    ]
    extra_downloaded_ses = sorted(list(set(present_processed_sessions_sessions) - unique_sessions))

    output_file_path = pathlib.Path(__file__).parent.parent / "derivatives" / "used_sessions.txt"
    output_file_path.write_text(data="\n".join(sorted(list(unique_sessions))))

if __name__ == "__main__":
    _run()
