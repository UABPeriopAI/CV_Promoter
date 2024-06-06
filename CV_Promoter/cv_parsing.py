import re
from datetime import datetime
from typing import Dict, List

from CV_Promoter_config import config


class CVParser:
    """
    The `CVParser` class in Python is designed to extract text from a CV document based on specified
    sections and date ranges.
    """

    def __init__(self, cv, start_year: int):
        self.cv = cv
        self.present_year = datetime.now().year
        self.start_year = start_year
        self.differential = self.present_year - self.start_year + config.NIH_FUNDING_WINDOW

    def extract_text(self, instructions: Dict) -> List[str]:
        """
        This Python function extracts text based on given instructions, including extracting text
        between sections and after a specific section, with a fallback mechanism if no text is
        extracted.

        Args:
          instructions (Dict): The `instructions` parameter is expected to be a dictionary where the
        keys represent different types of instructions and the values are the corresponding values for
        those instructions. The function then processes these instructions to extract text based on the
        specified criteria.

        Returns:
          The function `extract_text` returns a list of strings that have been extracted based on the
        provided instructions.
        """
        extracted_text = []

        for instruction_type, value in instructions.items():
            if "between" in instruction_type:
                start_section, end_section = value
                filter_years = "filter_years" in instruction_type
                extracted_text += self.extract_text_between_sections(start_section, end_section, filter_years)
            elif "after" in instruction_type:
                filter_years = "filter_years" in instruction_type
                extracted_text += self.extract_text_after_section(value, filter_years)

        if not extracted_text:
            # Fallback mechanism
            extracted_text = self.extract_text_after_section("", True)

        return extracted_text

    def extract_text_after_section(self, section_header: str, filter_years: bool) -> List[str]:
        """
        This function extracts text paragraphs following a specified section header, optionally filtering by
        years.

        Args:
          section_header (str): The `section_header` parameter is a string that represents the header of a
        section in a document. The function `extract_text_after_section` uses this parameter to identify the
        section in the document from which text needs to be extracted.
          filter_years (bool): The `filter_years` parameter is a boolean flag that determines whether to
        filter the extracted text based on years. If `filter_years` is set to `True`, the extracted text
        will be filtered based on years. If it is set to `False`, no filtering based on years will be
        applied.

        Returns:
          A list of strings containing text extracted from paragraphs in the CV document after the specified
        section header, based on the provided conditions.
        """
        is_target_section = not section_header.strip()
        extracted_text = []

        for paragraph in self.cv.paragraphs:
            if self._is_section_header(paragraph.text, section_header):
                is_target_section = True
            if is_target_section and self._should_include(paragraph.text, filter_years):
                extracted_text.append(paragraph.text)

        return extracted_text

    def extract_text_between_sections(
        self, start_section: str, end_section: str, filter_years: bool
    ) -> List[str]:
        """
        This function extracts text between specified start and end sections in a document, optionally
        filtering by years.

        Args:
          start_section (str): The `start_section` parameter is a string that represents the section header
        that marks the beginning of the text you want to extract from the document. It is used to identify
        the starting point for extracting text between sections.
          end_section (str): The `end_section` parameter is used to specify the section header that marks
        the end of the text extraction process. When the code encounters this section header while iterating
        through the paragraphs of the document, it stops extracting text and returns the collected text up
        to that point.
          filter_years (bool): The `filter_years` parameter is a boolean flag that determines whether the
        extracted text should be filtered based on years. If `filter_years` is set to `True`, the extracted
        text will be filtered based on some criteria related to years. If it is set to `False`, no filtering
        based on

        Returns:
          The function `extract_text_between_sections` returns a list of strings containing the text
        paragraphs found between the start_section and end_section headers in the CV paragraphs, based on
        the conditions specified by the `filter_years` parameter.
        """
        is_target_section = False
        extracted_text = []

        for paragraph in self.cv.paragraphs:
            if self._is_section_header(paragraph.text, start_section):
                is_target_section = True
            if self._is_section_header(paragraph.text, end_section):
                break
            if is_target_section and self._should_include(paragraph.text, filter_years):
                extracted_text.append(paragraph.text)

        return extracted_text

    def _is_section_header(self, text: str, section_header: str) -> bool:
        """
        This function checks if a given text is a section header by comparing it with a specified section
        header string, ignoring case sensitivity.

        Args:
          text (str): The `text` parameter is a string that represents the text content that you want to
        check for a section header. It is the text in which you want to search for the section header.
          section_header (str): The `section_header` parameter is a string that represents the header of a
        section in a text document. The `_is_section_header` method is used to check if a given text matches
        the specified section header.

        Returns:
          The function is checking if the `text` string matches the `section_header` string exactly
        (ignoring case) and returning a boolean value indicating whether there is a match or not.
        """
        return bool(re.search(f"^{section_header}$", text, re.IGNORECASE))

    def _should_include(self, text: str, filter_years: bool) -> bool:
        """
        The function `_should_include` checks if a given text should be included based on specified
        criteria, including filtering by years.

        Args:
          text (str): The `text` parameter is a string that represents some information or content that
        needs to be checked for inclusion based on certain conditions.
          filter_years (bool): The `filter_years` parameter is a boolean flag that determines whether or not
        to filter based on years. If `filter_years` is `True`, the function will check if the text contains
        a date within a certain range or if it includes the words "present" or "current" in any case

        Returns:
          a boolean value.
        """
        return text.strip() and (
            not filter_years
            or self._is_date_in_range(text)
            or "present" in text.lower().split()
            or "current" in text.lower().split()
        )

    def _is_date_in_range(self, text: str) -> bool:
        """
        The function `is_date_in_range` checks if a given text contains a date within a specified range of
        years, including the current year.

        Args:
        text: The `text` parameter is a string that represents the text in which you want to search for
        dates. It can contain any text, such as sentences, paragraphs, or even a whole document.
        current_year: The current_year parameter represents the current year. It is used to determine the
        range of valid years for the dates in the text.
        year_differential: The `year_differential` parameter is an optional parameter that specifies the
        range of years to consider as valid. By default, it is set to 11, which means that the function will
        consider dates within the current year and the next 11 years as valid. For example, if the current
        year. Defaults to 11

        Returns:
        a boolean value indicating whether a valid date within the specified range is found in the given
        text.
        """
        # Define patterns for various date formats
        date_patterns = [
            r"\b(0?[1-9]|1[0-2])[-/–](0?[1-9]|[12]\d|3[01])[-/–](\d{2})\b",  # MM/DD/YY with valid MM and DD
            r"\b(0?[1-9]|1[0-2])[-/–](0?[1-9]|[12]\d|3[01])[-/–](\d{4})\b",  # MM/DD/YYYY with valid MM and DD
            r"\b(0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])[-/](\d{2})\b",  # MM/DD/YY with valid MM and DD
            r"\b(0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])[-/](\d{4})\b",  # MM/DD/YYYY with valid MM and DD
            r"\b(0[1-9]|1[0-2])[-/](\d{2})\b(?![-/]\d{2})",  # MM-YY with valid MM and not followed by another set of numbers
            r"\b(0[1-9]|1[0-2])[-/](\d{4})\b",  # MM-YYYY with valid MM
            r"\b(\d{4})\b",  # YYYY
            r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+(\d{2,4})\b",
        ]

        valid_dates_found = False

        for pattern in date_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                if isinstance(match, tuple):
                    year = match[-1]
                else:
                    year = match.split("/")[-1]  # Get the last part which is likely the year

                # If the year is a full date like "March 29, 2023", extract just the year
                if "," in year:
                    year = year.split(",")[-1].strip()

                if len(year) == 2:  # If YY format, convert to YYYY
                    year = "20" + year if int(year) < self.present_year % 100 else "19" + year

                if (int(year) >= (self.present_year - 1)) and (
                    int(year) <= (self.present_year + self.differential)
                ):
                    valid_dates_found = True
                    break

        return valid_dates_found or ("present" in text.lower()) or ("current" in text.lower())
