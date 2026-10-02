function handleLogin(e) {
    e.preventDefault();
    triggerToast('Login berhasil! Mengalihkan...');
    setTimeout(() => {
        window.location.href = 'index.html';
    }, 1000);
}