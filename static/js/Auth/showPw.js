function togglePass(inputId, btnElement) {
    const input = document.getElementById(inputId);
    if (!input) return;

    // Ambil elemen SVG di dalam button yang diklik
    const svg = btnElement.querySelector('svg');

    // Path SVG untuk ikon mata dan mata dicoret
    const eyeIcon = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />`;
    const eyeSlashIcon = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858-5.908A9.954 9.954 0 0112 5c4.478 0 8.268 2.943 9.542 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21M3 3l18 18" />`;

    if (input.type === 'password') {
        input.type = 'text';
        document.getElementById('password').placeholder = 'Admin#1234'; // Ganti placeholder saat password ditampilkan
        svg.innerHTML = eyeSlashIcon; // Ganti ke ikon mata dicoret
    } else {
        input.type = 'password';
        document.getElementById('password').placeholder = '••••••••'; // Ganti placeholder saat password disembunyikan
        svg.innerHTML = eyeIcon; // Balik ke ikon mata biasa
    }
}