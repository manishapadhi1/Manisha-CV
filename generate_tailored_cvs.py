from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEX_DIR = ROOT / "tailored_tex"
PDF_DIR = ROOT / "tailored_pdfs"
TEX_DIR.mkdir(exist_ok=True)
PDF_DIR.mkdir(exist_ok=True)

COMMON_CONTACT = {
    "name_first": "Manisha",
    "name_last": "Padhi",
    "address": "Lgh 1301, Skoldvagen 7, Stockholm, 15151, Sweden",
    "phone": "+46 767852019",
    "email": "manishapadhi08@gmail.com",
    "github": "manishapadhi1",
}

BASE_EXPERIENCE = {
    "msc": {
        "role": "Senior Java Developer",
        "company": "MSC Technology",
        "location": "Torino, Italy",
        "dates": "Apr 2022 to Present",
    },
    "clariter": {
        "role": "Associate Engineer - Backend",
        "company": "Clariter",
        "location": "Rome, Italy",
        "dates": "Aug 2021 to Feb 2022",
    },
    "apps": {
        "role": "Associate Consultant",
        "company": "Apps Associates",
        "location": "Hyderabad, India",
        "dates": "Aug 2017 to Aug 2019",
    },
}

COMMON_EDUCATION = [
    ("Masters in International Finance and Economics", "University of Macerata", "Macerata, Italy", "Sep 2019 -- Feb 2022", ["International Finance, Economics, Business Management"]),
    ("Bachelor of Technology in Computer Science", "JNTU Kakinada", "Andhra Pradesh, India", "Sep 2013 -- May 2017", ["Computer Science, Java, Data Structures, DBMS, Software Engineering"]),
]

VARIANTS = {
    "scania-scrum-master": {
        "display_role": "Scrum Master - Security Platform, Software Update and Diagnostics",
        "position": "Scrum Master | Agile Delivery | Java Backend | Diagnostics Platform",
        "summary": [
            "Software Developer with 8+ years of IT experience and strong hands-on background in Java backend systems, agile delivery, production support and cross-functional collaboration.",
            "Well matched to Scania/TRATON Scrum Master work through experience with sprint-based delivery, product owners, QA, DevOps, engineers, code reviews, knowledge sharing, impediment handling, CI/CD and production-quality software.",
            "Brings practical technical credibility for teams working with backend services, microservices, diagnostics-adjacent platforms, connectivity, security mindset and continuous improvement.",
        ],
        "target_fit": [
            "Can facilitate sprint planning, reviews, retrospectives and daily stand-ups from a developer perspective while keeping delivery focused on value, flow and quality.",
            "Experienced collaborating with product owners, QA, DevOps and engineers to align priorities, dependencies and release readiness in agile teams.",
            "Hands-on Java, Spring Boot, REST API, microservice, Kubernetes, CI/CD, Grafana and production support background gives credibility with technical teams.",
            "Comfortable coaching colleagues, reviewing code, documenting workflows and strengthening common ways of working across distributed teams.",
            "Motivated by TRATON values: customer first, respect, team spirit, responsibility and elimination of waste through continuous improvement.",
        ],
        "skills": [
            ("Agile leadership", "Scrum ceremonies, sprint planning, reviews, retrospectives, daily stand-ups, backlog coordination, impediment removal, continuous improvement"),
            ("Delivery", "Cross-functional teams, product owner collaboration, QA, DevOps, release readiness, documentation, stakeholder communication"),
            ("Technical context", "Java 17, Spring Boot, REST APIs, microservices, PostgreSQL, Redis, Docker, Kubernetes, GitHub Actions, CI/CD"),
            ("Observability", "Grafana, Prometheus, NewRelic, logging, metrics, incident analysis, production troubleshooting"),
            ("Security platform fit", "Secure interfaces, API checks, integration testing, reliability, quality mindset, diagnostics and connectivity domain interest"),
        ],
        "msc_bullets": [
            "Develop and maintain Java 17 backend services for business-critical production systems using Spring Boot, REST APIs, microservices and databases.",
            "Work in cross-functional agile teams with product owners, QA, DevOps and engineers to deliver end-to-end changes with clear priorities and ownership.",
            "Support team flow by clarifying requirements, reviewing code, documenting workflows and helping colleagues resolve technical blockers.",
            "Improve delivery quality through JUnit, Mockito, integration tests, API checks, CI/CD practices and production monitoring.",
            "Use Kubernetes, Docker, Git, GitHub Actions, Maven, Grafana, Prometheus and NewRelic to support stable delivery and operational transparency.",
            "Coach colleagues, share knowledge and contribute to a developer chapter culture focused on learning, collaboration and continuous improvement.",
        ],
    },
    "scania-applied-ai-solutions-engineer": {
        "display_role": "Applied AI Solutions Engineer - TRATON R&D AI Enablement",
        "position": "Applied AI Solutions Engineer | Backend Automation | Agentic Workflows",
        "summary": [
            "Software Developer with 8+ years of experience building backend services, APIs, automation and production systems, with strong interest in AI-powered developer workflows and practical enterprise adoption.",
            "Well matched to TRATON R&D AI Enablement through hands-on engineering, ability to translate unclear needs into working prototypes, and experience collaborating with users, product owners, QA, DevOps and engineers.",
            "Brings a pragmatic build-first mindset for agentic workflows: decomposing problems, connecting tools and APIs, iterating with users and measuring impact on speed, quality and collaboration.",
        ],
        "target_fit": [
            "Can analyze business or engineering friction and split work into deterministic logic, human review and AI-assisted workflow steps.",
            "Experienced building backend services, REST APIs, automation, testable integrations and CI/CD flows that can become reusable AI-enabled capabilities.",
            "Comfortable working hands-on with stakeholders to clarify ambiguous needs, prototype solutions and improve adoption based on feedback.",
            "Practical exposure to AI-powered development tools, cloud concepts, Docker, GitHub Actions and developer enablement workflows.",
            "Strong fit for hub-and-spoke AI Enablement because of communication, knowledge sharing, documentation and collaborative engineering habits.",
        ],
        "skills": [
            ("AI enablement", "LLM interest, AI-powered development tools, agentic workflow awareness, human-in-the-loop workflows, guardrails, prototype-to-adoption mindset"),
            ("Software engineering", "Java 17/21, Spring Boot, REST APIs, backend logic, automation, integrations, secure interfaces, modular services"),
            ("Developer tooling", "Git, GitHub Actions, CI/CD, Docker, Maven, test automation, documentation, repeatable delivery"),
            ("Cloud and data", "AWS CDK project exposure, PostgreSQL, SQL, Redis, JSON, XML, data validation, monitoring"),
            ("Collaboration", "Technical discovery, stakeholder dialogue, mob/team collaboration mindset, fast feedback, knowledge sharing"),
        ],
        "msc_bullets": [
            "Build Java backend services and REST APIs that translate business needs into reliable, maintainable production functionality.",
            "Break down unclear requirements with product owners, QA, DevOps and engineers, then iterate toward working solutions with measurable delivery value.",
            "Use automated testing, integration checks, CI/CD and monitoring to improve speed, quality and confidence in software changes.",
            "Create documentation and share knowledge so teams can adopt repeatable workflows and operate services effectively.",
            "Explore AI-powered development tools and automation opportunities to improve engineering productivity and developer experience.",
            "Work with PostgreSQL, Redis, JSON, XML, Docker, Kubernetes, GitHub Actions, Grafana and logs to support practical integration and operational use cases.",
        ],
    },
    "scania-vehicle-function-owner": {
        "display_role": "Vehicle Function Owner - Charging Domain",
        "position": "Vehicle Function Owner | Requirements | Backend Integration | Charging Domain",
        "summary": [
            "Software Developer with 8+ years of IT experience connecting business needs, system behaviour, requirements, implementation, testing and production quality.",
            "Relevant to Scania/TRATON Vehicle Function Owner work through structured requirements handling, stakeholder communication, traceability mindset, integration testing, risk awareness and experience with complex distributed systems.",
            "Brings strong software engineering discipline for charging-related vehicle functions: translating needs into clear requirements, aligning teams and ensuring testable, reliable delivery.",
        ],
        "target_fit": [
            "Can translate customer and stakeholder needs into clear functional requirements, acceptance criteria, test cases and delivery follow-up.",
            "Experienced managing dependencies across product owners, QA, DevOps, engineers and operational stakeholders in agile delivery.",
            "Strong testing and quality mindset through JUnit, Mockito, integration tests, API checks, production support and incident analysis.",
            "Relevant technical foundation in distributed systems, APIs, secure interfaces, data validation and reliable system behaviour.",
            "Motivated by electrification, charging systems, sustainable transport, functional safety and cyber security processes as learning domains.",
        ],
        "skills": [
            ("Function ownership", "Requirements engineering, traceability, stakeholder input, dependency management, risk follow-up, test coverage, delivery readiness"),
            ("System development", "Java, Spring Boot, REST APIs, microservices, distributed systems, secure interfaces, integration testing"),
            ("Quality", "JUnit, Mockito, automated tests, API checks, validation, root-cause analysis, documentation"),
            ("Domain alignment", "Battery electric vehicle interest, charging systems interest, functional safety awareness, cyber security awareness"),
            ("Collaboration", "Product owners, architects, test engineers, QA, DevOps, agile teams, international communication"),
        ],
        "msc_bullets": [
            "Translate business and stakeholder needs into Java backend functionality, REST APIs, validation rules and testable service behaviour.",
            "Collaborate with product owners, QA, DevOps and engineers to clarify requirements, dependencies, risks and release readiness.",
            "Support traceability between requirements, implementation, integration tests, API checks and production monitoring evidence.",
            "Maintain reliable distributed services using PostgreSQL, SQL, Redis, JSON and XML with strong focus on data correctness and operational quality.",
            "Improve automated testing with JUnit, Mockito, integration tests and API checks to strengthen coverage and reduce delivery risk.",
            "Troubleshoot production issues using logs, metrics, Grafana, Prometheus and NewRelic, then document improvements and workflows.",
        ],
    },
    "scania-developer-traton-rd-iot-gateway": {
        "display_role": "Developer for TRATON R&D IoT Gateway",
        "position": "Backend Developer | IoT Gateway | Cloud Connectivity | DevSecOps",
        "summary": [
            "Senior backend developer with 8+ years of experience and 3+ years focused on Java, Spring Boot, REST APIs, microservices, databases, production systems and agile delivery.",
            "Strong match for TRATON R&D IoT Gateway through backend service development, cloud and container exposure, secure integrations, CI/CD, monitoring, production support and interest in vehicle connectivity.",
            "Can contribute to robust communication platforms by building APIs, internal tools, event-ready services, test automation and operational improvements with a DevSecOps mindset.",
        ],
        "target_fit": [
            "Build, test, deploy and maintain backend services and internal tools with end-to-end ownership and production accountability.",
            "Experience with REST APIs, microservices, Docker, Kubernetes, CI/CD, Grafana, databases and clean maintainable backend code.",
            "Project exposure to AWS CDK, Docker and CI/CD through Smart Trader cloud data platform; strong interest in AWS/cloud-native development.",
            "Relevant secure communication mindset through JWT, OAuth2, role-based access control, secure interfaces and API validation.",
            "Ready to transfer Java backend experience into C#/.NET ecosystems while contributing immediately to API design, testing, monitoring and DevSecOps practices.",
        ],
        "skills": [
            ("Backend", "Java 17/21, Spring Boot, Spring WebFlux, REST APIs, microservices, internal tools, maintainable code, clean architecture awareness"),
            ("Cloud and DevSecOps", "Docker, Kubernetes, GitHub Actions, CI/CD, AWS CDK exposure, Maven, Linux, infrastructure-as-code interest"),
            ("Connectivity fit", "IoT interest, vehicle connectivity interest, secure communication, API integration, message routing, event-driven architecture awareness"),
            ("Security", "JWT, OAuth2, role-based access control, secure APIs, certificate/PKI awareness, DevSecOps mindset"),
            ("Operations", "Grafana, Prometheus, NewRelic, logging, metrics, alerting, troubleshooting, SQL, PostgreSQL, Redis"),
        ],
        "msc_bullets": [
            "Develop and maintain Java 17 backend services and REST APIs for business-critical production systems with end-to-end ownership.",
            "Build secure, reliable integrations using Spring Boot, Spring WebFlux, PostgreSQL, Redis, JSON, XML and validation logic.",
            "Use Docker, Kubernetes, Git, GitHub Actions, Maven and CI/CD practices to support stable delivery and operational efficiency.",
            "Monitor and troubleshoot production systems using Grafana, Prometheus, NewRelic, logs and metrics to improve reliability.",
            "Improve quality through JUnit, Mockito, integration tests, API checks and maintainable service design.",
            "Collaborate in agile teams with product owners, QA, DevOps and engineers to turn complex requirements into working backend solutions.",
        ],
    },
    "scania-business-it-analyst": {
        "display_role": "Business IT Analyst - Technical Training and BCM",
        "position": "Business IT Analyst | Training Coordination | Agile Change Management",
        "summary": [
            "Software and business-oriented IT professional with 8+ years of experience across backend systems, stakeholder dialogue, agile delivery, documentation, training support and production operations.",
            "Strong fit for Business IT Analyst work through structured coordination, backlog follow-up, training material quality, stakeholder communication, Jira-style agile collaboration and continuous improvement.",
            "Combines technical understanding with clear communication to bridge business users, trainers, system owners and development teams in international environments.",
        ],
        "target_fit": [
            "Can coordinate backlog items, follow up activities, create structure and maintain clarity across multiple stakeholders.",
            "Experienced documenting workflows, supporting users, clarifying needs and communicating technical topics to non-technical stakeholders.",
            "Comfortable in agile teams with product owners, QA, DevOps, engineers and business stakeholders, including facilitation and follow-up.",
            "Technical background in software engineering, databases, integrations and production support helps understand CAD/PDM-adjacent IT environments quickly.",
            "Fluent in English and experienced in Swedish-friendly international business contexts; motivated to support training and change management.",
        ],
        "skills": [
            ("Business analysis", "Stakeholder dialogue, requirements clarification, backlog coordination, process structure, follow-up, continuous improvement"),
            ("Training and BCM", "Training material quality checks, documentation, user support, knowledge sharing, learning setup improvement"),
            ("Agile", "Scrum/Kanban awareness, agile ways of working, facilitation, product owner collaboration, Jira-style coordination"),
            ("Technical base", "Java, REST APIs, SQL, PostgreSQL, integrations, production systems, CI/CD, Grafana, troubleshooting"),
            ("Communication", "International teams, business and IT bridge, clear English, Swedish-friendly workplace communication"),
        ],
        "msc_bullets": [
            "Work with product owners, QA, DevOps, engineers and stakeholders to clarify needs, coordinate delivery and follow up end-to-end changes.",
            "Document workflows, operational procedures and technical decisions to support knowledge sharing, onboarding and consistent delivery quality.",
            "Translate business needs into backend service behaviour, validation rules, API changes and testable acceptance criteria.",
            "Support production systems by analyzing incidents, communicating status, coordinating fixes and confirming release outcomes.",
            "Use agile delivery practices, CI/CD awareness, automated testing and monitoring to improve transparency and team reliability.",
            "Collaborate with technical and non-technical colleagues in international environments using clear English and Swedish-friendly business communication.",
        ],
    },
    "scania-devops-product-owner": {
        "display_role": "DevOps Product Owner",
        "position": "DevOps Product Owner | CI/CD | Developer Experience | Platform Engineering",
        "summary": [
            "Senior software developer with 8+ years of IT experience across backend systems, CI/CD, containers, monitoring, production support and agile team collaboration.",
            "Well matched to DevOps Product Owner work through practical developer experience, backlog and priority collaboration, automation mindset, stakeholder communication and focus on engineering productivity.",
            "Can translate developer needs into clear platform value around CI/CD, infrastructure, automation, security, quality, observability and developer experience.",
        ],
        "target_fit": [
            "Understands developer pain points first-hand and can prioritize DevOps capabilities that improve speed, quality and operational excellence.",
            "Experience with GitHub Actions, Docker, Kubernetes, Maven, Linux, CI/CD, Grafana, Prometheus, logging and production troubleshooting.",
            "Comfortable collaborating with developers, architects, DevOps, QA, product owners and business stakeholders to align technical needs with business value.",
            "Can monitor delivery capability through KPIs such as build quality, deployment reliability, incident trends, automation coverage and developer feedback.",
            "Ready to work with GitLab CI, Jenkins, AWS, Terraform, Ansible, Artifactory, Jira and Confluence using strong adjacent DevOps foundations.",
        ],
        "skills": [
            ("Product ownership", "Backlog prioritization, roadmap input, stakeholder collaboration, business value translation, delivery follow-up"),
            ("DevOps", "CI/CD, GitHub Actions, Docker, Kubernetes, Linux, Maven, Gradle awareness, OpenShift awareness, automation"),
            ("Platform engineering", "Developer experience, engineering productivity, quality, security, reusable workflows, modern engineering practices"),
            ("Observability", "Grafana, Prometheus, NewRelic, logging, metrics, KPIs, troubleshooting, production support"),
            ("Tooling alignment", "Jira-style coordination, Confluence-style documentation, GitLab CI/Jenkins/AWS/Terraform/Ansible awareness"),
        ],
        "msc_bullets": [
            "Use CI/CD practices, GitHub Actions awareness, Docker, Kubernetes, Maven and Git to support stable backend software delivery.",
            "Collaborate with product owners, QA, DevOps, architects and engineers to prioritize technical improvements and release readiness.",
            "Improve developer and operator experience by documenting workflows, reducing recurring incidents and strengthening automated tests.",
            "Monitor services with Grafana, Prometheus and NewRelic, using logs and metrics to drive continuous reliability improvements.",
            "Build and maintain Java backend services and REST APIs, giving practical insight into developer platform needs and delivery friction.",
            "Support production incidents, root-cause analysis and operational follow-up with responsibility for quality and stakeholder communication.",
        ],
    },
    "scania-lead-solution-architect": {
        "display_role": "Lead Solution Architect - Finance IT",
        "position": "Solution Architecture | Enterprise Integration | Finance IT Transformation",
        "summary": [
            "Senior software developer with 8+ years of experience in enterprise applications, backend services, integrations, databases, production systems and stakeholder collaboration.",
            "Relevant to Lead Solution Architect work through strong hands-on architecture foundations: APIs, microservices, data handling, secure interfaces, cloud/container awareness, integration design and maintainable enterprise solutions.",
            "Can support Finance IT transformation by bridging business and IT, documenting target-state decisions, aligning stakeholders and designing scalable, secure, value-driven solutions.",
        ],
        "target_fit": [
            "Practical experience designing and maintaining APIs, microservices, database-backed systems, integrations and production-quality enterprise applications.",
            "Background in finance and economics plus software engineering supports understanding of Finance IT, legal/compliance-adjacent processes and ERP transformation contexts.",
            "Can collaborate with architects, product owners, DevOps, engineers and business stakeholders to align solution design with business goals.",
            "Relevant exposure to data platforms, APIs, event-driven architecture awareness, cloud concepts, AI/LLM interest and reusable data products.",
            "Strong communication, documentation, code review and mentoring habits that support architectural leadership and team guidance.",
        ],
        "skills": [
            ("Architecture", "Solution design, API design, microservices, integration patterns, secure interfaces, scalability, maintainability, governance awareness"),
            ("Enterprise IT", "Finance/economics background, ERP awareness, data platforms, legacy modernization, stakeholder alignment, capability mapping awareness"),
            ("Technology", "Java 17/21, Spring Boot, REST APIs, PostgreSQL, SQL, Redis, Docker, Kubernetes, CI/CD, cloud concepts"),
            ("Data and integration", "JSON, XML, data validation, query optimisation, event-driven architecture awareness, reusable data product interest"),
            ("Leadership", "Code reviews, mentoring, technical documentation, cross-functional collaboration, business and IT communication"),
        ],
        "msc_bullets": [
            "Design, develop and maintain Java backend services, REST APIs and data integrations for business-critical production systems.",
            "Collaborate with product owners, QA, DevOps and engineers to align solution design with business needs, technical constraints and release goals.",
            "Use PostgreSQL, SQL, Redis, JSON and XML to support reliable data handling, validation, integration flows and service behaviour.",
            "Apply microservice, secure interface, CI/CD, Docker, Kubernetes and observability practices to improve scalability and maintainability.",
            "Review code, document workflows, mentor colleagues and share knowledge to support consistent engineering decisions and quality.",
            "Troubleshoot production issues using Grafana, Prometheus, NewRelic, logs and metrics, then feed learnings into technical improvements.",
        ],
    },
}

# Add clariter/apps/project bullets common or lightly tailored
COMMON_CLARITER = [
    "Built Java backend applications and ETL services for data-driven business processes.",
    "Developed REST APIs and secure authentication flows using JWT, OAuth2 and role-based access control.",
    "Worked with SQL, relational databases, integration logic, automated tests and stakeholder clarification.",
]
COMMON_APPS = [
    "Developed and supported enterprise applications and integrations using Java, SQL and PL/SQL.",
    "Maintained business-critical systems, handled production incidents, analyzed root causes and communicated fixes.",
    "Improved batch jobs, data checks, reports and integration flows used by operations teams; promoted within 1 year.",
]
COMMON_PROJECTS = [
    ("Smart Trader, Cloud Data Platform", "Python, Docker, AWS CDK, CI/CD", "2024 to 2026", [
        "Built a backend and web application with service structure, tests and repeatable delivery.",
        "Used Docker, cloud infrastructure concepts and CI/CD practices to support maintainable operations.",
        "Practiced fintech-style data handling, automation, monitoring awareness and reliable release flow.",
    ]),
    ("EFK Observability Stack", "Elasticsearch, Fluentd, Kibana, Docker", "2020", [
        "Worked with log aggregation using Elasticsearch, Fluentd and Kibana.",
        "Used Docker based environments to explore observability, monitoring and production visibility.",
    ]),
    ("Nexus SSO Integration", "Java, Docker, Keycloak, SSO", "2024", [
        "Studied and adapted a Java based single sign-on integration for secure backend access.",
        "Worked with Docker, Keycloak, authentication, access control and service configuration.",
    ]),
]

ACHIEVEMENTS = [
    ("Promotions", "Promoted from Associate Trainee to Associate Consultant within 1 year"),
    ("Certifications", "CMMI Certified within 2 years. Ranked top 3 in Java Certification course"),
    ("Languages", "Fluent in English; Swedish-friendly business communication context"),
    ("Work authorization", "EU long-term residence permit; does not need sponsorship"),
]


def tex_escape(s: str) -> str:
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
        "–": "--",
        "—": "--",
        "‑": "-",
        "’": "'",
        "“": "\"",
        "”": "\"",
        "´": "'",
    }
    return ''.join(repl.get(ch, ch) for ch in s)


def cvitems(items):
    return "\\begin{cvitems}\n" + "\n".join(f"  \\item {{{tex_escape(x)}}}" for x in items) + "\n\\end{cvitems}"


def cvskills(items):
    return "\\begin{cvskills}\n" + "\n".join(f"  \\cvskill{{{tex_escape(k)}}}{{{tex_escape(v)}}}" for k, v in items) + "\n\\end{cvskills}"


def cventry(role, company, location, dates, bullets):
    return (
        f"\\cventry{{{tex_escape(role)}}}{{{tex_escape(company)}}}{{{tex_escape(location)}}}{{{tex_escape(dates)}}}{{\n"
        f"{cvitems(bullets)}\n}}"
    )


def render(label, data):
    title = f"Scania - {data['display_role']}"
    parts = []
    parts.append("%!TEX TS-program = xelatex")
    parts.append("%!TEX encoding = UTF-8 Unicode")
    parts.append("\\documentclass[11pt, a4paper]{awesome-cv}")
    parts.append("\\fontdir[fonts/]")
    parts.append("\\colorlet{awesome}{awesome-red}")
    parts.append(f"\\hypersetup{{pdftitle={{{tex_escape(title)}}}, pdfauthor={{Manisha Padhi}}, pdfsubject={{{tex_escape(data['display_role'])}}}, pdfkeywords={{{tex_escape(data['position'])}}}}}")
    parts.append(f"\\name{{{COMMON_CONTACT['name_first']}}}{{{COMMON_CONTACT['name_last']}}}")
    parts.append(f"\\position{{{tex_escape(data['position'])}}}")
    parts.append(f"\\address{{{tex_escape(COMMON_CONTACT['address'])}}}")
    parts.append(f"\\mobile{{{tex_escape(COMMON_CONTACT['phone'])}}}")
    parts.append(f"\\email{{{tex_escape(COMMON_CONTACT['email'])}}}")
    parts.append(f"\\github{{{tex_escape(COMMON_CONTACT['github'])}}}")
    parts.append("\\headersocialsep[ \\textbar{} ]")
    parts.append("\\usepackage{import}")
    parts.append("\\begin{document}")
    parts.append("\\makecvheader")
    parts.append(f"\\cvsection{{Target Role}}\n{cvskills([('Company and role', title), ('Location', 'Sodertalje / Stockholm region, Sweden'), ('Work authorization', 'EU long-term residence permit; does not need sponsorship')])}")
    parts.append("\\cvsection{Professional Summary}\n" + cvskills([("Summary", s) for s in data["summary"]]))
    parts.append("\\cvsection{Target Role Fit}\n" + cvitems(data["target_fit"]))
    parts.append("\\cvsection{Technical Skills}\n" + cvskills(data["skills"]))
    parts.append("\\cvsection{Work Experience}\n\\begin{cventries}")
    parts.append(cventry(BASE_EXPERIENCE["msc"]["role"], BASE_EXPERIENCE["msc"]["company"], BASE_EXPERIENCE["msc"]["location"], BASE_EXPERIENCE["msc"]["dates"], data["msc_bullets"]))
    parts.append(cventry(BASE_EXPERIENCE["clariter"]["role"], BASE_EXPERIENCE["clariter"]["company"], BASE_EXPERIENCE["clariter"]["location"], BASE_EXPERIENCE["clariter"]["dates"], COMMON_CLARITER))
    parts.append(cventry(BASE_EXPERIENCE["apps"]["role"], BASE_EXPERIENCE["apps"]["company"], BASE_EXPERIENCE["apps"]["location"], BASE_EXPERIENCE["apps"]["dates"], COMMON_APPS))
    parts.append("\\end{cventries}")
    parts.append("\\cvsection{Project Highlights}\n\\begin{cventries}")
    for titlep, tech, date, bullets in COMMON_PROJECTS:
        parts.append(cventry(tech, titlep, "GitHub: manishapadhi1", date, bullets))
    parts.append("\\end{cventries}")
    parts.append("\\cvsection{Education}\n\\begin{cventries}")
    for role, company, loc, dates, bullets in COMMON_EDUCATION:
        parts.append(cventry(role, company, loc, dates, bullets))
    parts.append("\\end{cventries}")
    parts.append("\\cvsection{Achievements and Certifications}\n" + cvskills(ACHIEVEMENTS))
    parts.append("\\end{document}\n")
    return "\n\n".join(parts)

for label, data in VARIANTS.items():
    (TEX_DIR / f"{label}.tex").write_text(render(label, data), encoding="utf-8")

readme = ["# Tailored Scania CV PDFs", "", "Generated from the Scania job listings supplied by the user. Filenames follow `company-role` labels.", ""]
for label, data in VARIANTS.items():
    readme.append(f"- `{label}.pdf` — {data['display_role']}")
(Path(ROOT) / "tailored_pdfs" / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
print(f"Generated {len(VARIANTS)} tailored LaTeX files in {TEX_DIR}")
