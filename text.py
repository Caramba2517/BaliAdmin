from statistic.signals import cur, db

cur.execute("""INSERT INTO "texts_in_bot_text" ("id", "action", "text_in_russian", "text_in_english", "text_in_indonesian") VALUES
(14,	14,	'Тип недвижимости:

(Вы можете выбрать несколько вариантов)',	'Accommodation type:

(You can choose several answer)',	'Tipe akomodasi:

(Anda dapat memilih beberapa jawaban)'),
(15,	15,	'Не выбрана ни одна локация!',	'No location selected!',	'Tidak ada lokasi yang dipilih!'),
(16,	16,	'Удобства:

(Вы можете выбрать несколько вариантов)',	'Additional request:

(You can choose several answer)',	'Permintaan tambahan:

(Anda dapat memilih beberapa jawaban)'),
(1,	1,	'привет! Рады видеть вас в VillaBot!

Давайте найдем подходящее жилье для вас!',	'hello! Happy to see you in VillaBot!

Let''s find awesome villa!',	'Halo! Senang melihat Anda di VillaBot!

Ayo temukan vila yang luar biasa!'),
(2,	2,	'Ваши избранные апартаменты:',	'Your favourite apartment:',	'Apartemen favorit Anda:'),
(3,	3,	'Ничего не найдено!',	'Nothing found!',	'Tidak ada yang ditemukan!'),
(4,	4,	'Действие отменено!

Попробуйте заново - /start',	'Action canceled!

Try again - /start',	'Tindakan dibatalkan!

Coba lagi - /start'),
(5,	5,	'Выберите тип обращения:',	'Choose feedback type:',	'Pilih jenis umpan balik:'),
(6,	6,	'Напишите текстовое сообщение для админа:',	'Write text message for admin:',	'Tulis pesan teks untuk admin:'),
(7,	7,	'Ваше обращение было отправлено! Пожалуйста, ожидайте ответа от администратора.',	'Your feedback has been sent! Wait for a response from the administrator.',	'Umpan balik Anda telah dikirim! Tunggu tanggapan dari administrator.'),
(8,	8,	'У вас есть открытое обращение, пожалуйста, ожидайте ответа!',	'You have an open question, please wait for an answer!',	'Anda memiliki pertanyaan terbuka, harap tunggu jawaban!'),
(9,	9,	'Вы закрыли чат с администратором!',	'You finish chat with admin!',	'Anda selesai mengobrol dengan admin!'),
(10,	10,	'Пожалуйста, ответьте на вопросы о вашей будущей вилле!

Период:',	'Please, answer the following question about your future villa!

Rental period:',	'Tolong, jawab pertanyaan berikut tentang vila masa depan Anda!

Periode sewa:'),
(11,	11,	'Выберите валюту:',	'Choose currency:',	'Pilih mata uang:'),
(12,	12,	'Выберите ваш бюджет:

(Вы можете выбрать несколько вариантов)',	'Choose your budget:

(You can choose several answer)',	'Pilih anggaran Anda:

(Anda dapat memilih beberapa jawaban)'),
(13,	13,	'Локация:

(Вы можете выбрать несколько вариантов)',	'Accommodation location:

(You can choose several answer)',	'Lokasi akomodasi:

(Anda dapat memilih beberapa jawaban)'),
(17,	17,	'Ваш запрос был сохранен!

Вы можете найти его в основном меню по кнопке "Последний сохраненный запрос"',	'Your request has been saved!

You can find in the mine menu under "Last saved request"',	'Permintaan Anda telah disimpan!

Anda dapat menemukan di menu tambang di bawah "Last saved request"'),
(18,	18,	'Поиск...',	'Searching...',	'Mencari...'),
(19,	19,	'Вам нравится этот вариант?

Если вы хотите получить контакт агента, пожалуйста, оформите подписку на наш сервис на один месяц.',	'Do you like this variant?

If you want to contact the renter please turn on the subscription for our service for one month.',	'Suka varian ini?

Jika ingin menghubungi pihak penyewa silahkan aktifkan langganan layanan kami selama satu bulan.'),
(20,	20,	'Апартаменты сохранены в избранное!',	'Apartment save to favourite!',	'Simpan apartemen ke favorit!'),
(21,	21,	'Апартаменты уже сохранены в избранном!',	'Apartment already in your favourite!',	'Apartemen sudah menjadi favorit Anda!'),
(22,	22,	'Подписка активирована!',	'Subscription activate!',	'Langganan aktif!')""")

db.commit()