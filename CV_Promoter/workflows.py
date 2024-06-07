from abc import abstractmethod
from datetime import datetime

from dateutil.relativedelta import relativedelta
from llm_utils.api_utils.AugmentedResponse import SearchResponseHandler
from llm_utils.api_utils.WorkflowHandler import WorkflowHandler

import streamlit as st
from CV_Promoter.cv_parsing import CVParser
from CV_Promoter_config import api_config, instructions_config, prompt_config


class FormFiller(WorkflowHandler):
    """This Python class `FormFiller` is a subclass of `WorkflowHandler` that processes a CV document by
    extracting relevant text, assembling a prompt, generating a response using a search response
    handler, and updating the total cost.
    """

    def __init__(self, start_date, cv_document, system_prompt, human_prompt, table_name):
        super().__init__()
        self.start_date = start_date
        self.cv_input = cv_document
        self.system_prompt = system_prompt
        self.human_prompt = human_prompt
        self.table_name = table_name
        self.start_year = self._get_start_year()
        self.cv_parser = CVParser(
            self.cv_input,
            self.start_year,
        )

    @abstractmethod
    def _assemble_prompt(self, search_response, relevant_text):
        raise NotImplementedError

    @abstractmethod
    def _get_instructions(self):
        raise NotImplementedError

    def _get_start_year(self):
        """
        This function returns the year of the start date.

        Returns:
          The _get_start_year method returns the year of the start_date attribute.
        """
        return self.start_date.year

    def extract_relevant_text(self, instructions):
        """
        The `extract_relevant_text` function extracts relevant text using provided instructions.

        Args:
          instructions: It looks like you have a function called `extract_relevant_text` that takes in a
        parameter called `instructions`. This function is likely part of a class, as it uses `self` to
        access another method called `extract_text` from the `cv_parser` object. The purpose of this
        function

        Returns:
          the relevant text extracted using the provided instructions by calling the `extract_text` method
        of `cv_parser`.
        """
        return self.cv_parser.extract_text(instructions)

    def process(self):
        """
        The function processes a CV document by extracting relevant text, assembling a prompt, generating a
        response using a search response handler, and updating the total cost.

        Returns:
          The `process` method returns the `generated_response` after processing the search response,
        extracting relevant text from the CV document, assembling a prompt, and generating a response based
        on the assembled prompt.
        """
        search_response = SearchResponseHandler(st.session_state.chat_config, self.cv_input)
        instructions = self._get_instructions()
        # Extract relevant text from CV document
        relevant_text = self.extract_relevant_text(instructions)
        print("relevant text - ", relevant_text)
        print("Assembling Prompt")
        # Assemble Prompt
        assembled_prompt = self._assemble_prompt(search_response, relevant_text)
        print("Generating Response")
        generated_response, response_meta = search_response.generate_response(assembled_prompt)
        self._update_total_cost(response_meta)
        return generated_response


class AnnualReviewDrafter(FormFiller):
    """
    This Python class `AnnualReviewDrafter` initializes with focus areas and a CV document, generating
    prompts and instructions for annual reviews based on the specified focus area.
    """

    def __init__(self, focus_area: str, cv_document):
        self.focus_area = focus_area
        print("focus area = ", self.focus_area)
        start_date = datetime.now() - relativedelta(years=1)
        super().__init__(
            start_date=start_date,
            cv_document=cv_document,
            system_prompt=prompt_config.review_system_template,
            human_prompt=self._prep_human_prompt(),
            table_name=api_config.REVIEW_TABLE_NAME,
        )
        print("start time  = ", self.start_date)

    def _get_instructions(self):
        """
        This function returns instructions based on the focus area specified.

        Returns:
          The `_get_instructions` method is returning the instructions for the current focus area from the
        `instructions_config` dictionary using the `self.focus_area` as the key.
        """
        return instructions_config.section_instructions[self.focus_area]

    def _prep_human_prompt(self):
        """
        The `_prep_human_prompt` function prepares a human prompt by combining various strings from
        configuration files.

        Returns:
          The `_prep_human_prompt` function returns the prepped human prompt, which is a formatted string
        containing the review human prefix, instructions for a specific focus area, and the review human
        suffix.
        """
        prepped_human_prompt = (
            prompt_config.review_human_prefix
            + "\n\n"
            + instructions_config.section_instructions[self.focus_area]["form"]
            + "\n\n"
            + prompt_config.review_human_suffix
        )
        return prepped_human_prompt

    def _assemble_prompt(self, search_response, relevant_text):
        """
        The `_assemble_prompt` function assembles a prompt using various input parameters.

        Args:
          search_response: The `search_response` parameter seems to be an object that contains information
        related to a search response. It is used in the `_assemble_prompt` method to retrieve data needed
        for assembling a prompt.
          relevant_text: The `relevant_text` parameter in the `_assemble_prompt` function is used to provide
        context or additional information that is relevant to the prompt being assembled. This text is
        typically used to help generate a more personalized or targeted prompt based on the specific content
        or context provided.

        Returns:
          the assembled prompt generated by the `assemble_prompt` method of the `aug_service.preparer`
        object in the `search_response` object. The assembled prompt is created using various parameters
        such as `system_prompt`, `user_prompt`, `start_date`, `context`, and `category` provided to the
        `assemble_prompt` method.
        """
        assembled_prompt = search_response.aug_service.preparer.assemble_prompt(
            system_prompt=self.system_prompt,
            user_prompt=self.human_prompt,
            start_date=self.start_year,
            context=relevant_text,
            category=self.focus_area,
        )
        return assembled_prompt


class NarrativePortfolioDrafter(FormFiller):
    """
    The `NarrativePortfolioDrafter` class is a subclass of `FormFiller` that drafts narrative portfolios
    based on a specified focus area, start date, and CV document.
    """

    def __init__(self, focus_area: str, start_date: datetime, cv_document):
        self.focus_area = focus_area
        super().__init__(
            start_date=start_date,
            cv_document=cv_document,
            system_prompt=prompt_config.narrative_system_template,
            human_prompt=prompt_config.narrative_human_template,
            table_name=api_config.NARRATIVE_TABLE_NAME,
        )

    def _assemble_prompt(self, search_response, relevant_text):
        """
        The `_assemble_prompt` function assembles a prompt using various input parameters.

        Args:
          search_response: It looks like you were about to provide information about the `search_response`
        parameter in the `_assemble_prompt` method. Could you please provide more details or complete the
        information so that I can assist you further?
          relevant_text: The `relevant_text` parameter in the `_assemble_prompt` method is used to provide
        context or additional information related to the search response. It is passed to the
        `assemble_prompt` method as the `context` argument. This context can help in generating a more
        tailored prompt based on the specific content or

        Returns:
          the assembled prompt generated by the `assemble_prompt` method of the `aug_service.preparer`
        object in the `search_response` object.
        """
        assembled_prompt = search_response.aug_service.preparer.assemble_prompt(
            system_prompt=self.system_prompt,
            user_prompt=self.human_prompt,
            start_date=self.start_year,
            context=relevant_text,
            narrative_section=self.focus_area,
            narrative_instructions=self._get_instructions(),
        )
        return assembled_prompt

    def _get_instructions(self):
        """
        This function returns the narrative instructions based on the focus area specified.

        Returns:
          The `_get_instructions` method is returning the narrative instructions for the focus area
        specified by `self.focus_area` from the `instructions_config` module.
        """
        return instructions_config.narrative_instructions[self.focus_area]


class RecommendationLetterDrafter(FormFiller):
    """
    This Python class `RecommendationLetterDrafter` is designed to draft recommendation letters based on
    specified focus areas, start date, and CV document, utilizing prompts and instructions for each area
    of interest.
    """

    def __init__(self, focus_areas: list, start_date: datetime, cv_document):
        self.sections_of_interest = focus_areas
        super().__init__(
            start_date=start_date,
            cv_document=cv_document,
            system_prompt=prompt_config.letter_system_template,
            human_prompt=prompt_config.letter_human_template,
            table_name=api_config.LETTER_TABLE_NAME,
        )

    def _assemble_prompt(self, search_response, relevant_text):
        """
        The function `_assemble_prompt` takes various inputs and uses them to assemble a prompt for a search
        response.

        Args:
          search_response: It looks like you were about to provide information about the `search_response`
        parameter, but the information is missing. Could you please provide more details or complete the
        information about the `search_response` parameter so that I can assist you further with the
        `_assemble_prompt` method?
          relevant_text: The `_assemble_prompt` method takes in several parameters to create a prompt. Here
        is a brief explanation of each parameter:

        Returns:
          The function `_assemble_prompt` returns the assembled prompt generated by the
        `search_response.aug_service.preparer.assemble_prompt` method, which is constructed using various
        parameters such as system_prompt, user_prompt, start_date, context, excellence_areas, and
        area_instructions.
        """
        assembled_prompt = search_response.aug_service.preparer.assemble_prompt(
            system_prompt=self.system_prompt,
            user_prompt=self.human_prompt,
            start_date=self.start_year,
            context=relevant_text,
            excellence_areas=" & ".join(self.sections_of_interest),
            area_instructions=self._get_instructions(),
        )
        return assembled_prompt

    def _get_instructions(self):
        """
        The function `_get_instructions` joins the narrative form instructions for sections of interest and
        returns them as a single string.

        Returns:
          The `_get_instructions` method returns the area instructions for the sections of interest as a
        joined string with double newlines separating each instruction.
        """
        print("joining area of interest instructions")
        area_instructions = "\n\n".join(
            [
                instructions_config.narrative_instructions[section]["form"]
                for section in self.sections_of_interest
            ]
        )
        return area_instructions

    def extract_relevant_text(self, instructions):
        """
        The function `extract_relevant_text` takes a list of instructions, extracts relevant text based on
        specified sections of interest, combines the extracted text from all sections, and returns the final
        text as a string.

        Args:
          instructions: It looks like the code snippet you provided is a method called
        `extract_relevant_text` that takes in a parameter `instructions`. The method seems to extract
        relevant text based on sections of interest defined in `self.sections_of_interest`.

        Returns:
          The `extract_relevant_text` method returns the final combined text extracted from the specified
        sections of interest.
        """
        # Ensure sections_of_interest is a list for consistency
        if not isinstance(self.sections_of_interest, (list, tuple)):
            self.sections_of_interest = [self.sections_of_interest]

        all_texts = []
        for section in self.sections_of_interest:
            instructions = instructions_config.narrative_instructions[section]
            extracted_text = self.cv_parser.extract_text(instructions)
            all_texts.extend(extracted_text)
        final_text = "\n\n".join(all_texts)  # combine texts from all sections
        print("final text - ", final_text)
        return final_text
