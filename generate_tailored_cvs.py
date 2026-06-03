from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEX_DIR = ROOT / "tailored_tex"
PDF_DIR = ROOT / "tailored_pdfs"
TEX_DIR.mkdir(exist_ok=True)
PDF_DIR.mkdir(exist_ok=True)

COMMON_CONTACT = {
    "name_first": "Manisha",
    "name_last": "Padhi",
    "address": "Stockholm, Sweden | Female | EU long-term residence permit | No sponsorship required",
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
        "position": "Software Developer | Agile Delivery | Backend Services | Continuous Improvement",
        "summary": [
            "Software Developer with 8+ years of IT experience and strong hands-on background in Java backend systems, agile delivery, production support and cross-functional collaboration.",
            "Experienced in sprint-based delivery with product owners, QA, DevOps, and engineering teams, including code reviews, knowledge sharing, impediment handling, CI/CD, and production-quality software.",
            "Brings practical technical credibility for teams working with backend services, microservices, diagnostics-adjacent platforms, connectivity, security mindset and continuous improvement.",
        ],
        "target_fit": [
            "Facilitates agile delivery conversations from a developer perspective, keeping team discussions focused on value, flow, quality, and release readiness.",
            "Experienced collaborating with product owners, QA, DevOps and engineers to align priorities, dependencies and release readiness in agile teams.",
            "Hands-on Java, Spring Boot, REST API, microservice, Kubernetes, CI/CD, Grafana and production support background gives credibility with technical teams.",
            "Comfortable coaching colleagues, reviewing code, documenting workflows and strengthening common ways of working across distributed teams.",
            "Motivated by TRATON values: customer first, respect, team spirit, responsibility and elimination of waste through continuous improvement.",
        ],
        "skills": [
            ("Agile delivery", "Scrum ceremonies, sprint planning, reviews, retrospectives, daily stand-ups, SAFe-inspired PI context, backlog flow, impediment removal"),
            ("Delivery", "Cross-functional teams, product owner collaboration, QA, DevOps, release readiness, documentation, stakeholder communication"),
            ("Technical context", "Java 17, Spring Boot, REST APIs, microservices, PostgreSQL, Redis, Docker, Kubernetes, GitHub Actions, CI/CD"),
            ("Observability", "Grafana, Prometheus, NewRelic, logging, metrics, incident analysis, production troubleshooting"),
            ("Diagnostics platform context", "secure interfaces, backend services, API checks, integration testing, reliability, diagnostics/connectivity domain context"),
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
        "position": "Software Developer | Backend Services | APIs | Automation | AI-Enabled Workflows",
        "summary": [
            "Software Developer with 8+ years of experience building backend services, APIs, automation and production systems, with practical exposure to AI-powered developer workflows and enterprise automation patterns.",
            "Experienced translating unclear user and engineering needs into working prototypes, backend integrations, and production-ready services in collaboration with users, product owners, QA, DevOps, and engineering teams.",
            "Brings a pragmatic build-first mindset for agentic workflows, including agentic architectures, tool use, guardrails, agent security, model tiering and hybrid deployments across frontier and smaller models.",
        ],
        "target_fit": [
            "Analyzes business and engineering friction, separating deterministic logic, human review steps, agent/tool orchestration and AI-assisted workflow opportunities.",
            "Experienced building backend services, REST APIs, automation, testable integrations and CI/CD flows that can become reusable AI-enabled capabilities.",
            "Comfortable working hands-on with stakeholders to clarify ambiguous needs, prototype solutions and improve adoption based on feedback.",
            "Understands enterprise AI tooling patterns including Codex-style coding agents, ChatGPT Enterprise, Microsoft 365 Copilot, GitLab Duo, model repositories and Hugging Face model consumption.",
            "Strong fit for hub-and-spoke AI Enablement because of communication, knowledge sharing, documentation and collaborative engineering habits.",
        ],
        "skills": [
            ("AI platforms", "LangChain, AutoCodeRover, Codex-style coding agents, ChatGPT Enterprise, Microsoft 365 Copilot, GitLab Duo, agentic workflows"),
            ("Agentic architecture", "tool orchestration, human-in-the-loop design, guardrails, agent security, model tiering, GAIA-style evaluation, hybrid AI deployments"),
            ("Developer tooling", "Git, GitHub Actions, CI/CD, Docker, Maven, test automation, documentation, repeatable delivery, developer enablement workflows"),
            ("Model and data operations", "AWS CDK project exposure, PostgreSQL, SQL, Redis, JSON, XML, Hugging Face model consumption, Artifactory model repositories"),
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
        "position": "Software Developer | Requirements | Backend Integration | Quality Engineering",
        "summary": [
            "Software Developer with 8+ years of IT experience connecting business needs, system behaviour, requirements, implementation, testing and production quality.",
            "Experienced in structured requirements handling, stakeholder communication, traceability mindset, integration testing, risk management, and complex distributed systems.",
            "Brings strong software engineering discipline for charging-related vehicle functions: translating needs into clear requirements, aligning teams and ensuring testable, reliable delivery.",
        ],
        "target_fit": [
            "Translates customer and stakeholder needs into requirements, acceptance criteria, traceability links, test cases, risk follow-up and delivery readiness.",
            "Experienced managing dependencies across product owners, QA, DevOps, engineers and operational stakeholders in agile delivery.",
            "Strong testing and quality mindset through JUnit, Mockito, integration tests, API checks, production support and incident analysis.",
            "Relevant technical foundation in distributed systems, APIs, secure interfaces, data validation and reliable system behaviour.",
            "Motivated by electrification, charging systems, sustainable transport, functional safety and cyber security processes as learning domains.",
        ],
        "skills": [
            ("Function ownership", "requirements engineering, function breakdown, traceability, dependency management, risk follow-up, test coverage, delivery readiness"),
            ("System development", "Java, Spring Boot, REST APIs, microservices, distributed systems, secure interfaces, integration testing"),
            ("Quality", "JUnit, Mockito, automated tests, API checks, validation, root-cause analysis, documentation"),
            ("Vehicle domain", "charging systems context, electrical power distribution concepts, ISO 26262/HARA concepts, ISO 21434/TARA concepts, UNECE R155/R156 regulatory context"),
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
        "position": "Backend Developer | Cloud Connectivity | APIs | DevSecOps",
        "summary": [
            "Senior backend developer with 8+ years of experience and 3+ years focused on Java, Spring Boot, REST APIs, microservices, databases, production systems and agile delivery.",
            "Strong background in backend service development, cloud and container exposure, secure integrations, CI/CD, monitoring, production support, and connected-system reliability.",
            "Contributes to robust communication platforms through APIs, internal tools, event-ready services, test automation, and operational improvements with a DevSecOps mindset.",
        ],
        "target_fit": [
            "Builds, tests, deploys and maintains backend services and internal tools with end-to-end ownership, monitoring and production accountability.",
            "Experience with REST APIs, microservices, Docker, Kubernetes, CI/CD, Grafana, databases and clean maintainable backend code.",
            "Delivered Smart Trader cloud data platform project work using AWS CDK concepts, Docker and CI/CD practices, strengthening cloud-native delivery readiness.",
            "Relevant secure communication mindset through JWT, OAuth2, role-based access control, secure interfaces and API validation.",
            "Ready to transfer Java backend experience into C#/.NET ecosystems while contributing immediately to API design, testing, monitoring and DevSecOps practices.",
        ],
        "skills": [
            ("Backend", "Java 17/21, Spring Boot, Spring WebFlux, REST APIs, microservices, internal tools, maintainable code, clean architecture principles"),
            ("Cloud and DevSecOps", "AWS, Docker, Kubernetes, GitHub Actions, CI/CD, AWS CDK project exposure, Maven, Linux, infrastructure-as-code concepts"),
            ("Connectivity", "vehicle connectivity context, secure communication, REST APIs, message routing, Kafka/Kinesis/SQS concepts, telecom/network protocol concepts"),
            ("Security", "JWT, OAuth2, role-based access control, secure APIs, certificates, PKI/HSM concepts, DevSecOps mindset"),
            ("Operations", "Grafana, Prometheus, NewRelic, logging, metrics, alerting, test automation, troubleshooting, SQL, PostgreSQL, Redis"),
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
        "position": "Software Developer | Business IT Analysis | Agile Coordination | Training Support",
        "summary": [
            "Software and business-oriented IT professional with 8+ years of experience across backend systems, stakeholder dialogue, agile delivery, documentation, training support and production operations.",
            "Experienced in structured coordination, backlog follow-up, documentation quality, stakeholder communication, agile collaboration, and continuous improvement.",
            "Combines technical understanding with clear communication to bridge business users, trainers, system owners and development teams in international environments.",
        ],
        "target_fit": [
            "Coordinates backlog items, training activities, quality checks and stakeholder follow-up to create structure and clarity across business and IT teams.",
            "Experienced documenting workflows, supporting users, clarifying needs and communicating technical topics to non-technical stakeholders.",
            "Comfortable in agile teams with product owners, QA, DevOps, engineers and business stakeholders, including facilitation and follow-up.",
            "Technical background in software engineering, databases, integrations and production support helps understand CAD/PDM-adjacent IT environments quickly.",
            "Fluent in English and experienced in Swedish-friendly international business contexts; motivated to support training and change management.",
        ],
        "skills": [
            ("Business analysis", "stakeholder dialogue, requirements clarification, backlog coordination, process structure, activity follow-up, continuous improvement"),
            ("Training and BCM", "training material quality checks, LMS coordination, user support, documentation ownership, knowledge sharing, learning setup improvement"),
            ("Agile coordination", "Scrum/Kanban, agile ways of working, meeting facilitation, product owner collaboration, Jira-style coordination"),
            ("Technical base", "Java, REST APIs, SQL, PostgreSQL, integrations, production systems, CI/CD, Grafana, troubleshooting"),
            ("Communication", "International teams, business and IT bridge, clear English, Swedish-friendly workplace communication"),
        ],
        "msc_bullets": [
            "Work with product owners, QA, DevOps, engineers and stakeholders to clarify needs, coordinate delivery and follow up end-to-end changes.",
            "Document workflows, operational procedures and technical decisions to support knowledge sharing, onboarding and consistent delivery quality.",
            "Translate business needs into backend service behaviour, validation rules, API changes and testable acceptance criteria.",
            "Support production systems by analyzing incidents, communicating status, coordinating fixes and confirming release outcomes.",
            "Use agile delivery practices, CI/CD practices, automated testing and monitoring to improve transparency and team reliability.",
            "Collaborate with technical and non-technical colleagues in international environments using clear English and Swedish-friendly business communication.",
        ],
    },
    "scania-devops-product-owner": {
        "display_role": "DevOps Product Owner",
        "position": "Software Developer | DevOps | CI/CD | Developer Experience",
        "summary": [
            "Senior software developer with 8+ years of IT experience across backend systems, CI/CD, containers, monitoring, production support and agile team collaboration.",
            "Combines practical developer experience with backlog and priority collaboration, automation mindset, stakeholder communication, and focus on engineering productivity.",
            "Can translate developer needs into clear platform value around CI/CD, infrastructure, automation, security, quality, observability and developer experience.",
        ],
        "target_fit": [
            "Prioritizes DevOps capabilities that improve developer experience, CI/CD flow, quality gates, security, operational readiness and platform cost optimisation.",
            "Works with AWS, Kubernetes, Docker, GitLab/GitHub CI/CD pipelines, pipeline parallelisation, SonarQube-style quality gates and clean code practices.",
            "Collaborates with developers, architects, DevOps, QA, product owners and business stakeholders to translate technical platform needs into business value.",
            "Uses delivery signals such as build quality, deployment reliability, incident trends, automation coverage, developer feedback and operational KPIs to guide improvements.",
            "Aligns platform tooling around GitLab CI, Jenkins, AWS, Terraform, Ansible, Artifactory, Jira, Confluence, Grafana and Prometheus concepts.",
        ],
        "skills": [
            ("Product ownership", "DevOps backlog prioritization, roadmap input, stakeholder collaboration, business value translation, delivery capability follow-up"),
            ("DevOps", "AWS, Kubernetes, Docker, GitLab CI/CD, GitHub Actions, pipeline parallelisation, Maven, Linux, OpenShift, automation"),
            ("Platform engineering", "developer experience, engineering productivity, reusable workflows, clean code practices, SonarQube/code quality gates, secure delivery"),
            ("Operations", "Grafana, Prometheus, NewRelic, logging, metrics, KPIs, troubleshooting, operationalisation, production support"),
            ("Cost and tooling", "platform cost optimisation, Jira, Confluence, GitLab CI, Jenkins, AWS, Terraform, Ansible, Artifactory"),
        ],
        "msc_bullets": [
            "Dockerize and maintain Java backend services and REST APIs, using Git, Maven, CI/CD practices and Kubernetes-based delivery patterns for stable releases.",
            "Improve delivery confidence through automated tests, integration checks, clean code practices and code review, with SonarQube-style quality gate alignment.",
            "Collaborate with product owners, QA, DevOps, architects and engineers to prioritize technical improvements, release readiness and operationalisation.",
            "Use Grafana, Prometheus, NewRelic, logs and metrics to monitor services, troubleshoot incidents and turn operational signals into reliability improvements.",
            "Contribute to developer experience through documentation, repeatable workflows, automation opportunities and reduced delivery friction across teams.",
            "Bring practical backend experience to DevOps product decisions around CI/CD pipeline design, pipeline parallelisation, platform cost optimisation, quality gates and secure delivery.",
        ],
    },
    "scania-lead-solution-architect": {
        "display_role": "Lead Solution Architect - Finance IT",
        "position": "Software Developer | Solution Architecture | Enterprise Integration",
        "summary": [
            "Senior software developer with 8+ years of experience in enterprise applications, backend services, integrations, databases, production systems and stakeholder collaboration.",
            "Brings hands-on architecture foundations in APIs, microservices, data handling, secure interfaces, cloud and container concepts, integration design, and maintainable enterprise solutions.",
            "Supports Finance IT transformation by bridging business and IT, documenting target-state decisions, aligning stakeholders and designing scalable, secure, value-driven solutions.",
        ],
        "target_fit": [
            "Designs and maintains APIs, microservices, database-backed systems, integrations and production-quality enterprise applications with architecture discipline.",
            "Background in finance and economics plus software engineering supports understanding of Finance IT, legal/compliance-adjacent processes and ERP transformation contexts.",
            "Collaborates with architects, product owners, DevOps, engineers, and business stakeholders to align solution design with business goals.",
            "Relevant exposure to data platforms, APIs, event-driven architecture concepts, cloud concepts, AI-enabled solution concepts and reusable data products.",
            "Strong communication, documentation, code review and mentoring habits that support architectural leadership and team guidance.",
        ],
        "skills": [
            ("Architecture", "solution design, API design, microservices, integration patterns, event-driven architecture, secure interfaces, scalability, governance"),
            ("Enterprise IT", "finance/economics background, ERP concepts, data platforms, legacy modernization, capability mapping, stakeholder alignment"),
            ("Technology", "Java 17/21, Spring Boot, REST APIs, PostgreSQL, SQL, Redis, Docker, Kubernetes, CI/CD, cloud concepts"),
            ("Data and integration", "JSON, XML, data validation, query optimisation, reusable data products, API-led integration, data governance concepts"),
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
COMMON_QUANTIFIED_HIGHLIGHTS = [
    "8+ years of enterprise IT experience, including 3+ years focused on Java/Spring Boot backend development for production systems.",
    "Recognized career progression: promoted from Associate Trainee to Associate Consultant within 1 year.",
    "CMMI certified within 2 years and ranked top 3 in a Java certification course, supporting a quality-focused engineering profile.",
]

COMMON_PROJECTS = [
    ("Smart Trader, Cloud Data Platform", "Python, Docker, AWS CDK, CI/CD", "2024 to 2026", [
        "Built a backend and web application with service structure, tests and repeatable delivery.",
        "Used Docker, cloud infrastructure concepts and CI/CD practices to support maintainable operations.",
        "Practiced fintech-style data handling, automation, monitoring and reliable release flow.",
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


def cvparagraphs(items):
    blocks = []
    for item in items:
        blocks.append(f"\\noindent\\descriptionstyle{{{tex_escape(item)}}}\\par")
    return "\\vspace{-0.5ex}\n" + "\n\\vspace{0.6ex}\n".join(blocks)


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
    parts.append("\\cvsection{Professional Summary}\n" + cvparagraphs(data["summary"]))
    parts.append("\\cvsection{Selected Achievements and Highlights}\n" + cvitems(data["target_fit"][:3] + COMMON_QUANTIFIED_HIGHLIGHTS))
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
