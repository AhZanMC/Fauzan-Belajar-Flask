function handleRegister(e) {
    e.preventDefault();

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Pengecekan apakah password dan konfirmasi password sama atau nggak :v
    if (password !== confirmPassword) {
        triggerToast('Password dan konfirmasi password tidak sama!', 'error');
        return; // Stop kalo hasilnya nggak sama dan gabisa login wkwkwkwk
    }

    // Nahh kalo passwordnya sama, lanjut ke sini cuy dan user bisa login :)
    triggerToast('Pendaftaran berhasil! Silakan login.');
    setTimeout(() => {
        window.location.href = 'login.html';
    }, 1200);
}