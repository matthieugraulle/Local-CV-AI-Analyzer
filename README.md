# 🤖 Local CV AI-Analyzer (Ollama + Llama 3)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-Llama3-orange.svg)](https://ollama.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 Description
Ce projet est un outil d'analyse de CV automatisé conçu pour fonctionner **100% localement**. En utilisant **Llama 3** via **Ollama**, il permet d'extraire des informations stratégiques d'un CV (PDF) sans envoyer de données personnelles sur le cloud. 

Initialement conçu pour un profil **DevOps / Cloud Engineer**, cet outil aide à optimiser le positionnement de carrière, préparer des entretiens et améliorer le référencement ATS.

## ✨ Fonctionnalités
* **Extraction PDF Directe** : Lecture robuste via `pypdf`.
* **Analyse de Profil** : Résumé automatique et identification des compétences clés.
* **Simulateur d'Entretien** : Génération de questions techniques ciblées (Lead DevOps / Expert IA).
* **Optimisation ATS** : Suggestions de mots-clés et d'améliorations structurelles.
* **Confidentialité Totale** : Aucune donnée ne quitte votre machine.

## 🛠️ Stack Technique
* **LLM** : Llama 3 (8B) via Ollama.
* **Langage** : Python 3.10.
* **Bibliothèques** : `ollama` (Python SDK), `pypdf`.

## 🚀 Installation & Utilisation

### 1. Prérequis
* Installer [Ollama](https://ollama.com/)
* Télécharger Llama 3 : `ollama run llama3`

### 2. Installation du projet
```bash
# Cloner le repo
git clone [https://github.com/TON_USER/IA-CV-Analyzer.git](https://github.com/TON_USER/IA-CV-Analyzer.git)
cd IA-CV-Analyzer

# Installer les dépendances
pip install ollama pypdf
