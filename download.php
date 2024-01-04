<?php
$url = $_POST['url'];
$expiry = $_POST['expiry'];

// دانلود ویدیو
$file = file_get_contents($url);
$file_path = '/path/to/download/directory/video.mp4';
file_put_contents($file_path, $file);

// ایجاد لینک دانلود
$download_link = 'http://yourserver.com/path/to/download/directory/video.mp4';

// تنظیم زمان انقضا
$expiry_time = time() + ($expiry * 60 * 60); // convert hours to seconds

echo "لینک دانلود: " . $download_link . "<br>";
echo "زمان انقضا: " . date('Y-m-d H:i:s', $expiry_time);
?>
