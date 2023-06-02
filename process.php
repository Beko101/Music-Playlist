<!DOCTYPE html>
<html>
<head>
    <title>Müzik Çalma Listeleri - Sonuç</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Müzik Çalma Listeleri - Sonuç</h1>
        <ul class="playlist">
            <?php
            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $music_service = $_POST["music_service"];
                $access_token = $_POST["access_token"];

                if ($music_service == "spotify") {
                    // Spotify API ile çalma listelerini almak için gerekli Python komutunu buraya yazın
                    $command = "python3 get_playlists.py spotify " . escapeshellarg($access_token);
                } elseif ($music_service == "apple_music") {
                    // Apple Music API ile çalma listelerini almak için gerekli Python komutunu buraya yazın
                    $command = "python3 get_playlists.py apple_music " . escapeshellarg($access_token);
                } elseif ($music_service == "amazon_music") {
                    // Amazon Music API ile çalma listelerini almak için gerekli Python komutunu buraya yazın
                    $command = "python3 get_playlists.py amazon_music " . escapeshellarg($access_token);
                } elseif ($music_service == "deezer") {
                    // Deezer API ile çalma listelerini almak için gerekli Python komutunu buraya yazın
                    $command = "python3 get_playlists.py deezer " . escapeshellarg($access_token);
                }

                // Python komutunu çalıştır ve çıktıyı ekrana yazdır
                $output = shell_exec($command);
                $playlists = json_decode($output, true);

                foreach ($playlists as $playlist) {
                    echo "<li>" . $playlist . "</li>";
                }
            }
            ?>
        </ul>
    </div>
</body>
</html>
