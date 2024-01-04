<?php

if(isset($_GET['id'])) {
    $uniqueId = $_GET['id'];

    $filePath = "links/{$uniqueId}.json";
    if(file_exists($filePath)) {
        $linkData = json_decode(file_get_contents($filePath), true);
        
        // بررسی معتبر بودن زمان لینک
        if(time() < $linkData['expiry']) {
            header("Location: " . $linkData['videoURL']);
            exit;
        } else {
            echo "لینک دانلود منقضی شده است.";
        }
    } else {
        echo "لینک دانلود معتبر نیست.";
    }
} else {
    echo "درخواست نامعتبر.";
}

?>