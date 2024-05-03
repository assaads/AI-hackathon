---
title: Versioning: Starlight Project
description: Understanding versioning and updates within the Starlight project.
---

## Versioning

The Starlight project, like many software projects, follows a versioning system to track changes and improvements over time. Understanding versioning is crucial for staying up-to-date with the latest features and ensuring compatibility. 

### Semantic Versioning

Starlight adheres to [semantic versioning](https://semver.org/), which uses a three-part version number format: `MAJOR.MINOR.PATCH`.

*   **MAJOR:** Incremented for significant changes that may introduce breaking compatibility with previous versions.
*   **MINOR:** Incremented for new features or functionality that are backward-compatible.
*   **PATCH:** Incremented for bug fixes or minor updates that do not affect compatibility.

### Checking Current Version

To determine the current version of Starlight you are using, refer to the `package.json` file in the root directory of your project. The version number will be listed under the `dependencies` or `devDependencies` section.

### Updating to a New Version

1.  **Check Release Notes:** Before updating, review the release notes for the new version to understand the changes and any potential compatibility issues.
2.  **Update Dependencies:** Use npm or yarn to update the `@astrojs/starlight` package to the desired version:

```bash
npm update @astrojs/starlight
```

or

```bash
yarn upgrade @astrojs/starlight
```

3.  **Address Breaking Changes:** If the new version introduces breaking changes, modify your code accordingly to ensure compatibility. 

## Migration Guide

For major version updates that involve significant changes, a migration guide will be provided to assist users in transitioning their projects to the new version smoothly. This guide will outline the necessary steps and highlight any adjustments required to maintain functionality. 
