async function refreshFiles() {
  const res = await fetch('/list_files');
  const files = await res.json();
  const list = document.getElementById('fileList');
  list.innerHTML = '';
  files.forEach(f => {
    const li = document.createElement('li');
    const link = document.createElement('a');
    link.href = `/download/${f}`;
    link.textContent = f;
    li.appendChild(link);
    list.appendChild(li);
  });
}

// 上傳檔案
document.getElementById('uploadForm').addEventListener('submit', async e => {
  e.preventDefault();
  const fileInput = document.getElementById('fileInput');
  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  const res = await fetch('/upload', { method: 'POST', body: formData });
  const result = await res.json();
  alert(result.message || result.error);
  refreshFiles(); // 上傳完自動更新列表
});

document.getElementById('refreshBtn').addEventListener('click', refreshFiles);

window.onload = refreshFiles;
