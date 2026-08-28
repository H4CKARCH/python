/* ===================================================
 * FileVault — GitHub-hosted file storage frontend
 * Uses GitHub API (v3) for file listing and uploads.
 * =================================================== */

const CONFIG_KEY = 'filevault_config';

// ─── State ──────────────────────────────────────────
let config = loadConfig();
let files = [];
let filteredFiles = [];

// ─── DOM refs ───────────────────────────────────────
const fileGrid      = document.getElementById('fileGrid');
const searchInput   = document.getElementById('searchInput');
const categoryFilter= document.getElementById('categoryFilter');
const sortFilter    = document.getElementById('sortFilter');
const fileCountSpan = document.getElementById('fileCount');
const totalSizeSpan = document.getElementById('totalSize');
const statusMsg     = document.getElementById('statusMessage');
const uploadZone    = document.getElementById('uploadZone');
const fileInput     = document.getElementById('fileInput');
const uploadLink    = document.getElementById('uploadLink');
const configBtn     = document.getElementById('configBtn');
const configModal   = document.getElementById('configModal');
const configForm    = document.getElementById('configForm');
const repoInput     = document.getElementById('repoInput');
const tokenInput    = document.getElementById('tokenInput');
const branchInput   = document.getElementById('branchInput');
const configCancel  = document.getElementById('configCancel');

// ─── Helpers ────────────────────────────────────────
function loadConfig() {
    try {
        const raw = localStorage.getItem(CONFIG_KEY);
        return raw ? JSON.parse(raw) : null;
    } catch { return null; }
}

function saveConfig(cfg) {
    localStorage.setItem(CONFIG_KEY, JSON.stringify(cfg));
    config = cfg;
}

function formatSize(bytes) {
    if (bytes === 0) return '0 B';
    const units = ['B', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(1024));
    return (bytes / Math.pow(1024, i)).toFixed(i > 0 ? 1 : 0) + ' ' + units[i];
}

function formatDate(iso) {
    if (!iso) return '—';
    const d = new Date(iso);
    return d.toLocaleDateString('en-US', {
        year: 'numeric', month: 'short', day: 'numeric',
        hour: '2-digit', minute: '2-digit'
    });
}

function getFileCategory(name) {
    const ext = name.split('.').pop().toLowerCase();
    const docs    = ['pdf','doc','docx','xls','xlsx','ppt','pptx','txt','md','csv','odt','rtf'];
    const images  = ['jpg','jpeg','png','gif','bmp','webp','svg','ico','tiff'];
    const videos  = ['mp4','avi','mkv','mov','wmv','flv','webm'];
    const audio   = ['mp3','wav','ogg','flac','aac','wma','m4a'];
    const archives= ['zip','rar','7z','tar','gz','bz2','xz','zst'];
    const code    = ['js','ts','py','rb','go','java','c','cpp','cs','php','swift','kt','rs','sh','bash','yml','yaml','json','xml','html','css','sql','dockerfile','toml','ini','cfg'];
    if (docs.includes(ext))       return 'document';
    if (images.includes(ext))     return 'image';
    if (videos.includes(ext))     return 'video';
    if (audio.includes(ext))      return 'audio';
    if (archives.includes(ext))   return 'archive';
    if (code.includes(ext))       return 'code';
    return 'other';
}

function getFileIcon(category) {
    const icons = {
        document: '📄', image: '🖼️', video: '🎬', audio: '🎵',
        archive: '📦', code: '💻', other: '📄'
    };
    return icons[category] || '📄';
}

// ─── GitHub API ─────────────────────────────────────
async function apiRequest(endpoint, options = {}) {
    if (!config) throw new Error('GitHub not configured. Click ⚙️ Configure.');
    const { repo, token, branch } = config;
    const base = `https://api.github.com/repos/${repo}/contents`;
    const url  = `${base}${endpoint}`;
    const headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'FileVault'
    };
    if (token) headers['Authorization'] = `Bearer ${token}`;
    const res = await fetch(url, { ...options, headers });
    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.message || `HTTP ${res.status}`);
    }
    return res.json();
}

async function listFiles() {
    const data = await apiRequest('/assets/files');
    if (!Array.isArray(data)) {
        // Single file or directory doesn't exist
        return [];
    }
    return data
        .filter(item => item.type === 'file')
        .map(item => ({
            name: item.name,
            path: item.path,
            size: item.size,
            sha: item.sha,
            download_url: item.download_url,
            html_url: item.html_url,
            updated_at: null  // GitHub API doesn't provide per-file dates in contents endpoint
        }));
}

async function uploadFile(file) {
    const reader = new FileReader();
    return new Promise((resolve, reject) => {
        reader.onload = async () => {
            try {
                const base64 = reader.result.split(',')[1]; // strip data:...;base64,
                const path = `assets/files/${file.name}`;
                const data = await apiRequest(`/${path}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        message: `Upload ${file.name}`,
                        content: base64,
                        branch: config.branch
                    })
                });
                resolve(data);
            } catch (err) {
                reject(err);
            }
        };
        reader.onerror = () => reject(new Error('Failed to read file'));
        reader.readAsDataURL(file);
    });
}

async function deleteFile(path) {
    // Need SHA to delete — fetch file metadata first
    const meta = await apiRequest(`/${path}`);
    await apiRequest(`/${path}`, {
        method: 'DELETE',
        body: JSON.stringify({
            message: `Delete ${path.split('/').pop()}`,
            sha: meta.sha,
            branch: config.branch
        })
    });
}

// ─── Render ─────────────────────────────────────────
function render() {
    const query = searchInput.value.toLowerCase().trim();
    const cat   = categoryFilter.value;
    const sort  = sortFilter.value;

    filteredFiles = files.filter(f => {
        if (query && !f.name.toLowerCase().includes(query)) return false;
        if (cat !== 'all' && getFileCategory(f.name) !== cat) return false;
        return true;
    });

    // Sort
    filteredFiles.sort((a, b) => {
        switch (sort) {
            case 'name-asc':  return a.name.localeCompare(b.name);
            case 'name-desc': return b.name.localeCompare(a.name);
            case 'size-asc':  return a.size - b.size;
            case 'size-desc': return b.size - a.size;
            case 'date-asc':  return (a.updated_at || '').localeCompare(b.updated_at || '');
            case 'date-desc': return (b.updated_at || '').localeCompare(a.updated_at || '');
            default: return 0;
        }
    });

    // Stats
    fileCountSpan.textContent = `${filteredFiles.length} file${filteredFiles.length !== 1 ? 's' : ''}`;
    const totalBytes = filteredFiles.reduce((acc, f) => acc + f.size, 0);
    totalSizeSpan.textContent = formatSize(totalBytes);

    if (filteredFiles.length === 0) {
        fileGrid.innerHTML = `<div class="empty-state">📭 No files found</div>`;
        return;
    }

    fileGrid.innerHTML = filteredFiles.map(f => {
        const cat = getFileCategory(f.name);
        const icon = getFileIcon(cat);
        return `
            <div class="file-card" data-path="${f.path}">
                <div class="file-card-header">
                    <span class="file-icon">${icon}</span>
                    <span class="file-name" title="${f.name}">${f.name}</span>
                </div>
                <div class="file-meta">
                    <span>${formatSize(f.size)}</span>
                    <span>${formatDate(f.updated_at)}</span>
                </div>
                <div class="file-actions">
                    <a href="${f.download_url}" target="_blank" class="btn btn-outline btn-sm" download>⬇️ Download</a>
                    <button class="btn btn-danger btn-sm delete-btn" data-path="${f.path}">🗑️ Delete</button>
                </div>
            </div>
        `.trim();
    }).join('');

    // Wire delete buttons
    document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.stopPropagation();
            const path = btn.dataset.path;
            if (!confirm(`Delete "${path.split('/').pop()}"?`)) return;
            try {
                await deleteFile(path);
                showStatus(`Deleted ${path.split('/').pop()}`, 'success');
                await refresh();
            } catch (err) {
                showStatus(`Delete failed: ${err.message}`, 'error');
            }
        });
    });
}

async function refresh() {
    if (!config) { render(); return; }
    fileGrid.innerHTML = `<div class="loading-spinner"></div>`;
    try {
        files = await listFiles();
        render();
    } catch (err) {
        showStatus(`Failed to load files: ${err.message}`, 'error');
        files = [];
        render();
    }
}

function showStatus(msg, type = 'info') {
    statusMsg.textContent = msg;
    statusMsg.className = `status-message ${type}`;
    statusMsg.classList.remove('hidden');
    setTimeout(() => statusMsg.classList.add('hidden'), 5000);
}

// ─── Upload handling ────────────────────────────────
async function handleUpload(file) {
    if (!config) {
        showStatus('Configure GitHub first (⚙️ button)', 'error');
        return;
    }
    try {
        await uploadFile(file);
        showStatus(`✅ ${file.name} uploaded`, 'success');
        await refresh();
    } catch (err) {
        showStatus(`Upload failed: ${err.message}`, 'error');
    }
}

uploadZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadZone.classList.add('dragover');
});
uploadZone.addEventListener('dragleave', () => {
    uploadZone.classList.remove('dragover');
});
uploadZone.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadZone.classList.remove('dragover');
    const dropped = Array.from(e.dataTransfer.files);
    dropped.forEach(f => handleUpload(f));
});

uploadLink.addEventListener('click', (e) => {
    e.preventDefault();
    fileInput.click();
});
fileInput.addEventListener('change', () => {
    Array.from(fileInput.files).forEach(f => handleUpload(f));
    fileInput.value = '';
});

// ─── Modal config ───────────────────────────────────
configBtn.addEventListener('click', () => {
    if (config) {
        repoInput.value   = config.repo   || '';
        tokenInput.value  = config.token  || '';
        branchInput.value = config.branch || 'main';
    }
    configModal.classList.remove('hidden');
});

configCancel.addEventListener('click', () => {
    configModal.classList.add('hidden');
});

configForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const repo   = repoInput.value.trim();
    const token  = tokenInput.value.trim();
    const branch = branchInput.value.trim() || 'main';
    if (!repo || !token) {
        showStatus('Repository and token are required.', 'error');
        return;
    }
    saveConfig({ repo, token, branch });
    configModal.classList.add('hidden');
    showStatus('Configuration saved!', 'success');
    refresh();
});

// Click outside modal to close
configModal.addEventListener('click', (e) => {
    if (e.target === configModal) configModal.classList.add('hidden');
});

// ─── Event listeners for filters ────────────────────
searchInput.addEventListener('input', render);
categoryFilter.addEventListener('change', render);
sortFilter.addEventListener('change', render);

// ─── Init ───────────────────────────────────────────
refresh();
