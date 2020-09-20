let browserSync = require('browser-sync').create();

browserSync.init({
    proxy: 'localhost:8000/new_order',
    files: ['**/*'],
    serveStatic: ['static'],
});

// В папке с проектом инициализируйте проект в консоли 
// npm init 
// (при инициализации достаточно ввести название проекта)

// Установите Browser-sync: наберите в консоли 
// npm i browser-sync --save-dev

// Запустите в консоли node proxy.js