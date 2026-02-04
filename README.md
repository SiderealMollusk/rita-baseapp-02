# FastAPI CI/CD Experiment

This project is a minimal FastAPI application demonstrating a full CI/CD loop using GitHub Actions, Docker, Helm, and ArgoCD.

## Features

- **FastAPI Application**: Simple `/hello` and `/health` endpoints.
- **Dockerized**: Multi-stage build for a small footprint.
- **Helm Chart**: Ready for Kubernetes deployment.
- **CI/CD**:
  - Linting and testing on every push.
  - Automated versioning with Semantic Release.
  - Automated Docker image build and push to GHCR on release.
- **GitOps**: ArgoCD manifest for automated deployment.

## Repository Structure

- `.github/workflows/`: GitHub Actions for CI and CD.
- `app/`: FastAPI application code.
- `charts/fastapi-hello/`: Helm chart for Kubernetes.
- `gitops/`: ArgoCD Application manifest.
- `Dockerfile`: Multi-stage Docker build.
- `requirements.txt`: Python dependencies.

## Setup Instructions

To get this experiment running in your own environment, you need to replace some placeholders:

### 1. Update ArgoCD Manifest
In `gitops/argocd-app.yaml`, update the `repoURL`:
```yaml
repoURL: https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
```

### 2. Update Helm Values
In `charts/fastapi-hello/values.yaml`, update the image repository:
```yaml
image:
  repository: ghcr.io/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME
```

### 3. GitHub Actions
The GitHub Actions are configured to automatically use your repository name:
- `ghcr.io/${{ github.repository }}`

Ensure your GitHub repository has the following settings:
- **Actions Permissions**: "Read and write permissions" (under Settings > Actions > General > Workflow permissions) to allow Semantic Release to create tags and releases.
- **GHCR Permissions**: The first time you push an image, you might need to ensure the package visibility is set to Public or appropriately shared with your cluster.

## Deployment

1. **Commit and Push**: Push your changes to the `main` branch using [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `feat: add hello endpoint`).
2. **Release**: The "Build" workflow will trigger Semantic Release, which will create a new GitHub Tag and Release.
3. **Delivery**: The "Delivery" workflow will trigger on the new Release, build the Docker image, and push it to GHCR.
4. **ArgoCD**: If you have ArgoCD installed and have applied the `gitops/argocd-app.yaml`, it will detect the changes and deploy the application to the `hello-world` namespace in your cluster.

## Local Testing

```bash
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:.
pytest
uvicorn app.main:app --reload
```
