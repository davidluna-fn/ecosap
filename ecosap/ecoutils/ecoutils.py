import re

import datetime
import pandas as pd
from pathlib import Path


def extract_datetime_from_filename(filename: str):
    """Extract date and time from a filename.

    The filename should have the format 'YYYYMMDD_HHMMSS' somewhere in its name.

    Args:
        filename (str): The filename to extract the date and time from.

    Returns:
        tuple: A tuple containing the date and time as datetime objects.
    """
    datetime_str = re.search(r'\d{8}_\d{6}', filename)
    if datetime_str:
        datetime_str = datetime_str.group()
        date_obj = datetime.strptime(datetime_str[:8], '%Y%m%d')
        time_obj = datetime.strptime(datetime_str[9:], '%H%M%S')
        return date_obj, time_obj
    else:
        return None, None

def list_audio_files(path: str) -> pd.DataFrame:
    """List all audio files (wav) in a directory and its subdirectories.

    The files should be wav format and the filename should have the format 'YYYYMMDD_HHMMSS' somewhere in its name.


    Args:
        path (str): The path to the directory containing audio files.

    Returns:
        pd.DataFrame: A DataFrame with the following columns:
            - 'Name': Name of each audio file.
            - 'Folder': Name of the parent folder for each audio file.
            - 'Date': Date extracted from the filename in format (YYYY-MM-DD).
            - 'Time': Time extracted from the filename in format (HH:MM:SS).
            - 'Path': Full path of each audio file.

    """
    audio_data = []

    try:
        for audio_path in Path(path).rglob('*.[Ww][Aa][Vv]'):
            try:
                file_name = audio_path.name
                parent_folder = audio_path.parent.name
                date, time = extract_datetime_from_filename(file_name)

                audio_data.append({
                    'Name': file_name,
                    'Folder': parent_folder,
                    'Date': date,
                    'Time': time,
                    'Path': str(audio_path)
                })
            except Exception as e:
                print(f"Error processing file: {str(audio_path)} - {e}")

    except Exception as e:
        print(f"Error accessing path: {path} - {e}")

    return pd.DataFrame(audio_data)