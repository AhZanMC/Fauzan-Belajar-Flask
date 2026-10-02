const crudModal = document.getElementById('crudModal');
const modalTitle = document.getElementById('modalTitle');
const inputName = document.getElementById('inputName');
const inputCategory = document.getElementById('inputCategory');
const inputStatus = document.getElementById('inputStatus');

function openCrudModal(mode, name = '', category = '', status = 'Aktif') {
    crudModal.classList.remove('hidden');
    if (mode === 'add') {
        modalTitle.innerText = 'Tambah Item Baru';
        inputName.value = '';
        inputCategory.value = '';
        inputStatus.value = 'Aktif';
    } else {
        modalTitle.innerText = 'Edit Item Proyek';
        inputName.value = name;
        inputCategory.value = category;
        inputStatus.value = status;
    }
}

function closeCrudModal() {
    crudModal.classList.add('hidden');
}

function handleFormSubmit(e) {
    e.preventDefault();
    closeCrudModal();
    triggerToast('Data berhasil disimpan ke sistem!');
}

function deleteItem(buttonElement, name) {
    if (confirm(`Apakah Anda yakin ingin menghapus "${name}"?`)) {
        const row = buttonElement.closest('tr');
        row.remove();
        triggerToast(`Item "${name}" telah dihapus.`);
    }
}