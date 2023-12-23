Salam.

Bu Proyekt Python Django ilə hazırlanıb.

 -- Proyekti (Run) etmək üçün. İlk öncə VS Code'dan istifadə edək. (fərqlidə ola bilər)
1. Proyektin linkini kopyalayın və Terminaldan istifadə edərək (git clone) edin.
2. VS Code da Terminalı başladın və (python -m venv env) kodundan istifadə edərək virtual environment yaradın.(Macos üçün.)
3. (source env/bin/activate) kodundan istifadə edərək virtual environment aktivləşdirin.(Macos üçün.)
4. Proyekt Docker vasitəsi ilə PostgreSQL dən istifadə edir. settings.py dan dəyişə bilərsiniz. Docker ilə run etsəz (docker-compose up -d) kamandası ilə başladın. Və (pip install Django) kamandasını başladın

5. Docker başlandıqdan sonra (pip install -r requirements.txt) kamandasını başladın və pip list edərək yüklənib yüklənmədiyini yoxlayın.
6. (python manage.py makemigrations) kamandasından istifadə edin. 
7. (python manage.py migrate) kamandasından istifadə edin. 

8. Hərşey (migrate'lər - OK) olduqdundan əmin olun
9. python manage.py runserver kamandası ilə proyekti başladın.
10. Terminalda localhost linki görünəcək ona klikləyərək (koypalayaraq) brauserdə açın.

Admin panelə giriş etmək üçün (https://hcyevelnur.pythonanywhere.com/sfhagfjkhjkajskfbjafbka1407-Admin-Panel/) <- bu linkdən istifadə et.
 Admin panel 
    -- Nömrə : 0515400979
    -- Şifrə : elnurr123


-- Səhifələr Bootstrap 5 dir. Hava proqnozu APİ ilə işləyir.
