"""
This module contains the data for Indonesian courier services.
Used for initial database population.
"""

COURIERS = [
    {
        'code': 'jne',
        'name': 'JNE (Jalur Nugraha Ekakurir)',
        'website': 'https://www.jne.co.id',
        'services': [
            {
                'code': 'OKE',
                'name': 'Ongkos Kirim Ekonomis',
                'description': 'Layanan pengiriman ekonomis untuk semua kebutuhan'
            },
            {
                'code': 'REG',
                'name': 'Layanan Reguler',
                'description': 'Layanan pengiriman reguler dengan estimasi 2-3 hari'
            },
            {
                'code': 'YES',
                'name': 'Yakin Esok Sampai',
                'description': 'Layanan pengiriman cepat dengan estimasi 1 hari'
            }
        ]
    },
    {
        'code': 'tiki',
        'name': 'TIKI (Titipan Kilat)',
        'website': 'https://tiki.id',
        'services': [
            {
                'code': 'ECO',
                'name': 'Ekonomis',
                'description': 'Layanan pengiriman ekonomis untuk semua kebutuhan'
            },
            {
                'code': 'REG',
                'name': 'Reguler Service',
                'description': 'Layanan pengiriman reguler dengan estimasi 2-4 hari'
            },
            {
                'code': 'ONS',
                'name': 'Over Night Service',
                'description': 'Layanan pengiriman cepat dengan estimasi 1 hari'
            }
        ]
    },
    {
        'code': 'pos',
        'name': 'POS Indonesia',
        'website': 'https://www.posindonesia.co.id',
        'services': [
            {
                'code': 'Paket Kilat Khusus',
                'name': 'Paket Kilat Khusus',
                'description': 'Layanan pengiriman cepat Pos Indonesia'
            },
            {
                'code': 'Express Next Day',
                'name': 'Express Next Day',
                'description': 'Layanan pengiriman sangat cepat dengan estimasi 1 hari'
            }
        ]
    },
    {
        'code': 'jnt',
        'name': 'J&T Express',
        'website': 'https://www.jet.co.id',
        'services': [
            {
                'code': 'EZ',
                'name': 'J&T Economy',
                'description': 'Layanan pengiriman ekonomis J&T'
            },
            {
                'code': 'REG',
                'name': 'J&T Regular',
                'description': 'Layanan pengiriman reguler dengan estimasi 2-3 hari'
            }
        ]
    },
    {
        'code': 'sicepat',
        'name': 'SiCepat',
        'website': 'https://www.sicepat.com',
        'services': [
            {
                'code': 'REG',
                'name': 'Regular Service',
                'description': 'Layanan pengiriman reguler dengan estimasi 1-2 hari'
            },
            {
                'code': 'BEST',
                'name': 'Best Service',
                'description': 'Layanan pengiriman hemat dengan estimasi 2-3 hari'
            },
            {
                'code': 'SIUNT',
                'name': 'SiUntung',
                'description': 'Layanan pengiriman ekonomis'
            }
        ]
    },
    {
        'code': 'anteraja',
        'name': 'AnterAja',
        'website': 'https://anteraja.id',
        'services': [
            {
                'code': 'REG',
                'name': 'Regular Service',
                'description': 'Layanan pengiriman reguler dengan estimasi 2-3 hari'
            },
            {
                'code': 'ND',
                'name': 'Next Day',
                'description': 'Layanan pengiriman cepat dengan estimasi 1 hari'
            },
            {
                'code': 'SD',
                'name': 'Same Day',
                'description': 'Layanan pengiriman dalam hari yang sama'
            }
        ]
    },
    {
        'code': 'wahana',
        'name': 'Wahana Prestasi Logistik',
        'website': 'https://www.wahana.com',
        'services': [
            {
                'code': 'Normal',
                'name': 'Normal Service',
                'description': 'Layanan pengiriman standar Wahana'
            }
        ]
    },
    {
        'code': 'ninja',
        'name': 'Ninja Xpress',
        'website': 'https://www.ninjaxpress.co',
        'services': [
            {
                'code': 'Standard',
                'name': 'Standard Service',
                'description': 'Layanan pengiriman standar Ninja'
            }
        ]
    }
]
