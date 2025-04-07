"""
This module contains a sample list of Indonesian cities.
Used for initial database population. In a production environment,
this would contain the full list of cities.
"""

# Sample of major cities across Indonesia (for demonstration purposes)
# In a real application, this would be a comprehensive list of all cities/regions
CITIES = [
    # Jakarta
    {'id': 1, 'province_id': 6, 'name': 'Jakarta Pusat', 'type': 'kota', 'postal_code': '10000'},
    {'id': 2, 'province_id': 6, 'name': 'Jakarta Utara', 'type': 'kota', 'postal_code': '14000'},
    {'id': 3, 'province_id': 6, 'name': 'Jakarta Barat', 'type': 'kota', 'postal_code': '11000'},
    {'id': 4, 'province_id': 6, 'name': 'Jakarta Selatan', 'type': 'kota', 'postal_code': '12000'},
    {'id': 5, 'province_id': 6, 'name': 'Jakarta Timur', 'type': 'kota', 'postal_code': '13000'},
    
    # Jawa Barat
    {'id': 22, 'province_id': 9, 'name': 'Bandung', 'type': 'kota', 'postal_code': '40000'},
    {'id': 23, 'province_id': 9, 'name': 'Bekasi', 'type': 'kota', 'postal_code': '17000'},
    {'id': 24, 'province_id': 9, 'name': 'Bogor', 'type': 'kota', 'postal_code': '16000'},
    {'id': 25, 'province_id': 9, 'name': 'Depok', 'type': 'kota', 'postal_code': '16400'},
    {'id': 26, 'province_id': 9, 'name': 'Cimahi', 'type': 'kota', 'postal_code': '40500'},
    
    # Jawa Tengah
    {'id': 27, 'province_id': 10, 'name': 'Semarang', 'type': 'kota', 'postal_code': '50000'},
    {'id': 28, 'province_id': 10, 'name': 'Surakarta', 'type': 'kota', 'postal_code': '57100'},
    {'id': 29, 'province_id': 10, 'name': 'Pekalongan', 'type': 'kota', 'postal_code': '51100'},
    
    # Jawa Timur
    {'id': 30, 'province_id': 11, 'name': 'Surabaya', 'type': 'kota', 'postal_code': '60000'},
    {'id': 31, 'province_id': 11, 'name': 'Malang', 'type': 'kota', 'postal_code': '65100'},
    {'id': 32, 'province_id': 11, 'name': 'Sidoarjo', 'type': 'kabupaten', 'postal_code': '61200'},
    
    # Bali
    {'id': 33, 'province_id': 1, 'name': 'Denpasar', 'type': 'kota', 'postal_code': '80000'},
    {'id': 34, 'province_id': 1, 'name': 'Badung', 'type': 'kabupaten', 'postal_code': '80351'},
    {'id': 35, 'province_id': 1, 'name': 'Gianyar', 'type': 'kabupaten', 'postal_code': '80500'},
    
    # DI Yogyakarta
    {'id': 36, 'province_id': 5, 'name': 'Yogyakarta', 'type': 'kota', 'postal_code': '55000'},
    {'id': 37, 'province_id': 5, 'name': 'Sleman', 'type': 'kabupaten', 'postal_code': '55500'},
    
    # Banten
    {'id': 38, 'province_id': 3, 'name': 'Tangerang', 'type': 'kota', 'postal_code': '15000'},
    {'id': 39, 'province_id': 3, 'name': 'Serang', 'type': 'kota', 'postal_code': '42100'},
    
    # Sumatera Utara
    {'id': 40, 'province_id': 34, 'name': 'Medan', 'type': 'kota', 'postal_code': '20000'},
    {'id': 41, 'province_id': 34, 'name': 'Binjai', 'type': 'kota', 'postal_code': '20700'},
    
    # Sumatera Selatan
    {'id': 42, 'province_id': 33, 'name': 'Palembang', 'type': 'kota', 'postal_code': '30000'},
    {'id': 43, 'province_id': 33, 'name': 'Prabumulih', 'type': 'kota', 'postal_code': '31100'},
    
    # Sulawesi Selatan
    {'id': 44, 'province_id': 28, 'name': 'Makassar', 'type': 'kota', 'postal_code': '90000'},
    {'id': 45, 'province_id': 28, 'name': 'Parepare', 'type': 'kota', 'postal_code': '91100'},
    
    # Kalimantan Timur
    {'id': 46, 'province_id': 15, 'name': 'Samarinda', 'type': 'kota', 'postal_code': '75000'},
    {'id': 47, 'province_id': 15, 'name': 'Balikpapan', 'type': 'kota', 'postal_code': '76100'}
]
