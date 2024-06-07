# Define a dictionary to map sections of interest to extraction methods
section_instructions = {
    "Scholarly Activity": {
        "between": ("MAJOR RESEARCH INTERESTS:", "TEACHING EXPERIENCE:"),
        "after_filter_years": "Grant Support",
        "form": """| **2. Current research projects (list title and objective)** |
|---|
| <For each project give 'Title:' and 'Objective:', separate lines with `\` followed by a new line rather than just a new line. Do this twice between projects> |

---
    
| **3. Current external research funding (list title, source, amount, role, salary support, dates of award)** |
|---|
| <Often indicated on a CV by a funding agency (like NIH), funding amount ($), or RFA number. Format each grant as <list title, source, amount, role, salary support, dates of award; separate lines with `\` followed by a new line rather than just a new line. Do this twice between projects.> |

---
    
| **4. Grants submitted (list title, source, amount, role, salary support, expected dates of award)** |
|---|
| <Often indicated on a CV by a funding agency (like NIH), funding amount ($), or RFA number. Format each grant as <list title, source, amount, role, salary support, dates of award> |

---

| **5. Grants to be submitted (list title, source, amount, role, salary support, expected submission date)** |
|---|
| <Often indicated on a CV by a funding agency (like NIH), funding amount ($), or RFA number. Format each grant as <list title, source, amount, role, salary support, dates of award> |

---
 
| **6. Research manuscripts published (list citations)** | **Total Number:**   Number |
|---|---|
| Comment |

---
 
| **7. Research manuscripts accepted and in production (list)** | **Total Number:**   Number |
|---|---|
| Comment |

---
    
| **8. Research manuscripts submitted and under review (list)** | **Total Number:**   Number |
|---|---|
| Comment |

---

| **9. Research presentations (title, authors, meeting, format, date)** | **Total Number:**   Number |
|---|---|
| Comment |

---

| **10. Other research activities (e.g. list editorial boards, manuscript reviewer and journals, study section, etc.)** |
|---|
| Comment |

---

| **11. Education manuscripts published (list citations)** | **Total Number:**   Number |
|---|---|
| Comment |

---

| **12. Education manuscripts accepted and in production (list)** | **Total Number:**   Number |
|---|---|
| Comment |

---

| **13. Education manuscripts submitted and under review (list)** | **Total Number:**   Number |
|---|---|
| Comment |

---

| **14. Books and book chapters published (list)** | **Total Number:**   Number |
|---|---|
| Comment |

---

| **15. Educational exhibits (list title, meeting, format, date)** | **Total Number:**   Number |
|---|---|
| Comment |

---

| **16. Visiting professorships (list title, location, and date)** | **Total Number:**   Number |
|---|---|
| Comment |

---

| **17. Grand rounds (list title, location, and date)** | **Total Number:**   Number |
|---|---|
| Comment |

---

| **18. Other scholarly activities (list and describe)** |
|---|
| Comment |""",
    },
    "Teaching": {
        "between": ("TEACHING EXPERIENCE", "GRANT SUPPORT"),
        "between_filter_years": ("AWARDS/HONORS", "MAJOR RESEARCH INTERESTS"),
        "after_filter_years": "MISCELLANEOUS",
        "form": """| **2. Number of teaching awards** | Number |
|---|---|
| Comments |  |

---

| **3. Number of resident/fellow lectures** | **Number** |
|---|---|
| Comments |  |

---

| **4. Number of medical student lectures** | **Number** |
|---|---|
| Comments |  |

---

| **5. Development of educational curriculum or innovating teaching methods (list and describe)** |
|---|
| Comment |

---

| **6. Plenary lectures at national conference (list title, conference, and date)** | **Total Number:** | Number |
|---|---|---|
| Comment |  |  |

---

| **7. Other educational presentations (list title, format, conference)** | **Total Number:** | Number |
|---|---|---|
| Comment |  |  |

---

| **8. Mentoring activities (list mentees, mentee's position, and describe mentorship activity)** |
|---|
| Comment |""",
    },
    "Clinical Service": {
        "between_filter_years": ("ACADEMIC APPOINTMENTS:", "MAJOR RESEARCH INTERESTS:"),
        "after": "MANUSCRIPTS:",
        "form": """| **3. Other quality improvement service activities (list and describe)** |
|---|
| Comment |

---

| **4. Performs special or unique clinical procedure (list and describe)** |
|---|
| Comment |

---

| **5. Demonstration of patient-centeredness (List and describe; e.g. shared decision making, personalized care, coordination of care, access to care, follow-up care)** |
|---|
| Comment |

---

| **6. Contributions to clinical interdisciplinary conferences (list and describe)** |
|---|
| Comment |

---

| **7. Objective evidence of cost containment efforts and results (list and describe; e.g. reduce costs for supplies, personnel, and other resources)** |
|---|
| Comment |

---

| **8. Charitable, community service or outreach activities (list and describe)** |
|---|
| Comment |

---

| **9. Other clinical accomplishments or activities (list awards, clinical leadership or administrative roles & effort, etc.)** |
|---|
| Comment |
""",
    },
}

narrative_instructions = {
    "Research": {
        "between": ("MAJOR RESEARCH INTERESTS:", "TEACHING EXPERIENCE:"),
        "after_filter_years": "Grant Support",
        "form": """All faculty are expected to engage in scholarly activities to some degree. To that end, scholarly work takes many 
forms including research and other creative activities. A faculty member's effectiveness can be demonstrated by a 
continuous track record of extramural funding, original peer reviewed publications and invited presentations at other 
institutions and at national/international meetings. The quality of an individual's scholarly approach, capacity for 
independent thought, originality, and products of research is best determined by critical review from one's peers. 
Several parameters are considered in determining Excellence in Research. These include, but are not limited to: 
1. Demonstration of a sustained, externally funded and independent research program, with continuity 
over time and becoming more important for the higher-level award (e.g., awarding of Tenure, 
promotion to Professor). While traditionally the NIH funding was deemed critical, funding obtained 
from any agency or foundation is recognized. 
2. Evidence of research productivity is measured by original publications in peer reviewed journals, 
books/book chapters, electronic media, and by presenting scientific papers, and exhibits at scholarly 
meetings. There is no absolute benchmark number of manuscripts that are required for promotion 
and/or tenure, but it would be expected that a productive faculty member would have ~20 when 
seeking promotion to Associate Professor, ~35-40 for Professor, with consideration taken for the 
impact level of the journal, and the position of authorship. Authorship on all manuscripts is valued. 
However, when authorship is not in the first or last position, it is important to discuss the scientific 
contribution in the research portfolio. It is appreciated that all authors have important contributions to a 
scientific manuscript, especially those reporting the findings from large clinical trials and other “team 
science” efforts. 
As applicable, the significance of the faculty member’s research should be described, including: 
1. Recognition from peer groups, awards, elected to important offices, appointments to consultative 
committees, being asked to contribute significant sections to textbooks 
2. The level of innovation 
3. The prospect for future research 
4. Benefits to the Department and/or UAB 
5. Development of an objective method of evaluation service in a manner that can be 
quantified and statistically analyzed 
6. Editorial consultation or reviews of scientific books and articles 
7. Invited presentations of original scientific data at major national or international meetings, or at major 
institutions or research organizations 
Activities that support a strong reputation for the faculty member’s scholarship include, but are not limited to: 
1. Membership on a national planning committee, NIH study section, and foundation grant reviewer 
2. Editor of a journal or membership of an editorial board 
Examples of activities that are valued, but by themselves do not reach the level of Excellence include: 
1. Membership on editorial boards 
2. Ad hoc manuscript reviewer 
3. Internal (UAB) grant reviewer 
4. Small scale publications, such as case reports, or educational materials. """,
    },
    "Teaching": {
        "between": ("TEACHING EXPERIENCE", "GRANT SUPPORT"),
        "between_filter_years": ("AWARDS/HONORS", "MAJOR RESEARCH INTERESTS"),
        "after_filter_years": "MISCELLANEOUS",
        "form": """Superior and effective teaching is a distinct value for consideration of appointment promotion and/or tenure. All 
faculty are expected to participate in the educational mission of the SOM in some manner. Student evaluations 
should be solicited and, where possible, letters of support should also include colleague evaluations of teaching 
credentials, experience, and scholarly activities. 
Specific expectations to be met to achieve Excellence in Teaching include, but are not limited to: 
1. Leadership or course master in a divisional, departmental, or SOM teaching program. This includes 
the development of a new course or program, or documented improvement of an existing course or 
program. Formal evaluations are required.
2. Mentoring, including leadership of a dissertation committee, or role as a primary mentor. This should be 
accompanied by names, dates, and outcome. Testimonial letters from trainees are useful. 
3. Leadership in curriculum development at the local or national level, including development of 
objectives, materials, and methods of evaluation 
4. Objective evidence of teaching excellence, such student/resident/fellow evaluations, teaching 
awards, recognition by faculty, or professional organizations. 
The consistent theme for activities that reach Excellence in Teaching is leadership and intellectual input. There 
are many Teaching activities that are valuable and are expected from a faculty member in an academic medical 
center, but by themselves do not reach the level of excellence. Examples of activities that are valued, but by 
themselves do not reach the level of Excellence include: 
1. Participation as a course lecturer 
2. Hosting a graduate student on a rotation 
3. Serving as a poster judge in various UAB educational activities 
4. Teaching of students, post-graduate students, or residents in the classroom, laboratory, clinical 
setting, or other specific area of expertise (this includes continuing education) 
5. Efforts to improve personal teaching skills, with outcome data 
6. Informal student, resident, or fellow advising and counseling 
7. Participation in student, resident, or fellow recruiting. 
8. Serving as a member of education, curriculum, or admissions committees """,
    },
    "Service": {
        "between_filter_years": ("ACADEMIC APPOINTMENTS:", "MAJOR RESEARCH INTERESTS:"),
        "after": "MANUSCRIPTS:",
        "form": """Service functions are recognized as positive evidence for appointment, promotion and/or award of tenure provided 
that this service emanates from the special competence of the individual in an assigned field and is an extension of 
the individual's role as a scholar-teacher. In addition to service at UAB, participation at the level of the Birmingham 
community and the State of Alabama, as well as in regional, national, or international groups are also valued. 
Excellence in Service is achieved by having a leadership role with a strong intellectual component. Such activities 
include, but are not limited to: 
1. Leadership in a professional service organization 
2. Leadership in a major UAB educational, clinical, or research committee (local/national) 
3. Director/Co-Director of a training program (e.g. graduate or residency program) 
4. Director/Co-Director of a research core facility 
5. Participation in committee work 
6. Fulfillment of significant administrative duties, which should also include positive outcome measures 
7. Leadership in community outreach 
A typical faculty member will have many service activities that do not rise to the level of excellence but are valued. 
Participation in such activities falls under the general service category of ‘citizenship’, which indicates a faculty 
member’s willingness to be a contributor to the overall well-being of the department and/or university. 
Examples of activities that are valued, but by themselves do not reach the level of Excellence include, but are not 
limited to: 
1. Contributions to the improvement of student and faculty life 
2. Faculty consultation within or outside UAB 
3. Organizing department retreats or social events 
4. Interviewing faculty candidates and meeting with visiting scientists/clinicians 
5. Judging poster sessions at UAB research events 
Note: many service activities are related to activities in education and/or research, and can be listed in both 
Clinical Service 
Excellence in patient care is an integral part of a clinical faculty member's service role and is therefore recognized as 
a special competence. Excellence in clinical service is judged by several parameters, including but not limited to: 
1. Patient volume, as compared to local, regional, and national peers 
2. Development of a clinical care path or area of specialty. This may be the creation of new area of 
clinical service, or the expansion and enhancement of an existing clinical service 
3. Creating or expanding a unique or highly specialized clinical service 
4. Development of new treatments, surgical procedures, or innovative diagnostic techniques, the 
results of which are disseminated to the professional community by publication or scientific 
presentation 
Note: Many clinical services activities can interconnect with educational and research activities as well
""",
    },
}
