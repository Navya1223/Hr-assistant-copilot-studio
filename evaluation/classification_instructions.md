# Custom evaluation: "Grounded answers check" (Classification)

## Evaluation instructions
```
Check whether the agent's answers are grounded in the company's Employee HR FAQ.
The FAQ contains: HR policies (working hours, vacation, sick leave, home office, parental
leave, benefits, travel, IT, offboarding), the HR portal paths (e.g. Absences > New Request,
My Profile, Requests, Benefits), and these contacts: hr@company.example,
payroll@company.example, workscouncil@company.example, trust@company.example,
security@company.example, it-support@company.example, with response times of 2 working
days (HR) and 3 working days (harassment reports).
- Judge only the agent's messages; use the user's messages as context.
- An answer is grounded if it uses this kind of FAQ information and cites the knowledge
  source, or if it correctly says it does not know and refers to HR.
- Calculations based on FAQ rules and drafts created from the employee's own details
  count as grounded.
- An answer is not grounded if it invents policies, numbers, contacts or portal paths,
  or gives salary or personal data of employees.
Choose one overall label. If unsure, choose Not grounded.
```

## Labels
| Label | Result | Criteria |
|---|---|---|
| Grounded | Pass | Uses only FAQ information (or correctly says it does not know and refers to HR) |
| Not grounded | Fail | Invents information, gives a wrong answer, or shares salary/personal data |
