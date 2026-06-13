# JSON Python Quiz System

An object-oriented, console-based quiz management system built in Python utilizing stateless JSON serialization engines for managing user profiles, modular questionnaires, and historical student metrics.

![Language](https://img.shields.io/badge/Language-Python%203.8+-blue?logo=python&logoColor=white)
![Storage Engine](https://img.shields.io/badge/Storage-JSON%20Flat%20Files-orange?logo=json&logoColor=white)
![Design Pattern](https://img.shields.io/badge/Pattern-Object--Oriented%20%28OOP%29-green)
![Interface](https://img.shields.io/badge/Interface-Console%20Terminal-lightgrey)

---

## 🌐 Engine Overview

The JSON Python Quiz System features a terminal-driven workspace for both students and instructors. By decoupling transactional file storage states (`users.json`, `questions.json`, `performance.json`) from runtime validation threads, the platform allows role-based system access, random sampling across question banks, and dynamic analytics tracking without memory exhaustion patterns.

---

## 📍 Quick Navigation

* [🌐 Project Overview](#-engine-overview)
* [💻 Languages & Technologies Used](#%EF%B8%8F-tech-stack)
* [📁 Repository Structure and Module Index](#-repository-structure-and-module-index)
* [🧱 Document Structure (`P2 Project.py`)](#-repository-structure-and-module-index)
* [⚙️ Application Logic (`performance.json`)](#-architectural-highlights)

---

## 📦 System Architecture

<div align="center">

```text
┌───────────────────────────────────────────────────────────────┐
│                    TERMINAL INTERACTION LAYER                 │
├───────────────────────────────────────────────────────────────┤
│              Student Menus / Instructor Portals               │
│               (Quiz Selection, Performance Views)             │
└──────────────────────────────┬────────────────────────────────┘
                               ↓
┌───────────────────────────────────────────────────────────────┐
│                APPLICATION DATA INTERFACE ENGINE              │
├────────────┬─────────────┬────────────┬─────────────┬─────────┤
│ Student    │ Instructor  │ QuizSystem │ Randomizer  │ File IO │
│ Execution  │ Validation  │ Core State │ Question    │ JSON    │
│ Context    │ Nodes       │ Router     │ Sampler     │ Parsers │
└────────────┴─────────────┴────────────┴─────────────┴─────────┘
                               ↓
┌───────────────────────────────────────────────────────────────┐
│                    STATELESS DATA PERSISTENCE                 │
├───────────────────────────────────────────────────────────────┤
│      users.json  │  questions.json  │  performance.json       │
└───────────────────────────────────────────────────────────────┘

```

| Architectural Layer | Core Components & Strategies | Quick Links / Reference |
| --- | --- | --- |
| **Top: Presentation** | Terminal navigation structures and option validation wrappers | [Setup & Execution Guide](https://www.google.com/search?q=%23-setup--execution-guide) |
| **Middle: System Engine** | Object-oriented model routing, random shuffling filters, and entity states | [Repository Structure](https://www.google.com/search?q=%23-repository-structure-and-module-index) |
| **Bottom: Persistence** | Flattened key-value tables writing system arrays back to static files | [Application Core Interfaces](https://www.google.com/search?q=%23-application-core-interfaces) |

---

## ✨ Key Architecture Features

✅ **Role-Based Execution Environments** - Segregates operational boundaries strictly between Student evaluation contexts and Instructor analytics boards.

✅ **Robust JSON Data Pipelines** - Implements defensive file ingestion handlers that verify document paths and inject boilerplate fallback templates if target assets are missing.

✅ **Stochastic Sample Generators** - Employs pseudo-random runtime distribution bounds to pick unique subsets of target questions, mitigating repetitive pattern matching.

✅ **Hierarchical Performance Schemas** - Maps user evaluation scoring metrics inside a structured, multi-tier JSON tree index sorted by `Subject -> Difficulty -> User`.

---

## 📁 Repository Structure and Module Index

The workspace organizes runtime code dependencies cleanly alongside operational flat-file databases:

### 🐍 Production Python App Engines

* **`P2 Project.py`** - Primary system runtime containing foundational class structures (`Student`, `Instructor`, `QuizSystem`), structural file persistence systems, and target terminal loop listeners.
* **`ramdom class...attribues.py`** - Technical playground document mapping core Object-Oriented patterns including base class inheritance trees, method overriding, private variables ($\text{\_\_variable}$), and lambda filters.

### 🗃️ Flat-File Storage Matrix

* **`performance.json`** - System transaction ledger logging student validation outcomes across explicit subject difficulty bins.
* **`users.json`** *(Auto-generated)* - Credential directory securing profile roles and system access tokens.
* **`questions.json`** *(Auto-generated)* - Standard question repository structuralizing option lists, answers, and error-hint trackers.

---

## 🛠️ Tech Stack

| Component | Technology | Quick Links |
| --- | --- | --- |
| **Core Ecosystem** | Python 3.8+ Standard Implementation Runtime | [python.org](https://www.python.org/) |
| **Data Serialization** | Native JSON Encoding & Decoding Library Subsystems | [docs.python.org/3/library/json](https://docs.python.org/3/library/json.html) |
| **Stochastic Engine** | Python Pseudo-Random Array Transformation Utilities | [docs.python.org/3/library/random](https://www.google.com/search?q=https://docs.python.org/3/library/random.html) |
| **File Architecture** | Native OS Virtual Path Interaction Drivers | [docs.python.org/3/library/os](https://docs.python.org/3/library/os.html) |

---

## 💻 System Requirements

Ensure your local execution device confirms to these baseline configurations:

* **Interpreter Version:** Python 3.8 or higher installed over the target runtime terminal.
* **Disk Constraints:** Read/Write privileges enabled inside the running execution directory to allow state synchronization.
* **Interface Driver:** Standard Interactive Console Shell supporting basic text input processing.

---

## 🚀 Setup & Execution Guide

### Step 1: Clone the Quiz Workspace Environment

Pull down the repository workspace directly to your local computer platform:

```bash
git clone [https://github.com/MoNsT3R-code/json-python-quiz.git](https://github.com/MoNsT3R-code/json-python-quiz.git)
cd json-python-quiz

```

### Step 2: Initialize and Run the System

Launch the application directly through your console terminal framework. The application engine manages file generation tracks seamlessly without manual parameter intervention:

```bash
python3 "P2 Project.py"

```

### Step 3: Interacting via the Terminal Interface

1. **Register Profile Roles:** Choose **`R`** to spin up a new security record profile, and flag it as a Student (**`S`**) or Instructor (**`I`**).
2. **Access Execution Contexts:** Choose **`L`** to authenticate credentials.
3. **Run Evaluations:** Students can fire up evaluation arrays via **`Q`**, step through questions sequentially using **`N`**, or finalize performance states using **`S`**.

---

## 📊 Application Core Interfaces

Data processing updates synchronize across these explicit structural files:

| File Context Target | Storage Blueprint Profile | Functional Dependency | Data Schema Example |
| --- | --- | --- | --- |
| **`users.json`** | Directory Map Dictionary | Authenticates credentials and logs runtime profile access layers. | `{"Musfira": {"password": "123", "role": "student"}}` |
| **`questions.json`** | Hierarchical Array Map | Structural quiz templates managing choice items and hints. | `{"maths": {"low": [{"question": "2+2", "answer": "4"}]}}` |
| **`performance.json`** | Nested Statistical Tree | Logs historical student milestones for instructor analysis. | `{"maths": {"low": {"Ali": 4}}}` |

---

## 🏗️ Architectural Highlights

### 🎯 Sample Sizing Constraints

The evaluation module limits memory footprints by analyzing active sample ceilings against maximum array counts, using safe sampling boundaries to prevent indexing breakdowns:

$$\text{Active Question Sample Sizing} = \min(k, \mathcal{N}_{\text{available}})$$

### 🔐 Enforced Access Separation

Methods and profile workflows run completely decoupled from one another. Student evaluation contexts only access localized score submission pipes, while analytical metrics indices are restricted entirely behind Instructor authentication keys.

---

## 📄 License & Terms

This project is open-source. Feel free to copy, modify, and redistribute the quiz systems modules and object-oriented scripts as required.
