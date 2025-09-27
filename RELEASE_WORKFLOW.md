# Release workflow — native-builder (Windows, Linux, macOS)

**Purpose**
This document describes the streamlined release workflow for building and preparing native executables for `dgupdater` using the `native-builder` GitHub Actions workflow. It covers usage on **Windows, Linux, and macOS**.

---

## Workflow

### 1. Create a new branch for your changes

Create a new feature branch from the main branch and make your changes there.

---

### 2. Move changes to the native-builder branch

Before switching, make sure to **commit or push all local changes** so nothing is lost or blocked. Then switch to the `native-builder` branch, bring in your changes from the feature branch, and push. This will trigger the GitHub Actions workflow.

---

### 3. Wait for GitHub Actions to complete

Monitor the workflow run on the Actions tab until it finishes successfully.

---

### 4. Switch back to your feature branch

Once the workflow has completed, return to your feature branch to continue.

---

### 5. Get the latest run ID

Make sure you have **GitHub CLI (gh)** installed. Then fetch the latest run ID:

```bash
gh run list --workflow native-builder.yml --repo Ashif4354/dgupdater --limit 1
```

---

### 6. Download build artifacts

Download the artifacts produced by the workflow run:

```bash
gh run download <run-id> --repo Ashif4354/dgupdater --dir ./native-builds
```

Replace `<run-id>` with the actual ID from the previous step.

---

### 7. Copy executables into project structure

Copy the built executables into the appropriate directories under `dgupdater/bin/`.

#### Windows (PowerShell)

```powershell
Copy-Item native-builds/dgupdater-macos-latest/dist/dgupdaterupdate_mac dgupdater/bin/dgupdaterupdate_mac
Copy-Item native-builds/dgupdater-ubuntu-latest/dist/dgupdaterupdate_lin dgupdater/bin/dgupdaterupdate_lin
Copy-Item native-builds/dgupdater-windows-latest/dist/dgupdaterupdate_win.exe dgupdater/bin/dgupdaterupdate_win.exe
```

#### Windows (CMD)

```cmd
copy native-builds\dgupdater-macos-latest\dist\dgupdaterupdate_mac dgupdater\bin\dgupdaterupdate_mac
copy native-builds\dgupdater-ubuntu-latest\dist\dgupdaterupdate_lin dgupdater\bin\dgupdaterupdate_lin
copy native-builds\dgupdater-windows-latest\dist\dgupdaterupdate_win.exe dgupdater\bin\dgupdaterupdate_win.exe
```

#### Linux / macOS (Bash)

```bash
cp native-builds/dgupdater-macos-latest/dist/dgupdaterupdate_mac dgupdater/bin/dgupdaterupdate_mac
cp native-builds/dgupdater-ubuntu-latest/dist/dgupdaterupdate_lin dgupdater/bin/dgupdaterupdate_lin
cp native-builds/dgupdater-windows-latest/dist/dgupdaterupdate_win.exe dgupdater/bin/dgupdaterupdate_win.exe
```

> You can also copy files manually with **Ctrl+C / Ctrl+V** if you prefer.

---

### 8. Update version number

Update the version string in `setup.py` according to whether this is a minor or patch release.

---

### 9. Create PR

Open a pull request from your feature branch to `main`.

---

### 10. Merge PR

Merge the pull request after approval.

---

### 11. Create release

Create a GitHub release with the new version tag. The GitHub Actions workflow will automatically publish the new version to PyPI.

---

## Quick checklist

```
[x] Create feature branch and make changes
[x] Commit/push all changes before switching to native-builder
[x] Move changes into native-builder and push
[x] Wait for Actions to finish
[x] Switch back to your feature branch
[x] gh run list --workflow native-builder.yml --limit 1
[x] gh run download <run-id> --dir ./native-builds
[x] Copy artifacts (PowerShell / CMD / Bash or manually)
[x] Update version in setup.py
[x] Create PR
[x] Merge PR
[x] Create GitHub release (tag vX.X.X)
```

---

## Closing note

This workflow ensures that native executables are always properly built, versioned, and released with minimal manual effort. Follow the steps carefully, and the release process will stay smooth and consistent.
