# Fruit Management System

Bu loyiha mevalar va ularning turlarini boshqarish uchun yaratilgan Django asosidagi veb-ilovadir. Loyiha bog'bonlar va ularning yetishtirgan mevalari haqida ma'lumotlarni ko'rish, qo'shish va tahrirlash imkonini beradi.

## Talablar

- Python 3.x
- Django 3.x yoki undan yuqori
- Django CKEditor
- Django ModelTranslation

## O'rnatish

1. **Reponi klonlash**:

   ```bash
   git clone <repo-url>
   cd fruit_management_system
   ```

2. **Virtual muhit yaratish**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. **Talablarni o'rnatish**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Django konfiguratsiyasi**:

   Django sozlamalari (`settings.py`) faylini oching va kerakli o'zgarishlarni amalga oshiring, masalan, ma'lumotlar bazasi konfiguratsiyasi va CKEditor sozlamalari.

5. **Migratsiyalarni yaratish va amalga oshirish**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Superadmin yaratish**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Serverni ishga tushirish**:

   ```bash
   python manage.py runserver
   ```

## Foydalanish

1. Brauzerda `http://127.0.0.1:8000/admin` manziliga o'ting.
2. O'zingiz yaratgan superadmin hisobingiz bilan kirish qiling.
3. "Fruit Types" va "Fruits" bo'limlaridan foydalanib, mevalar va ularning turlarini boshqaring.

## Qanday yordam berish mumkin

Agar sizda har qanday savol yoki muammo bo'lsa, menga murojaat qilishingiz mumkin.

## Litsenziya

Bu loyiha MIT litsenziyasi bilan tarqatiladi.
