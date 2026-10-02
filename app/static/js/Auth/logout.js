function handleLogout() {
    // Mungkin dipakai untuk template admin panel ini
    triggerToast("Berhasil logout! Mengalihkan ke halaman login...");

    setTimeout(() => {
        window.location.href = 'login.html';
    }, 1000);
}