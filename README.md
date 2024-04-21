# SRT Translator

The SRT Translator is a Python script that translates subtitles in .srt format from one language to another using the Google Translate API. It preserves the original structure and timing of the subtitles while providing translated content.

## Features

- Translates .srt subtitles from one language to another.
- Retains the original timing and formatting of subtitles.
- Handles multiline subtitles and empty lines between entries.
- Supports progress tracking during translation.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/KylHA/Subtitle-Translation.git
    ```

2. Navigate to the project directory:

    ```bash
    cd srt-translator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place the original .srt file to be translated in the project directory.

2. Open a terminal and navigate to the project directory.

3. Run the script with the following command:

    ```bash
    python translator.py --input original_file.srt --output translated_file.srt --source en --target tr
    ```

    Replace `original_file.srt` with the filename of your original .srt file, and `translated_file.srt` with the desired filename for the translated .srt file. Adjust `--source` and `--target` parameters according to the source and target languages.

4. Wait for the translation process to complete. Progress will be displayed in the terminal.

5. Once the translation is finished, you will find the translated .srt file in the project directory.

## Dependencies

- `tqdm`: For displaying progress bars during translation.
- `deep-translator`: For accessing the Google Translate API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Acknowledgments

- This script was inspired by the need for easy translation of .srt subtitles for various video projects.
