# FileVault — GitHub-hosted file storage

A static file storage website hosted on **GitHub Pages** with a clean dark UI,
search/filter, and full GitHub API integration for listing, uploading, and deleting files.

## Quick Start

### 1. Fork / create a repo

Create a new GitHub repository (public or private).

### 2. Upload these files

Place `index.html`, `css/style.css`, and `js/app.js` in the root.
Create an empty `assets/files/` directory (GitHub won't track empty folders,
so add a `.gitkeep` file inside it).

### 3. Enable GitHub Pages

- Go to **Settings → Pages**
- Set **Source** to `Deploy from a branch`
- Choose `main` / `master` and `/ (root)` folder
- Save → your site will be live at `https://yourusername.github.io/yourrepo/`

### 4. Configure in the browser

1. Open your GitHub Pages URL
2. Click the **⚙️ Configure** button (top right)
3. Enter:
   - **Repository**: `yourusername/yourrepo`
   - **Token**: a [GitHub personal access token](https://github.com/settings/tokens)
     with **`repo`** scope (full control of private repositories)
   - **Branch**: `main` (or whichever branch GitHub Pages serves from)
4. Click **Save**

Your files will appear automatically. Drag & drop files onto the upload zone to add more.

## Features

| Feature              | Description |
|----------------------|-------------|
| 📁 File listing      | Browse all files in `assets/files/` |
| 🔍 Search & filter   | Live search by name, filter by category |
| 📊 Stats bar         | Shows total file count and aggregate size |
| ⬆️ Drag & drop upload| Upload via drag-and-drop or file picker |
| 🗑️ Delete files      | Remove files directly from the UI |
| ⚙️ Config modal      | GitHub API key and repo settings |

## Security notes

- Your GitHub token is stored **only in localStorage** (never sent to any server except `api.github.com`).
- For public repos, a token with `public_repo` scope is sufficient.
- For private repos, use `repo` scope.
- Always use a **fine-grained** token scoped to just this repository when possible.

## Customization

- Edit `css/style.css` to change colors, layout, or theme.
- Modify `js/app.js` to change file paths (e.g., `assets/files/` to `storage/`).
- Extend file category detection in `getFileCategory()` for custom types.
