import re
from datetime import datetime, timedelta


class SRTSlicerLogic:
    def __init__(self):
        self.input_file = None
        self.output_file = None
        self.distribution_method = "equal"
        self.preserve_structure = True
        self.progress_callback = None
        self.status_callback = None

    def configure(self, input_file, output_file, distribution_method,
                 preserve_structure, progress_callback=None, status_callback=None):
        """Configure the processor with all settings."""
        self.input_file = input_file
        self.output_file = output_file
        self.distribution_method = distribution_method
        self.preserve_structure = preserve_structure
        self.progress_callback = progress_callback
        self.status_callback = status_callback

    def parse_timestamp(self, timestamp_str):
        """Convert timestamp string to datetime object."""
        return datetime.strptime(timestamp_str, '%H:%M:%S,%f')

    def generate_word_timestamps(self, start_time, end_time, words):
        """Generate individual timestamps for each word based on selected distribution method."""
        total_duration = (self.parse_timestamp(end_time) - self.parse_timestamp(start_time)).total_seconds()

        if len(words) == 1:
            return [(start_time, end_time, words[0])]

        if self.distribution_method == "equal":
            time_per_word = total_duration / len(words)
            word_timestamps = []
            for i, word in enumerate(words):
                word_start_time = (self.parse_timestamp(start_time) + timedelta(seconds=i * time_per_word)).strftime(
                    '%H:%M:%S,%f')[:-3]
                word_end_time = (self.parse_timestamp(start_time) + timedelta(
                    seconds=(i + 1) * time_per_word)).strftime('%H:%M:%S,%f')[:-3]
                word_timestamps.append((word_start_time, word_end_time, word))
            return word_timestamps
        else:
            total_chars = sum(len(word) for word in words)
            word_timestamps = []
            current_start = self.parse_timestamp(start_time)

            for word in words:
                word_proportion = len(word) / total_chars
                word_duration = total_duration * word_proportion

                word_start_time = current_start.strftime('%H:%M:%S,%f')[:-3]
                current_start += timedelta(seconds=word_duration)
                word_end_time = current_start.strftime('%H:%M:%S,%f')[:-3]

                word_timestamps.append((word_start_time, word_end_time, word))

            return word_timestamps

    def process(self):
        """Main processing method that handles the SRT file conversion."""
        if self.status_callback:
            self.status_callback("Processing...")

        # Read input file
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Subtitle block extraction regex
        subtitle_pattern = re.compile(
            r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\n|\Z)', re.DOTALL)

        word_level_srt = []
        global_counter = 1

        # Find all subtitle blocks
        matches = list(subtitle_pattern.finditer(content))
        total_matches = len(matches)

        for i, match in enumerate(matches):
            # Update progress
            if self.progress_callback:
                progress = (i / total_matches) * 100
                self.progress_callback(progress)

            start_time = match.group(2)
            end_time = match.group(3)
            dialog = match.group(4).strip()

            # Split dialog into words
            words = dialog.split()

            # Generate word-level timestamps
            word_timestamps = self.generate_word_timestamps(start_time, end_time, words)

            # Preserve original subtitle structure if enabled
            if self.preserve_structure:
                subtitle_entry = f"Original Subtitle: {dialog}\n\n"
                word_level_srt.append(subtitle_entry)

            # Prepare word-level SRT content
            for word_start, word_end, word in word_timestamps:
                word_level_srt.append(f"{global_counter}\n{word_start} --> {word_end}\n{word}\n\n")
                global_counter += 1

        # Write to output file
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.writelines(word_level_srt)

        # Final progress update
        if self.progress_callback:
            self.progress_callback(100)