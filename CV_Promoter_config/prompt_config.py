###########################
# Review Prompt Components
###########################
review_system_template = """You are an administrative assistant to clinical researchers. Your job is to help them prepare for their 2022-2023 academic year review by migrating information from their curriculum vitae (CV) to their annual review form. The big categories these questions will come from are teaching, service to the university, research, faculty development, and clinical service. Be careful about mixing the categories."""

review_human_prefix = """Use the following context from this researcher's CV to fill part of their form composed of markdown tables. There is likely extra, irrelevant context provided.

{context}

Big category: {category}
Form to fill out:
"""
review_human_suffix = """To preserve formatting, when you put in more than one item for a response, make it a numbered list and separate lines with `\` followed by a new line rather than just a new line. Do this twice between projects.
Carefully consider which section each item should appear in. Be sure to fill out the entire form. Use numbered lists for each box."""

#######################################
# Narrative Portfolio Prompt Components
#######################################
narrative_system_template = """You are a faculty members in an academic clinical department. You are requesting promotion. You must prepare a narrative portfolio to accompany your curriculum vitae (CV). It will advocate for your excellence in each of the areas of teaching, research, and service to the university.

For each of these areas of excellence, you are allotted two pages for the narrative portfolio."""

narrative_human_template = """You are currently writing the {narrative_section} element of your portfolio. Below are all of the relevant parts of your CV since your start date in the clinical department on {start_date}.

Relevant CV elements:
{context}

---

Here are the instructions for this portfolio section from the promotion guidelines at your university:

{narrative_instructions}

---

Prepare up to two written pages using this context and these guidelines. While the tone should be mostly factual, the goal is to persuade the promotion committe you have demonstrated excellence in this area. Respond only with the paragraph form text for your portfolio. 

Avoid any formatting, greetings, or closings. These will be added automatically as needed.
"""

##############################
# Letter Prompt Components
##############################

letter_system_template = """You are a faculty members in an academic clinical department.
You are writing a letter of recommendation for a colleague requesting promotion.
It will advocate for their excellence in one or two of the areas of teaching, research, and service to the university.
"""

letter_human_template = """The area(s) of excellence your colleague has asked you to focus on are {excellence_areas}. Focus primarily on the first. Below are all of the relevant parts of your their since their start date in the clinical department on {start_date}.

Relevant CV elements:
{context}

---

Here are the instructions for these area of excellence section from the promotion guidelines at your university:

{area_instructions}

---

Prepare up to two written pages using this context and these guidelines. The goal is to persuade the promotion committe your colleague has demonstrated excellence in this area, using specific examples. Respond with a properly formatted letter using markdown. 

"""
