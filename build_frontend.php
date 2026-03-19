<?php

$outputDir = __DIR__ . '/php_frontend_only';
$assetsDir = $outputDir . '/assets';

// 1. Clean and recreate directory
if (is_dir($outputDir)) {
    exec("rmdir /s /q " . escapeshellarg($outputDir)); // Windows command
}
mkdir($outputDir, 0777, true);
mkdir($assetsDir, 0777, true);

// 2. Copy assets (excluding index.php)
$publicItems = scandir(__DIR__ . '/public');
foreach ($publicItems as $item) {
    if ($item === '.' || $item === '..' || $item === 'index.php') {
        continue;
    }
    $src = __DIR__ . '/public/' . $item;
    $dst = $assetsDir . '/' . $item;
    if (is_dir($src)) {
        exec("xcopy /e /i /y " . escapeshellarg($src) . " " . escapeshellarg($dst) . " > NUL");
    } else {
        copy($src, $dst);
    }
}

// 3. Copy templates
exec("xcopy /e /i /y " . escapeshellarg(__DIR__ . '/templates') . " " . escapeshellarg($outputDir) . " > NUL");

// Helper: recursively find files returning array of string paths
function getFiles($dir) {
    $result = [];
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir));
    foreach ($iterator as $file) {
        if ($file->isFile()) {
            $result[] = $file->getPathname();
        }
    }
    return $result;
}

// 4. Rename .html.twig to .php
$allFiles = getFiles($outputDir);
$renamedFiles = [];
foreach ($allFiles as $file) {
    if (substr($file, -10) === '.html.twig') {
        $phpPath = substr($file, 0, -10) . '.php';
        rename($file, $phpPath);
        $renamedFiles[] = $phpPath;
    } else {
        $renamedFiles[] = $file;
    }
}

// 5. Process contents
foreach ($renamedFiles as $file) {
    if (pathinfo($file, PATHINFO_EXTENSION) !== 'php') {
        continue;
    }
    
    $content = file_get_contents($file);

    // Replace include with PHP include
    $content = preg_replace_callback('/\{\{\s*include\([\'"](.*?)(\.html\.twig)?[\'"]\)\s*\}\}/', function($matches) {
        $path = $matches[1] . '.php';
        return "<?php include '{$path}'; ?>";
    }, $content);

    // Replace asset()
    $content = preg_replace_callback('/\{\{\s*asset\([\'"](.*?)[\'"]\)\s*\}\}/', function($matches) {
        return "/assets/" . ltrim($matches[1], '/');
    }, $content);

    // Handle Layout Extends 
    // {% extends 'base.html.twig' %}
    if (preg_match('/\{%\s*extends\s+[\'"](.*?)\.html\.twig[\'"]\s*%\}/', $content, $matchExtends)) {
        $layoutName = $matchExtends[1] . ".php";
        // Remove extends definition
        $content = preg_replace('/\{%\s*extends\s+[\'"](.*?)[\'"]\s*%\}/', '', $content);
        
        // Wrap block body
        $content = preg_replace('/\{%\s*block\s+body\s*%\}/', '<?php ob_start(); ?>', $content);
        $content = preg_replace('/\{%\s*endblock\s*%\}/', '<?php $content = ob_get_clean(); include \'' . $layoutName . '\'; ?>', $content);
    } else {
        // If parsing layout itself (e.g. base.html.twig -> base.php)
        $content = preg_replace('/\{%\s*block\s+[a-zA-Z0-9_]+\s*%\}.*?\{%\s*endblock\s*%\}/s', '<?php echo $content ?? \'\'; ?>', $content);
    }

    // Strip out remaining unsupported TWIG logic tags to prevent raw syntax in PHP output
    $content = preg_replace('/\{%.*?%\}/', '', $content);
    $content = preg_replace('/\{\{.*?\}\}/', '', $content);

    // Fix absolute CSS/JS paths by prepending /assets/ (but ignore // or http://)
    $content = str_replace(
        ['href="/css/', 'href="/js/', 'href="/images/', 'href="/sass/'], 
        ['href="/assets/css/', 'href="/assets/js/', 'href="/assets/images/', 'href="/assets/sass/'], 
        $content
    );
    $content = str_replace(
        ['src="/css/', 'src="/js/', 'src="/images/', 'src="/sass/'], 
        ['src="/assets/css/', 'src="/assets/js/', 'src="/assets/images/', 'src="/assets/sass/'], 
        $content
    );

    file_put_contents($file, $content);
}

// 6. Create .htaccess
$htaccess = <<<EOD
RewriteEngine On

# Remove .php from URL
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.php -f
RewriteRule ^(.+)$ $1.php [L]

# Default route
DirectoryIndex index.php
EOD;
file_put_contents($outputDir . '/.htaccess', $htaccess);

// 7. Zip output
$zipFile = __DIR__ . '/php_frontend_only.zip';
if (file_exists($zipFile)) {
    unlink($zipFile);
}
// Zip using PowerShell
$psCommand = "Compress-Archive -Path " . escapeshellarg($outputDir . '/*') . " -DestinationPath " . escapeshellarg($zipFile) . " -Force";
exec("powershell -Command \"$psCommand\"");

echo "Frontend successfully built to php_frontend_only.zip\n";
