### 1. Build Docker Image (DockerBuild.yml)

This workflow is triggered on every push to the main branch. It sets up a Docker Buildx environment, checks out the repository, and builds a Docker image using a multi-platform build configuration. The resulting image is tagged as `camilbenameur/cicd_project:latest` and supports both `linux/amd64` and `linux/arm64` architectures.

### 2. Build Main (BuildMain.yml)

This workflow is triggered on pushes to the main branch, changes to specific files (`main.py`, `requirements.txt`, `pylintrc.txt`), pull requests affecting the same files, or manually triggered via workflow_dispatch. It checks out the repository, sets up Python 3.8, installs dependencies from `requirements.txt`, and runs pylint on `main.py` with a custom configuration file (`pylintrc.txt`).

### 3. Docker Push to DockerHub (DockerPushDockerHub.yml)

This workflow is triggered on pushes with tags following semantic versioning (`vX.X.X`). It checks out the code, sets up Docker Buildx, logs in to DockerHub using secrets, extracts the semantic version from the tag, and builds/pushes a Docker image to DockerHub. The image is tagged with the DockerHub username, repository name (`cicd-project`), and the extracted semantic version.

### 4. Docker Push to GCR (DockerPushGCR.yml)

This workflow is manually triggered via workflow_dispatch or on every push with any tag. It checks out the code, sets up Docker Buildx, authenticates with Google Cloud using provided credentials, configures Docker to use GCR as a container registry, and builds/pushes a Docker image to GCR. The image is tagged with the specified repository path and the GitHub repository and reference name.
