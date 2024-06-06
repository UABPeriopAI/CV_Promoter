# CV_Promoter
This application uses generative artificial intelligence (AI) to support academic faculty with tasks related to their Curriculum Vitae (CV).  Each tool in the software uses an uploaded CV to construct the pertinent documentation.

## Features
1. **Drafting Narrative Portfolio** - Many institutions require a narrative portfolio as part of a promotion and tenure packet. This tool accepts as input the users CV, start date, and area of focus for the narrative portfolio.  The areas of focus include "Research", "Teaching", and "Service" as that constitutes the tripartite initiative of many academic medical centers.
2.  **Annual Review Preparation** - Institutions often perform annual evaluation of their faculty to review the progress from the previous year and set goals for the upcoming year.  This tool will help faculty quickly extract their work from the previous year that's contained in their CV to facilitate prepartion for the annual review meetings.
3.  **Recommendation Letter Drafting** - Recommendation letter writing is an integral part of the academic process and can be time consuming. This tools takes in a CV, employment start date, and area(s) of focus (up to two) and will draft a letter of recommendation based on the focus areas selected.

## Setting up the Environment
The instructions for setting up the environment are identical to the previously released Grant Guide tool.  Refer to those instructions for setting up the environment to reliably deploy this software: https://github.com/UABPeriopAI/Grant_Guide/blob/main/README.md#setting-up-the-environment.

## Getting Started
### Obtain and Deploy the software
Once the environment is setup, follow these steps to access this generative AI grant drafting tool:

#### Clone the repository:
git clone https://github.com/UABPeriopAI/Grant_Guide.git
Navigate to the directory and open VSCode with
code .
Make sure that the dev container extension is installed in VSCode by going to the Extensions Tab (left-most portion of the user interface

#### Deploy the Docker container

in VS Code press f1 and type "Rebuild" a drop down menu will provide options and select "Dev Containers: Rebuild Container"
You may have to start the docker service with sudo service docker start

## Running the Application 
### Directly from source code
Run the application with the following command:
```
streamlit run streamlit/Home.py
```
Occasionally, the webpage will stall and require a refresh to fully deploy.  Once it deploys, the user will be asked to select an API key type (either Azure or OpenAI) and then need to enter their corresponding key in the text box below, as show in the figure.

<img width="538" alt="image" src="https://github.com/UABPeriopAI/Grant_Guide/assets/97175225/d6c9bf45-b797-477f-a188-66d3182534ff">

After the API key is validated the primary user interface is available by selecting Grant Guide from the tab on the left sidebar.  The user should then see an interface resembling the image below:

![image](https://github.com/UABPeriopAI/CV_Promoter/assets/97175225/1247f8e1-0589-482e-9e87-d2afafa3c3c5)

The user can then use the narrative portfolio, annual review preparation, or recommendation letter functionalities by selecting the corresponding tab on the user interface.

#### TODO
- [ ] Obtain LLM end-point (i.e., OpenAI or Azure), including necessary API Key.

## CV Format for Optimal Results
This application was designed for faculty at the University of Alabama at Birmingham and works best for CVs that are structured with that specific format.  The expected format is included below to facilitate users updating their CV to match or to facilitate modification of the code to adapt this structure to match that of their institution. 

## FORMAT FOR STANDARDIZED CURRICULUM VITAE
### University of Alabama at Birmingham
### School of Medicine Faculty
Date:
##### PERSONAL INFORMATION
Name:
Citizenship:
Foreign Language(s):
Home Address:
Phone:
##### RANK/TITLE
Department:
Business Address:
Phone:
Fax:
Email:
##### HOSPITAL AND OTHER (NON ACADEMIC) APPOINTMENTS:
##### PROFESSIONAL CONSULTANTSHIPS:
##### EDUCATION:
Year Degree Institution
##### MILITARY SERVICE:
##### LICENSURE:
##### BOARD CERTIFICATION:
##### POSTDOCTORAL TRAINING:
Year Degree Institution
##### ACADEMIC APPOINTMENTS: (In reverse chronological order)
Year Rank/Title Institution
##### AWARDS/HONORS:
##### PROFESSIONAL SOCIETIES:
##### MEMBERSHIPS:
##### COUNCILS AND COMMITTEES:
##### UNIVERSITY ACTIVITIES:
##### EDITORIAL BOARD MEMBERSHIPS:
##### MAJOR RESEARCH INTERESTS: (2-3 Sentences)
##### TEACHING EXPERIENCE:
##### MAJOR LECTURES AND VISITING PROFESSORSHIPS:
##### GRANT SUPPORT: (PAST AND CURRENT)

(Include year(s) of funding, amount of funding, PI on award, role on award if not PI)
##### OTHER:
##### BIBLIOGRAPHY:
##### MANUSCRIPTS:
(Numbered, in chronological order, faculty member’s name should underlined or highlighted)
Manuscripts already published
Manuscripts in Press
Manuscripts submitted but not yet accepted
Manuscripts in preparation
Other Publications (letters to the author, book reviews, etc.)
##### BOOKS:
(Numbered, in chronological order, faculty member’s name should underlined or highlighted)
Books and Book Chapters
##### Published abstracts
(Numbered, in chronological order, faculty member’s name should underlined or highlighted)
##### Poster Exhibits
##### Oral Presentations
(Numbered, in chronological order, faculty member’s name should underlined or highlighted)
Scientific papers presented at national and international meetings
Scientific papers presented at local and regional meetings
Invited workshops, etc. at national postgraduate courses and
meetings and at other universities
Invited lectures at local and regional courses and meetings
##### MISCELLANEOUS:
Films, educational tapes, syllabi, software packages and courses developed, etc.


