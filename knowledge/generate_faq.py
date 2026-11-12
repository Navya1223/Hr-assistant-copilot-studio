# Employee HR FAQ v3 -- full answers + alternative phrasings for better retrieval
# Format per entry: (question, [also asked as...], answer)
S = []
def sec(title, items): S.append((title, items))

sec("1. Onboarding and First Days", [
("What do I need to bring on my first day?",
 ["What documents do I need when I start?", "first day checklist"],
 "Please bring: your ID card or passport, your tax ID (Steuer-ID), your social security number, your health insurance details, your bank details (IBAN), and -- for working students -- your current certificate of enrolment (Immatrikulationsbescheinigung). If anything is missing, you can upload it later in the HR portal under \\emph{My Profile > Documents} within 2 weeks."),
("Who is my contact person in the first weeks?",
 ["Do I get a buddy?", "who helps me when I am new?"],
 "Your direct manager is your main contact. In addition, every new employee gets a buddy from the team for the first 3 months who helps with practical questions. HR (hr@company.example) is available for all contract and payroll questions."),
("When do I get my laptop and accounts?",
 ["I have no laptop yet", "my login does not work on day one"],
 "IT prepares your laptop, email account and system access for your first day. If something is missing or does not work, open a ticket with IT support (it-support@company.example) or ask your buddy to help you contact IT."),
("How long is the probation period and what does it mean?",
 ["Probezeit", "notice period during probation"],
 "The probation period is 6 months. During probation, either you or the company can end the contract with 2 weeks' notice. Around month 5 you have a feedback meeting with your manager."),
])

sec("2. Working Hours and Time Tracking", [
("What are the regular working hours?",
 ["When do I have to be at work?", "core hours", "flexitime"],
 "Full-time is 39 hours per week. We use flexitime: you can start between 7:00 and 10:00 and finish between 15:00 and 19:00, as long as you are available during core hours from 9:30 to 15:00 (Fridays until 13:00)."),
("How many hours can working students work?",
 ["Werkstudent hours", "can I work more in the semester break?"],
 "During the semester, working students may work a maximum of 20 hours per week. During semester breaks, up to 39 hours per week are possible after agreement with your manager. Please inform HR of your semester dates at the start of each semester."),
("Can I request a flexible or different work schedule?",
 ["flexible work schedule", "Can I change my working hours?", "Can I work part-time?", "reduce my hours"],
 "Yes. Steps: 1) Talk to your manager about the schedule you want. 2) Submit the request in the HR portal under \\emph{Requests > Working Time}. 3) HR answers within 2 weeks. Changes usually start on the 1st of the following month. Core hours still apply. Part-time requests should be submitted at least 3 months before the desired start."),
("How do I record my working time?",
 ["time tracking", "Zeiterfassung", "I forgot to clock in"],
 "Record your working time daily in the HR portal under \\emph{Time Tracking}, including breaks. If you forgot an entry, you can correct it yourself within 7 days; after that, ask your manager to correct it."),
("What are the rules for breaks?",
 ["How long is my lunch break?", "break rules"],
 "If you work more than 6 hours, you must take at least 30 minutes of break; if you work more than 9 hours, at least 45 minutes. Breaks can be split into blocks of at least 15 minutes."),
("What is the maximum working time per day?",
 ["How long can I work in one day?", "rest time"],
 "Normally 8 hours, at most 10 hours per day. Between two working days you must have at least 11 hours of rest."),
("How is overtime handled?",
 ["Is overtime paid?", "Überstunden"],
 "Overtime must be approved by your manager in advance. It is recorded in time tracking and compensated with time off within 3 months. Overtime is not paid out."),
])

sec("3. Vacation and Time Off", [
("How many vacation days do I have?",
 ["vacation policy", "holiday entitlement", "Urlaubstage", "How many days off do I get?"],
 "Full-time employees (5 days per week) have 30 vacation days per calendar year. Part-time employees and working students get vacation pro rata: 30 x (your working days per week) / 5. Example: 3 days per week = 18 vacation days. In your first and last year of employment, you get 1/12 of your annual vacation for each full month worked. You can see your remaining days in the HR portal under \\emph{Absences}."),
("How do I request vacation or time off?",
 ["What steps should I follow to request time off?", "apply for holiday", "book vacation"],
 "Steps: 1) Check with your team that the dates work. 2) Submit the request in the HR portal under \\emph{Absences > New Request}. 3) Submit at least 2 weeks in advance; for more than 5 consecutive working days, at least 4 weeks in advance. 4) Your manager approves or rejects it within 3 working days, and you get an email. 5) Enter the absence in your Outlook calendar and set an out-of-office message."),
("Can I take half-days of vacation?",
 ["half day off", "Can I take vacation by the hour?"],
 "Yes. You can take vacation as half-days (0.5 day). Choose \\emph{Half day} when you create the request in the HR portal under \\emph{Absences > New Request}. Hourly vacation is not possible."),
("What happens to vacation I don't use?",
 ["Can I carry over vacation?", "remaining vacation", "Resturlaub"],
 "Remaining vacation can be carried over and taken until 31 March of the following year. After that it expires. Vacation is not paid out, except when you leave the company and could not take it."),
("Are there company closure days?",
 ["Christmas closure", "Betriebsferien"],
 "Yes. The company is closed from 20 December to 2 January. 3 of your vacation days are planned for this period; public holidays in between do not count as vacation."),
("Do I get special leave for personal events?",
 ["Sonderurlaub", "day off for my wedding", "day off for moving", "bereavement leave"],
 "Yes, paid special leave: your own wedding 2 days, birth of your child 1 day, death of a close family member (partner, child, parent, sibling) 2 days, moving house 1 day (once per year). Request it in the HR portal under \\emph{Absences > Special Leave}, with a document if possible."),
("What happens if I get sick during my vacation?",
 ["sick on holiday"],
 "Days of illness with a doctor's certificate are not counted as vacation; you get those days back. Inform your manager and HR immediately, and make sure the certificate covers those days."),
("Can I take unpaid leave or a sabbatical?",
 ["unpaid leave", "sabbatical", "longer break"],
 "Unpaid leave of up to 3 months is possible after agreement with your manager and HR. Submit the request in the HR portal at least 2 months in advance."),
])

sec("4. Sick Leave", [
("What do I do if I am sick?",
 ["I feel sick today", "how to call in sick", "Krankmeldung"],
 "Inform your manager by phone or Teams before 9:00 on the first day of illness, and say how long you expect to be absent. Also enter the absence in the HR portal under \\emph{Absences > Sick Leave}."),
("When do I need a doctor's certificate?",
 ["sick note", "AU", "doctor's note"],
 "From the 3rd day of illness. The certificate (eAU) is retrieved electronically from your health insurance, so you do not need to send a paper copy -- just tell your doctor that you are employed."),
("Do I get paid when I am sick?",
 ["sick pay", "Krankengeld"],
 "Yes. Your salary continues for up to 6 weeks per illness. After that, your health insurance pays sick pay (Krankengeld)."),
("What if my child is sick?",
 ["child sick day", "Kinderkrankentage"],
 "Inform your manager on the same day. You need a doctor's certificate for your child. Days caring for a sick child are covered by the statutory children's sick days through your health insurance; HR helps with the forms."),
])

sec("5. Working from Home and Workplace", [
("Can I work from home?",
 ["remote work policy", "home office", "Can I work remotely?"],
 "Office roles may work up to 2 days per week from home, agreed with the team. Warehouse and shipping roles cannot work from home. Enter home office days in the team calendar. You must be reachable during core hours and follow the IT security rules."),
("Is there a formal process after my manager approves home office?",
 ["Do I need to submit a home office request to HR?", "home office approval"],
 "No separate HR application is needed for regular home office (up to 2 days per week). After agreeing with your manager and team: 1) enter your home office days in the team calendar, 2) make sure your laptop has the VPN installed (IT support can help), 3) be reachable during core hours. Only working from abroad needs written HR approval."),
("Can I work from abroad?",
 ["work from another country", "workation"],
 "Working from abroad is only possible after written approval from HR, for at most 10 working days per year, and only within the EU. Submit the request at least 4 weeks in advance in the HR portal under \\emph{Requests}."),
("What equipment do I get for home office?",
 ["Can I get a monitor?", "home office equipment"],
 "The company provides a laptop and headset. A monitor, keyboard and mouse can be ordered through IT support."),
("Is there a home office allowance?",
 ["home office money"],
 "No separate allowance is paid. You can claim home office days in your own tax return."),
("What should I do if I lose my access card or badge?",
 ["lost employee badge", "lost access card"],
 "Report it immediately to security@company.example so the card can be blocked. A replacement card can be picked up at reception the next working day."),
])

sec("6. Personal Data, Salary and Payroll", [
("How do I update my personal data, address or emergency contact?",
 ["How do I report a change of address?", "update emergency contact", "change my name", "new phone number"],
 "Update your address, phone number, emergency contact and bank details yourself in the HR portal under \\emph{My Profile}. Changes made after the 15th of a month apply to payroll from the following month. For a name change, upload the official document (e.g. marriage certificate) in the same place."),
("When is my salary paid?",
 ["pay day"],
 "Salary is paid on the last working day of each month."),
("Where can I find my payslip?",
 ["Gehaltsabrechnung", "salary statement"],
 "Payslips are available in the HR portal under \\emph{Documents} by the 25th of each month."),
("I changed my tax class. What do I do?",
 ["Steuerklasse"],
 "Tax class changes are reported by the tax office electronically. Please also inform HR so they can check your next payslip."),
("Who do I contact about errors on my payslip?",
 ["wrong salary", "payroll question"],
 "Contact payroll at payroll@company.example within 4 weeks of receiving the payslip, and include your employee number and what you think is wrong."),
])

sec("7. Benefits", [
("Where can I find information about employee benefits?",
 ["benefits overview", "What benefits do I get?"],
 "All benefits are listed in the HR portal under \\emph{Benefits}, with instructions on how to apply. They include: 50\\% of the Deutschlandticket, bike leasing, a company pension with a 20\\% employer top-up, a training budget of EUR 1,000 per year, an employee assistance programme, and a referral bonus."),
("Is there support for public transport?",
 ["Deutschlandticket", "Jobticket"],
 "Yes. The company pays 50\\% of the Deutschlandticket. Apply in the HR portal under \\emph{Benefits}; the subsidy is paid with your next salary."),
("Can I lease a company bike?",
 ["JobRad", "bike leasing"],
 "Yes. Employees with a permanent contract can lease a bike through salary conversion after the probation period. Apply in the HR portal under \\emph{Benefits}."),
("Is there a company pension?",
 ["bAV", "retirement plan"],
 "Yes. The company adds 20\\% on top of your own contribution to the company pension scheme (bAV). You can join at any time in the HR portal under \\emph{Benefits}."),
("How do I sign up for health insurance?",
 ["health insurance benefits", "Krankenversicherung"],
 "In Germany you choose your own statutory health insurance (Krankenkasse) and give the details to HR on your first day. The company does not offer a separate health insurance plan. Changes of your insurance must be reported to HR in the HR portal under \\emph{My Profile}."),
("Is my family or are my dependents covered by health insurance?",
 ["health insurance for dependents", "Can my children be insured?", "family insurance"],
 "In Germany, your spouse and children can often be insured free of charge through your own statutory health insurance (Familienversicherung), if their own income is below the legal limit. Apply directly with your health insurance (Krankenkasse), not with the company. If you add dependents, please inform HR in the HR portal under \\emph{My Profile > Family}, because it can affect your tax and child allowances."),
("Is there a training budget?",
 ["courses", "certification", "Weiterbildung"],
 "Each employee has a training budget of EUR 1,000 per year for courses and certifications. Agree on the training with your manager, then submit the request in the HR portal under \\emph{Requests > Training} before booking."),
("Can I get a reward for referring a candidate?",
 ["referral bonus"],
 "Yes. If a candidate you referred is hired and passes probation, you receive a bonus of EUR 1,000 with the next salary."),
])

sec("8. Wellbeing and Support", [
("Is there support for mental health and wellbeing?",
 ["How do I access support for workplace wellbeing?", "stress support", "EAP", "counselling"],
 "Yes. All employees can use a free and confidential employee assistance programme (EAP) by phone or video, 24 hours a day, 7 days a week. Your employer is not informed when you use it. Details and the phone number are in the HR portal under \\emph{Wellbeing}. You can also talk to your manager or HR."),
("Where can I report discrimination or harassment?",
 ["Is there a process for reporting workplace harassment?", "complaint", "bullying"],
 "You can contact HR, the works council, or the confidential contact person at trust@company.example. All reports are treated confidentially, and you will not face disadvantages for reporting. HR confirms receipt within 3 working days and explains the next steps."),
("Is there a whistleblowing channel?",
 ["anonymous report"],
 "Yes. Reports can be made anonymously through the whistleblowing portal on the intranet."),
])

sec("9. Travel and Expenses", [
("Do business trips need approval?",
 ["business trip"],
 "Yes. Every business trip must be approved by your manager in advance in the HR portal under \\emph{Travel}."),
("Which train class may I book?",
 ["train ticket", "first class"],
 "2nd class; for journeys longer than 4 hours, 1st class."),
("How much do I get for using my private car?",
 ["mileage", "Kilometerpauschale"],
 "EUR 0.30 per kilometre."),
("Is there a meal allowance on business trips?",
 ["Verpflegungsmehraufwand", "per diem"],
 "Yes, according to the statutory rates: EUR 14 for trips of more than 8 hours away from home, EUR 28 for a full day."),
("How do I submit my travel expenses?",
 ["Reisekostenabrechnung", "expense claim"],
 "Submit the claim in the HR portal under \\emph{Travel > Expenses} with photos of all receipts within 4 weeks after the trip. Reimbursement follows with the next salary."),
])

sec("10. Parental Leave and Family", [
("How do I apply for parental leave (Elternzeit)?",
 ["parental leave steps", "Elternzeit beantragen"],
 "Steps: 1) Inform HR in writing at least 7 weeks before your planned start (for example, for a start on 1 September, by 14 July at the latest). 2) Send the request to hr@company.example or submit it in the HR portal under \\emph{Requests > Parental Leave}. 3) HR confirms receipt within 5 working days. You can take up to 3 years per child, split into up to 3 periods."),
("What must my parental leave request include?",
 ["What information do I need for parental leave?", "parental leave documents"],
 "Your written request must include: your name and employee number, the planned start and end date, the child's name and date of birth (or the expected due date), and whether you want to work part-time during the leave. A copy of the birth certificate can be submitted later."),
("Can I work part-time during parental leave?",
 ["Teilzeit in Elternzeit"],
 "Yes, up to 32 hours per week after agreement with your manager. Mention it in your parental leave request."),
("When does maternity protection start?",
 ["Mutterschutz", "I am pregnant"],
 "Maternity protection starts 6 weeks before the expected due date and normally ends 8 weeks after the birth. Please inform HR as soon as you know about the pregnancy so that your workplace can be checked for safety."),
])

sec("11. Development and Performance", [
("When are performance reviews held?",
 ["Where can I find information about annual performance reviews?", "appraisal"],
 "Once a year in Q1, plus a short check-in every 3 months with your manager. The form and guidelines are in the HR portal under \\emph{Performance}."),
("How do I apply for an internal position?",
 ["internal job"],
 "Internal jobs are published on the intranet. Inform your manager and apply directly in the HR portal."),
("Can working students get support for their thesis?",
 ["Bachelor thesis", "Master thesis"],
 "Yes. Thesis topics with a company connection are possible after agreement with your manager and HR."),
])

sec("12. IT and Data Protection", [
("How do I contact IT support?",
 ["IT problem", "laptop broken"],
 "Open a ticket in the ticket system or write to it-support@company.example. IT support is available Monday to Friday, 7:30 to 17:00."),
("How often must I change my password?",
 ["password"],
 "Every 180 days. Two-factor sign-in is mandatory."),
("May I install private software?",
 ["install software"],
 "No. Only software approved by IT may be installed."),
("What do I do if I receive a suspicious email?",
 ["phishing"],
 "Do not click any links or open attachments. Forward the email to security@company.example and delete it."),
])

sec("13. Leaving the Company", [
("What is the notice period?",
 ["How do I resign?", "Kündigungsfrist"],
 "After probation, the statutory notice period applies: 4 weeks to the 15th or the end of a month. A resignation must be in writing with a handwritten signature and handed to HR; email is not enough."),
("Do I get a reference letter?",
 ["Arbeitszeugnis"],
 "Yes. You receive a qualified reference letter (Arbeitszeugnis) with your last working day. You can request an interim reference at any time from HR."),
("What do I return when I leave?",
 ["offboarding"],
 "Laptop, headset, access card and any other company equipment, on your last working day."),
])

sec("14. Contacts and Questions Not Covered", [
("What should I do if the FAQ doesn't answer my question?",
 ["Who do I contact if my question isn't covered?", "I need more help"],
 "Contact HR at hr@company.example (Monday to Friday, 9:00 to 16:00). Describe your question and include your employee number. HR replies within 2 working days."),
("What if the agent cannot answer my question?",
 ["The assistant does not know", "I need a person"],
 "The HR Assistant only answers from this FAQ. For anything else, write to hr@company.example with your question and employee number. HR replies within 2 working days. Urgent personal matters: call HR directly, Monday to Friday, 9:00 to 16:00."),
("Who do I contact for payroll questions?", ["salary question", "Lohnbuero"], "Payroll: payroll@company.example, Monday to Thursday, 9:00 to 15:00. Payroll replies within 3 working days. Include your employee number."),
("How do I reach the works council?", ["Betriebsrat"], "Works council: workscouncil@company.example. Office hours every Tuesday 10:00 to 12:00 in room B.104. The works council replies within 5 working days, and all conversations are confidential."),
("Who is the confidential contact person?", ["Vertrauensperson", "someone confidential to talk to"], "The confidential contact person can be reached at trust@company.example. They reply within 3 working days, and reports are always treated confidentially."),
("How quickly do the different contacts respond?", ["response times", "How long until I get an answer?"], "HR (hr@company.example): 2 working days. Payroll (payroll@company.example): 3 working days. Works council (workscouncil@company.example): 5 working days. Confidential contact (trust@company.example): 3 working days. IT support (it-support@company.example): first response within 4 working hours. Security (security@company.example): urgent reports such as a lost access card or phishing are handled the same working day. Your manager: please agree directly with your manager."),
])

pre = r"""\documentclass[10pt,a4paper]{article}
\usepackage[a4paper,margin=1.8cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[scaled=0.92]{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{titlesec}
\usepackage{xcolor}
\input{glyphtounicode}\pdfgentounicode=1
\setlength{\parindent}{0pt}\setlength{\parskip}{3pt}\sloppy
\definecolor{accent}{RGB}{31,58,95}
\titleformat{\section}{\large\bfseries\color{accent}}{}{0pt}{}
\titlespacing*{\section}{0pt}{10pt}{3pt}
\begin{document}
{\LARGE\bfseries\color{accent} Employee HR FAQ}\\[3pt]
\textit{Fictional example document for an AI agent demo. All policies, numbers and contacts are made up. Version 5, November 2026.}
"""
out=[pre]; n=0
for t,items in S:
    out.append(r"\section{%s}"%t)
    for q,alts,a in items:
        n+=1
        line=r"\textbf{Q: %s}"%q
        if alts: line+=r"\\ {\small\color{gray} Also asked as: %s}"%"; ".join(alts)
        out.append(line+r"\\ A: %s\par\vspace{3pt}"%a)
out.append(r"\section{15. Overview: Contacts}")
out.append(r"\begin{tabular}{@{}p{4.2cm}p{5.6cm}p{6.4cm}@{}}\textbf{Contact}&\textbf{Email}&\textbf{Availability / response time}\\ \hline HR&hr@company.example&Mon--Fri 9:00--16:00, reply within 2 working days\\ Payroll&payroll@company.example&Mon--Thu 9:00--15:00, reply within 3 working days\\ IT support&it-support@company.example&Mon--Fri 7:30--17:00, first response within 4 working hours\\ Security&security@company.example&Urgent reports handled the same working day\\ Works council&workscouncil@company.example&Tue 10:00--12:00 (room B.104), reply within 5 working days\\ Confidential contact&trust@company.example&Reply within 3 working days, confidential\\ Employee assistance (EAP)&see HR portal > Wellbeing&24/7, free and confidential\\ \end{tabular}")
out.append(r"\section{16. Overview: HR Portal Paths}")
out.append(r"\begin{tabular}{@{}p{6.5cm}p{9.7cm}@{}}\textbf{Task}&\textbf{Where in the HR portal}\\ \hline Request vacation, half-day or special leave&Absences > New Request / Special Leave\\ Report sick leave&Absences > Sick Leave\\ See remaining vacation days&Absences\\ Record working time&Time Tracking\\ Change address, bank details, emergency contact, family&My Profile\\ Upload documents&My Profile > Documents\\ Payslips&Documents\\ Working time change, flexible schedule, part-time&Requests > Working Time\\ Parental leave&Requests > Parental Leave\\ Training&Requests > Training\\ Working from abroad, unpaid leave&Requests\\ Business trips and expenses&Travel / Travel > Expenses\\ Benefits (Deutschlandticket, bike, pension)&Benefits\\ Wellbeing and EAP&Wellbeing\\ Performance review forms&Performance\\ \end{tabular}")
out.append(r"\end{document}")
open("/home/claude/agent_demo/Employee_HR_FAQ.tex","w").write("\n".join(out))
print("questions:",n)
