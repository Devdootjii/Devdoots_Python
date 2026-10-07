# 🚀 DevDoots Python Sprint — Production Learning Repository

> **Official Python Development & Software Engineering Repository for Team DevDoots.**  
> Focused on real-world business logic, modular programming, enterprise Git workflows, and zero-compromise code discipline.

---

## 📌 Repository Overview & Structure

Is repository ka structure ek enterprise micro-services workspace ki tarah design kiya gaya hai, jahan har developer ka apna isolated workspace folder hai taaki koi merge conflicts na hon:

```text
Devdoots_Python/
│
├── Members/                      # Individual Developer Workspaces (Golden Rule)
│   ├── Aryan/                    # Aryan's daily tasks
│   ├── Balram/                   # Balram's daily tasks
│   ├── Divyansh/                 # Divyansh's daily tasks
│   ├── Harsh/                    # Harsh's daily tasks
│   ├── Khushi/                   # Khushi's daily tasks
│   └── Ritesh/                   # Ritesh's daily tasks
│
├── Tasks/                        # Official Daily Sprint Problem Statements
├── Assignments/                  # Peer Reviews & Extended Practice Code
├── Screenshots/                  # Proof of Work (PoW) Terminal Outputs
├── Docs/                         # Engineering Guidelines & Workflow Rules
├── .gitignore                    # Python cache & virtualenv protection
└── README.md                     # Central Documentation Engine


👥 Team Roles & Responsibilities
Confusion aur dependency khatam karne ke liye team me clear role division hai:
Member                       Engineering Role                    Core Responsibilities
Divyansh Kumar               TPM(Lead Architect)                 Daily task roadmap, architecture review, PR audits, and main branch merges.

Harsh                        Discipline & Compliance Head        Daily 8:45 PM submission tracking, Git rule compliance, attendance, and penalty enforcement.
Balram Singh                 Content & Task Lead                 Sprint task documentation, problem statement design, test datasets, and README templates.
Ritesh, Aryan, Khushi        Core Software Developers            Clean code implementation, feature branch workflow, peer code reviews, and PoW logging.

⚙️ Official DevDoots Git Workflow & 8 Golden Rules
Production standard maintain karne ke liye ye 8 niyam strictly enforced hain:

1. Direct Push Strictly Forbidden: main branch hamesha clean aur protected rahegi. Kabhi bhi main par seedha commit/push nahi hoga.

2. Branch Naming Standard: Har task ke liye format: user/<yourname>-pytask<number> (Example: user/ritesh-pytask05).

3.  Workspace Isolation (Golden Rule): Koi common file edit nahi hogi. Har member sirf Members/<YourName>/ me apne naam ki file banayega.

4. Structured Commit Messages: Format: [PY-XX] <name> <detailed description> (Generic messages jaise "done" ya "update" prohibited hain).

5. PR Checklist Verification: TPM merge tabhi karega jab code run ho raha ho, naming conventions sahi hon, aur header log bhara ho.

6. Discord Standup Mandatory: Roz raat 9:00 PM standup me 5-minute technical explanation dena compulsory hai.

7. Task Sizing Principle: Har task 45 se 60 minute ke focus block me khatam hone layak structured hai.

8. Penalty Protocol: Bina valid reason ke late submit karne ya rules todne par Discipline Head dwara 1 Strike lagaya jata hai (3 Strikes = explain duty + 1-on-1 review).

## 🧠 SPRINT CURRICULUM: DAY 01 TO DAY 05 & REAL-WORLD IMPACT

| Day / Task | Technical Concepts Covered | Core Problem Solved | Real-World & Industry Application |
| :--- | :--- | :--- | :--- |
| **Day 01 (PY-01)** | • Control Flow (`if-elif-else`)<br>• Typecasting (`float()`)<br>• Logical Operators (`and`, `or`)<br>• f-string Formatting | **Smart E-Commerce Billing & Tax System** | **Dynamic Checkout Engines (e.g. Amazon / Zomato):** Real-world cart checkout me dynamic slab discounts (20%, 10%), membership perks (VIP), student verification, aur statutory GST tax calculation. |
| **Day 02 (PY-02)** | • Loops (`while True`)<br>• Flow Control (`break`, `continue`)<br>• Accumulator Pattern<br>• Zero-Division Handling | **Daily Sales & Transaction Log Processor** | **FinTech & ATM Core Banking Software:** Live streaming entries process karna, malicious/fraud transactions (₹10L+) par auto system lockdown, invalid inputs skip karna, aur safe daily revenue analytics generate karna. |
| **Day 03 (PY-03)** | • Tuples (Immutability)<br>• Lists (Mutability)<br>• Methods (`.append()`, `.remove()`, `.sort()`)<br>• Slicing (`[::-1]`, `[-3:]`)<br>• Aggregations | **Smart Inventory & Price Audit Manager** | **Warehouse & Supply Chain Systems:** Store metadata ko tamper-proof (Tuple) rakhna, dynamic inventory stocking, out-of-stock items drop karna, aur automated Top-3 premium vs budget catalog slicing. |
| **Day 04 (PY-04)** | • Dictionaries (`dict`)<br>• Key-Value Hash Lookups<br>• Safe Retrieval (`.get()`)<br>• Sets (`set`) Deduplication<br>• Aggregations | **Customer Loyalty & Unique Category Audit** | **CRM & Customer Reward Engines (Starbucks / CRED):** Key-Value mapping ke zariye instant customer point lookups, missing key crashes se bachna (`.get()`), aur raw category tags me se duplicate tags ko clean karna. |
| **Day 05 (PY-05)** | • Functions (`def`)<br>• Parameters & Positional Arguments<br>• Return Values (`return`)<br>• Scoping (Local vs Global)<br>• DRY Principle | **Modular E-Commerce Order Billing Engine** | **Microservice Payment Pipelines (Razorpay / Stripe):** Monolithic code ko decoupled functions me todna. Billing function se nikla amount logistics function me chain hokar free vs standard delivery decide karta hai. |

💻 Standard Git Execution Workflow
Roz ka submission cycle terminal me in steps par execute hota hai:
# Step 1: Upstream sync
git checkout main
git pull origin main

# Step 2: Create isolated feature branch
git checkout -b user/<yourname>-pytask<number>

# Step 3: Stage only your files
git add Members/<yourname>/<yourname>_task<number>.py

# Step 4: Enterprise commit message
git commit -m "[PY-XX] <yourname> completed <task description>"

# Step 5: Push to remote
git push -u origin user/<yourname>-pytask<number>
