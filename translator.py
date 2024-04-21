import re
from tqdm import tqdm
from deep_translator import GoogleTranslator

class SubtitleEntry:
    def __init__(self, index, time_frame, subtitle):
        self.index = index
        self.time_frame = time_frame
        self.subtitle = subtitle

    def __str__(self):
        return f"{self.index}\n{self.time_frame}\n{self.subtitle}\n"

    @classmethod
    def from_lines(cls, lines):
        index = lines[0].strip()
        time_frame = lines[1].strip()
        subtitle_lines = []
        for line in lines[2:]:
            line = line.strip()
            if not line:  # Empty line indicates the end of subtitle
                break
            subtitle_lines.append(line)
        subtitle = '\n'.join(subtitle_lines)
        return cls(index, time_frame, subtitle)

def load_srt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def translate_subtitle(subtitle_entry):
    translated_text = GoogleTranslator(source='en', target='tr').translate(text=subtitle_entry.subtitle)
    if translated_text is None or translated_text.strip() == '':
        print(f"Failed to translate subtitle: {subtitle_entry.subtitle}")
        return subtitle_entry  # Keep the original subtitle if translation failed
    return SubtitleEntry(subtitle_entry.index, subtitle_entry.time_frame, translated_text)

def translate_srt_file(original_file_path, export_file_path):
    original_subtitles = load_srt_file(original_file_path)
    translated_subtitles = []

    progress_bar = tqdm(total=len(original_subtitles)//4, desc='Translating Subtitles', unit='subtitle')

    i = 0
    while i < len(original_subtitles):
        subtitle_lines = []
        for line in original_subtitles[i:]:
            line = line.strip()
            if not line:  # Empty line indicates the end of subtitle
                i += 1
                break
            subtitle_lines.append(line)
            i += 1
        subtitle_entry = SubtitleEntry.from_lines(subtitle_lines)
        translated_subtitle_entry = translate_subtitle(subtitle_entry)
        translated_subtitles.append(str(translated_subtitle_entry))
        translated_subtitles.append('\n')  # Add an empty line after each subtitle entry
        progress_bar.update(1)

    progress_bar.close()

    with open(export_file_path, 'w', encoding='utf-8') as export_file:
        export_file.writelines(translated_subtitles)

# Example usage:
original_file_path = 'PATH/TO/org.srt'
export_file_path = 'PATH/TO/translated.srt'
translate_srt_file(original_file_path, export_file_path)
