// Jalankan hanya setelah DOM siap
document.addEventListener("DOMContentLoaded", function () {

  // === Grafik Tren UMKM ===
  const umkmCanvas = document.getElementById('umkmChart');
  if (umkmCanvas) {
    const umkmCtx = umkmCanvas.getContext('2d');
    fetch('umkm.php')
    new Chart(umkmCtx, {
      type: 'bar',
      data: {
        labels: ['2020', '2021', '2022', '2023', '2024'],
        datasets: [{
          label: 'Jumlah UMKM Terdaftar',
          data: [240, 300, 370, 450, 520],
          backgroundColor: 'rgba(40, 167, 69, 0.7)'
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }

  // === Jenis Usaha UMKM (Doughnut) ===
  const usahaCanvas = document.getElementById('jenisUsahaChart');
  if (usahaCanvas) {
    const usahaCtx = usahaCanvas.getContext('2d');
    new Chart(usahaCtx, {
      type: 'doughnut',
      data: {
        labels: ['Kuliner', 'Fashion', 'Kerajinan', 'Jasa', 'Pertanian'],
        datasets: [{
          label: 'Persentase',
          data: [35, 25, 20, 10, 10],
          backgroundColor: [
            '#007bff',
            '#28a745',
            '#ffc107',
            '#17a2b8',
            '#dc3545'
          ],
          borderColor: '#fff',
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'bottom'
          },
          tooltip: {
            callbacks: {
              label: function (context) {
                return `${context.label}: ${context.parsed}%`;
              }
            }
          }
        }
      }
    });
  }

  // === Kategori UMKM (Pie) ===
  const kategoriCanvas = document.getElementById('kategoriPieChart');
  if (kategoriCanvas) {
    const kategoriCtx = kategoriCanvas.getContext('2d');
    new Chart(kategoriCtx, {
      type: 'pie',
      data: {
        labels: ['Mikro', 'Kecil', 'Menengah'],
        datasets: [{
          data: [60, 30, 10],
          backgroundColor: ['#4CAF50', '#FFC107', '#2196F3'],
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: 'bottom' }
        }
      }
    });
  }

  // === Status Pengajuan (Horizontal Bar) + Dropdown Bulan ===
  const statusCanvas = document.getElementById('statusPengajuanChart');
  const bulanSelect = document.getElementById('bulanSelect');

  const dataPerBulan = {
    jan: [100, 50, 30],
    feb: [150, 60, 45],
    mar: [200, 70, 90],
    apr: [720, 120, 380],
    mei: [500, 200, 100],
    jun: [300, 150, 50]
  };

  if (statusCanvas && bulanSelect) {
    const statusCtx = statusCanvas.getContext('2d');
    let statusChart = new Chart(statusCtx, {
      type: 'bar',
      data: {
        labels: ['Disetujui', 'Ditolak', 'Diproses'],
        datasets: [{
          label: 'Jumlah Pengajuan',
          data: dataPerBulan[bulanSelect.value],
          backgroundColor: ['#28a745', '#dc3545', '#ffc107']
        }]
      },
      options: {
        responsive: true,
        indexAxis: 'y',
        scales: {
          x: {
            beginAtZero: true
          }
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: function (context) {
                return `${context.label}: ${context.parsed} pengajuan`;
              }
            }
          }
        }
      }
    });

    bulanSelect.addEventListener('change', function () {
      const selected = bulanSelect.value;
      statusChart.data.datasets[0].data = dataPerBulan[selected];
      statusChart.update();
    });
  }

  // === Peta Leaflet ===
  const mapDiv = document.getElementById('petaKegiatan');
  if (mapDiv) {
    const map = L.map('petaKegiatan').setView([-7.2575, 112.7521], 12); // Koordinat Surabaya
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Tambahkan marker contoh
    L.marker([-7.2504, 112.7688]).addTo(map)
      .bindPopup('<b>Kegiatan UMKM</b><br>Kecamatan Genteng');
    L.marker([-7.2756, 112.6426]).addTo(map)
      .bindPopup('<b>Kegiatan UMKM</b><br>Kecamatan Lakarsantri');
  }

});
