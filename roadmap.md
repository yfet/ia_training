# 🗺️ Roadmap — De Développeur Web Senior à Freelance AI / ML Engineer

> Durée estimée : **8 à 9 mois** — profil avancé
> Dernière mise à jour : Mai 2026 — Version 2.0

---

## 📊 Tableau de suivi — Fil d'Ariane

> Mettre à jour à chaque session terminée.
> Légende : ✅ Terminé   🔄 En cours   ⬜ À faire   ⏸ En pause

### 🟢 Phase 1 — Fondations ML (5 semaines)

#### Semaine 1 — Python pour développeur

| Statut | Jour        | Sujet                                              | Date       |
|:------:|-------------|----------------------------------------------------|------------|
|   ✅   | Jour 1      | Types, listes, dicts, fonctions, classes           | 2026-05-04 |
|   ✅   | Jour 2      | Modules, pip, environnements virtuels              | 2026-05-04 |
|   ⬜   | Jour 3      | Fichiers CSV, JSON                                 | —          |
|   ⬜   | Jour 4      | List comprehensions, lambdas, gestion erreurs      | —          |
|   ⬜   | Jour 5      | NumPy — tableaux et opérations vectorielles        | —          |
|   ⬜   | Application | Mini-projet : script stats sur CSV                 | —          |

**Notes** : _______________________________________________

#### Semaine 2 — Pandas & Exploration de données

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | DataFrame, Series, read_csv, head/info             | —    |
|   ⬜   | Jour 2      | Filtres, colonnes, valeurs manquantes              | —    |
|   ⬜   | Jour 3      | Groupby, agrégations, pivot tables                 | —    |
|   ⬜   | Jour 4      | Visualisation Matplotlib                           | —    |
|   ⬜   | Jour 5      | Nettoyage de données réelles                       | —    |
|   ⬜   | Application | Projet : EDA dataset e-commerce                    | —    |

**Notes** : _______________________________________________

#### Semaine 3 — scikit-learn : Classification

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | ML supervisé, features, labels, train/test         | —    |
|   ⬜   | Jour 2      | Régression logistique                              | —    |
|   ⬜   | Jour 3      | Random Forest                                      | —    |
|   ⬜   | Jour 4      | Métriques : accuracy, precision, recall, F1        | —    |
|   ⬜   | Jour 5      | Cross-validation, overfitting                      | —    |
|   ⬜   | Application | Projet : Prédiction de churn client                | —    |

**Notes** : _______________________________________________

#### Semaine 4 — scikit-learn : Régression & Pipelines

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Régression linéaire, Ridge, Lasso                  | —    |
|   ⬜   | Jour 2      | Métriques régression : MAE, MSE, R²                | —    |
|   ⬜   | Jour 3      | Feature engineering, encodage, normalisation       | —    |
|   ⬜   | Jour 4      | Pipeline scikit-learn                              | —    |
|   ⬜   | Jour 5      | Sauvegarder / charger un modèle (joblib)           | —    |
|   ⬜   | Application | Projet : Prédiction prix immobilier                | —    |

**Notes** : _______________________________________________

#### Semaine 5 — Hugging Face Hub & Consolidation

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Découverte du Hub, modèles, datasets, Spaces       | —    |
|   ⬜   | Jour 2      | Hugging Face Inference API (requête HTTP)          | —    |
|   ⬜   | Jour 3      | Choisir le bon modèle HF pour un cas business      | —    |
|   ⬜   | Jour 4      | Documenter un projet ML (README pro)               | —    |
|   ⬜   | Jour 5      | Push GitHub des 2 projets Phase 1                  | —    |
|   ⬜   | Application | Finalisation portfolio Phase 1                     | —    |

**Notes** : _______________________________________________

✅ **PHASE 1 TERMINÉE le** : ____________

---

### 🟡 Phase 2 — ML Engineering / Production (3 semaines)

#### Semaine 6 — De Jupyter à un projet structuré

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Structure projet ML (src/, data/, models/...)      | —    |
|   ⬜   | Jour 2      | Refactoring notebook churn en scripts Python       | —    |
|   ⬜   | Jour 3      | Tests unitaires basiques (pytest)                  | —    |
|   ⬜   | Jour 4      | MLflow : logger métriques, comparer runs           | —    |
|   ⬜   | Jour 5      | MLflow Model Registry                              | —    |
|   ⬜   | Application | Package Python propre (projet churn)               | —    |

**Notes** : _______________________________________________

#### Semaine 7 — API ML avec FastAPI

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | FastAPI, endpoint /predict                         | —    |
|   ⬜   | Jour 2      | Validation inputs avec Pydantic                    | —    |
|   ⬜   | Jour 3      | Charger le modèle au démarrage, gestion erreurs    | —    |
|   ⬜   | Jour 4      | Dockeriser l'API ML                                | —    |
|   ⬜   | Jour 5      | Tests API avec curl et Postman                     | —    |
|   ⬜   | Application | Projet : API de scoring de leads                   | —    |

**Notes** : _______________________________________________

#### Semaine 8 — Déploiement & Monitoring

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Déploiement Railway                                | —    |
|   ⬜   | Jour 2      | Variables d'env, secrets, health checks            | —    |
|   ⬜   | Jour 3      | Logging des prédictions en base                    | —    |
|   ⬜   | Jour 4      | Monitoring basique, data drift (concept)           | —    |
|   ⬜   | Jour 5      | Documentation API Swagger                          | —    |
|   ⬜   | Application | API + frontend Next.js consommant l'API            | —    |

**Notes** : _______________________________________________

✅ **PHASE 2 TERMINÉE le** : ____________

---

### 🔵 Phase 3 — Deep Learning Essentiel (3 semaines) — Google Colab

#### Semaine 9 — Concepts réseaux de neurones

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Neurone, perceptron, activation functions          | —    |
|   ⬜   | Jour 2      | Architecture réseau dense                          | —    |
|   ⬜   | Jour 3      | Backpropagation (comprendre le concept)            | —    |
|   ⬜   | Jour 4      | PyTorch sur Colab — tenseurs, premier réseau       | —    |
|   ⬜   | Jour 5      | Training loop : loss, optimizer                    | —    |
|   ⬜   | Application | Réseau de prédiction simple (tabular)              | —    |

**Notes** : _______________________________________________

#### Semaine 10 — Hugging Face Transformers

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Architecture Transformer (concept, sans maths)     | —    |
|   ⬜   | Jour 2      | HF pipeline() — modèle en 3 lignes                 | —    |
|   ⬜   | Jour 3      | Classification de texte avec modèle pré-entraîné   | —    |
|   ⬜   | Jour 4      | Embeddings texte — concept et usage pratique       | —    |
|   ⬜   | Jour 5      | Comparer plusieurs modèles HF                      | —    |
|   ⬜   | Application | Projet : Classifier avis clients avec HF           | —    |

**Notes** : _______________________________________________

#### Semaine 11 — DL vs ML + Consolidation

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Tableau de décision DL vs ML classique             | —    |
|   ⬜   | Jour 2      | Présenter le choix à un client non-technique       | —    |
|   ⬜   | Jour 3      | Révision Phases 1, 2, 3                            | —    |
|   ⬜   | Jour 4      | Nettoyage et documentation GitHub                  | —    |
|   ⬜   | Jour 5      | Préparation Phase 4 (LLM, RAG, embeddings)         | —    |
|   ⬜   | Application | Push final tous les projets Phases 1–3             | —    |

**Notes** : _______________________________________________

✅ **PHASE 3 TERMINÉE le** : ____________

---

### 🟣 Phase 4 — LLM & AI Engineering — Zone payante (8 semaines)

#### Semaine 12 — Fondations LLM

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Fonctionnement LLM, tokenisation, température      | —    |
|   ⬜   | Jour 2      | Appeler APIs OpenAI et Mistral en Python           | —    |
|   ⬜   | Jour 3      | Prompt engineering (rôles, instructions, CoT)      | —    |
|   ⬜   | Jour 4      | Prompt avancé : few-shot, JSON output              | —    |
|   ⬜   | Jour 5      | Comparer GPT-4o vs Mistral vs Claude               | —    |
|   ⬜   | Application | Assistant de rédaction avec historique de conv.    | —    |

**Notes** : _______________________________________________

#### Semaine 13 — Embeddings & Bases vectorielles

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Concept d'embedding (texte → vecteur)              | —    |
|   ⬜   | Jour 2      | Embeddings API OpenAI (text-embedding-3-small)     | —    |
|   ⬜   | Jour 3      | ChromaDB : collection, ajout documents             | —    |
|   ⬜   | Jour 4      | Similarity search — comment ça fonctionne          | —    |
|   ⬜   | Jour 5      | ChromaDB vs Qdrant                                 | —    |
|   ⬜   | Application | Projet : moteur de recherche sémantique            | —    |

**Notes** : _______________________________________________

#### Semaine 14 — RAG Partie 1

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Architecture RAG (indexation, retrieval, gen.)     | —    |
|   ⬜   | Jour 2      | Chunking de documents (stratégies)                 | —    |
|   ⬜   | Jour 3      | Pipeline RAG basique avec LlamaIndex               | —    |
|   ⬜   | Jour 4      | Améliorer le retrieval (reranking, filtres)        | —    |
|   ⬜   | Jour 5      | Évaluer un RAG — métriques de pertinence           | —    |
|   ⬜   | Application | RAG sur un PDF métier                              | —    |

**Notes** : _______________________________________________

#### Semaine 15 — RAG Partie 2

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | RAG multi-documents                                | —    |
|   ⬜   | Jour 2      | Citations et sourcing des réponses                 | —    |
|   ⬜   | Jour 3      | Mémoire conversationnelle dans un RAG              | —    |
|   ⬜   | Jour 4      | Sécurité données, filtrage par utilisateur         | —    |
|   ⬜   | Jour 5      | Déployer le RAG comme API FastAPI                  | —    |
|   ⬜   | Application | Projet : Chatbot RAG documentation PME fictive     | —    |

**Notes** : _______________________________________________

#### Semaine 16 — Interface Next.js + Agents IA

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Vercel AI SDK, useChat, streaming réponses         | —    |
|   ⬜   | Jour 2      | Interface chatbot avec Next.js App Router          | —    |
|   ⬜   | Jour 3      | Connecter interface → backend RAG FastAPI          | —    |
|   ⬜   | Jour 4      | Agents IA simples — concept et tools               | —    |
|   ⬜   | Jour 5      | Agent avec outils (web search, fichier, calcul)    | —    |
|   ⬜   | Application | ⭐ PROJET CLÉ : Chatbot RAG complet Next.js         | —    |

**Notes** : _______________________________________________

#### Semaine 17 — Fine-tuning basique

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | Fine-tuning vs prompt engineering, quand l'utiliser| —    |
|   ⬜   | Jour 2      | Préparer un dataset JSONL (format OpenAI)          | —    |
|   ⬜   | Jour 3      | Lancer et monitorer un fine-tuning job OpenAI      | —    |
|   ⬜   | Jour 4      | Tester modèle fine-tuné vs modèle de base          | —    |
|   ⬜   | Jour 5      | Cas d'usage vendables du fine-tuning               | —    |
|   ⬜   | Application | Fine-tuning sur dataset classification emails      | —    |

**Notes** : _______________________________________________

#### Semaine 18 — n8n + Automatisation IA

| Statut | Jour        | Sujet                                              | Date |
|:------:|-------------|----------------------------------------------------|------|
|   ⬜   | Jour 1      | n8n en local (Docker) — workflow basique           | —    |
|   ⬜   | Jour 2      | Intégrer un LLM dans un workflow n8n               | —    |
|   ⬜   | Jour 3      | Webhook → IA → réponse automatique                 | —    |
|   ⬜   | Jour 4      | Automatisation #1 : résumé automatique PDF         | —    |
|   ⬜   | Jour 5      | Automatisation #2 : qualification de leads         | —    |
|   ⬜   | Application | Démo n8n packagée pour client                      | —    |

**Notes** : _______________________________________________

#### Semaine 19 — Semaine tampon / rattrapage Phase 4

| Statut | Tâches à rattraper / approfondir                              | Date |
|:------:|---------------------------------------------------------------|------|
|   ⬜   | _______________________________________________               | —    |

**Notes** : _______________________________________________

✅ **PHASE 4 TERMINÉE le** : ____________

---

### 🔴 Phase 5 — Freelance IA Ready (6 semaines)

| Statut | Semaine     | Objectif de la semaine                              | Date |
|:------:|-------------|-----------------------------------------------------|------|
|   ⬜   | Semaine 20  | 4 fiches offres IA (chatbot, doc, scoring, n8n)     | —    |
|   ⬜   | Semaine 21  | Démo live chatbot RAG + pitch 5 min                 | —    |
|   ⬜   | Semaine 22  | Template devis IA + CGV basiques                    | —    |
|   ⬜   | Semaine 23  | Malt + LinkedIn + Tefy Labs optimisés               | —    |
|   ⬜   | Semaine 24  | Simulateur de coûts projet IA                       | —    |
|   ⬜   | Semaine 25  | 10 contacts, 1 conversation engagée minimum         | —    |

**Client/POC en cours** : _________________________________

**Notes** : _______________________________________________

✅ **PHASE 5 TERMINÉE le** : ____________

---

### ⚫ Phase 6 — Scaling & Positionnement (4 semaines)

| Statut | Semaine     | Objectif de la semaine                              | Date |
|:------:|-------------|-----------------------------------------------------|------|
|   ⬜   | Semaine 26  | Templates et automatisation interne                 | —    |
|   ⬜   | Semaine 27  | Cloud ML basique (AWS Bedrock ou GCP Vertex)        | —    |
|   ⬜   | Semaine 28  | Open source vs APIs payantes                        | —    |
|   ⬜   | Semaine 29  | Connexion Tefy Labs + limites légales               | —    |

**Notes** : _______________________________________________

✅ **PHASE 6 TERMINÉE le** : ____________

---

🏁 **ROADMAP COMPLÈTE TERMINÉE le** : ____________

- Premier client IA signé le    : ____________
- Revenu IA first month         : ____________
- Objectif mois 6 atteint (Y/N) : ____________

---
---

# 📘 Plan global de formation — Version 2 (révisée)

## 🎯 Objectif final

Devenir **Freelance AI / ML Engineer orienté business**, capable de :
- Concevoir des solutions IA utiles aux PME
- Construire, déployer et maintenir des modèles ML, des API IA, des chatbots métier (RAG, assistants)
- Vendre des projets IA concrets, pas de la théorie
- Alimenter les produits SaaS Tefy Labs (Beauplume, futurs produits)

## 🧑‍💻 Profil de départ

- Développeur web senior freelance, Madagascar
- Stack : React / Next.js, Node.js, C# / ASP.NET Core, Docker, Railway, Git
- Déjà en contact avec les APIs IA (Semantic Kernel, OpenAI via Beauplume)
- Notions Docker, déploiement VPS/Hetzner, PostgreSQL
- Temps disponible : **8 h / semaine** (1h/jour lundi–vendredi + 3h week-end)
- Matériel : Topton M600 (Ryzen 9 6900HX, GPU intégré — pas adapté aux modèles locaux lourds)

## 🧠 Philosophie pédagogique

- ✅ Apprentissage orienté business réel
- ✅ Peu de maths, beaucoup de compréhension
- ✅ Chaque notion = un projet
- ✅ Chaque projet = vendable
- ✅ Guide technique actif : Claude fournit les données, fichiers, instructions et code à chaque étape
- ❌ Pas d'apprentissage académique inutile
- ❌ Pas de GPU local requis — tout fonctionne via APIs et Google Colab

## ⚠️ Note importante : GPU local vs API

Hugging Face désigne deux choses différentes :
1. **Le Hub** (huggingface.co) — dépôt de modèles en ligne, accessible via navigateur. Aucun prérequis matériel.
2. **Les modèles téléchargeables** — tournent en local, nécessitent GPU VRAM 8–24 GB. **NON adapté à ton setup actuel.**

Solution retenue dans cette roadmap :
- **Phases 1–2** : scikit-learn tourne parfaitement en local (CPU suffit)
- **Phase 3** : Google Colab (GPU gratuit de Google) pour PyTorch
- **Phase 4–5** : APIs payantes (OpenAI, Mistral, Anthropic) + Hugging Face Inference API (gratuit avec quota)
- **Phase 6** : Si client exige modèle open-source → louer GPU à la demande (RunPod, Vast.ai, Hetzner GPU)

## ⏱️ Organisation hebdomadaire type

- **Jour 1 – Jour 5 (1h/jour)** : Concept + code guidé (fourni par Claude)
- **Application (3h)** : Construction du projet de la semaine

→ **Résultat** : un livrable concret toutes les 1–2 semaines.

À chaque étape, Claude fournit :
- Le dataset ou fichier de travail
- Le code de départ (starter code)
- Les instructions pas à pas
- Les critères de validation ("tu es prêt à passer à la suite si…")

---

## 🗺️ Détail des phases

### 🟢 Phase 1 — Fondations Machine Learning (5 semaines)

> Durée réduite : 8 sem → 5 sem (Git, API REST, Docker, logique de données déjà maîtrisés)

**🎯 Objectif** : comprendre le ML utile aux entreprises et entraîner un premier modèle fiable.

**Compétences visées**
- Penser un problème en termes de données et de prédiction
- Manipuler des données réelles avec Pandas
- Entraîner, évaluer et interpréter un modèle ML
- Expliquer le résultat à un client non technique

**Technologies**
- Python, NumPy, Pandas, scikit-learn, Jupyter
- Hugging Face Hub (exploration uniquement)
- Git / GitHub — portfolio public dès le premier projet

**Détail semaine par semaine**

#### Semaine 1 — Python pour développeur
- Jour 1 : Types, listes, dictionnaires, fonctions, classes basiques
- Jour 2 : Modules, pip, environnements virtuels (venv)
- Jour 3 : Fichiers CSV, JSON — lecture et écriture
- Jour 4 : List comprehensions, lambdas, gestion d'erreurs
- Jour 5 : NumPy — tableaux, opérations vectorielles
- Application : Mini-projet — script stats sur CSV

→ Claude fournit : dataset CSV (ventes fictives), squelette du script, consignes

#### Semaine 2 — Pandas & Exploration de données
- Jour 1 : DataFrame, Series, read_csv, head/info/describe
- Jour 2 : Filtres, sélection de colonnes, valeurs manquantes
- Jour 3 : Groupby, agrégations, pivot tables
- Jour 4 : Visualisation avec Matplotlib (graphiques basiques)
- Jour 5 : Nettoyage de données (duplicates, types, outliers)
- Application : Projet — EDA dataset e-commerce

→ Claude fournit : dataset clients + commandes (CSV), notebook de départ

#### Semaine 3 — scikit-learn : Classification
- Jour 1 : ML supervisé, features, labels, train/test split
- Jour 2 : Régression logistique
- Jour 3 : Random Forest
- Jour 4 : Métriques : accuracy, precision, recall, F1, matrice de confusion
- Jour 5 : Cross-validation, overfitting, underfitting
- Application : Projet — Prédiction de churn client

→ Claude fournit : dataset churn (Telco Customer Churn), notebook guidé

#### Semaine 4 — scikit-learn : Régression & Pipelines
- Jour 1 : Régression linéaire, Ridge, Lasso
- Jour 2 : Métriques régression : MAE, MSE, R²
- Jour 3 : Feature engineering — encodage, normalisation
- Jour 4 : Pipeline scikit-learn
- Jour 5 : Sauvegarder / charger un modèle (joblib)
- Application : Projet — Prédiction du prix d'un bien immobilier

→ Claude fournit : dataset immobilier, pipeline de départ

#### Semaine 5 — Hugging Face Hub & Consolidation
- Jour 1 : Découverte du Hub — modèles, datasets, Spaces
- Jour 2 : Hugging Face Inference API (requête HTTP simple)
- Jour 3 : Choisir le bon modèle pour un cas business
- Jour 4 : Documenter un projet ML (README professionnel)
- Jour 5 : Push GitHub des 2 projets Phase 1
- Application : Finalisation portfolio Phase 1

**Livrables Phase 1**
- ✅ GitHub public — 2 projets ML documentés
- ✅ Notebook churn + script de prédiction
- ✅ Notebook régression prix immobilier
- ✅ README lisible par un client non-technique

---

### 🟡 Phase 2 — ML Engineering / Production (3 semaines)

> Durée fortement réduite : 8 sem → 3 sem (Docker, FastAPI, Git, Railway déjà maîtrisés)

**🎯 Objectif** : Passer du notebook à une API ML déployée et consommable.

**Technologies** : scikit-learn avancé, FastAPI, Docker, Git, MLflow, Railway

#### Semaine 6 — Projet Python structuré
- Jour 1 : Structure projet ML (src/, data/, models/, tests/, notebooks/)
- Jour 2 : Refactoring notebook churn en scripts Python modulaires
- Jour 3 : Tests unitaires basiques (pytest)
- Jour 4 : MLflow — logger métriques, comparer des runs
- Jour 5 : MLflow Model Registry
- Application : Package Python propre

→ Claude fournit : structure de dossiers type, templates de scripts

#### Semaine 7 — API ML avec FastAPI
- Jour 1 : FastAPI — endpoint /predict
- Jour 2 : Validation inputs avec Pydantic
- Jour 3 : Charger le modèle au démarrage, gestion des erreurs
- Jour 4 : Dockeriser l'API ML
- Jour 5 : Tests avec curl et Postman
- Application : Projet — API de scoring de leads

→ Claude fournit : dataset scoring leads, code FastAPI de départ, Dockerfile

#### Semaine 8 — Déploiement & Monitoring
- Jour 1 : Déploiement sur Railway
- Jour 2 : Variables d'env, secrets, health checks
- Jour 3 : Logging des prédictions en base
- Jour 4 : Monitoring basique — data drift (concept + implémentation)
- Jour 5 : Documentation Swagger
- Application : API déployée + frontend Next.js consommant l'API

→ Claude fournit : frontend Next.js de démo, instructions de connexion

**Livrables Phase 2**
- ✅ API ML de scoring déployée sur Railway (URL publique)
- ✅ Projet structuré sur GitHub avec MLflow
- ✅ Frontend Next.js consommant l'API
- ✅ Documentation Swagger

---

### 🔵 Phase 3 — Deep Learning Essentiel (3 semaines) — Google Colab

**🎯 Objectif** : Comprendre les bases de l'IA moderne, savoir choisir DL vs ML classique.

> ⚠️ Tout se fait sur Google Colab — pas besoin de GPU local.

**Technologies** : PyTorch (bases) via Colab, Hugging Face Transformers, Matplotlib

#### Semaine 9 — Réseaux de neurones
- Jour 1 : Neurone artificiel, perceptron, activation functions
- Jour 2 : Architecture réseau dense
- Jour 3 : Backpropagation (comprendre, pas démontrer)
- Jour 4 : PyTorch sur Colab — tenseurs, premier réseau
- Jour 5 : Training loop — loss, optimizer
- Application : Réseau de prédiction simple (tabular)

→ Claude fournit : notebook Colab de départ, dataset, consignes

#### Semaine 10 — Hugging Face Transformers
- Jour 1 : Architecture Transformer (concept, sans maths)
- Jour 2 : HF pipeline() — utiliser un modèle en 3 lignes
- Jour 3 : Classification de texte avec modèle pré-entraîné
- Jour 4 : Embeddings texte — concept et utilisation
- Jour 5 : Tester plusieurs modèles HF
- Application : Projet — Classifier avis clients avec HF

→ Claude fournit : dataset d'avis clients, notebook Colab

#### Semaine 11 — DL vs ML + Consolidation
- Jour 1 : Tableau de décision DL vs ML
- Jour 2 : Présenter ce choix à un client non-technique
- Jour 3 : Révision Phases 1, 2, 3
- Jour 4 : Nettoyage et documentation GitHub
- Jour 5 : Préparation Phase 4
- Application : Push final projets Phases 1–3

**Livrables Phase 3**
- ✅ Notebook Colab PyTorch (prédiction)
- ✅ Notebook Colab classification avis clients HF Transformers
- ✅ Document de décision DL vs ML (1 page, lisible par un client)

---

### 🟣 Phase 4 — LLM & AI Engineering — Zone payante (8 semaines)

**🎯 Objectif** : Construire des solutions LLM utiles en entreprise.
⭐ **Premier client possible dès la semaine 16–17.**

**Technologies** : APIs LLM (OpenAI, Anthropic, Mistral), LlamaIndex, ChromaDB / Qdrant, FastAPI, Next.js + Vercel AI SDK, Hugging Face Inference API

#### Semaine 12 — Fondations LLM
- Jour 1 : Tokenisation, contexte, température, top-p
- Jour 2 : Appeler APIs OpenAI et Mistral en Python
- Jour 3 : Prompt engineering (rôles, CoT, instructions claires)
- Jour 4 : Prompt avancé (few-shot, JSON output, contraintes)
- Jour 5 : Comparer GPT-4o vs Mistral vs Claude
- Application : Assistant de rédaction avec historique de conversation

→ Claude fournit : starter code Python, templates de prompts, cas de test

#### Semaine 13 — Embeddings & Bases vectorielles
- Jour 1 : Concept d'embedding
- Jour 2 : Embeddings API OpenAI
- Jour 3 : ChromaDB — collection, ajout documents
- Jour 4 : Similarity search
- Jour 5 : ChromaDB vs Qdrant
- Application : Moteur de recherche sémantique

→ Claude fournit : corpus 50 documents, code ChromaDB de départ

#### Semaine 14 — RAG Partie 1
- Jour 1 : Architecture RAG (indexation, retrieval, génération)
- Jour 2 : Chunking de documents (stratégies)
- Jour 3 : Pipeline RAG basique avec LlamaIndex
- Jour 4 : Améliorer le retrieval (reranking, filtres)
- Jour 5 : Évaluer un RAG — métriques
- Application : RAG sur un PDF métier

→ Claude fournit : PDF 20 pages (doc fictive), code LlamaIndex de départ

#### Semaine 15 — RAG Partie 2
- Jour 1 : RAG multi-documents
- Jour 2 : Citations et sourcing des réponses
- Jour 3 : Mémoire conversationnelle
- Jour 4 : Sécurité — filtrage données, confidentialité
- Jour 5 : Déployer le RAG comme API FastAPI
- Application : Chatbot RAG documentation PME fictive

→ Claude fournit : 5 PDFs métier, code complet de départ

#### Semaine 16 — Interface Next.js + Agents IA
- Jour 1 : Vercel AI SDK, useChat, streaming
- Jour 2 : Interface chatbot Next.js App Router
- Jour 3 : Connecter interface → backend RAG FastAPI
- Jour 4 : Agents IA simples — concept et tools
- Jour 5 : Agent avec outils (web search, fichier, calcul)
- Application : ⭐ **PROJET CLÉ** — Chatbot RAG complet Next.js déployé en ligne

→ Claude fournit : template Next.js de départ, code agent, instructions déploiement

#### Semaine 17 — Fine-tuning basique
- Jour 1 : Fine-tuning vs prompt engineering — quand l'utiliser
- Jour 2 : Préparer un dataset JSONL
- Jour 3 : Lancer et monitorer un fine-tuning job OpenAI
- Jour 4 : Tester modèle fine-tuné vs modèle de base
- Jour 5 : Cas d'usage vendables du fine-tuning
- Application : Fine-tuning classification emails client

→ Claude fournit : dataset JSONL prêt (200 exemples), instructions complètes

#### Semaine 18 — n8n + Automatisation IA
- Jour 1 : n8n en local (Docker) — workflow basique
- Jour 2 : Intégrer un LLM dans un workflow n8n
- Jour 3 : Webhook → IA → réponse automatique
- Jour 4 : Automatisation vendable #1 — résumé automatique PDF
- Jour 5 : Automatisation vendable #2 — qualification de leads
- Application : Démo n8n packagée pour client

→ Claude fournit : workflows n8n exportables (.json), instructions

**Livrables Phase 4**
- ⭐ Chatbot métier RAG — Next.js + FastAPI — déployé
- ✅ Moteur de recherche sémantique
- ✅ Fine-tuning modèle custom
- ✅ Workflow n8n avec IA
- ✅ GitHub à jour

---

### 🔴 Phase 5 — Freelance IA Ready (6 semaines)

**🎯 Objectif** : Transformer la technique en offres vendables. Signer les premiers clients.

**Offres types**

| # | Offre | Prix |
|---|-------|------|
| 1 | Chatbot interne PME             | 800 – 2 000 € + 200 €/mois |
| 2 | Assistant documentaire          | 1 200 – 3 000 € + abonnement |
| 3 | Scoring / Prédiction client     | 1 500 – 4 000 € (modèle + API) |
| 4 | Automatisation IA avec n8n      | 500 – 1 500 € + 150 €/mois |

**Canaux de prospection**
- Malt (France/Europe)
- LinkedIn — posts démos, cas clients, contenu éducatif PME
- Réseau local Madagascar — PMEs locales et startups africaines
- Tefy Labs / Beauplume — vitrine de compétences IA

**Détail**
- Semaine 20 : 4 fiches offres IA packagées
- Semaine 21 : Démo live + pitch 5 min
- Semaine 22 : Template devis IA + CGV
- Semaine 23 : Profils Malt + LinkedIn + Tefy Labs optimisés
- Semaine 24 : Simulateur de coûts API
- Semaine 25 : 10 contacts, 1 client ou POC signé

---

### ⚫ Phase 6 — Scaling & Positionnement (4 semaines)

**🎯 Objectif** : Stabiliser et scaler l'activité freelance IA.

- Semaine 26 : Templates réutilisables (RAG, API ML, chatbot)
- Semaine 27 : Cloud ML basique — AWS Bedrock ou GCP Vertex AI
- Semaine 28 : Guide de décision LLM open-source vs API payante
- Semaine 29 : Connexion Tefy Labs + limites légales (RGPD, hallucinations)

---

## 📦 Portfolio final (4 projets clés)

1. ✅ **Moteur de prédiction ML** — churn + scoring leads (API FastAPI déployée)
2. ⭐ **Chatbot métier RAG** — PDFs internes, interface Next.js, sources citées
3. ✅ **Assistant IA** — workflow n8n automatisé avec LLM
4. ✅ **Fine-tuning custom** — modèle OpenAI spécialisé sur un cas métier

---

## 💰 Positionnement commercial

**Tu ne vends PAS :**
- ❌ "du machine learning" / "du LLM" / "de l'IA"

**Tu vends :**
- ✅ "Automatisation intelligente"
- ✅ "Assistant IA métier"
- ✅ "Réduction du temps humain"
- ✅ "Aide à la décision"

---

## 📊 Planning révisé synthétique

| Phase | Sujet | Durée révisée | Original |
|-------|-------|---------------|----------|
| 1 | Fondations ML            | 5 semaines | 8 |
| 2 | ML Engineering           | 3 semaines | 8 |
| 3 | Deep Learning            | 3 semaines | 8 |
| 4 | LLM & AI Engineering     | 8 semaines | 8 *(ne pas raccourcir)* |
| 5 | Freelance IA Ready       | 6 semaines | 8 |
| 6 | Scaling                  | 4 semaines | 8 |
| **TOTAL** | | **~29 semaines (~7,5 mois)** | |

---

## 🤖 Guide technique — Comment fonctionne l'accompagnement

**Démarrer une session**
> "Claude, je commence la Semaine X / Jour Y de la Phase Z"
→ Claude donne le dataset, starter code et instructions pour cette session.

**Valider une étape**
> "Claude, voici mon code / résultat, est-ce que c'est bon ?"
→ Claude évalue, corrige, confirme si tu es prêt à avancer.

**Ce que Claude fournit à chaque session**
- Dataset ou fichier de travail (CSV, PDF, JSON, JSONL...)
- Starter code adapté au niveau
- Instructions pas à pas
- Critères de validation
- Explication business (comment vendre ce que tu viens d'apprendre)
