// Buat Sidebar
const sidebar = document.getElementById('sidebar');
const sidebarToggle = document.getElementById('sidebarToggle');
const mobileSidebarToggle = document.getElementById('mobileSidebarToggle');
const toggleIcon = document.getElementById('toggleIcon');
const sidebarTexts = document.querySelectorAll('.sidebar-text');

let isCollapsed = false;

function toggleSidebar() {
    isCollapsed = !isCollapsed;

    if (isCollapsed) {
        sidebar.classList.remove('sidebar-expanded');
        sidebar.classList.add('sidebar-collapsed');
        toggleIcon.classList.add('rotate-180');

        // Sembunyikan teks label di sidebar
        sidebarTexts.forEach(el => el.classList.add('hidden'));
    } else {
        sidebar.classList.remove('sidebar-collapsed');
        sidebar.classList.add('sidebar-expanded');
        toggleIcon.classList.remove('rotate-180');

        // Tampilkan kembali teks label
        sidebarTexts.forEach(el => el.classList.remove('hidden'));
    }
}

if (sidebarToggle) {
    sidebarToggle.addEventListener('click', toggleSidebar);
}

// Mobile drawer toggle
if (mobileSidebarToggle) {
    mobileSidebarToggle.addEventListener('click', () => {
        sidebar.classList.toggle('hidden');
    });
}