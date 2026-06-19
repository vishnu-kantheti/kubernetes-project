# Kubernetes Full Stack Application Deployment 

A full-stack web application deployed on Kubernetes using containerization, networking, persistent storage, and ingress routing.

This project demonstrates how a DevOps engineer deploys and manages a multi-container application in a Kubernetes environment.

---

# Project Overview

The application consists of:

- Frontend (Nginx + HTML/CSS/JavaScript)
- Backend (Flask API)
- Database (MySQL)

Each component runs inside its own Kubernetes workload and communicates through Kubernetes Services.


---
             
# Technologies Used

- Kubernetes
- Docker
- Docker Hub
- Nginx
- Flask
- MySQL
- Kubernetes Services
- Ingress Controller
- Persistent Volumes
- Secrets
- Git & GitHub

---

# Kubernetes Concepts Implemented

## Containerization

- Created Docker images for frontend and backend applications
- Stored images in Docker Hub
- Deployed containers using Kubernetes

---

## Deployments

Created Kubernetes Deployments for:

- Frontend
- Backend
- MySQL

Benefits:

- Pod management
- Self healing
- Replica management

---

## Services

Implemented Kubernetes Services:

### Frontend Service

Exposes frontend pods internally.

### Backend Service

Provides stable communication between frontend and backend.

### MySQL Service

Allows backend pods to communicate with database pods using service DNS.

Example:
backend → mysql-service → mysql pod
---

## Secrets

Database credentials are stored securely using Kubernetes Secrets.

Flow:
Secret

↓

MySQL Container

↓

Database Authentication

---

## Persistent Storage

Implemented Persistent Volume Claim (PVC) for MySQL.

Purpose:

- Data remains available even if the database pod restarts.

Flow:
MySQL Pod

↓

PVC

↓

Persistent Storage

---

## Ingress

Configured Nginx Ingress Controller for external access.

Routing:
myapp.local/

    ↓

frontend-service

myapp.local/api

    ↓

backend-service

---

# Project Structure
kubernetes-fullstack-project/

│

├── frontend/

│ ├── Dockerfile

│ └── index.html

├── backend/

│ ├── Dockerfile

│ └── app.py

├── kubernetes/

│

│ ├── frontend/

│ │ ├── deployment.yaml

│ │ └── service.yaml

│

│ ├── backend/

│ │ ├── deployment.yaml

│ │ └── service.yaml

│

│ ├── database/

│ │ ├── deployment.yaml

│ │ ├── service.yaml

│ │ ├── pvc.yaml

│ │ └── secret.yaml

│

│ └── ingress.yaml

└── README.md

---

# How To Run

## Clone Repository
# How To Run

## Clone Repository


git clone https://github.com/vishnu-kantheti/kubernetes-project


Go into project:


cd kubernetes-fullstack-project


---

## Deploy Namespace


kubectl apply -f namespace.yaml


---

## Deploy Database


kubectl apply -f kubernetes/database/


---

## Deploy Backend


kubectl apply -f kubernetes/backend/


---

## Deploy Frontend


kubectl apply -f kubernetes/frontend/


---

## Deploy Ingress


kubectl apply -f kubernetes/ingress.yaml


---

# Check Deployment

Check pods:


kubectl get pods -n portfolio-app


Check services:


kubectl get svc -n portfolio-app


Check ingress:


kubectl get ingress -n portfolio-app


---

# Application Access

Open:


http://myapp.local


Backend API:


http://myapp.local/api


---

# Key Learnings

Through this project:

- Containerized applications using Docker
- Managed workloads using Kubernetes
- Implemented Kubernetes networking
- Connected multiple services
- Managed secrets and storage
- Used ingress for application routing
- Built a production-style deployment architecture

---

# Author

**Kantheti Sai Vishnu**

DevOps | Cloud | Linux | Docker | Kubernetes






