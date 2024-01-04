<?php
if($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['videoURL']) && isset($_POST['expiry'])) {
    $videoURL = $_POST['videoURL'];
    $expiry = intval($_POST['expiry']);
    
    // تبدیل ساعت به ثانیه
    $expiryInSeconds = $expiry * 3600;
    
    // ایجاد شناسه یکتا برای لینک
    $uniqueId = uniqid();
    
    // ذخیره لینک و انقضا در فایل (یا دیتابیس)
    $linkData = json_encode(['videoURL' => $videoURL, 'expiry' => time() + $expiryInSeconds]);
    file_put_contents("links/{$uniqueId}.json", $linkData);
    
    // نمایش لینک دانلود به کاربر
    $downloadLink = "http://{$_SERVER['HTTP_HOST']}/serve.php?id={$uniqueId}";
    echo "لینک دانلود شما: <a href='{$downloadLink}'>دانلود ویدئو</a> <br> این لینک پس از {$expiry} ساعت منقضی می‌شود.";

} else {
    // خطا در صورت عدم ارسال فرم به درستی
    echo 'درخواست نامعتبر.';
}
?>