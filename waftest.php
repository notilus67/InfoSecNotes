<?php
        if(isset($_GET['host'])) {
                system('dig '.$_GET['host']);
        }
?>
