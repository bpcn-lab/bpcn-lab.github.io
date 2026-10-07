#!/usr/bin/env python3
# Generates people.qmd (English) and de/people.qmd (German) from the data
# below. Edit this file, then run: python3 scripts/build_people.py

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

T = {
    "en": dict(
        assets="/assets", title="People",
        description="Members and alumni of the BPCN department at Friedrich Schiller University Jena.",
        portrait="Portrait of {}", email="Email", profile="Institutional profile",
        learn_more="Learn more", currently="Currently: {}", now="Now: {}",
        doctoral="Doctoral candidates", phd_role="Ph.D. candidate, {{< var org.short >}}",
        students="Student assistants",
        alumni="Alumni",
        alumni_intro="Former researchers and students supervised by {{< var pi.name >}}, including those supervised before he joined Friedrich Schiller University Jena. A dagger (†) marks co-supervision as second supervisor.",
        g_researchers="Former researchers", g_doctoral="Doctoral alumni",
        g_master="Master's, diploma, and medical theses",
        g_master_note="Students who went on to a doctorate in the group are listed under doctoral alumni.",
        g_bachelor="Bachelor's theses", biology="(Biology)",
        phd="Ph.D. {}", drmed="Dr. med. {}",
        footer="*To add or correct a profile, open a [profile update request](https://github.com/bpcn-lab/bpcn-lab.github.io/issues/new/choose).*",
    ),
    "de": dict(
        assets="../assets", title="Team",
        description="Mitglieder und Alumni der Abteilung BPCN an der Friedrich-Schiller-Universität Jena.",
        portrait="Porträt von {}", email="E-Mail", profile="Profil der Einrichtung",
        learn_more="Mehr erfahren", currently="Heute: {}", now="Heute: {}",
        doctoral="Promovierende", phd_role="Promotion, {{< var org.short >}}",
        students="Studentische Hilfskräfte",
        alumni="Alumni",
        alumni_intro="Ehemalige wissenschaftliche Mitarbeitende sowie Studierende, die von {{< var pi.name >}} betreut wurden, auch vor seinem Wechsel an die Friedrich-Schiller-Universität Jena. Ein Kreuz (†) kennzeichnet eine Betreuung als Zweitgutachter.",
        g_researchers="Ehemalige wissenschaftliche Mitarbeitende", g_doctoral="Promovierte Alumni",
        g_master="Master-, Diplom- und medizinische Abschlussarbeiten",
        g_master_note="Wer anschließend in der Abteilung promoviert hat, ist unter den promovierten Alumni aufgeführt.",
        g_bachelor="Bachelorarbeiten", biology="(Biologie)",
        phd="Promotion {}", drmed="Dr. med. {}",
        footer="*Um ein Profil zu ergänzen oder zu korrigieren, eröffnen Sie eine [Änderungsanfrage](https://github.com/bpcn-lab/bpcn-lab.github.io/issues/new/choose).*",
    ),
}

# Current members -----------------------------------------------------------
MEMBERS = [
    dict(id="gyula-kovacs", name="{{< var pi.name >}}", alt="Prof. Dr. Gyula Kovács",
         photo="gyula-kovacs.jpeg", email="gyula.kovacs@uni-jena.de",
         role={"en": "{{< var pi.role >}}, {{< var org.short >}}", "de": "{{< var pi.role >}}, {{< var org.short >}}"},
         scholar="https://scholar.google.com/citations?hl=de&user=xTXqqyIAAAAJ&view_op=list_works&sortby=pubdate",
         more="{{< var contact.department_url >}}",
         bio={
             "en": "Leads the department's research on the neural background of perceptual and cognitive functions, including object and person recognition, the interaction between perception and memory, and predictive neural processes. The work combines electrophysiology, functional imaging, and transcranial magnetic stimulation.",
             "de": "Leitet die Forschung der Abteilung zu den neuronalen Grundlagen von Wahrnehmung und Kognition, darunter Objekt- und Personenerkennung, das Zusammenspiel von Wahrnehmung und Gedächtnis sowie prädiktive neuronale Prozesse. Die Arbeit verbindet Elektrophysiologie, funktionelle Bildgebung und transkranielle Magnetstimulation.",
         }),
    dict(id="mario-archila", name="Dr. Mario Archila", alt="Dr. Mario Archila",
         photo="mario-archila.jpeg", email="mario.archila@uni-jena.de",
         role={"en": "Researcher and Lecturer in Neuro-AI and Visual Perception",
               "de": "Wissenschaftlicher Mitarbeiter und Dozent für Neuro-KI und visuelle Wahrnehmung"},
         scholar="https://scholar.google.com/citations?hl=de&user=qYnQ7z4AAAAJ&view_op=list_works&sortby=pubdate",
         more="{{< var links.archila >}}",
         bio={
             "en": "Works at the interface of cognitive neuroscience and machine learning, applying computational methods to neural and behavioural data. Leads the Translational Neuro-AI research program within BPCN.",
             "de": "Arbeitet an der Schnittstelle von kognitiven Neurowissenschaften und maschinellem Lernen und wendet computergestützte Methoden auf neuronale und Verhaltensdaten an. Leitet das Forschungsprogramm Translational Neuro-AI am BPCN.",
         }),
    dict(id="susann-houben", name="Susann Houben", alt="Susann Houben",
         photo="susann-houben.jpeg", email="sekretariat.bpcn@uni-jena.de",
         role={"en": "Team Assistant", "de": "Teamassistenz"},
         bio={
             "en": "Contact for all questions about the department and the team of {{< var pi.name >}}.",
             "de": "Ansprechpartnerin für alle Fragen rund um die Abteilung und das Team von {{< var pi.name >}}.",
         }),
]

DOCTORAL_CANDIDATES = [
    dict(id="andras-sarkozy", name="András Sárközy, MSc", alt="András Sárközy",
         photo="andras-sarkozy.jpeg", email="andras.zoltan.sarkoezy@uni-jena.de",
         bio={
             "en": "Research focuses on consciousness and conscious access: how and when sensory information becomes available to subjective experience and report, and how prior expectations shape it. This work draws on psychophysics, eye tracking, pupillometry, and fMRI. A second line of research concerns neurodegeneration, first approached through molecular genetics and now studied in older and clinical populations, combining pupillometry with 7T fMRI during attention and cognitive control tasks. Altered states of consciousness, including psychedelic states, are a further interest that grows out of these questions.",
             "de": "Die Forschung befasst sich mit Bewusstsein und bewusstem Zugang: wie und wann sensorische Information dem subjektiven Erleben und dem Bericht darüber zugänglich wird und wie Vorerwartungen dies prägen. Dazu kommen Psychophysik, Eyetracking, Pupillometrie und fMRT zum Einsatz. Ein zweiter Schwerpunkt ist die Neurodegeneration, zunächst aus molekulargenetischer Sicht und heute bei älteren und klinischen Gruppen untersucht, wobei Pupillometrie mit 7T-fMRT bei Aufgaben zu Aufmerksamkeit und kognitiver Kontrolle kombiniert wird. Veränderte Bewusstseinszustände, einschließlich psychedelischer Zustände, sind ein weiteres Interesse, das aus diesen Fragen erwächst.",
         }),
    dict(id="yang-shi", name="Yang Shi, MSc", alt="Yang Shi",
         photo="yang-shi.jpeg", email="yang.shi@uni-jena.de",
         researchgate="https://www.researchgate.net/profile/Yang-Shi-51",
         bio={
             "en": "Research interests focus on the multidimensional factors that shape identity processing and familiarization during social interactions. This research combines EEG and fMRI with machine-learning-based multivariate analysis to investigate the neural representations and dynamics underlying person perception and familiarity.",
             "de": "Die Forschung befasst sich mit den vielfältigen Faktoren, die die Verarbeitung von Identität und das Vertrautwerden in sozialen Interaktionen prägen. Dazu werden EEG und fMRT mit multivariaten Analysen auf Basis maschinellen Lernens kombiniert, um die neuronalen Repräsentationen und Dynamiken der Personenwahrnehmung und Vertrautheit zu untersuchen.",
         }),
    dict(id="yeliz-dinc", name="Yeliz Dinc, MSc", alt="Yeliz Dinc",
         photo="yeliz-dinc.jpeg", email="yeliz.dinc@uni-jena.de",
         scholar="https://scholar.google.com/citations?user=Rcr0Dw4AAAAJ&hl=tr",
         bio={
             "en": "Research focuses on face perception and recognition, particularly familiarity, memory, and individual differences in face-recognition ability, and on how semantic information and visual context shape the way identities are processed and recognized. Using EEG and multivariate pattern analysis, this work investigates the neural processes involved in face recognition. Also involved in teaching the EmPra course \"Face Recognition in Cognitive Neuroscience.\" Outside the lab, Yeliz enjoys spending time with her cat, being in nature, good food, and sports.",
             "de": "Die Forschung befasst sich mit Gesichtswahrnehmung und Gesichtererkennung, insbesondere mit Vertrautheit, Gedächtnis und individuellen Unterschieden in der Fähigkeit, Gesichter zu erkennen, sowie damit, wie semantische Information und visueller Kontext die Verarbeitung und Erkennung von Identitäten prägen. Mit EEG und multivariater Musteranalyse untersucht diese Arbeit die neuronalen Prozesse der Gesichtererkennung. Außerdem lehrt sie im EmPra-Kurs „Face Recognition in Cognitive Neuroscience“. Außerhalb des Labors verbringt Yeliz gern Zeit mit ihrer Katze, in der Natur, mit gutem Essen und beim Sport.",
         }),
]

STUDENTS = [
    dict(id="marie-stoehr", name="Marie Stöhr", email="marie.stoehr@uni-jena.de",
         role={"en": "Student tutor", "de": "Studentische Tutorin"}),
    dict(id="nour-ogeiz", name="Nour Ogeiz", email="nour.ogeiz@uni-jena.de",
         role={"en": "Student assistant", "de": "Studentische Hilfskraft"}),
]

# Alumni ----------------------------------------------------------------------
# links: list of (kind, url[, alt]) where kind is researchgate, xing or website
RESEARCHERS = [
    dict(id="lars-rogenmoser", name="Dr. Lars Rogenmoser",
         role={"en": "Former habilitation candidate", "de": "Ehemaliger Habilitand"},
         now={"en": "Assistant Professor, James Madison University, United States",
              "de": "Assistant Professor, James Madison University, USA"},
         links=[("website", "https://www.jmu.edu/chbs/csd/people/rogenmoser-lars.shtml")]),
    dict(id="geza-gergely-ambrus", name="Dr. Géza Gergely Ambrus",
         role={"en": "Former member", "de": "Ehemaliges Mitglied"},
         now={"en": "Lecturer in Psychology, Bournemouth University, United Kingdom",
              "de": "Lecturer in Psychology, Bournemouth University, Vereinigtes Königreich"},
         links=[("website", "https://staffprofiles.bournemouth.ac.uk/display/gambrus")]),
]

# (id, name, year, degree "phd"/"drmed", co-supervised, now {en,de} or None, links)
DOCTORAL = [
    ("linda-ficco", "Dr. Linda Ficco", 2024, "phd", True,
     {"en": "Researcher, Swiss Center for Design and Health, Switzerland",
      "de": "Wissenschaftlerin, Swiss Center for Design and Health, Schweiz"},
     [("website", "https://www.scdh.ch/en/who-we-are", "Swiss Center for Design and Health")]),
    ("chenglin-li", "Dr. Chenglin Li", 2022, "phd", False,
     {"en": "School of Psychology, Zhejiang Normal University, China",
      "de": "School of Psychology, Zhejiang Normal University, China"},
     [("researchgate", "https://www.researchgate.net/profile/Chenglin-Li-15")]),
    ("charlotta-eick", "Dr. Charlotta Eick", 2021, "phd", False, None,
     [("xing", "https://www.xing.com/profile/Charlotta_Eick")]),
    ("sophie-marie-rostalski", "Dr. Sophie-Marie Rostalski", 2021, "phd", False, None,
     [("researchgate", "https://www.researchgate.net/profile/Sophie-Marie-Rostalski")]),
    ("petra-kovacs", "Dr. Petra Kovács", 2018, "phd", False, None, []),
    ("catarina-amado", "Dr. Catarina Amado", 2017, "phd", False, None,
     [("researchgate", "https://www.researchgate.net/profile/Catarina-Amado-2")]),
    ("claudia-menzel", "Dr. Claudia Menzel", 2016, "phd", True,
     {"en": "Researcher, Environmental Psychology, RPTU Kaiserslautern-Landau, Germany",
      "de": "Wissenschaftlerin, Umweltpsychologie, RPTU Kaiserslautern-Landau"},
     [("website", "https://psy.rptu.de/en/wus/social-environmental-and-economic-psychology/environmental-psychology-lab/team/dr-claudia-menzel")]),
    ("marlena-itz", "Dr. Marlena Itz", 2016, "phd", True,
     {"en": "Systems Neuroscience in Psychiatry group, Central Institute of Mental Health, Mannheim, Germany",
      "de": "Arbeitsgruppe Systems Neuroscience in Psychiatry, Zentralinstitut für Seelische Gesundheit, Mannheim"},
     []),
    ("lisa-muenke", "Dr. Lisa Münke", 2016, "drmed", False, None, []),
    ("kornel-nemeth", "Dr. Kornél Németh", 2016, "phd", False, None, []),
    ("pal-vakli", "Dr. Pál Vakli", 2016, "phd", False,
     {"en": "Research Fellow, Brain Imaging Centre, HUN-REN Research Centre for Natural Sciences, Budapest, Hungary",
      "de": "Wissenschaftlicher Mitarbeiter, Brain Imaging Centre, HUN-REN Research Centre for Natural Sciences, Budapest, Ungarn"},
     []),
    ("mareike-grotheer", "Dr. Mareike Grotheer", 2015, "phd", False,
     {"en": "Professor, Philipps-Universität Marburg, Germany",
      "de": "Professorin, Philipps-Universität Marburg"},
     [("website", "https://www.uni-marburg.de/en/fb04/team-grotheer/team/dr-mareike-grotheer")]),
    ("christian-walther", "Dr. Christian Walther", 2013, "phd", False, None, []),
    ("krisztina-nagy", "Dr. Krisztina Nagy", 2012, "phd", False, None, []),
    ("nicole-wolff", "Dr. Nicole Wolff", 2012, "phd", True,
     {"en": "Department of Child and Adolescent Psychiatry, University Hospital Carl Gustav Carus Dresden, Germany",
      "de": "Klinik und Poliklinik für Kinder- und Jugendpsychiatrie und -psychotherapie, Universitätsklinikum Carl Gustav Carus Dresden"},
     [("website", "https://www.uniklinikum-dresden.de/de/das-klinikum/kliniken-polikliniken-institute/kjp/forschung/AG_Roessner/cvs_wma/CV_NWolff")]),
    ("marta-zimmer", "Dr. Márta Zimmer", 2010, "phd", False,
     {"en": "Associate Professor, Department of Cognitive Science, Budapest University of Technology and Economics, Hungary",
      "de": "Associate Professor, Department of Cognitive Science, Technische und Wirtschaftswissenschaftliche Universität Budapest, Ungarn"},
     []),
    ("nadine-kloth", "Dr. Nadine Kloth", 2009, "phd", True,
     {"en": "Department of Neurology, University Hospital Münster, Germany",
      "de": "Klinik für Neurologie, Universitätsklinikum Münster"},
     [("website", "https://medizin.uni-muenster.de/klinik-fuer-neurologie/forschung/arbeitsgruppe-landmeyer-1/team.html")]),
    ("zoltan-chadaide", "Dr. Zoltán Chadaide", 2003, "phd", True, None, []),
    ("tamas-tompa", "Dr. Tamás Tompa", 2003, "phd", True,
     {"en": "Professor, University of Miskolc, Hungary", "de": "Professor, Universität Miskolc, Ungarn"},
     []),
]

DEG = {
    "en": dict(dp="Diploma (Psychology)", db="Diploma (Biology)", mcn="MSc Cognitive Neuroscience",
               mp="MSc Psychology", med="Medical thesis"),
    "de": dict(dp="Diplom (Psychologie)", db="Diplom (Biologie)", mcn="MSc Kognitive Neurowissenschaften",
               mp="MSc Psychologie", med="Medizinische Abschlussarbeit"),
}

# (name, degree key, year, co-supervised, now {en,de} or None, link or None)
MASTER = [
    ("Antonia Viel", "mp", 2026, False, None, None),
    ("Isabell Jakob", "mp", 2025, False, None, None),
    ("Mayla te Veer", "mp", 2025, True, None, None),
    ("Veronique Mann", "mp", 2024, True, None, None),
    ("Elena Giuliani", "mp", 2022, False, None, None),
    ("Katherine Schulte", "mp", 2022, True, None, None),
    ("Theresa Epperlein", "mp", 2022, True, None, None),
    ("Hanna Klink", "mp", 2021, False, None, None),
    ("Alexia Dalski", "mp", 2021, True,
     {"en": "Doctoral researcher, Philipps-Universität Marburg", "de": "Doktorandin, Philipps-Universität Marburg"},
     "https://www.uni-marburg.de/en/fb04/team-grotheer/team/alexia-dalski"),
    ("Rico Stecher", "mp", 2020, False, None, None),
    ("Philipp Böhm", "mp", 2019, False, None, None),
    ("Christian Bloszies", "mp", 2019, True, None, None),
    ("Fabian Kattlun", "mp", 2019, True, None, None),
    ("Lisa-Celine Sullwold", "mp", 2018, True, None, None),
    ("Viola Wagner", "mp", 2017, False, None, None),
    ("Rebecca Mayer", "mp", 2016, False, None, None),
    ("Maria Dotzer", "mp", 2016, True, None, None),
    ("Nadin Wanke", "mp", 2015, False, None, None),
    ("Jacob Itzhaki", "mcn", 2013, False, None, None),
    ("Daniel Kaiser", "dp", 2012, False,
     {"en": "Professor of Neural Computation, Justus Liebig University Giessen",
      "de": "Professor für Neural Computation, Justus-Liebig-Universität Gießen"}, None),
    ("Iulia Lavric", "dp", 2012, False, None, None),
    ("Lara Iffland", "mcn", 2012, False, None, None),
    ("Alexander Lüttich", "mcn", 2012, False,
     {"en": "Postdoctoral researcher, Nuffield Department of Clinical Neurosciences, University of Oxford",
      "de": "Postdoktorand, Nuffield Department of Clinical Neurosciences, University of Oxford"},
     "https://www.ndcn.ox.ac.uk/team/alexander-luettich"),
    ("Zsófia Szabó", "mcn", 2011, False, None, None),
    ("Marcin Posel", "dp", 2011, False, None, None),
    ("Csaba Cziraki", "dp", 2010, False, None, None),
    ("Wenrui Liu", "mcn", 2010, False, None, None),
    ("Krisztina Kovács", "dp", 2009, False, None, None),
    ("Zsanett Zsadányi", "dp", 2008, False, None, None),
    ("Irén Harza", "db", 2006, False, None, None),
    ("Éva Bankó", "db", 2005, False,
     {"en": "Senior Research Fellow, HUN-REN Research Centre for Natural Sciences, Budapest",
      "de": "Senior Research Fellow, HUN-REN Research Centre for Natural Sciences, Budapest"}, None),
    ("Béla Csákány", "med", 2004, False,
     {"en": "Department of Ophthalmology, Semmelweis University, Budapest",
      "de": "Klinik für Augenheilkunde, Semmelweis-Universität Budapest"}, None),
    ("Gábor Csifcsák", "med", 2004, False,
     {"en": "Professor of Cognitive Neuroscience, UiT The Arctic University of Norway",
      "de": "Professor für Kognitive Neurowissenschaften, UiT The Arctic University of Norway"}, None),
]

# (name, year, co-supervised, biology)
BACHELOR = [
    ("Marie Stöhr", 2026, False, False),
    ("Aaron Jakobi", 2025, False, False), ("Anna-Lena Wühr", 2025, False, False),
    ("Annika Thiel", 2025, False, False), ("Azlia Istiqomah", 2025, True, False),
    ("Emma Lippold", 2025, False, False), ("Jakob Menkens", 2025, False, False),
    ("Lena Breidt", 2025, True, False), ("Lotta Ulrich", 2025, True, False),
    ("Moritz Iffland", 2025, False, False), ("Sophie Mintert", 2025, True, False),
    ("Anna Seeber", 2024, False, False), ("Jennifer Kroker", 2024, True, True),
    ("Lara Wöhmann", 2024, True, False), ("Lisa Göschel", 2024, False, False),
    ("Richard Jahn", 2024, False, True), ("Robert Mathaus", 2024, False, False),
    ("Sophia Pawlik", 2024, False, False),
    ("Dominic Kühnlein", 2023, False, False),
    ("Dorothea Eichentopf", 2022, True, False),
    ("Janine Sommerfeld", 2021, True, False), ("Klemens Buttgereit", 2021, False, True),
    ("Laura Friedrich", 2021, False, False), ("Louisa Fortwengel", 2021, False, False),
    ("Pauline Wetzel", 2021, False, False),
    ("Anna Erlenbusch", 2020, True, False), ("Johannes Lehnen", 2020, False, False),
    ("Laura Froese", 2020, True, False), ("Lukas Korn", 2020, False, False),
    ("Marian Losse", 2020, True, False), ("Marie Wachter", 2020, False, False),
    ("Paulina Michal", 2020, True, False), ("Soyoung Jeong", 2020, True, False),
    ("Lu Steinhauer", 2019, False, False), ("Moriz Stabe", 2019, False, False),
    ("Ricarda Maria Budny", 2019, False, False), ("Sophia Karzai", 2019, False, False),
    ("Bahar Aydin", 2018, True, False), ("Dario Urban", 2018, True, False),
    ("Sandrine Hinrichs", 2018, False, False),
    ("Antonia Eisele", 2017, True, False), ("Anna Trimborn", 2017, True, False),
    ("Fabienne Windel", 2017, True, False), ("Laura Krohn", 2017, True, False),
    ("Madita Linke", 2016, False, False), ("Polina Stoyanova", 2016, False, False),
]


def build(lang):
    t = T[lang]
    A = t["assets"]

    def icon(href, name, alt):
        return f'<a href="{href}"><img class="social-icon" src="{A}/icons/{name}.svg" alt="{alt}"></a>'

    def link_icon(kind, url, alt=None):
        if kind == "researchgate":
            return icon(url, "researchgate", "ResearchGate")
        if kind == "xing":
            return icon(url, "xing", "XING")
        return icon(url, "website", alt or t["profile"])

    def email_line(addr):
        shown = addr.replace("@", "<wbr>@", 1)
        return (f'\n::: {{.person-email}}\n<a href="mailto:{addr}"><img class="social-icon" '
                f'src="{A}/icons/email.svg" alt="{t["email"]}"><span>{shown}</span></a>\n:::\n')

    def member(m, role):
        icons = []
        if m.get("scholar"):
            icons.append(icon(m["scholar"], "google-scholar", "Google Scholar"))
        if m.get("researchgate"):
            icons.append(icon(m["researchgate"], "researchgate", "ResearchGate"))
        social = ("\n::: {.person-social}\n" + "\n".join(icons) + "\n:::\n") if icons else ""
        more = (f'\n::: {{.person-links}}\n[{t["learn_more"]}]({m["more"]}){{.pl-web}}\n:::\n'
                if m.get("more") else "")
        return f'''::: {{.person}}

::: {{.person-aside}}
<img class="person-photo" src="{A}/people/{m["photo"]}" alt="{t["portrait"].format(m["alt"])}">

### {m["name"]} {{#{m["id"]}}}

::: {{.person-role}}
{role}
:::
{social}{email_line(m["email"])}:::

::: {{.person-body}}

{m["bio"][lang]}
{more}
:::

:::
'''

    def row(pid, name, role, now=None, links=(), email=None):
        out = f'''::: {{.person .alum}}

::: {{.person-body}}

#### {name} {{#{pid}}}

::: {{.person-role}}
{role}
:::
'''
        if now:
            out += f'\n::: {{.person-now}}\n{t["currently"].format(now)}\n:::\n'
        if email:
            out += email_line(email)
        if links:
            out += "\n::: {.person-social}\n" + "\n".join(link_icon(*l) for l in links) + "\n:::\n"
        return out + "\n:::\n\n:::\n"

    parts = [f'''---
title: "{t["title"]}"
description: "{t["description"]}"
---

<!-- Generated by scripts/build_people.py. Edit that file, not this page. -->
''']
    for m in MEMBERS:
        parts.append(member(m, m["role"][lang]))
    parts.append(f'## {t["doctoral"]}\n')
    for m in DOCTORAL_CANDIDATES:
        parts.append(member(m, t["phd_role"]))
    parts.append(f'## {t["students"]}\n')
    for s in STUDENTS:
        parts.append(row(s["id"], s["name"], s["role"][lang], email=s["email"]))
    parts.append(f'## {t["alumni"]}\n\n{t["alumni_intro"]}\n\n### {t["g_researchers"]} {{.alumni-group}}\n')
    for r in RESEARCHERS:
        parts.append(row(r["id"], r["name"], r["role"][lang], r["now"][lang], r["links"]))
    parts.append(f'\n### {t["g_doctoral"]} {{.alumni-group}}\n')
    for pid, name, year, deg, co, now, links in DOCTORAL:
        role = t[deg].format(year) + (" †" if co else "")
        parts.append(row(pid, name, role, now[lang] if now else None, links))

    deg = DEG[lang]
    master = []
    for name, d, year, co, now, href in MASTER:
        line = f"- **{name}**{' †' if co else ''}, {deg[d]}, {year}"
        if now:
            line += ". " + t["now"].format(f"[{now[lang]}]({href})" if href else now[lang])
        master.append(line)
    bachelor = [f"- **{n}**{' †' if co else ''}, {y}" + (f" {t['biology']}" if bio else "")
                for n, y, co, bio in BACHELOR]
    parts.append(f'''
### {t["g_master"]} {{.alumni-group}}

{t["g_master_note"]}

::: {{.thesis-list}}
{chr(10).join(master)}
:::

### {t["g_bachelor"]} {{.alumni-group}}

::: {{.thesis-list .thesis-list-compact}}
{chr(10).join(bachelor)}
:::

---

{t["footer"]}
''')
    return "\n".join(parts)


(ROOT / "people.qmd").write_text(build("en"), encoding="utf-8")
(ROOT / "de").mkdir(exist_ok=True)
(ROOT / "de" / "people.qmd").write_text(build("de"), encoding="utf-8")
print("wrote people.qmd and de/people.qmd")
